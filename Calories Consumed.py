#calories.py
#Sept 9, 2013
#Michelle Levine
#THis program prompts the user for the number of cookies consumed.
#Based on the calories per serving, the calories consumed
#calculated and displayed

def main():
    #Declare and initialize variables and constants
    #const int  COOKIES_PER_BAG=40
    COOKIES_PER_BAG=40
    #CONST INT NUM_SERVING=10
    NUM_SERVINGS=10
    #const float CALORIES_PER_SERVINGS=300.0
    CALORIES_PER_SERVING=300.0
    #float numCookiesConsumed=0.0
    numCookiesConsumed=0.0
    #float caloriesConsumed=0.0
    caloriesConsumed=0.0
    #float caloriesPerCookie=0.0
    caloriesPerCookie=0.0
    #float cookiesPerServing=0.0
    cookiesPerServing=0.0

    #Intro
    print(" WELCOME TO THE CALORIE COUNTER!!\n")

    #Prompt for numCookiesConsumed
    numCookiesConsumed=eval(input("Please enter the number of cookies consumed:))

    #Calculate cookiesPerServing
    cookiesPerServing=COOKIES_PER_SERVING/ NUM_SERNINGS

    #Calculate caloriesPerCookie
    caloriesPerCookie=CALORIES_PER_SERVING/cookiesPERSERVING

    #Calculate caloriesConsumed
    caloriesConsumed=caloriesPerCookie*numCookiesConsumed

    #Display caloriesConsumed
    print("\nYou consumed", caloriesConsumed, "calories.")
                                  
