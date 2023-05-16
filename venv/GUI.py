from PyQt5.QtWidgets import*
from PyQt5.QtCore import*

import siralamaGui2
class first_GUI(QWidget):
    def __init__(self):
        # super(first_GUI, self).__init__()
        # super().__init__()
        QWidget.__init__(self)
        siralamaGui2.Ui_MainWindow()


app = QApplication([])
widget = first_GUI()
widget.show()
app.exec_()