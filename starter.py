from main import StartMenuWindow
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartMenuWindow()
    ex.show()
    sys.exit(app.exec_())