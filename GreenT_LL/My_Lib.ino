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


/****************************Funções dos motores********************************/

void motor_setup() {
  //0-127: roda no sentido direto
  //127-255: roda no sentido inverso

  pinMode(LEFT_MOTOR, OUTPUT);
  pinMode(LEFT_MOTOR_PWM, OUTPUT);
  pinMode(RIGHT_MOTOR_PWM, OUTPUT);
  pinMode(RIGHT_MOTOR, OUTPUT);

  //initialization of motors

  digitalWrite(RIGHT_MOTOR, LOW);
  digitalWrite(LEFT_MOTOR, LOW);

  //alteracao da frequencia PWM Timer1: 4kHz
  TCCR2B = TCCR2B & 0b11111000 | 0x02;
}
/*******************************************************************************/

/*******************************************************************************/
void motorDir (int speed) {
  encoder1Pos = 0;
  digitalWrite(RIGHT_MOTOR, HIGH);
  if (speed >= 0)   {
    speed = map(speed, 0, 255, 127, 0);
    analogWrite(RIGHT_MOTOR_PWM, speed);
  }
  else {
    speed = map(speed, 0, -255, 127, 255);
    analogWrite(RIGHT_MOTOR_PWM, speed);
  }
}
/*******************************************************************************/

/*******************************************************************************/
void motorEsq (int speed) {
  encoder0Pos = 0;
  digitalWrite(LEFT_MOTOR, HIGH);
  if (speed >= 0)   {
    speed = map(speed, 0, 255, 127, 0);
    analogWrite(LEFT_MOTOR_PWM, speed);
  }
  else {
    speed = map(speed, 0, -255, 127, 255);
    analogWrite(LEFT_MOTOR_PWM, speed);
  }
}
/*******************************************************************************/


/*******************************************************************************/
/*******************************************************************************/

/**************************Funções dos encoders*********************************/

void encoder_setup() {
  //Mega possui interrupções nos pinos 2, 3, 21, 20, 19, 18

  pinMode(PinAencoder0, INPUT);
  pinMode(PinBencoder0, INPUT);

  pinMode(PinAencoder1, INPUT);
  pinMode(PinBencoder1, INPUT);

  attachInterrupt(0, processaEncoder0, RISING);  // encoder pin on interrupt 0 - pin 2
  attachInterrupt(1, processaEncoder1, RISING);  // encoder pin on interrupt 0 - pin 3
}
/*******************************************************************************/

/*******************************************************************************/
void processaEncoder0() {
  /* Se o pino A e B estiverem ambos a HIGH a rotação é para a frente
     Se forem diferentes a rotação é para trás
  */
  if (digitalRead(PinAencoder0) == digitalRead(PinBencoder0)) {
    encoder0Pos++;
  } else {
    encoder0Pos--;
  }

}
/*******************************************************************************/

/*******************************************************************************/
void processaEncoder1() {
  /* Se o pino A e B estiverem ambos a HIGH a rotação é para a frente
     Se forem diferentes a rotação é para trás
  */
  if (digitalRead(PinAencoder1) == digitalRead(PinBencoder1)) {
    encoder1Pos--;
  } else {
    encoder1Pos++;
  }

}

/* -------------------------------*/
