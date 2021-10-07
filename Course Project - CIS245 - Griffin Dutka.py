"""
Griffin Dutka
9/16/21
Course Project
"""
import requests

welcome = input("Welcome to the Weather Channel Program! \nTo look up your current local weather, press Enter!")
        
#Request by zip code to api for weather info
def zipcode():
    zipcode = int(input('Please enter a valid Zip Code: '))
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=316d8258fbfb3b5062feca8ad06583ac'.format(zipcode)
    res = requests.get(url)
    data = res.json()
    thedata(data)

    question = input('Would you like to look up another location? Type yes or no:')
    if question == 'yes':
        main()
    if question == 'no':
        print("Thank you for choosing our weather service! See you next time!")
        exit()

#Request from city name to api for weather info
def city():
    city = input('Please enter a valid city name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=316d8258fbfb3b5062feca8ad06583ac&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    thedata(data)

    question = input('Would you like to look up another location? Type yes or no: ')
    if question == 'yes':
        main()
    if question == 'no':
        print("Thank you choosing our weather service. See you next time!")
        exit() 

#Displays weather information in readable format
def thedata(data):
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    lowtemp = data['main']['temp_min']
    hightemp = data['main']['temp_max']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    
    print('---------------------------------------')
    print('The current weather for that location:')
    print('Description: {}'.format(description))
    print('Current Temp: {}℉'.format(temp))
    print('Low Temp: {}℉'.format(lowtemp))
    print('High Temp: {}℉'.format(hightemp))
    print('Humidity: {}%'.format(humidity)) 
    print('Wind Speed: {} m/s'.format(wind_speed))
    
#Main function including loop back for multiple searches and validation for entering valid data
def main():
    while True:
        answer = input("You can search by typing either zipcode or city to start: ")

        if answer == 'zipcode':
            try:
                print("*Connection has been established*")
                zipcode()

            except Exception:
                print("Please enter valid Zip Code! Try again!")
                zipcode()

        if answer == 'city':
            try:
                print("*Connection has been established*")
                city()

            except Exception:
                print("Please enter a valid city name! Try again!")
                city()
        else:
            print("Please enter either 'zipcode' or 'city' to search!")
main()