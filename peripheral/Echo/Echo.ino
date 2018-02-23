#include "R2ProtocolFSM.h"
uint8_t buffer[256];
r2pf_t fsm;

void setup() {
  Serial.begin(115200);
  fsm = r2pf_init(buffer, 256);
}

void loop() {
  while (Serial.available() > 0) {
    uint8_t b = Serial.read();
    r2pf_read(&fsm, b);
    if (fsm.done) {
      Serial.print(fsm.checksum);
      Serial.write('\n');

      Serial.write(fsm.type[0]);
      Serial.write(fsm.type[1]);
      Serial.write(fsm.type[2]);
      Serial.write(fsm.type[3]);
      Serial.write('\n');

      Serial.print(fsm.data_len);
      Serial.write('\n');
      
      for (uint32_t len = 0; len < fsm.data_len; len++) {
        Serial.write(fsm.data[len]);
      }
      Serial.write('\n');
      fsm.done = 0;
    }
  }
}
