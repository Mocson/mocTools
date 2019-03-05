# -*- coding:utf-8 -*-
from maya import cmds,mel
from ..lib import qt
import pymel.core as pm
import imp
import os


try:
    imp.find_module('PySide2')
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore import *

except ImportError:
    from PySide.QtGui import *
    from PySide.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('karakore')
        self.resize(300,100)

        widget = mainButton()
        self.setCentralWidget(widget)

class mainButton(QWidget):
    def __init__(self, *args, **kwargs):
        super(mainButton, self).__init__(*args, **kwargs)

        self.txt = ''

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.matbutton = QPushButton('SelectMaterial')
        self.matbutton.clicked.connect(self.secmat)
        self.layout.addWidget(self.matbutton)

        self.lineEdit = QLineEdit('lineEdit')
        self.lineEdit.setText('selectMat')
        self.layout.addWidget(self.lineEdit)

        self.button = QPushButton('SelectFile')
        self.button.clicked.connect(self.texFile)
        self.layout.addWidget(self.button)

        self.texSec = QLineEdit('lineEdit')
        self.texSec.setText('filePath')
        self.layout.addWidget(self.texSec)

        self.buttonA = QPushButton('BaseColor')
        self.buttonA.clicked.connect(self.clrBase)
        self.layout.addWidget(self.buttonA)

        self.buttonB = QPushButton('Specular')
        # self.buttonB.clicked.connect(self.printTxt)
        self.layout.addWidget(self.buttonB)

    def getFilePath(self):
        self.fileD = QFileDialog.getOpenFileName(self,'open Texture',os.path.expanduser('~') + '/Desktop')

        return self.fileD[0]

    def texFile(self):
        path = self.getFilePath()
        self.texSec.setText(path)

    def secmat(self):
        objs = pm.ls(sl=True)
        SG = pm.listConnections(objs, s=False, d=True, t='shadingEngine')
        mat = pm.ls(pm.listConnections(SG, s=True, d=False), mat=True)
        StrMat = ''.join(mat[0])
        print StrMat
        if not StrMat:
            cmds.error('Select a Material')
        self.lineEdit.setText(StrMat)

    def clrBase(self):
        baseColor = pm.shadingNode( 'file', asTexture=True, isColorManaged=True, n='baseColorFile')
        cc = pm.shadingNode( 'colorCorrect', asTexture=True, isColorManaged=True, n='baseCC')
        print baseColor
        texPath = self.texSec.text()
        nowTex = self.lineEdit.text()
        cmds.setAttr(baseColor+'.fileTextureName',texPath,type="string")

        pm.connectAttr(cc+'.outColor', nowTex+'.baseColor', f=True)
        pm.connectAttr(baseColor+'.outColor', cc+'.inColor', f=True)

    def spcBase(self):
        spcColor = pm.shadingNode ( 'file', asTexture=True, isColorManaged=True, n='spcColorFile')
        cc = pm.shadingNode( 'colorCorrect', asTexture=True, isColorManaged=True, n='specCC')
        texPath = self.texSec.text()
        nowTex = self.lineEdit.text()
        cmds.setAttr(spcColor+'.fileTextureName',texPath,type="string")

        pm.connectAttr(cc+'.outColor', nowTex+'.specularColor', f=True)
        pm.connectAttr(spcColor+'.outColor', cc+'.inColor', f=True)

def main():
    app = MainWindow(qt.getMayaWindow())
    app.show()
