#include "R2Protocol.h"

uint8_t buffer[256];
r2pf_t fsm;

void setup() {
  Serial.begin(115200);
  fsm = r2pf_init(buffer, 256);
}

void send(char type[5], const uint8_t* data, uint32_t data_len) {
  uint32_t written = r2p_encode(type, data, data_len, buffer, 256);
  Serial.write(buffer, written);
}

void loop() {
  while (Serial.available() > 0) {
    uint8_t b = Serial.read();
    r2pf_read(&fsm, b);
    if (fsm.done) {
      if (strncmp("WHO", fsm.type, 3) == 0) {
        send("WHO\0", reinterpret_cast<const uint8_t*>("ECHO"), 4);
      }
      else if (strncmp("PING", fsm.type, 4) == 0) {
        send("PONG", 0, 0);
      }
      else {
        send(fsm.type, fsm.data, fsm.data_len);
      }
      fsm.done = 0;
    }
  }
}
