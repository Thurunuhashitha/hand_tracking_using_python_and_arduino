int enA = 5;
int in1 = 2;
int in2 = 3;
int a = 0;
int b = 0;
int speed = 80;

void setup() {
  Serial.begin(9600);
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char receivedChar = Serial.read();
    if (isdigit(receivedChar)) {
      int number = receivedChar - '0';
      switch (number) {
        case 5:
          delay(70);
          a = 0;
          break;

        case 1:
          delay(70);
          a = 1;
          break;

        case 0:
          delay(70);
          b = 0;
          break;

        case 2:
          delay(70);
          b = 1;

          break;

        case 3:
          delay(70);
          b = 2;
          break;
      }
    }
  }
  if (a == 1) {

    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    analogWrite(enA, speed);
   // Serial.println(speed);
    if (b == 1) {
      if (speed < 255) {
        speed++;
        delay(150);
      }
    }
    if (b == 2) {
      if (speed > 70 ) {
        speed--;
        delay(150);
      }
    }
  }
  if (a == 0) {

    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    analogWrite(enA, 0);
   // Serial.println("stop");
  }
}
