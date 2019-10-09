from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class NumberDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    # override
    def createEditor(self, widget=QWidget, option=QStyleOptionViewItem, index=QModelIndex):
        editor = QDoubleSpinBox(widget)
        editor.setMaximum(999999.99999)
        editor.setDecimals(5)
        return editor

    # override
    def setEditorData(self, widget=QWidget, index=QModelIndex):
        widget.setValue(float(index.data()))
        pass

    # override
    def updateEditorGeometry(self, widget=QWidget, option=QStyleOptionViewItem, index=QModelIndex):
        widget.setGeometry(option.rect)
        pass

    # override
    def setModelData(self, widget=QWidget, model=QAbstractItemModel, index=QModelIndex):
        try:
            value = float(widget.value())
        except:
            value = 0
        model.setData(index, value, Qt.EditRole)
        pass
