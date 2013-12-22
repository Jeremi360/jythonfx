# -*- coding: utf-8 *-*
import fix
fix.getJavaFX()
from javafx.scene.layout import AnchorPane
from javafx.fxml import FXMLLoader as FxmlL


class FXMLLoader(AnchorPane):
    def __init__(self, fxmlfile):
        fxml = FxmlL(self.getClass().getResource(fxmlfile))
        fxml.setController(self)
        root = fxml.load()
        self.getChildren().add(root)
        self.root = root
        self.setIds(self.root)

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


