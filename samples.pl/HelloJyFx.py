# -*- coding: utf-8 *-*
#powyższa linjka włącza polskie kodowanie w python
# Copyright (C) 2012 Jeremi Bieracki <jeremi360@gmail.com>
# bazuje na: http://www.javamexico.org/blogs/jose_manuel/iniciando_con_javafx_jython_javafx

# "*" znaczy, że jest zaimportowane wszystko z danej biblioteki
from javafx.application import Application
from javafx.scene import *
from javafx.event import EventHandler

'''# komentarz wielo liniowy
w Jython/Python zamiast klamerek jako pocztków i końców bloków kodu używa
się wcieć - jedo wcięcie to 4 spacje - Eclipse i większość Edytorów
wspierających Pythona zamiena automatycznie tabulację na 4 spacje
'''

class HiJavaFX(Application):
# deklaracja klasy aplikacji -dziedziczy i implementuje Application i EventHandler

    def start(self, stage):
        '''start - właściwa część programu
        argument stage - potrzebna by móc zmienniać właściwości okna applikacji
        '''

        self.title = "JythonFX" #deklaracja zmiennej typu string/char (łańcuch znaków lub pojedynczy znak)
        #słowo kluczowe self pozwoli odwołać się do tej zmiennej z z innych metod klasy i na wywołanie ich w innej części kodu

        label = "Kliknij" #brak słowa kluczowego self - zmienna dostępna tylko w tym fragmencie kodu
        button = control.Button(label) #tworzymy przycisk - scene.control
        button.setOnAction(OnButtonClicked()) #ustawiamy akcję przycisku

        self.pane = layout.StackPane() #tworzymy układ - scene.layout
        self.pane.getChildren().add(button)#oddajemy przycisk do układu

        self.width = 300 #deklaracja zmiennej będącej liczbą
        self.height = 250

        stage.setTitle(self.title) #nadajemy tutuł oknu(stage)

        stage.setScene(Scene(self.pane, self.width, self.height))
        #ustawiamy pane jako układ i rozmiar sceny/okna

        stage.show()#wyświetlamy okno

class OnButtonClicked(EventHandler):
    #handle - obsługa zdarzeń dzięki implementacji EventHandler
    def handle(self, event):
        '''argument event aby móc skorzytać z danych
            o ustawionym do obsługi wydarzeniu np.:
            xy kursora myszy, przycisk na klawiaturze'''

        message = "Witaj świecie w JythonFX"
        print message #wyświatlamy napis

if __name__ == "__main__":#uruchamia aplikacje
    Application.launch(HiJavaFX().getClass(), [])
    
