# -*- coding: utf-8 *-*

import fix
fix.getJavaFX()
from javafx.event import EventHandler as EH

def EventHandler(method):
    class Temp(EH):
        def handle(self, event):
            method(event)
    return Temp()