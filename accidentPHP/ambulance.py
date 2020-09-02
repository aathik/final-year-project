import pymysql
import math 

connection = pymysql.connect(host="localhost",user="root",passwd="",database="accident" )
cursor = connection.cursor()
sqlV = "SELECT vehicleID,lat,lon FROM sensordata WHERE nearest_amb IS NULL ;"
cursor.execute(sqlV)
vehicles = cursor.fetchall()
sqlA = "SELECT name,lat,lon FROM ambulances;"
cursor.execute(sqlA)
ambulances = cursor.fetchall()
print(vehicles)



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
minAmb = {}
for i in range(len(vehicles)):
	latV = vehicles[i][1]
	lonV = vehicles[i][2]
	for j in range(len(ambulances)):
		latA = ambulances[j][1]
		lonA = ambulances[j][2]
		dist = haversine(latV, lonV,latA, lonA) 
		allDist[ambulances[j][0]] = dist
	minAmbulance = min(allDist, key=allDist.get)
	minAmb[vehicles[i][0]] = minAmbulance
	print(allDist)

print(minAmb)
for k in range(len(vehicles)):
	updateSQL = "UPDATE sensordata SET nearest_amb = %s WHERE vehicleID = %s ;"
	val = (minAmb[vehicles[k][0]],vehicles[k][0])
	cursor.execute(updateSQL,val)
	


connection.commit()	
connection.close()   	


