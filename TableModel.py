# importing modules
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant
# importing namespaces for enums
from PyQt5.QtCore import Qt


class TableModel(QAbstractTableModel):
    def __init__(self, size=(3, 3), parent=None):
        super().__init__(parent)
        self.__matrix = [[0 for _ in range(size[1])] for _ in range(size[0])]
        print(self.__matrix)
        pass

    def value(self):
        return self.__matrix

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

    def addRow(self):
        self.insertRows(len(self.__matrix) - 1, 1, None)
        pass

    def rmRow(self):
        if len(self.__matrix) > 1:
            self.removeRows(len(self.__matrix) - 1, 1, None)
        pass

    def addColumn(self):
        self.insertColumns(len(self.__matrix[0]) - 1, 1, None)
        pass

    def rmColumn(self):
        if len(self.__matrix[0]) > 1:
            self.removeColumns(len(self.__matrix[0]) - 1, 1, None)
        pass

    # override
    def insertRows(self, p_int, p_int_1, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), p_int, p_int)
        self.__matrix += [[0 for _ in range(len(self.__matrix[0]))]]
        self.endInsertRows()
        return True

    # override
    def insertColumns(self, p_int, p_int_1, parent=None, *args, **kwargs):
        self.beginInsertColumns(QModelIndex(), p_int, p_int)
        for row in self.__matrix:
            row.append(0)
        self.endInsertColumns()
        pass

    # override
    def removeRows(self, p_int, p_int_1, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), p_int, p_int)
        self.__matrix.pop()
        self.endRemoveRows()
        return True

    # override
    def removeColumns(self, p_int, p_int_1, parent=None, *args, **kwargs):
        self.beginRemoveColumns(QModelIndex(), p_int, p_int)
        for row in self.__matrix:
            row.pop()
        self.endRemoveColumns()
        pass
