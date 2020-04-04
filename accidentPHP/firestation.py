import pymysql
import math 

connection = pymysql.connect(host="localhost",user="root",passwd="",database="accident" )
cursor = connection.cursor()
sqlV = "SELECT vehicleID,lat,lon FROM sensordata WHERE nearest_fire IS NULL AND fire = '1' ;"
cursor.execute(sqlV)
vehicles = cursor.fetchall()
sqlF = "SELECT name,lat,lon FROM firestations"
cursor.execute(sqlF)
firestations = cursor.fetchall()


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
minFir = {}
for i in range(len(vehicles)):
	latV = vehicles[i][1]
	lonV = vehicles[i][2]
	for j in range(len(firestations)):
		latF = firestations[j][1]
		lonF = firestations[j][2]
		dist = haversine(latV, lonV,latF, lonF) 
		allDist[firestations[j][0]] = dist
	minFire = min(allDist, key=allDist.get)
	minFir[vehicles[i][0]] = minFire

for k in range(len(vehicles)):
	updateSQL = "UPDATE sensordata SET nearest_fire = %s WHERE vehicleID = %s ;"
	val = (minFir[vehicles[k][0]],vehicles[k][0])
	cursor.execute(updateSQL,val)

connection.commit()	
connection.close()