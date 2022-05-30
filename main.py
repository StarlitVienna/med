#!/usr/bin/env python3

# Import the necessary libraries
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
motorA = Motor(Port.A)
motorB = Motor(Port.B)

left_motor = motorA
right_motor = motorB

color_sensora = ColorSensor(Port.S1)
color_sensorb = ColorSensor(Port.S2)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=152)
robot.settings(straight_speed=100, straight_acceleration=100, turn_rate=100)

while robot.distance() <= 10000000:
    correction1 = (75- color_sensora.reflection())*3
    correction2 = (75 - color_sensorb.reflection())*3
    robot.drive(100, correction1)
    robot.drive(100, correction2)
    
robot.stop()
left_motor.brake()
right_motor.brake()


