#include <RH_ASK.h>
#include <SPI.h>
#include <Ethernet.h>
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

RH_ASK driver;

struct dataHolder{
  char id[10];
  float roll;
  float pitch;
  float force;
  double loc_lat; 
  double loc_lon;
};

char server[] = "192.168.1.103";
IPAddress ip(192,168,1,177);
EthernetClient client;



void setup() {
   Serial.begin(9600);  // Debugging only
   if (!driver.init())
   {
    Serial.println("init failed");
   }
   if(Ethernet.begin(mac)==0) {
    Serial.println("Failed to configure Ethernet");
    Ethernet.begin(mac,ip);
   }
   
   
}

void loop() {
  uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];
  uint8_t buflen = sizeof(buf);
  struct dataHolder *data;

  if (driver.recv(buf, &buflen)){
    data = (struct dataHolder *)buf;
/*
    Serial.print("ID = ");
    Serial.print(data->id);
    Serial.println("roll = ");
    Serial.print(data->roll);
    Serial.println("pitch = ");
    Serial.print(data->pitch);
    Serial.println("force = "); 
    Serial.print(data->force);
    Serial.println("lat = "); 
    Serial.print(data->loc_lat);
    Serial.println("lon = "); 
    Serial.print(data->loc_lon);
    Serial.println("-------------------------------"); */
    if(client.connect(server, 80)) {
    Serial.println("connected");

    Serial.print("GET /accidentPHP/serverdata.php?vehicleID=");
    client.print("GET /accidentPHP/serverdata.php?vehicleID=");
    Serial.println(data->id);
    client.print(data->id);
    
    client.print("&roll=");
    Serial.println("&roll=");
    client.print(data->roll);
    Serial.println(data->roll);

    client.print("&pitch=");
    Serial.println("&pitch=");
    client.print(data->pitch);
    Serial.println(data->pitch);

    client.print("&forceSensor=");
    Serial.println("&forceSensor=");
    client.print(data->force);
    Serial.println(data->force);

    client.print("&lat=");
    Serial.println("&lat=");
    client.print(data->loc_lat);
    Serial.println(data->loc_lat);

    client.print("&lon=");
    Serial.println("&lon=");
    client.print(data->loc_lon);
    Serial.println(data->loc_lon);

    client.print(" ");
    client.print("HTTP/1.1");
    client.println();
    client.println("Host: 192.168.1.103");
    client.println("Connection: close");
    client.println();
  }
  else{
    Serial.println("connection failed");
  }
   // SendingToDatabase(data);
   
  }
}

//void SendingToDatabase(dataHolder data){
  
//}
