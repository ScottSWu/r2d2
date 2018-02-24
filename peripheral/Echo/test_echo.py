import serial
import sys
import time
import unittest

sys.path.insert(0, "../../protocol/reference")
import R2Protocol

DEVICE_PATH = ""

class TestEcho(unittest.TestCase):
  def setUp(self):
    self.conn = serial.Serial(DEVICE_PATH, baudrate=115200, timeout=1)
    time.sleep(2)

  def tearDown(self):
    self.conn.close()
    time.sleep(0.1)

  def test_who(self):
    buffer = R2Protocol.encode(b"WHO", b"")
    golden = R2Protocol.encode(b"WHO", b"ECHO")
    self.conn.write(buffer)
    time.sleep(0.1)
    output = self.conn.read(self.conn.in_waiting)
    self.assertEqual(output, golden)

  def test_simple_echo(self):
    buffer = R2Protocol.encode(b"TEST", b"Hello world!")
    self.conn.write(buffer)
    time.sleep(0.1)
    output = self.conn.read(self.conn.in_waiting)
    self.assertEqual(output, buffer)

if __name__ == "__main__":
  DEVICE_PATH = sys.argv[1]
  sys.argv = sys.argv[:1]
  unittest.main()
