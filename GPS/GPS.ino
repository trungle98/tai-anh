#include <TinyGPS.h>


//long   lat,lon; // create variable for latitude and longitude object
float lat,lng;
TinyGPS gps; 
void setup(){
Serial.begin(11520);
Serial.begin(9600); // connect serial
Serial.println("The GPS Received Signal:");
Serial2.begin(9600); // connect gps sensor
Serial3.begin(9600);

}
 
void loop(){
    while(Serial2.available()){ // check for gps data
    if(gps.encode(Serial2.read()))// encode gps data
    { 
    gps.f_get_position(&lat,&lng); // get latitude and longitude

    Serial.print("Position: ");
    
    //Latitude
    Serial.print("Latitude: ");
    Serial.print(lat,6);
    
    Serial.print(",");
    
    //Longitude
    Serial.print("Longitude: ");
    Serial.println(lng,6); 
    Serial3.print("https://www.google.com/maps/place/");
    Serial3.print(lat);
    Serial3.print(",");
    Serial3.print(lng);
     Serial3.print("\n");
    sendingDataToWeb(lat, lng);
    delay(3000);
    
    
   }
   

 
 
}}
 void sendingDataToWeb(float latitude, float longtitude){
     while (Serial.available()) // this will be skipped if no data present, leading to
                             // the code sitting in the delay function below
  {
    delay(30);  //delay to allow buffer to fill 

      Serial.println(String(latitude) + "and "+String(longtitude));
      Serial.flush();
      break;
    }
  
    }
