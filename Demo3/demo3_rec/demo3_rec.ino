#include <RH_ASK.h>
#include <SPI.h>
#include <Ethernet.h>
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };


struct dataHolder{
  char id[10];
  float roll;
  float pitch;
  float force;
  double loc_lat; 
  double loc_lon;
  int fire;
};



unsigned int speed = 2000;
uint8_t rxPin = 9;
uint8_t txPin = 6;   // Any ways to avoid setting txPin?
uint8_t pttPin = 7;  // Any ways to avoid setting pttPin?
bool pttInverse = false;
RH_ASK driver(speed, rxPin, txPin, pttPin,pttInverse);

char server[] = "192.168.18.9";
IPAddress ip(192,168,18,18);
EthernetClient client;

char vh[10];
float pitch;
float roll;
int forceSensor;
double lati;
double longi;
int fire;


void setup() {
   Serial.begin(9600);  // Debugging only
   if (!driver.init())
   {
    Serial.println("init failed");
   }
   Serial.println("Configuring ethernetshield...........");
   if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    if (Ethernet.hardwareStatus() == EthernetNoHardware) {
      Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    } else if (Ethernet.linkStatus() == LinkOFF) {
      Serial.println("Ethernet cable is not connected.");
    }
    // no point in carrying on, so do nothing forevermore:
    while (true) {
      delay(1);
    }
  }
  Serial.print("My IP address: ");
  Serial.println(Ethernet.localIP());
   
   
}

void loop() {
  uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];
  uint8_t buflen = sizeof(buf);
  struct dataHolder *data;


  if (driver.recv(buf, &buflen)){
    data = (struct dataHolder *)buf;
    pitch = data->pitch;
    strcpy(vh,data->id);
    roll = data->roll;
    forceSensor = data->force;
    lati = data->loc_lat;
    longi = data->loc_lon;
    fire = data->fire;
    
    Serial.println("IN-----------");
    SendingToDatabase();
    
}
}

void SendingToDatabase(){
  if (client.connect(server, 80)) {
    Serial.println("connected");
    // Make a HTTP request:
    Serial.print("GET /Sample/sample.php?vehicleID=");
    client.print("GET /Sample/sample.php?vehicleID=");     //YOUR URL
    Serial.println(vh);
    client.print(vh);
    client.print("&roll=");
    Serial.println("&roll=");
    client.print(roll);
    Serial.println(roll);
    client.print("&pitch=");
    Serial.println("&pitch=");
    client.print(pitch);
    Serial.println(pitch);
    client.print("&forceSensor=");
    Serial.println("&forceSensor=");
    client.print(forceSensor);
    Serial.println(forceSensor);
    client.print("&lat=");
    Serial.println("&lat=");
    client.print(lati,6);
    Serial.println(lati,6);
    client.print("&lon=");
    Serial.println("&lon=");
    client.print(longi,6);
    Serial.println(longi,6);
    client.print("&fire=");
    Serial.println("&fire=");
    client.print(fire);
    Serial.println(fire);
    
    client.print(" ");      //SPACE BEFORE HTTP/1.1
    client.print("HTTP/1.1");
    client.println();
    client.println("Host: 192.168.18.9");
    client.println("Connection: close");
    client.println();

}
else{
  Serial.println("connection failed");
}
    
      
   
  }
  
