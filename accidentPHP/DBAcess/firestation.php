<?php
	
	class firestation{

		public function __construct(){
				require_once('DB/DBConnect.php');
				$conn = new DBConnect;
				$this->conn = $conn->connect();
			}

		public function getAllFireStations(){
				$sql = "SELECT sensordata.vehicleID, firestations.name, firestations.lat, firestations.lon FROM sensordata, firestations WHERE sensordata.nearest_fire = firestations.name;";
				$stmt = $this->conn->prepare($sql);
				$stmt->execute();
				return ($stmt->fetchAll(PDO::FETCH_ASSOC));
			}

	}

?>