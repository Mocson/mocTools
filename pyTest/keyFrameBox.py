from maya import cmds,mel
from PySide import QtGui
from .lib import qt

def cpy():
    mel.eval("timeSliderCopyKey;")

def pst():
    mel.eval("timeSliderPasteKey false;")

def dlt():
    mel.eval("timeSliderClearKey;")

def cut():
    mel.eval("timeSliderCutKey;")

class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Set Key')
        self.resize(250,100)

        widget = KeyButton()
        self.setCentralWidget(widget)

class KeyButton(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(KeyButton, self).__init__(*args, **kwargs)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)

        button = QtGui.QPushButton('Copy')
        button.clicked.connect(qt.Callback(cpy))
        layout.addWidget(button)

        button = QtGui.QPushButton('Paste')
        button.clicked.connect(qt.Callback(pst))
        layout.addWidget(button)

        button = QtGui.QPushButton('Delete')
        button.clicked.connect(qt.Callback(dlt))
        layout.addWidget(button)

        button = QtGui.QPushButton('Cut')
        button.clicked.connect(qt.Callback(cut))
        layout.addWidget(button)

def main():
    app = MainWindow(qt.getMayaWindow())
    app.show()
