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
for k in range(len(alertH)):
  updateSQL = "UPDATE sensordata SET curr_status = %s WHERE vehicleID = %s ;"
  val = ("MsgSent-Active",alertH[k][0])
  cursor.execute(updateSQL,val)

connection.commit() 
connection.close()






