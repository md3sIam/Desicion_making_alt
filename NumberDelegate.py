from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class NumberDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    # override
    def createEditor(self, widget=QWidget, option=QStyleOptionViewItem, index=QModelIndex):
        editor = QLineEdit(widget)
        return editor

    # override
    def setEditorData(self, widget=QWidget, index=QModelIndex):
        widget.setText(str(index.data()))
        pass

    # override
    def updateEditorGeometry(self, widget=QWidget, option=QStyleOptionViewItem, index=QModelIndex):
        widget.setGeometry(option.rect)
        pass

    # override
    def setModelData(self, widget=QLineEdit, model=QAbstractTableModel, index=QModelIndex):
        try:
            value = float(widget.text())
        except ValueError:
            return
        model.setData(index, QVariant(value), Qt.EditRole)
        pass
