import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.FilterList = QTreeWidget()
        self.setCentralWidget(self.FilterList)
        self.setWindowTitle("Form")
        self.setGeometry(50, 50, 800, 500)
        self.generateData()

    def generateData(self):
        self.FilterList.setColumnCount(3)
        self.FilterList.setHeaderLabels(["Filter Questions","File Size","Select"])
        DifficultyNode = QTreeWidgetItem(["Difficulty"])
        self.FilterList.addTopLevelItem(DifficultyNode)
        self.FilterList.itemChanged.connect(self.handleItemChanged)

        EasyNode = QTreeWidgetItem(["Easy","123.6MB","Unselected"])
        EasyNode.setCheckState(0, Qt.Unchecked)

        NormalNode = QTreeWidgetItem(["Normal"])
        NormalNode.setCheckState(0, Qt.Unchecked)

        HardNode = QTreeWidgetItem(["Hard"])
        HardNode.setCheckState(0, Qt.Unchecked)
        HardNode.setFlags(HardNode.flags() | QtCore.Qt.ItemIsEditable)
        MinNode = QTreeWidgetItem()

        DifficultyNode.addChild(EasyNode)
        # EasyNode.addChild(MinNode)
        DifficultyNode.addChild(NormalNode)
        DifficultyNode.addChild(HardNode)

        DifficultyNode1 = QTreeWidgetItem(["Difficulty1"])
        self.FilterList.addTopLevelItem(DifficultyNode1)
        EasyNode1 = QTreeWidgetItem(["Easy", "123.6MB", "Unselected"])
        EasyNode1.setCheckState(0, Qt.Unchecked)

        NormalNode1 = QTreeWidgetItem(["Normal"])
        NormalNode1.setCheckState(0, Qt.Unchecked)
        DifficultyNode1.addChild(EasyNode1)
        # self.setTextBox(MinNode, 1, "Min")
        # self.setTextBox(MinNode, 2, "Max")

    def setTextBox(self, item, column, text):
        box = QLineEdit(text)
        box.editingFinished.connect(lambda: item.setText(column, box.text()))
        self.FilterList.setItemWidget(item, column, box)

    def handleItemChanged(self, item, column):
        if item.checkState(column) == QtCore.Qt.Checked:
            print('Item Checked', item.text(column))
        elif item.checkState(column) == QtCore.Qt.Unchecked:
            print('Item Unchecked', item.text(column))





def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


main()