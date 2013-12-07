# -*- coding: utf-8 *-*
from javafx.scene.layout import AnchorPane
from javafx.fxml import FXMLLoader as FxmlL


class FXMLLoader(AnchorPane):
    def __init__(self, fxmlfile, ff = 2):
        fxml = FxmlL(self.getClass().getResource(fxmlfile))
        fxml.setController(self)
        root = fxml.load()
        self.getChildren().add(root)
        self.root = root
        self.setIds(self.root, ff)


    def fixFontSize(self, c, ff = 1):
        try:
            f = c.getFont()
            s = f.getSize()*ff
            f = f.font(s)
            c.setFont(f)
            print "set", c.getId(), "font size to", str(s)
        except:
            pass

    def setIds(self, children, ff = 1, prefix = ""):
        for c in children.getChildren():
            try:
                self.fixFontSize(c, ff)
                setattr(self, prefix + c.getId(), c)
                print "self." + prefix + c.getId()
                try:
                    self.setIds(c, ff, c.getId() + "_")
                except:
                    pass
            except:
                pass
