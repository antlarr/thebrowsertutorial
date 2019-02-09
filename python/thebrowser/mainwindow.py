import sys
import os.path
from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp

uifile = os.path.dirname(__file__) + "/../../cpp/mainwindow.ui"
MainWindowUI, MainWindowBase = uic.loadUiType(uifile)

class MainWindow(MainWindowBase, MainWindowUI):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        menubar = self.menuBar
        menu = menubar.addMenu(self.tr("File"))
        action = QAction(self.tr("Quit"), self)
        action.setIcon(QIcon.fromTheme("application-exit"))
        action.triggered.connect(qApp.quit)

        menu.addAction(action)
        self.mainToolBar.addAction(action)

    def loadLocation(self):
        url = QUrl(self.lineEdit.text())
        if not url.scheme():
            url.setScheme("https")
        self.webView.load(url)

    def urlChanged(self, url):
        self.lineEdit.setText(url.toString())


