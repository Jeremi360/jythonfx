# -*- coding: utf-8 *-*
import fix
fix.getJavaFX()
from javafx.fxml import FXMLLoader as FxmlL
from java.io import File


class FXMLLoader(object):
    def __init__(self, fxmlfile, prefix = ""):
        print fxmlfile
        fxml = FxmlL(File(fxmlfile).toURL())
        fxml.setController(self)

        self.body = fxml.load()
        self.getChildren().add(self.body, prefix)
        self.setIds(self.body)


    def setIds(self, children, prefix = ""):
        for c in children.getChildren():
            try:
                if c.getId != "":
                    setattr(self, prefix + c.getId(), c)
                    print "self." + prefix + c.getId()

                try:
                    if c.getChildren() != []:
                        self.setIds(c, c.getId())
                except:
                    pass

            except:
                pass

    def setTabsIds(self, children, prefix = ""):
        for c in children.getTabs():
            try:
                if c.getId != "":
                    setattr(self, prefix + c.getId(), c)
                    print "self." + prefix + c.getId()

                try:
                    if c.getChildren() != []:
                        self.setIds(c, c.getId())
                except:
                    pass

            except:
                pass


