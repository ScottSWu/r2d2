import serial, sys, time

if __name__ == "__main__":
  s = serial.Serial(sys.argv[1], baudrate=115200, timeout=1)
  time.sleep(2)
  s.write(b"\xa2\xb2\xc2\x00\x00TEST\x00\x00\x00\x0CHello world!\xd2\xe2\xf2")
  time.sleep(0.1)
  output = s.read(s.in_waiting)
  s.close()
  print(str(output, "utf8"))
