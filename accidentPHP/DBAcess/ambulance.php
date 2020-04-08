<?php
	
	class ambulance{

		public function __construct(){
				require_once('DB/DBConnect.php');
				$conn = new DBConnect;
				$this->conn = $conn->connect();
			}

		public function getAllAmbulances(){
				$sql = "SELECT sensordata.vehicleID, ambulances.name, ambulances.lat, ambulances.lon FROM sensordata, ambulances WHERE sensordata.nearest_amb = ambulances.name;";
				$stmt = $this->conn->prepare($sql);
				$stmt->execute();
				return ($stmt->fetchAll(PDO::FETCH_ASSOC));
			}

	}

?>