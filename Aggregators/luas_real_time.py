import pandas as pd
from sqlalchemy import create_engine
import time,logging, traceback
import luas.api
import psycopg2

try:
    engine_luas = create_engine('postgresql://postgres:citymangroup6@localhost:5432/bikes')
    connection = psycopg2.connect(user="postgres", password="citymangroup6", host="localhost", port="5432", database="bikes")
    cursor = connection.cursor()
    cursor.execute("SELECT abbr FROM luastations")
    stop_abbr = cursor.fetchall()
    luas_client = luas.api.LuasClient()
    station_list = dict()
    time_stamp = round(time.time())
    if luas_client:
        for st in stop_abbr:
            train_info = luas_client.stop_details(st[0])
            station_list["station_" + str(st[0])] = str(train_info['trams'])
        df_luas_realtime = pd.DataFrame(station_list, index=[time_stamp])
        df_luas_realtime.to_sql('rtluas', engine_luas, if_exists='append')
        print(df_luas_realtime)
        print("Inserted Luas Stations's Real time info Successfully")
    else:
        print("API not reachable.")
except Exception as e:
    logging.error(traceback.format_exc())


