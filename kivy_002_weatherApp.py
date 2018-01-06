#Project began 01-05-2018
#Folowing along book "Creating Apps in Kivy" by Dusty Phillips
#End result will be a Weather App which can display C or F, search locations, store locations between
#       app instances, use device GPS to select current location
#Chapter 1 complete 01-05-2018

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class WeatherApp(App):
    pass

class AddLocationForm(BoxLayout):
    def search_location(self):
        print("Explicit is better than implicit.")

if __name__ == "__main__":
    WeatherApp().run()


















