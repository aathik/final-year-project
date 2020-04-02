<?php

	class activenode
	{
		private $id;
		private $vehicleID;
		private $roll;
		private $pitch;
		private $forceSensor;
		private $lat;
		private $lon;
		private $timeOfAccident;
		private $conn;
		private $stmt;
		private $st;
		private $tableName = "sensordata";

		function setId($id) { $this->id = $id; }
		function getId() { return $this->id; }
		function setVehicleID($vehicleID) { $this->vehicleID = $vehicleID; }
		function getVehicleID() { return $this->vehicleID; }
		function setRoll($roll) { $this->roll = $roll; }
		function getRoll() { return $this->roll; }
		function setPitch($pitch) { $this->pitch = $pitch; }
		function getPitch() { return $this->pitch; }
		function setForceSensor($forceSensor) { $this->forceSensor = $forceSensor; }
		function getForceSensor() { return $this->forceSensor; }
		function setLat($lat) { $this->lat = $lat; }
		function getLat() { return $this->lat; }
		function setLon($lon) { $this->lon = $lon; }
		function getLon() { return $this->lon; }
		function setTimeOfAccident($timeOfAccident) { $this->timeOfAccident = $timeOfAccident; }
		function getTimeOfAccident() { return $this->timeOfAccident; }





		public function __construct(){
			require_once('DB/DBConnect.php');
			$conn = new DBConnect;
			$this->conn = $conn->connect();
		}


		public function getActiveNode(){
			$sql = "SELECT * FROM $this->tableName WHERE SEVERITY IS NOT NULL";
			$stmt = $this->conn->prepare($sql);
			$stmt->execute();
			return ($stmt->fetchAll(PDO::FETCH_ASSOC));
		}


	}



?>


