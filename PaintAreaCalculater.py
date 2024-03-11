import math
def paint_calc(height,width,cover):
  number_of_cans = (height * width) / cover
  round_up = math.ceil(number_of_cans)
  print(f"You'll need {round_up} cans of paint.")

h = int(input()) # Height of wall (m)
w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=h, width=w, cover=coverage)