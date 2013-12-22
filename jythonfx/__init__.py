# -*- coding: utf-8 *-*

import fxml
import event
import application

from java.lang import System as _jsys
from javax.swing import JOptionPane as _jop
from java.net import URL as _url
from java.awt import Desktop as _desk

import sys as _sys
import os as _os

def _checkJavaVer():
    ver = _jsys.getProperty("java.version")
    print "JVM version:", ver
    ver = ver.split(".")
    ver[-1] = float(ver[-1].replace("_", "."))
    ver[0] = float(str(ver[0]) + "." + str(ver[1]))
    ver.pop(1)

    def mess():
        mess = unicode("""Too old java version pleas upgrade to  7u11 or higher \n
                Zbyt stara wersja Java proszę zaktualizować do 7u11""")
        _jop.showMessageDialog(None, mess)
        try:
            _desk.getDesktop().browse(_url("http://www.java.com").toURI());
        except:
            pass

        _sys.exit()

    if ver[0] <= 1.6:
        mess()
    else:
        if ver[1] <= 0.11:
            mess()

def getJavaFX():
    _checkJavaVer()
    home =  _jsys.getProperty("java.home")
    print home
    try:
        _sys.path.insert(0, _os.path.join(home, "lib", "jfxrt.jar"))
    except:
        pass

