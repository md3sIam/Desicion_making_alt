from NumberDelegate import *
from TableModel import TableModel
from autogen_ui.Ui_MainWindow import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableViewA.setItemDelegate(NumberDelegate())
        self.ui.tableViewA.setModel(TableModel())

        self.ui.m_checkButton.setStyleSheet("QPushButton {"
                                            "   background-color: lightgray; "
                                            "   border: 0;"
                                            "   border-radius:30px;"
                                            "}"
                                            "QPushButton:pressed {"
                                            "   border: 1px solid black"
                                            "}")

        circleButtons = [self.ui.m_addRowButton, self.ui.m_addColumnButton,
                         self.ui.m_removeRowButton, self.ui.m_removeColumnButton]

        circleButtonStyleSheet = "QPushButton {" \
                                 "  color: white;" \
                                 "  border-radius: 20px;" \
                                 "  background-color: %s;" \
                                 "}" \
                                 "QPushButton:pressed {" \
                                 "  border: 1px solid black" \
                                 "}"
        redColor = "#ff5353"
        greenColor = "#79f079"

        for i in range(len(circleButtons)):
            circleButtons[i].setStyleSheet(circleButtonStyleSheet % (greenColor if i < 2 else redColor))

        # \todo доделать actions из menubar
        # \todo отступы grid layout'а при растяжении окна
