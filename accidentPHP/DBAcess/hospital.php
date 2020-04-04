<?php
	
	class hospital{

		public function __construct(){
				require_once('DB/DBConnect.php');
				$conn = new DBConnect;
				$this->conn = $conn->connect();
			}

		public function getAllHospitals(){
				$sql = "SELECT sensordata.vehicleID, hospitals.name, hospitals.lat, hospitals.lon FROM sensordata, hospitals WHERE sensordata.nearest_hospital = hospitals.name";
				$stmt = $this->conn->prepare($sql);
				$stmt->execute();
				return ($stmt->fetchAll(PDO::FETCH_ASSOC));
			}

	}

?>