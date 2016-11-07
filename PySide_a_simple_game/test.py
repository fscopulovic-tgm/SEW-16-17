import sys
from MyView import *
from PySide import QtGui

app = QtGui.QApplication(sys.argv)
win = QtGui.QMainWindow()
# create model view and controller.
view = Ui_Spiel()

view.setupUi(win)  # this initializes the created UI

win.show()
app.exec_()
sys.exit()