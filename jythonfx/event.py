# -*- coding: utf-8 *-*
from javafx.event import EventHandler as EH

def EventHandler(method):
    class Temp(EH):
        def handle(self, event):
            method(event)
    return Temp()