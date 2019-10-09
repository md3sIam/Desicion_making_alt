from PyQt5.QtCore import *


class TableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__matrix = [list(range(1, 4)),
                         list(range(11, 14))]
        pass

    # override
    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.__matrix)

    # override
    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.__matrix[0])

    # override
    def data(self, model_index=QModelIndex(), role=Qt.EditRole):
        if not model_index.isValid():
            return QVariant()

        if role == Qt.CheckStateRole:
            return QVariant()

        if role == Qt.TextAlignmentRole:
            return Qt.AlignHCenter | Qt.AlignVCenter
        else:
            return self.__matrix[model_index.row()][model_index.column()]

    # override
    def setData(self, model_index=QModelIndex(), value=QVariant(), role=None):
        self.__matrix[model_index.row()][model_index.column()] = value
        self.dataChanged.emit(model_index, model_index)
        return True

    # override
    def flags(self, model_index=QModelIndex()):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled

    # # override
    # def insertRows(self, p_int, p_int_1, parent=None, *args, **kwargs):
    #     self.beginInsertRows()
    #     # code
    #     self.endInsertRows()
    #     pass
    #
    # # override
    # def insertColumns(self, p_int, p_int_1, parent=None, *args, **kwargs):
    #     self.beginInsertColumns()
    #     self.endInsertColumns()
    #     pass
    #
    # # override
    # def removeRows(self, p_int, p_int_1, parent=None, *args, **kwargs):
    #     self.beginRemoveRows()
    #     self.endRemoveRows()
    #     pass
    #
    # # override
    # def removeColumns(self, p_int, p_int_1, parent=None, *args, **kwargs):
    #     self.beginRemoveColumns()
    #     self.endRemoveColumns()
    #     pass
