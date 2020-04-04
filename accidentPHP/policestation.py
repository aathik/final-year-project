import pymysql
import math 

connection = pymysql.connect(host="localhost",user="root",passwd="",database="accident" )
cursor = connection.cursor()
sqlV = "SELECT vehicleID,lat,lon FROM sensordata WHERE nearest_police IS NULL ;"
cursor.execute(sqlV)
vehicles = cursor.fetchall()
sqlP = "SELECT name,lat,lon FROM policestations"
cursor.execute(sqlP)
policestations = cursor.fetchall()


def haversine(lat1, lon1, lat2, lon2): 
	dLat = (lat2 - lat1) * math.pi / 180.0
	dLon = (lon2 - lon1) * math.pi / 180.0
	lat1 = (lat1) * math.pi / 180.0
	lat2 = (lat2) * math.pi / 180.0
	a = (pow(math.sin(dLat / 2), 2) +
		pow(math.sin(dLon / 2), 2) *
			math.cos(lat1) * math.cos(lat2)); 
	rad = 6371
	c = 2 * math.asin(math.sqrt(a)) 
	return rad * c 

allDist = {}
minPol = {}
for i in range(len(vehicles)):
	latV = vehicles[i][1]
	lonV = vehicles[i][2]
	for j in range(len(policestations)):
		latP = policestations[j][1]
		lonP = policestations[j][2]
		dist = haversine(latV, lonV,latP, lonP) 
		allDist[policestations[j][0]] = dist
	minPolice = min(allDist, key=allDist.get)
	minPol[vehicles[i][0]] = minPolice

for k in range(len(vehicles)):
	updateSQL = "UPDATE sensordata SET nearest_police = %s WHERE vehicleID = %s ;"
	val = (minPol[vehicles[k][0]],vehicles[k][0])
	cursor.execute(updateSQL,val)

connection.commit()	
connection.close()