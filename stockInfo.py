# Started 4/11/18
# Using Alpha Venture API for stock information

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.listview import ListItemButton


#ROOT CLASS
class StockApp(App):
    pass

class StartupScreen(BoxLayout):
    pass

class SearchButton(ListItemButton):
    pass

class SearchBar(BoxLayout):
    #search bar
    search_input = ObjectProperty() #search_input is created at a class level as instance of ObjectProperty
    
    #search button functionality
    def searchSymbol(self):
        #TODO add validation and functionality to search multiple symbols at once separate by commas
        #symbol = self.search_input.text #setting symbol from user input to 'symbol'
        #using list comprehension to strip whitespace (also splits at comma for future multi-symbol search)
        symbol = [x.strip() for x in self.search_input.text.split(',') if x != ''] #if x != '' so that it won't try splitting an empty string
        if len(symbol) < 1 or len(symbol) > 5: #validation: if not right length for a symbol, reject with message
            self.search_results.item_strings = ["Sorry that is not a valid stock symbol.", "Enter the symbol for a particular stock to see more information."]
        else: #validation: if passes test, proceed with search
            self.search_input.text = str(symbol[0]) #use index of list so the brackets aren't passed onto search_input when searching one symbol. Brackets will break the API url
            self.getStockInfo()

    def getStockInfo(self):
        #performs the UrlRequest to AlphaVenture API
        print("The user searched for {}.".format(self.search_input.text))
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={}&apikey=YXHPBU09EZW4JCV2".format(self.search_input.text)
        request = UrlRequest(url, self.foundSymbol, self.redirect, self.fail, self.err, self.progress) #UrlRequest(url, onSuccess, onRedirect, onFailure, onError, onProgress)
        print(request)
        
    def foundSymbol(self, request, data):
        #processes and reacts to the UrlRequest to AlphaVenture API
        print("Found symbol\n".format(request, data))
        if len(data['list']) == 0: #if there are no results, update message
            self.search_results.item_strings = ["There seems to be no results for that symbol. ", "Adjust your search and try again."]
        
    def redirect(self, request):
        print("Redirected\n" + str(request))
        
    def fail(self, request):
        print("Failed\n" + str(request))
        
    def err(self, request):
        print("Error\n" + str(request))
        
    def progress(self, request, data, extra):
        print("Progress\n{}\n{}\n{}\n\n".format(request, data, extra))
        




    def divScore(symbol_info):
    # Generate Div Score based on values of various properties
        #FAIL CASES



        ##########################
        
        score = 0
        #HIGH IMPACT
        
        #SUSPEND_RATIO SCORE
        susp_ratio = symbol_info[8]
        if susp_ratio == 0:   #ideal value
            sub_score = 25
        else:   #(suspend_ratio_max - suspend_ratio) / suspend_ratio_max
            percent = (0.2 - susp_ratio) / 0.2
            sub_score = 25 * percent

        score += sub_score
        print("SUSPEND_RATIO sub_score: {}".format(sub_score))
        sub_score = 0
        ##########################

        #YIELD SCORE
        yield_ratio = symbol_info[11]
        if yield_ratio >= 0.1 and yield_ratio < 0.2:
            diff = abs(0.1 - yield_ratio)
            percent = diff / 0.1
            sub_score = 6.5 + (percent * 2.25)
        elif yield_ratio >= 0.2 and yield_ratio < 0.3:
            diff = abs(0.2 - yield_ratio)
            percent = diff / 0.1
            sub_score = 12.5 + (percent * 6.25)
        elif yield_ratio >= 0.3 and yield_ratio < 0.4:
            diff = abs(0.3 - yield_ratio)
            percent = diff / 0.1
            sub_score = 19 + (percent * 6)
        elif yield_ratio >= 0.4 and yield_ratio < 0.5:
            diff = abs(0.4 - yield_ratio)
            percent = diff / 0.1
            sub_score = 9 + (percent * 3.25)
        elif yield_ratio >= 0.5 and yield_ratio < 0.6:
            diff = abs(0.5 - yield_ratio)
            percent = diff / 0.1
            sub_score = 2.5 + (percent * 3.75)
        score += sub_score
        print("YIELD_RATIO sub_score: {}".format(sub_score))
        sub_score = 0
        #############################

        #MEDIUM IMPACT
        #PRICE_RATIO SCORE
        price_ratio = symbol_info[4] / symbol_info[13] #price_ratio / funds_available
        if price_ratio >= 0.1 and price_ratio < 0.15:
            diff = abs(0.15 - price_ratio)
            percent = diff / 0.05
            sub_score = 6.29 - (percent * 3.37)
        elif price_ratio >= 0.15 and price_ratio < 0.25:
            diff = abs(0.25 - price_ratio)
            percent = diff / 0.1
            sub_score = 11.66 - (percent * 5.25)
        elif price_ratio >= 0.25 and price_ratio < 0.8:
            diff = abs(0.8 - price_ratio)
            percent = diff / 0.54
            sub_score = 2.79 - (percent * 1.63)
        score += sub_score
        print("PRICE_TO_FUNDS sub_score: {}".format(sub_score))
        sub_score = 0
        #####################################

        #REPAYMENT TERM SCORE
        repayment_term = symbol_info[9]
        if repayment_term >= 2 and repayment_term < 5:
            diff = abs(5 - repayment_term)
            percent = diff / 3
            sub_score = 6.29 - (percent * 3.37)
        elif repayment_term >= 5 and repayment_term < 6:
            diff = abs(6 - repayment_term)
            percent = diff / 1
            sub_score = 11.66 - (percent * 5.25)
        elif repayment_term >= 6 and repayment_term < 10:
            diff = abs(10 - repayment_term)
            percent = diff / 4
            sub_score = 2.79 - (percent * 1.63)
        score += sub_score
        print("REPAYMENT_TERM sub_score: {}".format(sub_score))
        sub_score = 0
        #########################################

        #CUT_RATIO SCORE
        cut_ratio = symbol_info[7]
        if cut_ratio == 0:
            sub_score = 11.66
        else:
            percent = (0.4 - cut_ratio) / 0.4
            sub_score = 11.66 * percent
        score += sub_score
        print("CUT_RATIO sub_score: {}".format(sub_score))
        sub_score = 0
        #########################################

        #LOW IMPACT
        #AVG_CUT SCORE
        div_history = symbol_info[5]
        div_history_cuts = []
        #populate list with cut values
        count = 0;
        while count < len(div_history):
            if count == 0: #if first div, skip
                count += 1
                print(count)
                continue
            elif div_history[count] < div_history[count - 1]: #if div is smaller than previous
                div_history_cuts.append(abs(div_history[count] - div_history[count-1])) #append the absolute value of the difference
                print("elif")
            count += 1
            print(count)
        avg_cut = sum(div_history_cuts) / len(div_history_cuts)

        #scoring
        if avg_cut >= 0 and avg_cut < 0.1:
            diff = abs(0.1 - avg_cut)
            percent = diff / 0.1
            sub_score = 5 - (percent * 1.5)
        elif avg_cut >= 0.1 and avg_cut < 0.5:
            diff = abs(0.5 - avg_cut)
            percent = diff * 0.4
            sub_score = 3.45 - (percent * 2.95)
        score += sub_score
        print("AVG_CUTS sub_score: {}".format(sub_score))
        sub_score = 0
        ###############################################

        #DIV_INCREASE SCORE
        #div_change is the percent the current div is in relation to the initial div payment.
        #the higher this number, the better (in most cases)
        #1 == 100% of initial div payment, which means the current div is the same as initial_div.
        div_change = symbol_info[1] / symbol_info[2]
        if div_change >= 10:
            sub_score = 5
        elif div_change >= 0.2 and div_change < 1:
            diff = abs(0.2 - div_change)
            percent = diff / 0.8
            sub_score = 0.5 + (percent * 0.95)
        elif div_change >= 1 and div_change < 1.5:
            diff = abs(1.5 - div_change)
            percent = diff / 0.5
            sub_score = 1.5 + (percent * 1.45)
        elif div_change >= 1.5 and div_change < 10:
            diff = abs(3 - div_change)
            percent = diff / 8.5
            sub_score = 3 + (percent * 2)
        score += sub_score
        print("DIV_CHANGE sub_score: {}".format(sub_score))
        sub_score = 0
        ###############################################

        #YEARS_PAYMENT SCORE
        #higher is better
        years_payment = symbol_info[12]

        if years_payment >= 80:
            sub_score = 5
        elif years_payment >=3 and years_payment < 10:
            diff = abs(3 - years_payment)
            percent = diff / 7
            sub_score = 0.5 + (percent * 0.95)
        elif years_payment >= 10 and years_payment < 80:
            diff = abs(10 - years_payment)
            percent = diff / 70
            sub_score = 1.5 + (percent * 3.5)
        score += sub_score
        print("YEARS_PAYMENT sub_score: {}".format(sub_score))
        sub_score = 0
        ################################################

        print("Final score is {}. ".format(score))


    symbol_list = ["OXLC", 0.14, 0.25, 10.51, 10.53, [0.25, 0.25, 0.14, 0.14], 1.62, 0.28, 0, 6.48, 0.56, 0.1538, 7, 50]
    divScore(symbol_list)


if __name__ == "__main__":
    StockApp().run()
    
