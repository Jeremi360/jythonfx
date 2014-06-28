# -*- coding: utf-8 *-*
from java.lang import System as jsys
from javax.swing import JOptionPane as jop
from java.net import URL as url
from java.awt import Desktop as desk

import sys
import os
import platform

def mess():
    print "unicode() - nie chce dzialc/n" +"unicode() - don't work :("
    part01 = "Too old java version pleas upgrade to  7u11 or higher.\n"
    message =  part01 + "Zbyt stara wersja Java prosze zaktualizowac do 7u11 lub wyzszej."
    jop.showMessageDialog(None, message)

    try:
        if platform.dist() == ('debian', 'wheezy/sid'):#for ubuntu
            getjava = "http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html"

        else:
            getjava = "http://www.java.com"

        desk.getDesktop().browse(url(getjava).toURI())

    except:
        pass

    sys.exit()

def getJavaFX():
    ver = jsys.getProperty("java.version")
    ver = ver.split(".")
    ver[-1] = float(ver[-1].replace("_", "."))
    ver[0] = float(str(ver[0]) + "." + str(ver[1]))
    ver.pop(1)

    print  ver

    if ver[0] <= 1.6:
        mess()

    elif ver[0] == 1.7:
        if ver[1] <= 0.11:
            mess()
            home = jsys.getProperty("java.home")

            try:
                jfxrt = os.path.join(home, "lib", "jfxrt.jar")
                sys.path.insert(0, jfxrt)

            except:
                part01 = "Nie można odnalesc biblioteki JavaFX(jfxrt.jar).\n"
                message = part01 + "Unable to find JavaFX lib (jfxrt.jar)."
                jop.showMessageDialog(None, message)
                sys.exit()

    else:
        pass


