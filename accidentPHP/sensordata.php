<?php

class sensordata{


	public $link='';
 	function __construct($vh,$roll,$pitch){
	  $this->connect();
	  $this->storeInDB($vh,$roll,$pitch);
	 }
	function connect(){
	  $this->link = mysqli_connect('localhost','root','') or die('Cannot connect to the DB');
	  mysqli_select_db($this->link,'accident') or die('Cannot select the DB');
 	}
 	function storeInDB($vh,$roll,$pitch){
	  $query = "insert into sensordata set vehicleID='".$vh."',roll='".$roll."',pitch='".$pitch."'";
	  $result = mysqli_query($this->link,$query) or die('Errant query:  '.$query);
 }

 }
 if($_GET['vehicleID'] != '' and  $_GET['roll'] != '' and  $_GET['pitch'] != ''){
 $sample=new sample($_GET['vehicleID'],$_GET['roll'],$_GET['pitch']);
}

?>