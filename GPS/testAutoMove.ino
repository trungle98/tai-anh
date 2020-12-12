#include <StringSplitter.h>
int  comma;
int lat;
int longt;
void setup() {
  // put your setup code here, to run once:
  Serial2.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  String check = checkingPeople();
  if (check != "" || check != "0,0") {
    comma = check.indexOf(',');
    lat = check.substring(0, comma).toInt();
    longt = check.substring(comma + 1, check.length()).toInt();
    Serial2.print("========lat: ");
    Serial2.print(lat);
    Serial2.print("\n");
    Serial2.print("========long: ");
    Serial2.print(longt);
    Serial2.print("\n");
    
    if (longt > 0) {
      moveFW();
      delay(2000 * longt);
      if (lat > 0) {
        turnRight();
        delay(4000);
        moveFW();
        delay(2000 * lat);
      } else {
        turnLeft();
        delay(5000);
        moveFW();
        delay(2000 * lat);
      }
    } else if(longt <0) {
      moveBW();
      delay(1000 * longt);
      if (lat > 0) {
        turnRight();
        delay(5000);
        moveFW();
        delay(1000 * lat);
      } else {
        turnLeft();
        delay(5000);
        moveFW();
        delay(1000 * lat);
      }
    }
  }

}
void moveFW() {
  Serial2.print("Move FW");
}
void moveBW() {
  Serial2.print("Move BW");
}
void moveST() {
  Serial2.print("Move ST");
}
void turnLeft() {
  Serial2.print("turnLeft");
}
void turnRight() {
  Serial2.print("turnRight");
}
String checkingPeople() {

  Serial2.print("Turn into checkingPeople: \n");
  String c;
  // Serial2 read section
  while (Serial2.available())
  {
    Serial2.print("pass");
    if (Serial2.available() > 0) {
      Serial2.print("Turn into received: ");
      c = Serial2.readStringUntil('\n');  //gets one byte from Serial2 buffer
      Serial2.print("end received: ");
      //readString = c; //makes the string readString
      Serial2.print("Arduino received: ");
      //      ans = readString.charAt(0) - '0';
      //      Serial2.println(ans);
      //      Serial2.flush();
      //      check = ans;
      //      sendingMessage(ans);
      //      return c.charAt(0) - '0';
      Serial2.print(c);
      Serial2.print("\n");
      return c;
    }


  }
  //  Serial2.flush();
  //  Serial2.print(Serial2.available());
  //  Serial2.setTimeout(10);
  //
  //
  //    String c = Serial2.readStringUntil('\n');  //gets one byte from Serial2 buffer
  //  Serial2.print("end received: ");
  //  Serial2.print(c);
  //  readString = c;


  //  return c.charAt(0) - '0';
  return c;


}
