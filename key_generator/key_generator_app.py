import locale
import os
import sys
from UI.key_generator_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import traceback
import wmi

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.drives = []

        self.ui.searchFailureLabel.hide()
        self.ui.diskTableFrame.hide()
        self.ui.generatorFrame.hide()

        self.ui.searchButton.clicked.connect(self.search_button_clicked)

    def search_button_clicked(self):
        pass


def main():
    locale.setlocale(locale.LC_ALL, '')
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    main_window.move(15, 30)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
