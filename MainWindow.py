from NumberDelegate import *
from TableModel import TableModel
from autogen_ui.Ui_MainWindow import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableView.setItemDelegate(NumberDelegate())
        self.ui.tableView.setModel(TableModel())
