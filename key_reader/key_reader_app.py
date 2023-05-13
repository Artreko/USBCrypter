import locale
import os
import sys
from UI.key_reader_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
import traceback
import wmi


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.searchFailureLabel.hide()
        self.ui.diskTableFrame.hide()
        self.ui.workFrame.hide()


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
