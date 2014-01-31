# -*- coding: utf-8 *-*

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from jythonfx import fix
fix.getJavaFX()
from jythonfx.application import Application
from javafx.scene import *
from jythonfx.event import EventHandler as EH

class HiJavaFX(Application):

    def start(self, stage):
        '''
        start - mine method of App
        arg stage - needed to change App's window
        '''

        self.title = "JythonFX"

        label = "Click Me!"
        button = control.Button(label) #crate button
        button.setOnAction(EH(self.OnButtonClicked)) #set button event on click

        self.pane = layout.StackPane() #create layout of scene
        self.pane.getChildren().add(button)#add button to scene

        self.width = 300
        self.height = 250

        stage.setTitle(self.title) #set caption for App's window

        stage.setScene(Scene(self.pane, self.width, self.height))
        #set self.pane as App's layout with self.width as App's width and self.height as App's height

        stage.show()#show App

    def OnButtonClicked(self, event):
        #handle event for clicked button
        #arg event - needed to get event data

        message = unicode("Hello World w JythonFX")#unicode to fix non English chars
        print message #display massage in console

if __name__ == "__main__": #run app
    Application.launch(HiJavaFX)

