# -*- coding: utf-8 -*-
from maya import OpenMayaUI, cmds
import imp

try:
    imp.find_module('PySide2')
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore import *

except ImportError:
    from PySide.QtGui import *
    from PySide.QtCore import *

try :
    import shiboken2 as shiboken
except:
    import shiboken



def getMayaWindow():
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    widget = shiboken.wrapInstance(long(ptr), QWidget)
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
