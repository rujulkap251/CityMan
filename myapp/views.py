
from django.shortcuts import render
from .models import Station, Rtstation, Form, Luastations, Rtluas, Rtdart, Dartstations 
from django.http import HttpResponse
import json
from django.template import loader
import folium
import re,ast
import itertools
import datetime
import time
from calendar import timegm
from django.db import connection, transaction
import datetime
import time
import requests
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from django.shortcuts import render, render_to_response
from bokeh.embed import components
import pandas as pd
from bokeh.resources import CDN
from bokeh.models import HoverTool

# Create your views here.
from bokeh.embed import file_html

def dictfetchall(cursor):
    #"Return all rows from a cursor as a dict"
    columns = [str(col[0].split("_")[-1]) for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def index(request):
    data = []
    #print("Hello from index")
    station = Station.objects.all()
    #print(type(station))

    for i in station:
        data_station = {}
        data_station['name'] = i.name
        data_station['number'] = i.number
        data_station['lat'] = i.lat
        data_station['log'] = i.lng
        data.append(data_station)
    resp = json.dumps(data)
    return HttpResponse(resp)


def homepage(request,timeIn=round(time.time())):
    context = {'time':timeIn}
    return render(request, 'myapp/homepage.html',context)

def luas(request):
    return render(request, 'myapp/homepage_luas.html')

def test(request):
    return render(request, 'myapp/amartest.html')

def dart(request):
    return render(request, 'myapp/homepage_dart.html')

def form(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('inputname', None)
            email = request.POST.get('inputemail', None)
            prob = request.POST['inputprob']
            url = request.POST.get('inputurl', None)
            des = request.POST.get('inputdesc', None)
            form_data = Form(name=name, email=email, problem=prob, url=url, des=des)
            form_data.save()
            #print(url)
            #print(prob)
        except Exception as e:
            print(e)
    return render(request, 'myapp/form.html')

def calendar(request):
    if request.method == 'POST':
        calendar = request.POST['calendar']
        utc_time = time.strptime(calendar, "%Y-%m-%dT%H:%M")
        epoch_time = timegm(utc_time)
        map(request, epoch_time)
    else:
        print("Boo")
    return render(request, 'myapp/calendar.html')

def map(request, input_time=round(time.time())):
    number = []
    timestamp = 1551293222
    if input_time != "NaN" and int(input_time) > 9999999999:
        input_time = int(input_time)/1000
    else:
        input_time = round(time.time()) 
    station_data = Station.objects.all()
    m = folium.Map(location=[53.3465,-6.2635], zoom_start=15)
    rtstation = Rtstation()
    print(input_time)
    cursor = connection.cursor()
    if round(time.time()) < int(input_time):
        cursor.execute("select * from future_rtbike where index < %s +300 and index > %s -300 order by index desc limit 1;",(input_time,input_time,))
        rtstation_row = dictfetchall(cursor)
        if  not rtstation_row:
            data = requests.get(f'http://35.232.102.222/predict?timestamp={input_time}')
            rtstation_row = data.json() 
            print("From Random Backend)")
        print("From future backend")
        print(rtstation_row) 
    else:
        cursor.execute("select * from rtstation where index < %s order by index desc limit 1;",(input_time,))
        rtstation_row = dictfetchall(cursor)
        print("From Backend)")
    for i in station_data:
        data = str(i.name) +" \n Stands Available"+ str((i.bike_stands)-(rtstation_row[0][str(i.number)]))+" bike Available:"+str(rtstation_row[0][str(i.number)])
        if(((2*i.bike_stands)/3) <=  rtstation_row[0][str(i.number)]):
            folium.Marker(location=[i.lat, i.lng],popup=data, icon=folium.Icon(color='green')).add_to(m)
        elif(((2*i.bike_stands)/3) >=  rtstation_row[0][str(i.number)] and ((i.bike_stands)/3) <=  rtstation_row[0][str(i.number)] ):
            folium.Marker(location=[i.lat, i.lng],popup=data, icon=folium.Icon(color='orange')).add_to(m)
        else:
            folium.Marker(location=[i.lat, i.lng],popup=data, icon=folium.Icon(color='red')).add_to(m)
    return HttpResponse(m.get_root().render())


def map_luas(request):
    number = []
    timestamp = 1551293222
    station_data  = Luastations.objects.all()
    m = folium.Map(location=[53.3465,-6.2635], zoom_start=13)
    rtluas = Rtluas()
    test = Rtluas._meta.get_fields()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM rtluas ORDER BY index DESC LIMIT 1")
    rtstation_row = dictfetchall(cursor)
    for i in station_data:
        rt_station = ast.literal_eval(rtstation_row[0][i.abbr])
        data = f'<strong style="font-size: 20px;">Station Name:{i.name}</strong> <hr> '
        for st_data in rt_station:
            d = f'<div style="width: 100.0%; height: 100.0%;"><strong style="font-size: 15px;">Destination:{st_data["destination"]}</strong> <strong style="font-size: 15px;"> Due:{st_data["due"]}</strong></div> <br>'
            data = data+d
        popup = folium.Popup(data, max_width=300)
        if(int(i.lineid) == 1):
            folium.Marker(location=[float(i.lat), float(i.long)], popup=popup, icon=folium.Icon(color='red')).add_to(m)
        else:
            folium.Marker(location=[float(i.lat), float(i.long)], popup=popup, icon=folium.Icon(color='green')).add_to(m)
    return HttpResponse(m.get_root().render())


def map_dart(request):
    number = []
    timestamp = 1551293222
    station_data  = Dartstations.objects.all()
    m = folium.Map(location=[53.3465,-6.2635], zoom_start=13)
    rtdart = Rtdart()
    test = Rtdart._meta.get_fields()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM rtdart ORDER BY index DESC LIMIT 1")
    rtstation_row = dictfetchall(cursor)
    for i in station_data:
        rt_station = ast.literal_eval(rtstation_row[0][i.code])
        data = f'<strong style="font-size: 20px;">Station Name:{i.description}</strong> <hr> '
        for st_data in rt_station[:4]:
            d = f'<div style="width: 100.0%; height: 100.0%;"> <strong style="font-size: 15px;">Train code:{st_data["Traincode"]}</strong> | <strong style="font-size: 15px;">Destination:{st_data["Destination"]}</strong> |  <strong style="font-size: 15px;">  Due:{st_data["Duein"]}</strong></div><br> '
            data = data+d
        popup = folium.Popup(data, max_width=400)
        folium.Marker(location=[float(i.lat), float(i.long)], popup=popup, icon=folium.Icon(color='blue')).add_to(m)
    return HttpResponse(m.get_root().render())
    return HttpResponse(m.get_root().render())

def analytics(request):
    currtime = round(time.time())
    cur = connection.cursor()
    df = pd.read_sql("SELECT rtstation.index as date, rtweather.index, rtweather.wind_speed, rain, (COALESCE(station_no_10,0)+ COALESCE(station_no_100,0)+COALESCE(station_no_101,0)+COALESCE(station_no_102,0)+COALESCE(station_no_103,0)+COALESCE(station_no_104,0)+COALESCE(station_no_105,0)+ COALESCE(station_no_106,0)+ COALESCE(station_no_107,0)+ COALESCE(station_no_108,0)+ COALESCE(station_no_109,0)+ COALESCE(station_no_11,0)+  COALESCE(station_no_110,0)+ COALESCE(station_no_111,0)+ COALESCE(station_no_112,0)+ COALESCE(station_no_113,0)+ COALESCE(station_no_114,0)+ COALESCE(station_no_115,0)+ COALESCE(station_no_12,0)+  COALESCE(station_no_13,0)+  COALESCE(station_no_14,0)+ COALESCE(station_no_15,0)+  COALESCE(station_no_16,0)+  COALESCE(station_no_17,0)+  COALESCE(station_no_18,0)+  COALESCE(station_no_19,0)+  COALESCE(station_no_2 ,0)+  COALESCE(station_no_21,0)+  COALESCE(station_no_22,0)+  COALESCE(station_no_23,0)+  COALESCE(station_no_24,0)+  COALESCE(station_no_25,0)+  COALESCE(station_no_26,0)+  COALESCE(station_no_27,0)+  COALESCE(station_no_28,0)+  COALESCE(station_no_29,0)+  COALESCE(station_no_3 ,0)+  COALESCE(station_no_30,0)+  COALESCE(station_no_31,0)+  COALESCE(station_no_32,0)+  COALESCE(station_no_33,0)+  COALESCE(station_no_34,0)+  COALESCE(station_no_35,0)+  COALESCE(station_no_36,0)+  COALESCE(station_no_37,0)+  COALESCE(station_no_38,0)+  COALESCE(station_no_39,0)+  COALESCE(station_no_4 ,0)+  COALESCE(station_no_40,0)+  COALESCE(station_no_41,0)+  COALESCE(station_no_42,0)+  COALESCE(station_no_43,0)+  COALESCE(station_no_44,0)+  COALESCE(station_no_45,0)+  COALESCE(station_no_46,0)+  COALESCE(station_no_47,0)+  COALESCE(station_no_48,0)+  COALESCE(station_no_49,0)+  COALESCE(station_no_5 ,0)+  COALESCE(station_no_50,0)+  COALESCE(station_no_51,0)+  COALESCE(station_no_52,0)+  COALESCE(station_no_53,0)+  COALESCE(station_no_54,0)+  COALESCE(station_no_55,0)+  COALESCE(station_no_56,0)+  COALESCE(station_no_57,0)+  COALESCE(station_no_58,0)+  COALESCE(station_no_59,0)+  COALESCE(station_no_6 ,0)+  COALESCE(station_no_60,0)+  COALESCE(station_no_61,0)+  COALESCE(station_no_62,0)+  COALESCE(station_no_63,0)+  COALESCE(station_no_64,0)+  COALESCE(station_no_65,0)+  COALESCE(station_no_66,0)+  COALESCE(station_no_67,0)+  COALESCE(station_no_68,0)+  COALESCE(station_no_69,0)+  COALESCE(station_no_7 ,0)+  COALESCE(station_no_70,0)+  COALESCE(station_no_71,0)+  COALESCE(station_no_72,0)+  COALESCE(station_no_73,0)+  COALESCE(station_no_74,0)+  COALESCE(station_no_75,0)+  COALESCE(station_no_76,0)+  COALESCE(station_no_77,0)+  COALESCE(station_no_78,0)+  COALESCE(station_no_79,0)+  COALESCE(station_no_8 ,0)+  COALESCE(station_no_80,0)+  COALESCE(station_no_81,0)+  COALESCE(station_no_82,0)+  COALESCE(station_no_83,0)+  COALESCE(station_no_84,0)+  COALESCE(station_no_85,0)+  COALESCE(station_no_86,0)+  COALESCE(station_no_87,0)+  COALESCE(station_no_88,0)+  COALESCE(station_no_89,0)+  COALESCE(station_no_9 ,0)+  COALESCE(station_no_90,0)+  COALESCE(station_no_91,0)+  COALESCE(station_no_92,0)+  COALESCE(station_no_93,0)+  COALESCE(station_no_94,0)+  COALESCE(station_no_95,0)+  COALESCE(station_no_96,0)+  COALESCE(station_no_97,0)+ COALESCE(station_no_98,0)+  COALESCE(station_no_99,0)) as CumulatedStations FROM rtstation JOIN rtweather ON rtstation.index = rtweather.index where  rtstation.index >  %(dstart)s - (60*60*24*7)", con=connection,params={"dstart":currtime})

    df.date = df.date.apply(lambda d: datetime.datetime.fromtimestamp(int(d)).strftime('%Y-%m-%d %H:%M'))
    df['date'] = pd.to_datetime(df['date'])
    df['tooltip'] = [x.strftime("%Y-%m-%d %H:%M:%S") for x in df['date']]
    source = ColumnDataSource(df)
    source1 = ColumnDataSource(df)
    print (df)

   # hover.tooltips = OrderedDict([('Date:', '@date'),('Bikes:', '@cumulatedstations'))])
   # hover.mode = 'mouse'

    p = figure(x_axis_type="datetime", plot_width=1500, plot_height=400)
    p1 = p.line('date', 'cumulatedstations', source=source, color='green', legend='Bikes Available')
    p.add_tools(HoverTool(renderers=[p1], tooltips=[('date',"@tooltip"),('Available Bikes',"@cumulatedstations")],mode='vline'))
    p.xaxis.axis_label = 'Time'
    p.yaxis.axis_label = 'Bikes Available'
    new_legend = p.legend[0]
    p.legend[0].plot = None
    p.add_layout(new_legend, 'right')
    script, div = components(p)

    q = figure(x_axis_type="datetime", plot_width=1500, plot_height=400)
    q.line('date', 'wind_speed', source=source1, color='red',legend='Wind Speed')
    q.line('date', 'rain', source=source1, color='blue',legend='Rainfall (mm)')
    q.xaxis.axis_label = 'Time'
    q.yaxis.axis_label = 'Wind Speed and Rainfall)'

    new_legend = q.legend[0]
    q.legend[0].plot = None
    q.add_layout(new_legend, 'right')
    scriptq, divq = components(q)
    return render(request, "myapp/analytics.html", {"the_script": script, "the_div": div, "the_scriptq": scriptq, "the_divq": divq})
