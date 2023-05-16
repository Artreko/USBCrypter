from ctypes import *
import _ctypes
import time
import csv
import math
import locale
import os
import sys
from UI.key_reader_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
import traceback
import wmi
from key_reader.check_key.check_key import read_file
from datetime import datetime, timedelta


def bubbleSort(times):
    while True:
        exchanges = False
        for i in range(len(times)-1):
            if times[i] > times[i + 1]:
                times[i], times[i + 1] = times[i + 1], times[i]
                exchanges = True
        if not exchanges:
            break


def avgTrustedIntervalMed(times):
    avg = sum(times)/len(times)
    bubbleSort(times)
    med = times[len(times)//2]
    sd = 0
    newAvg = 0
    newCnt = 0
    for t in times:
        sd += (t - avg) * (t - avg)
    sd /= (len(times) - 1)
    sd = math.sqrt(sd)
    for t in times:
        if med - sd <= t <= med + sd:
            newAvg += t
            newCnt += 1
    if newCnt == 0:
        newCnt = 1
    return newAvg / newCnt


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.searchButton.clicked.connect(self.search_button_clicked)
        self.ui.reSearchButton.clicked.connect(self.search_button_clicked)
        self.ui.diskChooseButton.clicked.connect(self.disc_choose_button_clicked)

        self.setParams()

        self.ui.vsButton.setEnabled(False)
        self.ui.gccButton.setEnabled(False)
        self.ui.cppbButton.setEnabled(False)

        self.ui.vsButton.clicked.connect(lambda: self.startDll('VScppDLL.dll'))
        self.ui.gccButton.clicked.connect(lambda: self.startDll("gccDLL.dll"))
        self.ui.cppbButton.clicked.connect(lambda: self.startDll("cppBuilderDLL.dll"))

        self.ui.searchFailureLabel.hide()
        self.ui.diskTableFrame.hide()
        self.ui.workFrame.hide()

        self.filename = 'secret.key'
        self.table_columns = ['id', 'name', 'status', 'owner', 'end_time']
        self.statuses = ('Нет доступа', 'Доступ истек', 'Есть доступ')
        self.drives = [dict]

    def get_drives(self) -> bool:
        w = wmi.WMI()
        self.drives = [{'id': drive.Name,
                        'name': drive.VolumeName or 'USB-накопитель',
                        'status': self.statuses[0],
                        'owner': None,
                        'level': 0,
                        'end_time': None,
                        'serial_number': drive.VolumeSerialNumber,
                        'access': False,
                        'access_by_time': False,
                        }
                       for drive in w.Win32_LogicalDisk()
                       if drive.DriveType == 2]
        if not self.drives:
            return False
        return True

    def get_drives_statuses(self):
        for drive in self.drives:
            try:
                if self.filename in os.listdir(drive['id']):
                    drive['access'] = True
                    key = read_file(fr'{drive["id"]}\{self.filename}',
                                    drive['serial_number'])
                    drive['owner'] = key['owner']
                    drive['level'] = key['level']
                    drive['end_time'] =\
                        datetime.strptime(key['date_creation'], '%Y-%m-%d %H:%M:%S.%f') + \
                        timedelta(minutes=key['lifetime'])
                    if drive['end_time'] > datetime.now():
                        drive['access_by_time'] = True
                    drive['status'] =\
                        self.statuses[int(drive['access']) << int(drive['access_by_time'])]
            except PermissionError:
                continue

    def search_button_clicked(self):
        self.ui.searchFailureLabel.hide()
        if not self.get_drives():
            self.ui.searchFailureLabel.show()
            self.ui.startFrame.show()
            return None
        self.get_drives_statuses()
        print(*self.drives, sep='\n')
        self.ui.diskTable.clearContents()
        self.ui.diskTable.setRowCount(len(self.drives))
        for row, drive in enumerate(self.drives):
            for col, key in enumerate(self.table_columns):
                value = drive[key] or ''
                value = value if type(value) == str else value.strftime('%X %x')
                item = QTableWidgetItem(value)
                self.ui.diskTable.setItem(row, col, item)
        self.ui.diskTable.resizeColumnsToContents()
        self.ui.diskTableFrame.show()
        self.ui.startFrame.hide()

    def disc_choose_button_clicked(self):
        drive = self.drives[self.ui.diskTable.currentRow()]
        if not drive['access_by_time']:
            QMessageBox.critical(self, 'Отказано в доступе', 'Вы не можете получить доступ к программе!')
            return None
        level = drive['level']
        self.ui.levelLabel.setText(f'Ваш уровень доступа: {level}')
        self.ui.ownerLabel.setText(drive['owner'])
        if level >= 1:
            self.ui.vsButton.setEnabled(True)
        if level >= 2:
            self.ui.gccButton.setEnabled(True)
        if level >= 3:
            self.ui.cppbButton.setEnabled(True)
        self.ui.diskTableFrame.hide()
        self.ui.workFrame.show()

    def cancel_button_clicked(self):
        self.ui.workFrame.hide()
        self.ui.vsButton.setEnabled(False)
        self.ui.gccButton.setEnabled(False)
        self.ui.cppbButton.setEnabled(False)
        self.search_button_clicked()

    def setParams(self):
        self.path = os.getcwd()
        self.path = os.path.join(self.path, "myDLLs")
        self.runs = 50
        self.size1 = 110000
        self.size2 = 120000
        self.H1 = 200
        self.W1 = 2500
        self.H2 = 300
        self.W2 = 2000

    def funcTimeCount(self, funcs, dll_name):
        arr1 = (c_int * self.size1)()
        for i in range(self.size1):
            arr1[i] = pow(-1, i) * (i % 100)
        arr2 = (c_int * self.size2)()
        for i in range(self.size2):
            arr2[i] = pow(-1, i) * (3 * i % 100)
        mas1 = (POINTER(c_double) * self.H1)()
        for i in range(self.H1):
            mas1[i] = (c_double * self.W1)()
        for i in range(self.H1):
            for j in range(self.W1):
                mas1[i][j] = (i + j) % 100 * pow(-1, i)
        mas2 = (POINTER(c_double) * self.H2)()
        for i in range(self.H2):
            mas2[i] = (c_double * self.W2)()
        for i in range(self.H2):
            for j in range(self.W2):
                mas2[i][j] = (i + j) % 100 * pow(-1, i)

        csvfile = open('Stats\\' + dll_name[:-4] + '_stat.csv', 'w', encoding='utf-8', newline='')
        csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([dll_name, 'min', 'max', 'avg'])
        self.ui.textBrowser.append('Function: oddNegativeSum')
        times = list()
        for j in range(self.runs):
            start = time.perf_counter_ns()
            funcs[0](arr1, self.size1, arr2, self.size2)
            end = time.perf_counter_ns()
            times.append((end - start) / 1000000)
        avg_time = avgTrustedIntervalMed(times)
        min_time = times[0]
        max_time = times[-1]
        self.ui.textBrowser.append(f'min: {min_time:.4f}ms. max: {max_time:.4f}ms. avg: {avg_time:.4f}ms.\n')
        csvwriter.writerow(['oddNegativeSum', min_time, max_time, f'{avg_time:.4f}'])

        self.ui.textBrowser.append('Function: maxAvgMerge')
        times.clear()
        for j in range(self.runs):
            temp = (c_int * self.size1)()
            for i in range(self.size1):
                temp[i] = arr1[i]
            start = time.perf_counter_ns()
            funcs[1](temp, self.size1, arr2, self.size2)
            end = time.perf_counter_ns()
            times.append((end - start) / 1000000)
        avg_time = avgTrustedIntervalMed(times)
        min_time = times[0]
        max_time = times[-1]
        self.ui.textBrowser.append(f'min: {min_time:.4f}ms. max: {max_time:.4f}ms. avg: {avg_time:.4f}ms.\n')
        csvwriter.writerow(['maxAvgMerge', min_time, max_time, f'{avg_time:.4f}'])

        self.ui.textBrowser.append('Function: mainDiagonalSub')
        times.clear()
        for j in range(self.runs):
            start = time.perf_counter_ns()
            funcs[2](mas1, self.H1, self.W1, mas2, self.H2, self.W2)
            end = time.perf_counter_ns()
            times.append((end - start) / 1000000)
        avg_time = avgTrustedIntervalMed(times)
        min_time = times[0]
        max_time = times[-1]
        self.ui.textBrowser.append(f'min: {min_time:.4f}ms. max: {max_time:.4f}ms. avg: {avg_time:.4f}ms.\n')
        csvwriter.writerow(['mainDiagonalSub', min_time, max_time, f'{avg_time:.4f}'])
        csvfile.close()

    def startDll(self, dll_name):
        self.ui.textBrowser.clear()
        dll_path = os.path.join(self.path, dll_name)
        lib_c = CDLL(dll_path)
        dll_funcs = list()
        dll_funcs.append(lib_c.oddNegativeSum)
        dll_funcs.append(lib_c.maxAvgMerge)
        dll_funcs.append(lib_c.mainDiagonalSub)
        dll_funcs[2].restype = c_double
        self.ui.textBrowser.append(f'Library ({dll_name}) loaded\n')
        self.funcTimeCount(dll_funcs, dll_name)
        self.ui.textBrowser.append(f'Library ({dll_name}) freed')
        _ctypes.FreeLibrary(lib_c._handle)

    def startCbDll(self, dll_name):
        self.ui.textBrowser.clear()
        dll_path = os.path.join(self.path, dll_name)
        lib_c = CDLL(dll_path)
        dll_funcs = list()
        dll_funcs.append(lib_c._oddNegativeSum)
        dll_funcs.append(lib_c._maxAvgMerge)
        dll_funcs.append(lib_c._mainDiagonalSub)
        dll_funcs[2].restype = c_double
        self.ui.textBrowser.append(f'Library ({dll_name}) loaded\n')
        self.funcTimeCount(dll_funcs, dll_name)
        self.ui.textBrowser.append(f'Library ({dll_name}) freed')
        _ctypes.FreeLibrary(lib_c._handle)


def main():
    def log_uncaught_exceptions(ex_cls, ex, tb):
        text = '{}: {}:\n'.format(ex_cls.__name__, ex)

        text += ''.join(traceback.format_tb(tb))

        print(text)
        QMessageBox.critical(None, 'Error', text)

        sys.exit()

    sys.excepthook = log_uncaught_exceptions

    locale.setlocale(locale.LC_ALL, '')
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    main_window.move(15, 30)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
