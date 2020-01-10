import pandas as pd
import time, logging, traceback
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine
from urllib.request import urlopen
import psycopg2
import json
try:
    engine_dart = create_engine('postgresql://postgres:citymangroup6@localhost:5432/bikes')
    connection = psycopg2.connect(user="postgres", password="citymangroup6", host="localhost", port="5432", database="bikes")
    cursor = connection.cursor()
    cursor.execute("select code from dartstations")
    stop_abbr = cursor.fetchall()
    attr = [ 'Traincode', 'Stationfullname', 'Stationcode', 'Origin',
            'Destination', 'Status', 'Duein', 'Direction']
    time_stamp = round(time.time())
    station_list = dict()
    for st in stop_abbr:
        requestURL = 'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML?StationCode='+st[0]
        rtinfo_url = urlopen(requestURL)
        if (rtinfo_url.getcode() == 200):
            print("response received")
            root = ET.parse(rtinfo_url).getroot()
            my_list = []
            for child in root:
                info  = dict()
                for c in child:
                    if c.tag[35:] in attr:
                        info[c.tag[35:]] = c.text
                my_list.append(info)
            station_list["station_" + str(st[0])] = str(my_list)
            #print(station_list)
            #input = json.loads(station_list)
        else:
           print("API not reachable")
    print(station_list)
    df_dart_realtime = pd.DataFrame(station_list, index=[time_stamp])
    print(df_dart_realtime)
    df_dart_realtime.to_sql('rtdart', engine_dart, if_exists='append')
    print("Inserted Dart Stations's Real time info Successfully")
    #print(df_dart_realtime)
except Exception as e:
    logging.error(traceback.format_exc())
finally:
    connection.close()
