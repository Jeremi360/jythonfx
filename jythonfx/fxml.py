# -*- coding: utf-8 *-*
import fix
fix.getJavaFX()
from javafx.fxml import FXMLLoader as FxmlL
from java.net import URL


class FXMLLoader(object):
    def __init__(self, fxmlfile):
        print fxmlfile
        root = "file:///"
        uroot = URL(root)
        fxml = FxmlL(URL(root + fxmlfile))
        fxml.setController(self)
        fxml.setLocation(uroot)

        self.body = fxml.load()
        self.getChildren().add(self.body)
        self.setIds(self.body)


    def setIds(self, children, prefix = ""):
        for c in children.getChildren():
            try:
                if c.getId != "":
                    setattr(self, prefix + c.getId(), c)
                    print "self." + prefix + c.getId()

                try:
                    if c.getChildren() != []:
                        self.setIds(c, c.getId() + "_")
                except:
                    pass

            except:
                pass


