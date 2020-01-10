import requests, json
import pandas as pd
from sqlalchemy import create_engine
import time,logging, traceback

try:
       engine_bike = create_engine('postgresql://postgres:citymangroup6@localhost:5432/bikes')
       response_bikedata = requests.get(
           'https://api.jcdecaux.com/vls/v1/stations/?contract=Dublin&apiKey=44dc31cd0a59d9c65406e966bc6e36f4d1efe7d4')

       engine_weather = create_engine('postgresql://postgres:citymangroup6@localhost:5432/bikes')
       response_weatherdata = requests.get(
           'https://api.openweathermap.org/data/2.5/weather?q=Dublin&appid=7610d9495d81e40df6a3c641f4425fde')

       time_stamp = round(time.time())
       if response_bikedata.status_code == 200:
               stations = response_bikedata.json()
               station_list = dict()
               for station in stations:
                       station_list["station_no_" + str(station['number'])] = station['available_bikes']
               df_station = pd.DataFrame(station_list,index=[time_stamp])
               df_station.to_sql('rtstation', engine_bike, if_exists='append')
               print("Inserted station Successfully")
       if response_weatherdata.status_code == 200:
               weather = response_weatherdata.json()
               weather_list = dict()
               #print (weather)
               weather_list['main'] = weather['weather'][0]['main']
               weather_list['description'] = weather['weather'][0]['description']
               weather_list['temperature'] = weather['main']['temp']
               weather_list['pressure'] = weather['main']['pressure']
               weather_list['humidity'] = weather['main']['humidity']
               weather_list['wind_speed'] = weather['wind']['speed']
               weather_list['city'] = weather['name']
               if 'rain' in weather.keys():
                   weather_list['rain'] = weather['rain']['1h']
               else:
                   weather_list['rain'] = 0
               df_weather = pd.DataFrame(weather_list,index=[round(time_stamp)])
               df_weather.to_sql('rtweather', engine_weather, if_exists='append')
               print("Inserted weather Successfully")
except Exception as e:
    logging.error(traceback.format_exc())
