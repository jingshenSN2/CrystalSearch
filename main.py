from PyQt5.QtWidgets import QApplication
import sys

from crystalsearchgui.main_ui import MainGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec_())