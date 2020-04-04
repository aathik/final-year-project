<?php
	
	class policestation{

		public function __construct(){
				require_once('DB/DBConnect.php');
				$conn = new DBConnect;
				$this->conn = $conn->connect();
			}

		public function getAllPolicestations(){
				$sql = "SELECT sensordata.vehicleID, policestations.name, policestations.lat, policestations.lon FROM sensordata, policestations WHERE sensordata.nearest_police = policestations.name";
				$stmt = $this->conn->prepare($sql);
				$stmt->execute();
				return ($stmt->fetchAll(PDO::FETCH_ASSOC));
			}

	}

?>