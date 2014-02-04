# -*- coding: utf-8 *-*
from java.lang import System as jsys
from javax.swing import JOptionPane as jop
from java.net import URL as url
from java.awt import Desktop as desk

import sys
import os
import platform

def checkJavaVer():
    ver = jsys.getProperty("java.version")
    ver = ver.split(".")
    ver[-1] = float(ver[-1].replace("_", "."))
    ver[0] = float(str(ver[0]) + "." + str(ver[1]))
    ver.pop(1)

    def mess():
        mess = unicode("""Too old java version pleas upgrade to  7u11 or higher. \n
                Zbyt stara wersja Java proszę zaktualizować do 7u11 lub wyższej.""")
        jop.showMessageDialog(None, mess)

        try:
            if platform.dist() == ('debian', 'wheezy/sid', ''):#for ubuntu
                getjava = "http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html"

            else:
                getjava = "http://www.java.com"

            desk.getDesktop().browse(url(getjava).toURI())

        except:
            pass

        sys.exit()

    print  ver

    if ver[0] <= 1.6:
        mess()

    else:
        if ver[1] <= 0.11:
            mess()

def getJavaFX():
    checkJavaVer()
    home = jsys.getProperty("java.home")

    try:
        sys.path.insert(0, os.path.join(home, "lib", "jfxrt.jar"))

    except:
        pass
