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


class Layout(FXMLLoader, AnchorPane):#second class must, be the same as root in FXML file
    def __init__(self):
        super(Layout, self).__init__("FXMLSample.fxml")#FXML file to load
        self.Button.setOnMouseClicked(EH(self.OnClick))
        self.clicked = False
        self.firstText = self.Text.getText()
        self.TextScaleX = self.Text.getScaleX()
        self.TextScaleY = self.Text.getScaleY()

    def OnClick(self, event):
        if not self.clicked:
            self.Text.setScaleX(self.TextScaleX/2)
            self.Text.setScaleY(self.TextScaleY/2)
            self.Text.setText("Hello FXML!")
            self.clicked = True
        else:
            self.Text.setScaleX(self.TextScaleX)
            self.Text.setScaleY(self.TextScaleY)
            self.Text.setText(self.firstText)
            self.clicked = False


class Sample(Application):
    def __init__(self):
        self.title = "FXML Sample"

    def start(self, stage):
        stage.setTitle(self.title)

        stage.setScene(Scene(Layout()))

        stage.show()

if __name__ == "__main__":
    Application.launch(Sample)
