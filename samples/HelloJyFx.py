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
        '''start - właściwa część programu
        argument stage - potrzebna by móc zmienniać właściwości okna applikacji
        '''

        self.title = "JythonFX" #deklaracja zmiennej typu string/char (łańcuch znaków lub pojedynczy znak)
        #słowo kluczowe self pozwoli odwołać się do tej zmiennej z z innych metod klasy i na wywołanie ich w innej części kodu

        label = "Kliknij" #brak słowa kluczowego self - zmienna dostępna tylko w tym fragmencie kodu
        button = control.Button(label) #tworzymy przycisk - scene.control
        button.setOnAction(EH(self.OnButtonClicked)) #ustawiamy akcję przycisku

        self.pane = layout.StackPane() #tworzymy układ - scene.layout
        self.pane.getChildren().add(button)#oddajemy przycisk do układu

        self.width = 300 #deklaracja zmiennej będącej liczbą
        self.height = 250

        stage.setTitle(self.title) #nadajemy tutuł oknu(stage)

        stage.setScene(Scene(self.pane, self.width, self.height))
        #ustawiamy pane jako układ i rozmiar sceny/okna

        stage.show()#wyświetlamy okno

    def OnButtonClicked(self, event):
        #obsługa zdarzenia będącego kilknienciem na przycisku
        '''argument event aby móc skorzytać z danych
            o ustawionym do obsługi wydarzeniu np.:
            xy kursora myszy, przycisk na klawiaturze'''

        message = unicode("Witaj świecie w JythonFX")
        print message #wyświatlamy napis w konsoli

if __name__ == "__main__":#uruchamia aplikacje
    Application.launch(HiJavaFX)

