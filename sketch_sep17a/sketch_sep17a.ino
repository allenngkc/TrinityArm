#include <Servo.h>
import serial
arduinoData=serial.Serial('com14', 115200)
Servo myservo1;  // create servo object to control a servo
// twelve servo objects can be created on most boards
Servo myservo2;
int pos;    // variable to store the servo position
float a1 = 20.0;
float a2 = 20.0;
float q1;
float q2;
int move1;
int move2;
float xpos;
float ypos;
int angle1=0;
int angle2=0;
void setup() {
  myservo1.attach(8);  // attaches the servo on pin 9 to the servo object
  myservo2.attach(9);
  Serial.begin(9600);
}
// void loop() {
//   for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
//     // in steps of 1 degree
//   myservo1.write(pos);
//   myservo2.writ%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%e(pos);
//     delay(5);            // tell servo to go to position in variable 'pos'
//   }
// }
void loop() {
  xpos = random(50); //receive xpos from glasses
  ypos = random(30); // receive ypos from glasses
  q2 = acos((pow(double(xpos), 2.0) + pow(double(ypos),2.0) -pow(double(a1),2) -pow(double(a2),2.0)/(2*a1*a2)));
  q1 = atan(ypos/xpos) - atan((a2*sin(q2))/(a1+a2*cos(q2)));
  move1 = int((q1 - angle1)*(360/2*3.141592654));
  move2 = int((q1 + q2 - angle2)*(360/2*3.141592654));
  if (move1 >= move2) {
    int pos2 = angle2;
    for (pos = angle1; pos <= move1+angle1; pos+=1) {
      myservo1.write(pos);
      myservo2.write(pos2);
      if (pos2 < move2+angle2) {
        pos2 += 1;
      delay(5);
      }
    }
  } else {
    int pos1 = angle1;
    Serial.println("Pos 2: " + myservo2.read());
    Serial.println("Pos 1: " + myservo1.read());
    for (pos = angle2; pos <= move2+angle2; pos+=1) {
      myservo2.write(pos);
      myservo1.write(pos1);
      if (pos1 < move1+angle1) {
        pos1 += 1;
      delay(5);
      }
    }

  //   if (myservo2.read() > angle2) {
  //   for (pos=myservo2.read(); pos >= angle2; pos-=1) {
  //     myservo1.write(pos);
  //     myservo2.write(pos1);
  //     if (myservo1.read() > angle1) {
  //       pos1 -= 1;
  //     delay(5);
  //     }
  //   }
  //   }
  // }
  angle1 = q1;
  angle2 = q2;
  }
}
// void movement(int angle, int angle2) {
//   while (angle != 0) {
//     // what is the current position fo the arm
//     //myservo1.
//     //Serial.println(myservo1.read());
//     // arm moving right
//     //for some reason left is positive
//     if(angle > 0) {
//       myservo1.write(pos - 45);
//     }
//     else if(angle < 0) {
//       myservo1.write(pos + 45);
//     }
//   }
// }