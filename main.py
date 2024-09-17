from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

app = QApplication([])
mw = MainWindow()
mw.show()
app.exec_()
