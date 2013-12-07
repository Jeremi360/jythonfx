# -*- coding: utf-8 *-*
from javafx.application import Application as Appfx



class Application(Appfx):
    def __init__(self):
        #this override method self.launch using self.__launch__
        setattr(self, "launch", self.__launch__)

    def __launch__(self, app):
        Appfx.launch(app().getClass(), [])
