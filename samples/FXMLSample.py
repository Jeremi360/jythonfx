# -*- coding: utf-8 *-*
#TODO: license & copyrights

from screens import Menu
from res.values.string import window_title

from jythonfx.application import Application
from javafx.scene import Scene



class GameFX(Application):
    def __init__(self):
        self.title = window_title

    def start(self, stage):
        stage.setTitle(self.title)

        m = Menu()
        stage.setScene(Scene(m))

        stage.show()

if __name__ == "__main__":
    Application.launch(GameFX)
