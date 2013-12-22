# -*- coding: utf-8 *-*
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import jythonfx
jythonfx.getJavaFX()
from javafx.application import Application as Appfx



class Application(Appfx):
    def __init__(self):
        #this override method self.launch using self.__launch__
        setattr(self, "launch", self.__launch__)

    def __launch__(self, app):
        Appfx.launch(app().getClass(), [])
