import os

Sum_pi = 0
I = -1
j = 0

while True:
    I = I + 2
    j = 1 - j
    if(j == 1):
        Sum_pi = Sum_pi + (4/I)
    else:
        Sum_pi = Sum_pi - (4/I)

    print(Sum_pi)
