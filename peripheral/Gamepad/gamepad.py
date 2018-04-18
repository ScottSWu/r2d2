import math
import pygame
import signal
import socket
import sys
import time

pygame.init()
pygame.joystick.init()

print("Joysticks:")
for i in range(pygame.joystick.get_count()):
  print("-", pygame.joystick.Joystick(i).get_name())
print()

if pygame.joystick.get_count() == 0:
  print("Error: No joysticks found")
  sys.exit(1)

# Setup
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Joystick {} buttons {} axes {} hats".format(joystick.get_numbuttons(), joystick.get_numaxes(), joystick.get_numhats()))

motor_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
motor_sock.connect((sys.argv[1], int(sys.argv[2])))

sound_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sound_sock.connect((sys.argv[1], int(sys.argv[3])))

def signal_handler(signal, frame):
  print("Exiting")
  motor_sock.close()
  sound_sock.close()
  joystick.quit()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print("Running")

def map_motor(x):
  s = -1 if x < 0 else 1
  x = abs(x)
  if x < 0.2:
    return 0.0
  return s * (x - 0.2) / 0.8 * 0.5

def tank_drive(jx, jy):
  jx = map_motor(jx)
  jy = map_motor(jy)
  # Rotate 135 degrees counter-clockwise so that up is forward
  r = math.hypot(jx, jy)
  a = math.atan2(jy, jx) - math.pi * 5.0 / 4.0
  return r * math.cos(a), r * math.sin(a)

running = True
last_sound = 0
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False

  if joystick.get_button(6) == 1: # Back button
    running = False

  print(joystick.get_axis(0), joystick.get_axis(1),
      joystick.get_button(0), joystick.get_button(1),
      joystick.get_button(2), joystick.get_button(3),
      joystick.get_hat(0))

  # Send motors, mapping [0.2, 1.0] to [0.0, 0.5]
  tx, ty = tank_drive(joystick.get_axis(0), joystick.get_axis(1))
  hd = 0.0
  if joystick.get_button(4) == 1:
    hd = -0.5
  elif joystick.get_button(5) == 1:
    hd = 0.5
  motor_sock.send("{},{},{}\n".format(tx, ty, hd).encode("utf8"))

  # Send buttons, using DPad as different sets, timeout 5 seconds
  btn = None
  for i in range(4):
    if joystick.get_button(i) == 1:
      btn = i

  if btn is not None:
    if time.time() - last_sound > 5:
      set = 0
      dx, dy = joystick.get_hat(0)
      if dx == 1:
        set = 1
      elif dx == -1:
        set = 2
      elif dy == 1:
        set = 3
      elif dy == -1:
        set = 4

      btn = set * 4 + btn
      sound_sock.send((str(btn) + "\n").encode("utf8"))
      last_sound = time.time()

  time.sleep(0.05)

joystick.quit()
pygame.quit()
sys.exit(0)
