from system import scapegoat
import math

input = calculator.input

def trig(type):
  radian = math.radian(int(calculator.input))
  if type.lower() == "sin":
    return math.sin(radian)
  elif type.lower() == "cos":
    return math.cos(radian)
  elif type.lower() == "tan":
    return math.tan(radian)

def pi():
  return math.pi

def calc():
  return eval(input)
