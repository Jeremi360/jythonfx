# -*- coding: utf-8 *-*
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import jythonfx
jythonfx.getJavaFX()
from javafx.event import EventHandler as EH

def EventHandler(method):
    class Temp(EH):
        def handle(self, event):
            method(event)
    return Temp()