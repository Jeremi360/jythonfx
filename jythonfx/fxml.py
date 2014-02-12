# -*- coding: utf-8 *-*
import fix
from test.test_isinstance import Child
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
        self.setIds(self.body)

    def inSetIds(self, c, prefix = ""):
        if c.getId != "":
            setattr(self, prefix + c.getId(), c)
            print "self." + prefix + c.getId()

            try:
                if c.getChildren() != []:
                    self.setIds(c, c.getId())

            except:
                pass

    def setIds(self, children, prefix = ""):
        try:
            for c in children.getChildren():
                self.inSetIds(c, prefix)

        except:
            try:
                for c in children.getChildrenUnmodifiable():
                    self.inSetIds(c, prefix)

            except:
                pass




