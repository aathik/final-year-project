
#include <Wire.h>
#include <RH_ASK.h>
#include <SPI.h>

#include <SoftwareSerial.h>
#include <TinyGPS++.h>                                                //GPS 
SoftwareSerial gpsSerial(8,9); //TX = 8 , RX = 9
TinyGPSPlus gps; 

RH_ASK driver;



int gyro_x, gyro_y, gyro_z;
long acc_x, acc_y, acc_z, acc_total_vector;
int temperature;
long gyro_x_cal, gyro_y_cal, gyro_z_cal;
long loop_timer;
int lcd_loop_counter;
float angle_pitch, angle_roll;
int angle_pitch_buffer, angle_roll_buffer;
boolean set_gyro_angles;
float angle_roll_acc, angle_pitch_acc;
float angle_pitch_output, angle_roll_output;
int flexiForcePin = A0;
boolean acci=false;                                                 //ACCELEROMETER GYROSCOPE

double latitude,longitude;

struct dataHolder{
  char id[10];
  float roll;
  float pitch;
  float force;
  double loc_lat; 
  double loc_lon;
}data;                                                                  //STRUCTURE TO SEND

int displaycount=0;

void setup() {
 
  
  Wire.begin(); 
  gpsSerial.begin(9600);
  Serial.begin(9600);
  
  setup_mpu_6050_registers();

  Serial.println("Calibrating Gyro");
  for (int cal_int = 0; cal_int < 2000 ; cal_int ++){                  
    if(cal_int % 125 == 0)Serial.print(".");                           
    read_mpu_6050_data();                                              
    gyro_x_cal += gyro_x;                                              
    gyro_y_cal += gyro_y;                                                   //CALIBRATE GYROSCOPE   
    gyro_z_cal += gyro_z;                                              
    delay(3);                                                          
  }
  gyro_x_cal /= 2000;                                                 
  gyro_y_cal /= 2000;                                                 
  gyro_z_cal /= 2000;  

  if (!driver.init())
         Serial.println("init failed");

  strncpy(data.id,"KL64",10);                                           //IDENTIFIER FOR EACH VEHICLE

  loop_timer = micros();

}

void loop() {
 
  read_mpu_6050_data();   


  gyro_x -= gyro_x_cal;                                                
  gyro_y -= gyro_y_cal;                                                     
  gyro_z -= gyro_z_cal;                                                

  //0.0000611 = 1 / (250Hz / 65.5)
  angle_pitch += gyro_x * 0.0000611;                                 
  angle_roll += gyro_y * 0.0000611;                                    
  

  angle_pitch += angle_roll * sin(gyro_z * 0.000001066);             
  angle_roll -= angle_pitch * sin(gyro_z * 0.000001066);               
  

  acc_total_vector = sqrt((acc_x*acc_x)+(acc_y*acc_y)+(acc_z*acc_z));  
  //57.296 = 1 / (3.142 / 180) The Arduino asin function is in radians
  angle_pitch_acc = asin((float)acc_y/acc_total_vector)* 57.296;     
  angle_roll_acc = asin((float)acc_x/acc_total_vector)* -57.296;       
  
  
  angle_pitch_acc -= 0.0;                                            
  angle_roll_acc -= 2.0;                                               

  if(set_gyro_angles){                                                  
    angle_pitch = angle_pitch * 0.9996 + angle_pitch_acc * 0.0004;   
    angle_roll = angle_roll * 0.9996 + angle_roll_acc * 0.0004;        
  }
  else{                                                                
    angle_pitch = angle_pitch_acc;                                    
    angle_roll = angle_roll_acc;                                        
    set_gyro_angles = true;                                            
  }
  
 
  angle_pitch_output = angle_pitch_output * 0.9 + angle_pitch * 0.1; 
  angle_roll_output = angle_roll_output * 0.9 + angle_roll * 0.1;    

  long flexiForceReading = analogRead(flexiForcePin);

  displaycount+=1;

  


  if(displaycount>100){// && acci==false){

    while(gpsSerial.available())
    {
    int data = gpsSerial.read();
      if (gps.encode(data))
      {
      latitude = (gps.location.lat());
      longitude = (gps.location.lng());
      
      }
    }

    
    
    Serial.print("Pitch : ");Serial.println(angle_pitch_output);
    Serial.print("Roll : ");Serial.println(angle_roll_output);
    Serial.print("Impact : ");Serial.println(flexiForceReading);
    Serial.print("Latitude : ");Serial.println(latitude,6);
    Serial.print("Longitude : ");Serial.println(longitude,6);
    
    if((angle_roll_output>10||angle_roll_output<-10||angle_pitch_output>10||angle_pitch_output<-10) && flexiForceReading>50 )
    {
    Serial.println("accident likely to occur");
    
    data.roll=angle_roll_output;
    data.pitch=angle_pitch_output;
    data.force=flexiForceReading;
    data.loc_lat=latitude;
    data.loc_lon=longitude;
    driver.send((uint8_t*)&data,sizeof(struct dataHolder));
    driver.waitPacketSent();
    
    
    }
    displaycount=0;
  }
  
 

  while(micros() - loop_timer < 4000);                                 
  loop_timer = micros();

}  

void read_mpu_6050_data(){                                             
  Wire.beginTransmission(0x68);                                        
  Wire.write(0x3B);                                                    
  Wire.endTransmission();                                              
  Wire.requestFrom(0x68,14);                                           
  while(Wire.available() < 14);                                        
  acc_x = Wire.read()<<8|Wire.read();                                  
  acc_y = Wire.read()<<8|Wire.read();                                  
  acc_z = Wire.read()<<8|Wire.read();                                  
  temperature = Wire.read()<<8|Wire.read();                            
  gyro_x = Wire.read()<<8|Wire.read();                                 
  gyro_y = Wire.read()<<8|Wire.read();                                 
  gyro_z = Wire.read()<<8|Wire.read();                                 

}

void setup_mpu_6050_registers(){
  //Activate the MPU-6050
  Wire.beginTransmission(0x68);                                        
  Wire.write(0x6B);                                                    
  Wire.write(0x00);                                                    
  Wire.endTransmission();                                              
  //Configure the accelerometer (+/-8g)
  Wire.beginTransmission(0x68);                                        
  Wire.write(0x1C);                                                    
  Wire.write(0x10);                                                    
  Wire.endTransmission();                                              
  //Configure the gyro (500dps full scale)
  Wire.beginTransmission(0x68);                                        
  Wire.write(0x1B);                                                    
  Wire.write(0x08);                                                    
  Wire.endTransmission();                                              
}
