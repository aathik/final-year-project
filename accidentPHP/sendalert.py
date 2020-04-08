import pymysql
import math 

connection = pymysql.connect(host="localhost",user="root",passwd="",database="accident" )
cursor = connection.cursor()
sqlH = "SELECT sensordata.vehicleID, hospitals.name, sensordata.lat, sensordata.lon, sensordata.severity, hospitals.phone FROM sensordata, hospitals WHERE sensordata.nearest_hospital = hospitals.name ;"
cursor.execute(sqlH)
alertH = cursor.fetchall()
sqlP = "SELECT sensordata.vehicleID, policestations.name, sensordata.lat, sensordata.lon, sensordata.severity, policestations.phone FROM sensordata, policestations WHERE sensordata.nearest_police = policestations.name"
cursor.execute(sqlP)
alertP = cursor.fetchall()
sqlF = "SELECT sensordata.vehicleID, firestations.name, sensordata.lat, sensordata.lon, sensordata.severity, firestations.phone FROM sensordata, firestations WHERE sensordata.nearest_fire = firestations.name"
cursor.execute(sqlF)
alertF = cursor.fetchall()
sqlA = "SELECT sensordata.vehicleID, ambulances.name, sensordata.lat, sensordata.lon, sensordata.severity, ambulances.phone, ambulances.email, ambulances.lat, ambulances.lon FROM sensordata, ambulances WHERE sensordata.nearest_amb = ambulances.name"
cursor.execute(sqlA)
alertA = cursor.fetchall()

import requests
import json


URL = 'https://www.sms4india.com/api/v1/sendCampaign'

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

senderid = "Team Final Year"
for i in range(len(alertH)):
  number = alertH[i][5]
  latlon = "%s,%s" %(alertH[i][2],alertH[i][3])
  textMessage = "vehicleID : %s \nHospital : %s \nLat & Lon : %s \nSeverity : %s" %(alertH[i][0],alertH[i][1],latlon,alertH[i][4])
  #response = sendPostRequest(URL, 'S3XNBK15JQ62U5NTMTBUITY90ONKT7LA', 'ZPSZJ8TF7082EPCS', 'stage', number, senderid, textMessage )
  #uncomment the above line for msging
for i in range(len(alertP)):
  number = alertP[i][5]
  latlon = "%s,%s" %(alertP[i][2],alertP[i][3])
  textMessage = "vehicleID : %s \nPolicestation : %s \nLat & Lon : %s \nSeverity : %s" %(alertP[i][0],alertP[i][1],latlon,alertP[i][4])
  #response = sendPostRequest(URL, 'S3XNBK15JQ62U5NTMTBUITY90ONKT7LA', 'ZPSZJ8TF7082EPCS', 'stage', number, senderid, textMessage )
  #uncomment the above line for msging
for i in range(len(alertF)):
  number = alertF[i][5]
  latlon = "%s,%s" %(alertF[i][2],alertF[i][3])
  textMessage = "vehicleID : %s \nfirestations : %s \nLat & Lon : %s \nSeverity : %s" %(alertF[i][0],alertF[i][1],latlon,alertF[i][4])
  #response = sendPostRequest(URL, 'S3XNBK15JQ62U5NTMTBUITY90ONKT7LA', 'ZPSZJ8TF7082EPCS', 'stage', number, senderid, textMessage )
  #uncomment the above line for msging  
for i in range(len(alertA)):
  number = alertA[i][5]
  latlon = "%s,%s" %(alertA[i][2],alertA[i][3])
  textMessage = "vehicleID : %s \nAmbulance : %s \nLat & Lon : %s \nSeverity : %s" %(alertA[i][0],alertA[i][1],latlon,alertA[i][4])
  #response = sendPostRequest(URL, 'S3XNBK15JQ62U5NTMTBUITY90ONKT7LA', 'ZPSZJ8TF7082EPCS', 'stage', number, senderid, textMessage )
  #uncomment the above line for msging  

import openrouteservice as ors
import folium
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

for i in range(len(alertA)):
  coordinates = []
  lonlatA = [alertA[i][8], alertA[i][7]]
  lonlatV = [alertA[i][3], alertA[i][2]]
  coordinates =[lonlatA,lonlatV]
  client = ors.Client(key='5b3ce3597851110001cf6248c228e625795c4872b8509fbb183226dc')

  m = folium.Map(location=[10.3070, 76.3341], tiles='openstreetmap', zoom_start=5)

  route = client.directions(
    coordinates=coordinates,
    profile='driving-car',
    format='geojson',
    
  )
  folium.Marker(
    location= [alertA[i][7],alertA[i][8]],
    popup=alertA[i][1],
    icon=folium.Icon(color='green')
  ).add_to(m)
  folium.Marker(
    location= [alertA[i][2],alertA[i][3]],
    popup=alertA[i][0],
    icon=folium.Icon(color='red')
  ).add_to(m)

  folium.PolyLine(locations=[list(reversed(coord)) 
                           for coord in 
                           route['features'][0]['geometry']['coordinates']]).add_to(m)


  m.save('RoutingMap.html')
  fromaddr = "accidentdetectionusingvanet@gmail.com"
  toaddr = alertA[i][6]


  attachment = open("RoutingMap.html", 'rb')

  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = "Accident"

  part = MIMEBase('application','octet-stream')
  part.set_payload(attachment.read())
  part.add_header('Content-Disposition',
                      'attachment',
                      filename="RoutingMap.html")
  encoders.encode_base64(part)
  msg.attach(part)

  smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
  smtpObj.ehlo()
  smtpObj.starttls()

  smtpObj.login('accidentdetectionusingvanet@gmail.com', 'dorffloamunzbgkg')

  text = msg.as_string()
  smtpObj.sendmail(fromaddr,toaddr,text)

  smtpObj.quit()



for k in range(len(alertH)):
  updateSQL = "UPDATE sensordata SET curr_status = %s WHERE vehicleID = %s ;"
  val = ("MsgSent-Active",alertH[k][0])
  cursor.execute(updateSQL,val)





connection.commit() 
connection.close()






