#StockRequest
#URL REQUEST stock information and display it in command line

import json
import requests


api_key = "YXHPBU09EZW4JCV2"
api_base_url = "https://www.alphavantage.co/query?"
#symbol = {symbol(0), div_now(1), div_initial(2), price_now(3), price_purchase(4), [div_history](5),
#                   annual_div(6), cut_ratio(7), suspend_ratio(8), repayment_term(9), xxx(10), yield_ratio(11),
#                   years_payments(12), xxx(13)


symbol = ["OXLC",]
print(symbol)
function = "TIME_SERIES_MONTHLY_ADJUSTED"
request_url = "{0}function={1}&symbol={2}&apikey={3}".format(api_base_url, function, symbol[0], api_key)
print(request_url)



req = requests.get(request_url)
response = json.loads(req.content.decode())
keys = ["Meta Data", "Monthly Adjusted Time Series"]
wanna_be_keys = ["open", "high",
                  "low", "close", "adjusted close", "volume", "dividend amount"]


#iterating through json response for debugging
#eventually use this for assigning values to symbol[]

#print("\n\nresponse.items()\n================")
#print(response.items())
people = { "Meta Data" : {'name': 'John', 'age': '27', 'sex': 'Male'},
          "Monthly Adjusted Time Series" : {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people)
print(people[keys[1]]['name'])
print(people[keys[1]]['age'])
print(people[keys[1]]['sex'])


print("\n\n\n\n=======================\n=======================\n\n")
def listKeys(dic):
    #iterates through dictionary and collects keys (and subkeys) above a specified index (the index simulated
    #       by the incremented "count" variable
    #collects keys that will be used to access sub-dictionaries, and assign values to manual list for manipulation
    #       in the score calculator
    #this code is reusable, not specific to any dictionary
    result = []
    count = 0
    condition = [2,3] #indices for values that are guaranteed to be present and desired for later use
    for key in dic.keys():
        if (count >= 6 or count in condition):
            result.append(key)
        count += 1

        for subkey in dic[key].keys():
            if (count >= 6 or count in condition):
                result.append(subkey)
            count +=1

    return result
#
#
# #########################################

print("\n\n\n\n=======================\n=======================\n\n")

list_response = listKeys(response)
for item in list_response:
    print("{}\n".format(item))

print(list_response)
print()
print()
symbol = [response[keys[0]][list_response[0]], response[keys[0]][list_response[1]]]
print(symbol)




#symbol = {symbol(0), div_now(1), div_initial(2), price_now(3), price_purchase(4), [div_history](5),
#                   annual_div(6), cut_ratio(7), suspend_ratio(8), repayment_term(9), xxx(10), yield_ratio(11),
#                   years_payments(12), xxx(13)



#MAYBE HAVE TWO REQUESTS, ONE WITH MONTHY (DIV) INFO
#       AND ANOTHER WITH CURRENT INFO FOR PRICE AND MORE VOLITILE INFO


#DIV HISTORY REQUIRES ANOTHER RECURSIVE METHOD. APPEND TO END OF s_dic DICTIONARY


s_dic = {  "symbol":    response[keys[0]][list_response[0]],    #index[0]
                "updated":  response[keys[0]][list_response[1]],    #index[1]
                "last_div": response[keys[1]][list_response[2]]["7. dividend amount"],
                "first_div": 'def getFirstDiv(dic)', #find the first month that does not have value 0 for dividend amount
                "div_freq": 'def getDivFreq(dic)', #find the frequency of dividend payments (typically 4 or 12 per year)
                "annual_div": 's_dic[last_div] * s_dic[div_freq]', #find annual dividend payment by div * frequency
                "yield_ratio": 'def getYieldRatio(dic)', #find yield by last_div * last_price ###last_price from another request
                "last_price": 'xxx', #parse additional request with daily info for up to date pricing
                "cut_ratio": 'xxx', # need cut_count from s_dic[div_history[]] and divide by years_payout
                "sus_ratio":  'xxx', #need sus_count from s_dic[div_history[]] and divide by years_payout
                "ytr": 'xxx', #i believe it was price / annual_div to find how many years until making revenue
                "years_payout": 'xxx', # how many years paying. find from diff between dates on first and last entry in list_response
                "div_history": { "InfoDateHere" :  { "div" : 'divAmountHere',
                                                                        "cut":  "if less than last div and not zero, true",
                                                                        "change_value":  "abs(last_div - div)",
                                                                        "change_percent": "div / last_div",
                                                                        "sus": "if div == 0 and last div != 0, true",
                                                                        "raise": "if greater than last div, true",

                                                                        }
                                        

                                        }


           }

print("\n\n\n=====\n\n\n=====\n\n\n{}".format(s_dic))
'''
0 - META DATA
    0.0 - INFORMATION: MONTHLY ADJUSTED PRICES AND VOLUMES
    0.1 - SYMBOL: "MSFT"
    0.2 - LAST REFRESHED: -DATE-
    0.3 - TIME ZONE: US/EASTERN

1 - "MONTHLY ADJUSTED TIME SERIES"
    1.0 - -DATE MOST RECENT-
        1.0.0 - OPEN
        1.0.1 - HIGH
        1.0.2 - LOW
        1.0.3 - CLOSE
        1.0.4 - ADJUSTED CLOSE
        1.0.5 - VOLUME
        1.0.6 -  DIVIDENT AMOUNT

    [. . .]
        [. . .]
        [. . .]
        [. . .]
        [. . .]

'''





    
