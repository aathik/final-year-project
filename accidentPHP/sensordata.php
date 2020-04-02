<?php

class sensordata{
	private $id;
	private $vehicleID;
	private $roll;
	private $pitch;
	private $forceSensor;
	private $lat;
	private $lon;
	private $timeOfAccident;
	
	

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




	public $link='';
	public function __construct($vehicleID,$roll,$pitch,$forceSensor,$lat,$lon){
		$this->connect();
		$this->storeInDB($vehicleID,$roll,$pitch,$forceSensor,$lat,$lon);
	}
	public function connect(){
		$this->link=mysqli_connect('localhost','root','') or die('Cannot Connect To DB');
		mysqli_select_db($this->link,'accident') or die('Cannot select the DB');
	}

	public function storeInDB($vehicleID,$roll,$pitch,$forceSensor,$lat,$lon){
		$query = "insert into sensordata set vehicleID='".$vehicleID."',roll='".$roll."',pitch='".$pitch."',forceSensor='".$forceSensor."',lat='".$lat."',lon='".$lon."'";
		$reslut = mysqli_query($this->link,$query) or die('Error in query: '.$query);
	}
	


}

if($_GET['vehicleID'] != '' and $_GET['roll'] != '' and $_GET['pitch'] != '' and $_GET['forceSensor'] != '' and $_GET['lat'] != '' and $_GET['lon'] != ''){

		$sensordata=new sensordata($_GET['vehicleID'],$_GET['roll'],$_GET['pitch'],$_GET['forceSensor'],$_GET['lat'],$_GET['lon']);
	}




?>