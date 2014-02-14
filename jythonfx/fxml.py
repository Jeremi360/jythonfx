# -*- coding: utf-8 *-*
import fix
fix.getJavaFX()
from javafx.fxml import FXMLLoader as FxmlL
from java.io import File


class FXMLLoader(object):
    def __init__(self, fxmlfile):
        print fxmlfile
        fxml = FxmlL(File(fxmlfile).toURL())
        fxml.setController(self)

        self.body = fxml.load()
        self.getChildren().add(self.body)
        self.setIds(self.body, "getChildren()")


    def setIds(self, children, way, prefix = ""):
        for c in getattr(children, way):
            try:
                if c.getId != "":
                    setattr(self, prefix + c.getId(), c)
                    print "self." + prefix + c.getId()

                try:
                    if getattr(c, way) != []:
                        self.setIds(c, c.getId())
                except:
                    pass

            except:
                pass



