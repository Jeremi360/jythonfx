# -*- coding: utf-8 *-*

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from jythonfx import fix
fix.getJavaFX()
from jythonfx.application import Application
from javafx.scene import Scene
from jythonfx.event import EventHandler as EH
from jythonfx.fxml import FXMLLoader
from javafx.scene.layout import AnchorPane


class Layout(FXMLLoader, AnchorPane):
    def __init__(self):
        super(Layout, self).__init__("FXMLSample.fxml")
        self.Button.setOnMouseClicked(EH(self.OnClick))
        self.clicked = False
        self.firstText = self.Text.getText()
        self.TextScale = self.TextScale.getScaleX()

    def OnClick(self, event):
        if not self.clicked:
            self.Text.setScaleX(self.TextScale/2)
            self.Text.setScaleY(self.TextScale/2)
            self.Text.setText("Hello FXML!")
        else:
            self.Text.setScaleX(self.TextScale)
            self.Text.setScaleY(self.TextScale)
            self.Text.setText(self.firstText)





class Sample(Application):
    def __init__(self):
        self.title = "FXML Sample"

    def start(self, stage):
        stage.setTitle(self.title)

        stage.setScene(Scene(Layout()))

        stage.show()

if __name__ == "__main__":
    Application.launch(Sample)
