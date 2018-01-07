#Project began 01-05-2018
#Folowing along book "Creating Apps in Kivy" by Dusty Phillips
#End result will be a Weather App which can display C or F, search locations, store locations between
#       app instances, use device GPS to select current location
#Chapter 1 complete 01-05-2018
#Chapter 2 complete 01-06-2018

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest

class WeatherApp(App):
    pass

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty() #search_input property is created at class level as instance of ObjectProperty class
    
    def search_location(self): #can print to console, this is called when button is pressed (defined in .kv file)
        print("The user searched for '{}'".format(self.search_input.text))
        search_template = "http://api.openweathermap.org/data/2.5/find?q={}&type=like&APPID=" + "YOUR_API_KEY" #free account, get api key from open weather map
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location, self.redirect, self.fail, self.err, self.progress)

        
    def found_location(self, request, data):
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        self.search_results.item_strings = cities
        
    #debugging functions that mark if something unusual happened with UrlRequest above
    def redirect(self, request, data):
        print("request Redirected")
        print(str(request))
        print(str(data))

    def fail(self, request, data):
        print("request Failed")
        print(str(request))
        print(str(data))

    def err(self, request, data):
        print("request Error")
        print(str(request))
        print(str(data))

    def progress(self, request, data, extra):
        print("request Progress")
        print(str(request))
        print(str(data))
        print(str(extra))
    
        

if __name__ == "__main__":
    WeatherApp().run()
