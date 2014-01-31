# -*- coding: utf-8 *-*
import fix
fix.getJavaFX()
from javafx.fxml import FXMLLoader as FxmlL

class FXMLLoader(object):
    def __init__(self, fxmlfile):
        print fxmlfile
        fxml = FxmlL(self.getClass().getResource(fxmlfile))
        fxml.setController(self)
        fxml.setLocation("/")

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


