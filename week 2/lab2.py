"""
Lab 2 - Individual/group Exercise
"""


"""
1. write a function named CelsiusToFarenheit 
   your function should ask the user for a temperature in celsius
   your function should convert the temperature to farenheit
   your function should print the Farenheit Temperature (no return statement)
   The formula for conversion is (°C × 9/5) + 32 = °F 
   Check your answer 0°C should be 32°F and 100°C should be 212°F
"""
def CelsiusToFarenheit():

    temp = input('Enter a temperature (as number) you want to convert from celsius to farenheit')
    #input validation
    while True:
        try:
            temp = float(temp)
            break
        except:
            temp = input('Enter a temperature (as number) you want to convert from celsius to farenheit')
    farenheit = (temp *9/5) +32
    print(farenheit)

"""
2. write a function named MarketingCampaign.
   your function should accept the following parameters:
       DigitalAds - an integer representing the budget for buying internet ads
       TVAds - an integer representing the budget for buying television ads 
       PrintAds - an integer representing the budget for buying newspaper ads 

   Calculation: Assume that at your company a single marketing campaign consists of 
            7 digital ads (cost: 1 unit per ad = 7 units)
            3 television ads (cost: 1 unit per ad = 3 units)
            6 print ads. (cost: 1 unit per ad = 6 units)
            and that ads of all types cost 1 unit.

    Return Value: 
       An integer representing the number of full marketing campaigns you can run


   Hint: there is a built-in python function called min() that may be useful
   Hint2:  you can solve this without conditionals.
   self-check your function if you have budget of 400 for digital, 22 for TV and 125 for print your output should be 7
"""
def MarketingCampaign(DigitalAds, TVAds, PrintAds):

    num_digital = DigitalAds // (7 * 1)
    num_tv = TVAds // (3 * 1)
    num_print = PrintAds // (6 * 1)

    num_campaign = min([num_digital, num_tv, num_print])

    return print('you can run {} maketing campains'.format(num_campaign))


"""
2B. make a second function that also asks the user to input the current prices for the three 
types of ads before calculating the number of marketing campaigns that can be run at the new
prices.
NOTE: a single marketing campaign still consists of: 
    7 digital ads (cost per add to be input by user)
    3 television ads (cost per add to be input by user)
    6 print ads (cost per add to be input by user)
"""

def MarketingCampaign(DigitalAds, TVAds, PrintAds):
    while True:
        cost_of_digital = input("What's the price of Digital Ads?")

        try:
            cost_of_digital = float(cost_of_digital)
            break
        except:
            print('Error. One or more of the add priced entered is not a number. Please try again')
    
    

    

    



# For extra practice (later) you can read through the following:
# 3. Read and work through examples in Chapter 4 Code Reuse: Functions & Modules in Head First Python: 
# https://www.oreilly.com/library/view/head-first-python/9781491919521/ch04.html  
# you can access for free as a UM student. 
# See the U-M Library instructions https://search.lib.umich.edu/databases/record/10263
# or visit https://www.safaribooksonline.com/library/view/temporary-access/ 
# and log in with your U-M email address.