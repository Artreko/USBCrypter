# Form implementation generated from reading ui file '.\UI\key_reader.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\free-icon-key-file-format-variant-29574.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowFilePath("")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.startFrame.setStyleSheet("")
        self.startFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.startFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.startFrame.setObjectName("startFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.startFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.searchButton = QtWidgets.QPushButton(parent=self.startFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.searchButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.searchButton.setStyleSheet("")
        self.searchButton.setObjectName("searchButton")
        self.verticalLayout_2.addWidget(self.searchButton)
        self.searchFailureLabel = QtWidgets.QLabel(parent=self.startFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchFailureLabel.sizePolicy().hasHeightForWidth())
        self.searchFailureLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(11)
        self.searchFailureLabel.setFont(font)
        self.searchFailureLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.searchFailureLabel.setStyleSheet("color: brown;")
        self.searchFailureLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.searchFailureLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.searchFailureLabel.setWordWrap(True)
        self.searchFailureLabel.setObjectName("searchFailureLabel")
        self.verticalLayout_2.addWidget(self.searchFailureLabel)
        self.verticalLayout.addWidget(self.startFrame)
        self.diskTableFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.diskTableFrame.setEnabled(True)
        self.diskTableFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.diskTableFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.diskTableFrame.setObjectName("diskTableFrame")
        self.formLayout = QtWidgets.QFormLayout(self.diskTableFrame)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.tableLabel = QtWidgets.QLabel(parent=self.diskTableFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableLabel.sizePolicy().hasHeightForWidth())
        self.tableLabel.setSizePolicy(sizePolicy)
        self.tableLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.tableLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableLabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.tableLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableLabel.setObjectName("tableLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.tableLabel)
        self.diskTable = QtWidgets.QTableWidget(parent=self.diskTableFrame)
        self.diskTable.setAlternatingRowColors(False)
        self.diskTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.diskTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.diskTable.setObjectName("diskTable")
        self.diskTable.setColumnCount(5)
        self.diskTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.diskTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.diskTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.diskTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.diskTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.diskTable.setHorizontalHeaderItem(4, item)
        self.diskTable.horizontalHeader().setCascadingSectionResizes(True)
        self.diskTable.horizontalHeader().setDefaultSectionSize(130)
        self.diskTable.horizontalHeader().setStretchLastSection(True)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.diskTable)
        self.reSearchButton = QtWidgets.QPushButton(parent=self.diskTableFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reSearchButton.sizePolicy().hasHeightForWidth())
        self.reSearchButton.setSizePolicy(sizePolicy)
        self.reSearchButton.setObjectName("reSearchButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.reSearchButton)
        self.diskChooseButton = QtWidgets.QPushButton(parent=self.diskTableFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diskChooseButton.sizePolicy().hasHeightForWidth())
        self.diskChooseButton.setSizePolicy(sizePolicy)
        self.diskChooseButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.diskChooseButton.setObjectName("diskChooseButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.diskChooseButton)
        self.verticalLayout.addWidget(self.diskTableFrame)
        self.workFrame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workFrame.sizePolicy().hasHeightForWidth())
        self.workFrame.setSizePolicy(sizePolicy)
        self.workFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.workFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.workFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.workFrame.setObjectName("workFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.workFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.workFrame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.vsButton = QtWidgets.QPushButton(parent=self.workFrame)
        self.vsButton.setObjectName("vsButton")
        self.gridLayout.addWidget(self.vsButton, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.workFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 4)
        self.gccButton = QtWidgets.QPushButton(parent=self.workFrame)
        self.gccButton.setObjectName("gccButton")
        self.gridLayout.addWidget(self.gccButton, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.workFrame)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.cppbButton = QtWidgets.QPushButton(parent=self.workFrame)
        self.cppbButton.setObjectName("cppbButton")
        self.gridLayout.addWidget(self.cppbButton, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.workFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.workFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.ownerLabel = QtWidgets.QLabel(parent=self.workFrame)
        self.ownerLabel.setObjectName("ownerLabel")
        self.gridLayout.addWidget(self.ownerLabel, 0, 0, 1, 1)
        self.levelLabel = QtWidgets.QLabel(parent=self.workFrame)
        self.levelLabel.setObjectName("levelLabel")
        self.gridLayout.addWidget(self.levelLabel, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.workFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор ключей"))
        self.searchButton.setText(_translate("MainWindow", "Поиск USB накопителей"))
        self.searchFailureLabel.setText(_translate("MainWindow", "USB накопители не найдены!"))
        self.tableLabel.setText(_translate("MainWindow", "Доступные диски"))
        item = self.diskTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Диск"))
        item = self.diskTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.diskTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.diskTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Владелец"))
        item = self.diskTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Действителен до"))
        self.reSearchButton.setText(_translate("MainWindow", "Повторить поиск"))
        self.diskChooseButton.setText(_translate("MainWindow", "Выбрать"))
        self.pushButton.setText(_translate("MainWindow", "Cменить ключь"))
        self.vsButton.setText(_translate("MainWindow", "VS"))
        self.gccButton.setText(_translate("MainWindow", "GCC"))
        self.label.setText(_translate("MainWindow", "Уровень 1"))
        self.cppbButton.setText(_translate("MainWindow", "cppBuilder"))
        self.label_3.setText(_translate("MainWindow", "Уровень 3"))
        self.label_2.setText(_translate("MainWindow", "Уровень 2"))
        self.ownerLabel.setText(_translate("MainWindow", "Owner"))
        self.levelLabel.setText(_translate("MainWindow", "Ваш уровень: "))
