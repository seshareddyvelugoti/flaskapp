from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import re
from datetime import datetime

from sqlitedb import *
app = Flask(__name__)


def read_devicestatus(deviceid):
   try:
      url = "http://183.82.41.227:8080/enviroconnect/AQMS?FunctionKey=107&plantId=48&deviceId=" + str(
         deviceid) + "&page=main"
      print(url)
      table_MN = pd.read_html(url)
      df1 = table_MN[0].values.tolist()
      d = str(df1[0])
      print(d)
      match_str = re.search(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}', d)
      res = datetime.strptime(match_str.group(), '%d-%m-%Y %H:%M:%S')
      return res
   except:
      pass

@app.route('/')
def hello_world():
   finaldata = []
   data = [["reddys labs unit-1",1170],["reddys labs unit-2",1171],["reddys labs unit-3",1443],["reddys labs unit-1",1444],["reddys labs unit-5",1445]]
   for d in data:
      lst = list(d)
      print(lst[1])
      t = read_devicestatus(lst[1])
      lst.append(t)
      print(lst)
      finaldata.append(lst)
   return render_template('liveview.html',data = finaldata)

if __name__ == '__main__':
   app.run()