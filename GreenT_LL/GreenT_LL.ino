/** ************************************************************************** */
/** ************************************************************************** */
/** **     GreenT                                                          *** */
/** **     Copyright (C) 2018                                              *** */
/** **     Daniel Cabaceira       daniel.cabaceira@gmail.com               *** */
/** **     Carlos Silva           cmiguelrsilva@gmail.com                  *** */
/** **                                                                     *** */
/** **     Instituto Politécnico de Tomar                                  *** */
/** **     Escola Superior de Tecnologia de Tomar                          *** */
/** **     Projeto Final - Licenciatura em Engenharia Informática          *** */
/** ************************************************************************** */
/** ************************************************************************** */

#include <ArduinoHardware.h>
#include <ros.h>
#include <std_msgs/Int16.h>

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#define LEFT_MOTOR   30
#define LEFT_MOTOR_PWM 9
#define RIGHT_MOTOR_PWM 10
#define RIGHT_MOTOR   32

#define PinAencoder0  2  //pino de interrupção - econder esq 
#define PinBencoder0  4  //Digital
#define PinAencoder1  3  //pino de interrupção 
#define PinBencoder1  5  //Digital

volatile signed int encoder0Pos = 0, encoder1Pos = 0;
int speedatual0, speedatual1, PWM_val0, PWM_val1, ultimo_erro0, ultimo_erro1, ultimo_comando0, ultimo_comando1;
const int LOOPTIME = 200;

ros::NodeHandle nh;

/*******************************************************************************/
//Subscribers for the PWM sent by the rasPi
/*******************************************************************************/
void motorD_cb( const std_msgs::Int16& cmd_msg) {
  motorDir(cmd_msg.data);
}
ros::Subscriber<std_msgs::Int16> motorD("cmd_vel", &motorD_cb );

void motorE_cb( const std_msgs::Int16& cmd_msg) {
  motorEsq(cmd_msg.data);
}
ros::Subscriber<std_msgs::Int16> motorE("cmd_vel1", &motorE_cb );

/*******************************************************************************/


/*******************************************************************************/
//Publishers for the encoders' data
/*******************************************************************************/
std_msgs::Int16 encoder1_value;
ros::Publisher encoder1("encoder1", &encoder1_value);

std_msgs::Int16 encoder0_value;
ros::Publisher encoder0("encoder0", &encoder0_value);
/*******************************************************************************/


void setup()
{
  motor_setup();
  encoder_setup();

  nh.initNode();
  nh.subscribe(motorD);
  nh.subscribe(motorE);
  nh.advertise(encoder0);
  nh.advertise(encoder1);
}

void loop()
{
  encoder1_value.data = encoder1Pos;
  encoder1.publish( &encoder1_value );

  encoder0_value.data = encoder0Pos;
  encoder0.publish( &encoder0_value );

  
  
  nh.spinOnce();
  delay(100);
}



