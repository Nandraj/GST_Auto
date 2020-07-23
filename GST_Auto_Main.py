from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5.QtCore import *
import sys
from Login_UI import Client_Master_and_Login_Window
from selenium import webdriver


class GSTAutoMainWindow(QMainWindow):
    def __init__(self):
        super(GSTAutoMainWindow, self).__init__()
        # setting central widget to Qstackwidget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        # setting login screen to self.central_widget
        self.login_screen = Client_Master_and_Login_Window()
        self.central_widget.addWidget(self.login_screen)

        # Main window heading, logo etc
        self.setWindowTitle("NR GST Auto")
        self.resize(self.login_screen.size())
        self.setStyleSheet(self.login_screen.styleSheet())
        self.setWindowIcon(QIcon(QPixmap("N.ico")))

#######################MAIN FUNCTION#########################


def main():
    app = QApplication(sys.argv)
    window = GSTAutoMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

webdriver.Chrome().quit()
