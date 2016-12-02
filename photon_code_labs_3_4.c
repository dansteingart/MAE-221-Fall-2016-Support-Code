//Lab 3 & 4 Code
//Base Spark Code for Labs 3 & 4 (Weeks 5-8)
//MAE 221 Fall 2015

//This code allows for all ports to be read simultaneously, while setting points one at a time or all at once
#include "math.h"
#include "stdio.h"
char publishString[200]; //a place holer for the publish string
int count = 0; //looper that allows us to have a control responsive photon while not flooding the cloud with data every 50 ms
int countto = 20; // wait 20 clicks before publishing data
int waiter = 50; //in ms
int samps = 50; //sampler counter for smooth smoothness

//Deprecated not used
int a_set_pwm;
int b_set_pwm;
int a_set_mode;
int b_set_mode;

int parr[6];
int PWMS[4];

void setup() //run this loop just once upon start, or upon reset
{
//This will send back the big data string
Spark.variable("lab_data", &publishString, STRING);
//We'll use these to send the digital state
Spark.function("setMotor", setMotor);

//set analog pins to input mode
pinMode(A0, INPUT);
pinMode(A1, INPUT);
pinMode(A2, INPUT);
pinMode(A3, INPUT);
pinMode(A4, INPUT);
pinMode(A5, INPUT);
pinMode(A6, OUTPUT);
pinMode(A7, INPUT);

//For Voltage Divider
digitalWrite(A5,0);
digitalWrite(A6,1);

pinMode(D0, OUTPUT); //PWM A
pinMode(D1, OUTPUT); //PWM B
pinMode(D2, OUTPUT); //AIN1
pinMode(D3, OUTPUT); //AIN2
pinMode(D4, OUTPUT); //BIN1
pinMode(D5, OUTPUT); //BIN2
pinMode(D6, OUTPUT); //free switch
pinMode(D7, OUTPUT); //led

}

void loop() //repeat this loop forever
{
//declare pin labels as integers
int a0 = 0;
int a1 = 0;
int a2 = 0;
int a3 = 0;
int a4 = 0;
int a5 = 0;
int a6 = 0;
int a7 = 0;

int d0;
int d1;
int d2;
int d3;
int d4;
int d5;

//average the readings at each port for stability
for (int j = 0; j < samps; j++) //sum values samps times
{
a0 += analogRead(A0);
a1 += analogRead(A1);
a2 += analogRead(A2);
a3 += analogRead(A3);
a4 += analogRead(A4);
a5 += analogRead(A5);

}
// take the average
a0 = a0/samps;
a1 = a1/samps;
a2 = a2/samps;
a3 = a3/samps;
a4 = a4/samps;
a5 = a5/samps;

d0 = digitalRead(0);
d1 = digitalRead(1);
d2 = digitalRead(2);
d3 = digitalRead(3);
d4 = digitalRead(4);
d5 = digitalRead(5);




//wait countto clicks before sending publish data; blink the led every X to let us know how hard it's working
if (count > countto )
{
 sprintf(publishString,"{\"a0\": %d, \"a1\": %d, \"a2\": %d,\"a3\": %d, \"a4\": %d, \"a5\": %d,\"d0\": %d,\"d1\": %d,\"d2\": %d,\"d3\": %d,\"d4\": %d,\"d5\": %d,\"a_pwm\": %d,\"a_mode\": %d,\"b_pwm\": %d,\"b_mode\": %d}",a0,a1,a2,a3,a4,a5,PWMS[0],PWMS[1],PWMS[2],PWMS[3],d4,d5,a_set_pwm,a_set_mode,b_set_pwm,b_set_mode);
 Spark.publish("lab_data",publishString);
 count = 0;
}

else count +=1;
digitalWrite(7,!digitalRead(7));
delay(waiter);
}

//set one input
int setMotor(String potter)
{

//break the input string down into two parts.
int motor = potter.charAt(0)-48; //1 or 2
int mode = potter.charAt(1)-48; //0 Brake, 1 Forward
int PWM = (potter.charAt(2)-48)100 +(potter.charAt(3)-48)10 + (potter.charAt(4)-48) ; //0 to 255 (8Bit control)

PWMS[motor] = PWM;


if (mode == 0)
{
    analogWrite(motor,0);
}
else if (mode == 1)
{
    analogWrite(motor,PWM); //0 or 1
}

else if (mode == 2)
{

    if (PWM > 0) digitalWrite(motor,1); //0 or 1
    else digitalWrite(motor,0); //0 or 1

}
return potter.toInt();
}
