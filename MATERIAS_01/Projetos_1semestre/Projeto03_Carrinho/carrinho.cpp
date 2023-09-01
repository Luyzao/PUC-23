#include <Servo.h>

// Definições dos pinos
const int leftServoPin = 5;
const int rightServoPin = 3;
const int lineFollowSensorPins[] = {12, 18, 17, 16, 19};
const int numSensors = sizeof(lineFollowSensorPins) / sizeof(lineFollowSensorPins[0]);

// Constantes do PID
const float Kp = 0.2;  // Ganho Proporcional
const float Ki = 0.1;  // Ganho Integral
const float Kd = 0.05; // Ganho Derivativo

// Valor de referência e valores iniciais
const int setpoint = 2; // Posição central
int lastError = 0;
int integral = 0;

Servo leftServo;
Servo rightServo;

void setup() {
  leftServo.attach(leftServoPin);
  rightServo.attach(rightServoPin);

  // Inicializa os sensores de seguidor de linha como entradas
  for (int i = 0; i < numSensors; i++) {
    pinMode(lineFollowSensorPins[i], INPUT);
  }
}

void loop() {
  int sensorValues[numSensors];

  // Lê os valores dos sensores
  for (int i = 0; i < numSensors; i++) {
    sensorValues[i] = digitalRead(lineFollowSensorPins[i]);
  }

  int erro = calcularErro(sensorValues);
  int sinalDeControle = calcularSinalDeControle(erro);

  // Ajusta as velocidades dos motores com base no sinal de controle
  int velocidadeEsquerda = constrain(1500 - sinalDeControle, 1000, 2000);
  int velocidadeDireita = constrain(1500 + sinalDeControle, 1000, 2000);

  leftServo.writeMicroseconds(velocidadeEsquerda);
  rightServo.writeMicroseconds(velocidadeDireita);
}

// Calcula o erro com base nos valores dos sensores
int calcularErro(int sensorValues[]) {
  int somaPonderada = 0;
  int soma = 0;

  for (int i = 0; i < numSensors; i++) {
    somaPonderada += sensorValues[i] * i;
    soma += sensorValues[i];
  }

  if (soma != 0) {
    return (somaPonderada / soma) - setpoint;
  } else {
    return 0;
  }
}

// Calcula o sinal de controle usando o algoritmo PID
int calcularSinalDeControle(int erro) {
  int proporcional = Kp * erro;
  integral += Ki * erro;
  int derivativo = Kd * (erro - lastError);

  lastError = erro;

  return proporcional + integral + derivativo;
}
