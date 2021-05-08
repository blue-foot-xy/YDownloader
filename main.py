import os
import re
import sys

from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QStatusBar

from download import download_media as downloadVids


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 597)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.bannerImage = QtWidgets.QLabel(self.centralwidget)
        self.bannerImage.setGeometry(QtCore.QRect(10, 10, 781, 351))
        self.bannerImage.setText("")
        self.bannerImage.setPixmap(QtGui.QPixmap("images/yt.png"))
        self.bannerImage.setScaledContents(True)
        self.bannerImage.setObjectName("bannerImage")

        self.videoURLTextAreaLabel = QtWidgets.QLabel(self.centralwidget)
        self.videoURLTextAreaLabel.setGeometry(QtCore.QRect(10, 360, 191, 31))
        self.videoURLTextAreaLabel.setObjectName("videoURLTextAreaLabel")

        self.qualitySelectLabel = QtWidgets.QLabel(self.centralwidget)
        self.qualitySelectLabel.setGeometry(QtCore.QRect(130, 440, 81, 20))
        self.qualitySelectLabel.setObjectName("qualitySelectLabel")

        # Progressbar functionality not yet available
        # self.downloadProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.downloadProgressBar.setGeometry(QtCore.QRect(10, 510, 671, 31))
        # self.downloadProgressBar.setProperty("value", 0)
        # self.downloadProgressBar.setObjectName("downloadProgressBar")

        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(10, 510, 781, 31))
        self.downloadButton.setObjectName("downloadButton")

        self.downloadPathTextAreaLabel = QtWidgets.QLabel(self.centralwidget)
        self.downloadPathTextAreaLabel.setGeometry(
            QtCore.QRect(490, 440, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(8)

        self.downloadPathTextAreaLabel.setFont(font)
        self.downloadPathTextAreaLabel.setObjectName(
            "downloadPathTextAreaLabel")

        self.browseFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseFolderButton.setGeometry(QtCore.QRect(740, 460, 51, 31))
        self.browseFolderButton.setObjectName("browseFolderButton")

        self.videoURLTextArea = QtWidgets.QTextEdit(self.centralwidget)
        self.videoURLTextArea.setGeometry(QtCore.QRect(10, 386, 781, 51))
        self.videoURLTextArea.setObjectName("videoURLTextArea")

        self.downloadPathTextArea = QtWidgets.QTextEdit(self.centralwidget)
        self.downloadPathTextArea.setGeometry(QtCore.QRect(490, 460, 241, 31))
        self.downloadPathTextArea.setObjectName("downloadPathTextArea")

        self.typeSelect = QtWidgets.QComboBox(self.centralwidget)
        self.typeSelect.setGeometry(QtCore.QRect(10, 460, 101, 31))
        self.typeSelect.setCurrentText("")

        self.typeSelect.setObjectName("typeSelect")
        self.typeSelect.addItem('video')
        self.typeSelect.addItem('audio')

        self.qualitySelect = QtWidgets.QComboBox(self.centralwidget)
        self.qualitySelect.setGeometry(QtCore.QRect(130, 460, 101, 31))
        self.qualitySelect.setObjectName("qualitySelect")

        self.typeSelectLabel = QtWidgets.QLabel(self.centralwidget)
        self.typeSelectLabel.setGeometry(QtCore.QRect(10, 440, 81, 20))
        self.typeSelectLabel.setObjectName("typeSelectLabel")

        self.getCaptionsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.getCaptionsCheckBox.setGeometry(QtCore.QRect(260, 450, 121, 20))
        self.getCaptionsCheckBox.setObjectName("getCaptionsCheckBox")

        self.ifAvailableLabel = QtWidgets.QLabel(self.centralwidget)
        self.ifAvailableLabel.setGeometry(QtCore.QRect(280, 470, 71, 20))
        self.ifAvailableLabel.setObjectName("ifAvailableLabel")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(380, 450, 91, 20))
        self.checkBox.setObjectName("checkBox")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 470, 91, 16))
        self.label.setObjectName("label")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(360, 450, 20, 51))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(240, 450, 20, 51))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(460, 450, 20, 51))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        self.menuOthers = QtWidgets.QMenu(self.menubar)
        self.menuOthers.setObjectName("menuOthers")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionCheck_For_Updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_For_Updates.setObjectName("actionCheck_For_Updates")

        self.menuOthers.addAction(self.actionAbout)
        self.menuOthers.addAction(self.actionCheck_For_Updates)
        self.menubar.addAction(self.menuOthers.menuAction())

        # Programing the browse button
        self.browseFolderButton.clicked.connect(self.getDir)

        # Programming the menu items
        self.actionAbout.triggered.connect(self.showInfo)
        self.actionCheck_For_Updates.triggered.connect(self.checkVersion)

        # adding quality select option
        for q in ('1080p', '720p', '480p', '360p',
                  '240p', '144p', '2160p', '1440p'):
            self.qualitySelect.addItem(q)

        # If you need to perform ant action upon type select
        # if self.typeSelect.currentText() == 'video/mp4'

        # Default download folder
        self.downloadPathTextArea.insertPlainText(
            str(os.path.join(Path.home(), "Downloads/YouTube Downloads")))

        # updates parameters upon editing the value on textbox
        # self.videoURLTextArea.textChanged.connect(self.update)

        # starts download upon clicking the download button
        self.downloadButton.clicked.connect(self.download)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Upon clicking the browse button
    def getDir(self):
        fileName = str(QtWidgets.QFileDialog.getExistingDirectory(
                           MainWindow, "Select Directory"))
        if fileName:
            self.downloadPathTextArea.clear()
            self.downloadPathTextArea.insertPlainText(fileName)

    # Upon clicking the download button
    def download(self):
        if self.checkBox.isChecked():
            singleDownload=False
        else:
            singleDownload=True

        links = re.split('; |, |\n |\s',self.videoURLTextArea.toPlainText())
        links[:] = (value for value in links if value != '')

        savePath = self.downloadPathTextArea.toPlainText()
        quality = self.qualitySelect.currentText()
        downloadType = self.typeSelect.currentText()

        if self.getCaptionsCheckBox.isChecked():
            downloadCaption = True
        else:
            downloadCaption = False

        downloadVids(links, savePath, quality,
                     downloadCaption, downloadType,
                     singleDownload)

    # Upon clicking about
    def showInfo(self):
        msg = QMessageBox()
        msg.setWindowTitle("YDownloader")
        msg.setText("\nDownload YouTube Videos and Playlists for free")
        # msg.setDetailedText("The details are as follows:")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    # Upon checking version
    def checkVersion(self):
        msg = QMessageBox()
        msg.setWindowTitle("YDownloader")
        msg.setText("Current Version: 1.0.0")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YDownloader"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.videoURLTextAreaLabel.setText(
            _translate("MainWindow", "Enter video URL(s):"))
        self.qualitySelectLabel.setText(
            _translate("MainWindow", "Vid Quality:"))
        self.downloadPathTextAreaLabel.setText(
            _translate("MainWindow", "Download Folder:"))
        self.browseFolderButton.setText(_translate("MainWindow", "..."))
        self.typeSelectLabel.setText(_translate("MainWindow", "Type:"))
        self.getCaptionsCheckBox.setText(
            _translate("MainWindow", "Get Captions "))
        self.ifAvailableLabel.setText(
            _translate("MainWindow", "(if available)"))
        self.checkBox.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "      playlist"))
        self.menuOthers.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCheck_For_Updates.setText(
            _translate("MainWindow", "Version Info"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
