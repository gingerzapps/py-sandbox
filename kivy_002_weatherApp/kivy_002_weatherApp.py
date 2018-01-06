#Project began 01-05-2018
#Folowing along book "Creating Apps in Kivy" by Dusty Phillips
#End result will be a Weather App which can display C or F, search locations, store locations between
#       app instances, use device GPS to select current location
#Chapter 1 complete 01-05-2018

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class WeatherApp(App):
    pass

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty() #search_input property is created at class level as instance of ObjectProperty class
    
    def search_location(self): #can print to console, this is called when button is pressed (defined in .kv file)
        print("The user searched for '{}'".format(self.search_input.text)) 

if __name__ == "__main__":
    WeatherApp().run()


















