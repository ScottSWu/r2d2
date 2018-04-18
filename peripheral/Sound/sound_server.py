#!/usr/bin/env python

import select
import serial
import signal
import socket
import struct
import subprocess
import sys
import time
import traceback

TCP_IP = '0.0.0.0'
TCP_PORT = 9001
BUFFER_SIZE = 8

def signal_handler(signal, frame):
  print("Exiting")
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print("Listening")

try:
  while True:
    try:
      conn, addr = s.accept()
      print("Accept")
      data = b""
      while True:
        try:
          r = conn.recv(BUFFER_SIZE)
          if not r:
            print("No data")
            break

          data += r
          if data[-1] == ord('\n'):
            data = data.strip().decode("utf8")
            print(data)
            sound_index = int(data)
            if 1 <= sound_index and sound_index <= 20:
              subprocess.call(["aplay", "-D", "hw:1", "../../../r2d2_sounds/" + str(sound_index) + ".wav"])

            data = b""
        except BlockingIOError:
          pass

      print("Close")
      conn.close()
    except BlockingIOError:
      pass
except Exception as e:
  print(e)
  traceback.print_exc()
