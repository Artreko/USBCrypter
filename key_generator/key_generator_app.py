import locale
import os
import sys
from UI.key_generator_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
import traceback
import wmi
from key_generator.generator.generate_key_file import write_key


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.drives = []
        self.ui.searchFailureLabel.hide()
        self.ui.diskTableFrame.hide()
        self.ui.generatorFrame.hide()
        self.ui.succsesLabel.hide()

        self.ui.searchButton.clicked.connect(self.search_button_clicked)
        self.ui.reSearchButton.clicked.connect(self.search_button_clicked)
        self.ui.diskChooseButton.clicked.connect(self.disc_choose_button_clicked)
        self.ui.cancelButton.clicked.connect(self.cancel_button_clicked)
        self.ui.generateKeyButton.clicked.connect(self.generate_key_button_clicked)

    def search_button_clicked(self):
        self.ui.succsesLabel.hide()
        self.ui.searchFailureLabel.hide()
        w = wmi.WMI()
        self.drives = [(drive.Name,
                        drive.VolumeName or 'USB-накопитель',
                        drive.Description,
                        drive.Size,
                        drive.VolumeSerialNumber)
                       for drive in w.Win32_LogicalDisk()
                       if drive.DriveType == 2]

        # print(* self.drives, sep='\n')
        d_count = len(self.drives)
        if d_count > 0:
            self.ui.diskTable.clearContents()
            self.ui.diskTable.setRowCount(d_count)
            for row, drive in enumerate(self.drives):
                for col, d_property in enumerate(drive[:-1]):
                    item = QTableWidgetItem(d_property)
                    if col == 3:
                        size = round(int(d_property) / 1_073_741_824, 1)
                        item.setText(f'{size} GB')
                    self.ui.diskTable.setItem(row, col, item)
            self.ui.generatorFrame.setEnabled(True)
            self.ui.diskTableFrame.show()
            self.ui.searchFailureLabel.hide()
            self.ui.startFrame.hide()
        else:
            self.ui.diskTableFrame.hide()
            self.ui.searchFailureLabel.show()
            self.ui.startFrame.show()

    def disc_choose_button_clicked(self):
        self.ui.diskTableFrame.setDisabled(True)
        self.ui.diskTableFrame.hide()
        self.ui.generatorFrame.show()

    def cancel_button_clicked(self):
        self.ui.generatorFrame.hide()
        self.search_button_clicked()

    def generate_key_button_clicked(self):
        print(self.ui.ownerNameEdit.text())
        owner = self.ui.ownerNameEdit.text()
        if owner == '':
            QMessageBox.critical(self, 'Недостаточно данных', 'Имя владельца должно быть заполнено!')
            return None
        row = self.ui.diskTable.currentRow()
        write_key(
            owner,
            self.ui.timeSpinBox.value(),
            self.ui.levelSpinBox.value(),
            self.drives[row][-1],
            self.drives[row][0]
        )
        self.ui.generatorFrame.hide()
        self.ui.startFrame.show()
        self.ui.succsesLabel.show()


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
