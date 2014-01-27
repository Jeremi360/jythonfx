# -*- coding: utf-8 *-*

import fix
fix.getJavaFX()
from javafx.event import EventHandler as EH

class EventHandler(EH):
    def __init__(self, method = None):
        super(EventHandler, self).__init__()

        if method != None:
            setattr(self, "handle", method)