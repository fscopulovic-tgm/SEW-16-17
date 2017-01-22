"""
@author Filip Scopulovic
@date 12-18-2016
@use Controller for the A10_Shared_Memory class
"""
import sys
from PySide.QtCore import *
from PySide.QtGui import *
import main_window, model

class Controller(QWidget):
    """
    Controller for the GUI
    """

    def __init__(self, parent=None):
        """
        Constructor for the controller
        """
        super(Controller, self).__init__(parent)

        self.__window = main_window.Ui_paint_widget()
        self.__window.setupUi(self)

        self.__model = model.Model([913, 609], 2, 10)

        self.green_slider = self.__window.horizontalSlider_2
        self.blue_slider = self.__window.horizontalSlider_3
        self.red_slider = self.__window.horizontalSlider_4
        self.size_slider = self.__window.horizontalSlider

        self.new_point = self.__window.new_button
        self.remove_point = self.__window.remove_button

        self.new_point.clicked.connect(self.__new_point)
        self.remove_point.clicked.connect(self.__model.del_last_process)

    def __new_point(self):
        """
        Calls the self.__model.new_point() method

        :return None:
        """
        self.__model.new_point(5, [256, 256, 256])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())