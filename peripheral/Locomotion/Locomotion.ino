// Left Motor
int LeftSpeedRead = A0;
int LeftSpeedSet = 11;
int LeftDir = 1;
int LeftCW = 10;
int LeftCCW = 9;

// Right Motor
int RightSpeedRead = A1;
int RightSpeedSet = 6;
int RightDir = 1;
int RightCW = 5;
int RightCCW = 4;

void setup() {
  pinMode(LeftSpeedRead, INPUT);
  pinMode(LeftSpeedSet, OUTPUT);
  pinMode(LeftCW, OUTPUT);
  pinMode(LeftCCW, OUTPUT);
  digitalWrite(LeftCW, HIGH);
  digitalWrite(LeftCCW, LOW);

  pinMode(RightSpeedRead, INPUT);
  pinMode(RightSpeedSet, OUTPUT);
  pinMode(RightCW, OUTPUT);
  pinMode(RightCCW, OUTPUT);
  digitalWrite(RightCW, LOW);
  digitalWrite(RightCCW, HIGH);

  analogWrite(LeftSpeedSet, 50); // x/255*100% PWM
  analogWrite(RightSpeedSet, 50); // x/255*100% PWM

  Serial.begin(115200);
}

char command;
int value;
int inputIndex = 0;

void loop() {
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (inChar == '\n') {
      Serial.println(command);
      Serial.println(value);

      // Parse command
      if (command == 'H') { // Head motor
        if (value < 0) {
          value = 0;
        }
        if (value > 180) {
          value = 180;
        }
        HeadSpeedSet = value;
      }
      else if (command == 'L') { // Left motor forward
        if (LeftDir == 0) {
          digitalWrite(LeftCW, HIGH);
          digitalWrite(LeftCCW, LOW);
          LeftDir = 1;
        }
        analogWrite(LeftSpeedSet, value);
      }
      else if (command == 'l') { // Left motor backward
        if (LeftDir == 1) {
          digitalWrite(LeftCW, LOW);
          digitalWrite(LeftCCW, HIGH);
          LeftDir = 0;
        }
        analogWrite(LeftSpeedSet, value);
      }
      else if (command == 'R') { // Right motor forward
        if (RightDir == 0) {
          digitalWrite(RightCW, LOW);
          digitalWrite(RightCCW, HIGH);
          RightDir = 1;
        }
        analogWrite(RightSpeedSet, value);
      }
      else if (command == 'r') { // Right motor backward
        if (RightDir == 1) {
          digitalWrite(RightCW,HIGH);
          digitalWrite(RightCCW,LOW);
          RightDir = 0;
        }
        analogWrite(RightSpeedSet, value);
      }

      inputIndex = 0;
      command = ' ';
      value = 0;
    }
    else {
      if (inputIndex == 0) {
        command = (char) inChar;
        inputIndex++;
      }
      else if (inputIndex == 1) {
        value = inChar;
        inputIndex++;
      }
    }
  }
}
