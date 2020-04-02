import pickle 													#unpickling the pre-trained model
with open('model_file.p', 'rb') as pickled:			
    data = pickle.load(pickled)  


gnb = data['GNBmodel']


import pymysql

connection = pymysql.connect(host="localhost",user="root",passwd="",database="accident" )
cursor = connection.cursor()
sql = "SELECT vehicleID,roll,pitch,forceSensor,fire FROM sensordata WHERE severity IS NULL ;"
cursor.execute(sql)
rows = cursor.fetchall()
result = []

for i in range(len(rows)):
	roll = rows[i][1]
	pitch = rows[i][2]
	forceSensor = rows[i][3]
	fire = rows[i][4]
	testing = [[roll,pitch,forceSensor,fire]]
	gnb_predictions = gnb.predict(testing)
	res = gnb_predictions[0]
	result.append(res)
for j in range(len(rows)):
	updateSQL = "UPDATE sensordata SET severity = %s WHERE vehicleID = %s ;"
	val = (result[j],rows[j][0])
	cursor.execute(updateSQL,val)

connection.commit()	
connection.close()   