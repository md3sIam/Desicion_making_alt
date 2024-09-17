import computeMatrix
from NumberDelegate import *
from TableModel import TableModel
from autogen_ui.Ui_MainWindow import *
from PyQt5.QtWidgets import *
import concurrent.futures, time


class MainWindow(QMainWindow):
    def __init__(self):

        DEFAULT_SIZE_A = (3, 3)
        DEFAULT_SIZE_B = (3, 1)

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # setting up main gui
        self.ui.tableViewA.setItemDelegate(NumberDelegate())
        self.ui.tableViewA.setModel(TableModel(DEFAULT_SIZE_A))

        self.ui.tableViewB.setItemDelegate(NumberDelegate())
        self.ui.tableViewB.setModel(TableModel(DEFAULT_SIZE_B))

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

        self.ui.m_addRowButton.clicked.connect(self.ui.tableViewA.model().addRow)
        self.ui.m_addRowButton.clicked.connect(self.ui.tableViewB.model().addRow)

        self.ui.m_removeRowButton.clicked.connect(self.ui.tableViewA.model().rmRow)
        self.ui.m_removeRowButton.clicked.connect(self.ui.tableViewB.model().rmRow)

        self.ui.m_addColumnButton.clicked.connect(self.ui.tableViewA.model().addColumn)
        self.ui.m_removeColumnButton.clicked.connect(self.ui.tableViewA.model().rmColumn)

        self.ui.m_checkButton.clicked.connect(self.processSystem)
        # \todo доделать actions из menubar
        # \todo ux

    # returns matrix A and vector b
    def matrices(self):
        return self.ui.tableViewA.model().value(), self.ui.tableViewB.model().value()

    # main app method
    def processSystem(self):
        # \todo должно вылазить окошко с результатом
        def x(sec):
            time.sleep(sec)
            print("end")
            return True

        waitMsgBox = QMessageBox(QMessageBox.NoIcon, "Результат", "Вычисление результата...", QMessageBox.Cancel)

        answer = None
        with concurrent.futures.ThreadPoolExecutor() as executor:
            answer = executor.submit(x, 2)#computeMatrix.compute_matrix, self.matrices())
            cancelButton = waitMsgBox.button(QMessageBox.Cancel)
            cancelButton.clicked.connect(answer.cancel)
            waitMsgBox.exec()
            # concurrent.futures.wait(answer)
            while answer.running():
                pass

        text = None
        if answer.result():
            text = "Система совместна!"
        else:
            text = "Система несовместна!"

        waitMsgBox.button(QMessageBox.Cancel).click()
        if not answer.cancelled():
            msgBox = QMessageBox(QMessageBox.NoIcon, "Результат", text, QMessageBox.Ok)
            msgBox.exec()
        pass

    def about(self):
        with open("README.md") as file:
            text = file.read()
            textEdit = QLabel(text, self)
            textEdit.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            textEdit.setFixedWidth(320)
            textEdit.setFixedHeight(240)
            textEdit.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            textEdit.setWindowFlag(Qt.Window)
            textEdit.setWindowFlag(Qt.WindowStaysOnTopHint)
            textEdit.setWindowModality(Qt.ApplicationModal)
            textEdit.show()
        pass
