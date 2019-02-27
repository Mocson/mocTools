# -*- coding: utf-8 -*-
from maya import OpenMayaUI, cmds
from PySide import QtGui
import shiboken

def getMayaWindow():
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    widget = shiboken.wrapInstance(long(ptr), QtGui.QWidget)
    return widget

class Callback(object):
    def __init__(self, func, *args, **kwargs):
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self):
        cmds.undoInfo(openChunk=True)
        try:
            return self.__func(*self.__args, **self.__kwargs)

        except:
            raise

        finally:
            cmds.undoInfo(closeChunk=True)
