matrix = [
    [i for i in range(1,10)],
    [i for i in range(11,20)],
    [i for i in range(21,30)],
    [i for i in range(31,40)],
    [i for i in range(41,50)],
    [i for i in range(51,60)],
    [i for i in range(61,70)],
    [i for i in range(71,80)],
    [i for i in range(81,90)],
    [i for i in range(91,100)],
    [i for i in range(101,110)],
    [i for i in range(111,120)],
    [i for i in range(121,130)],
    [i for i in range(131,140)],
    [i for i in range(141,150)],
    [i for i in range(151,160)],
    [i for i in range(161,170)],
    [i for i in range(171,180)],
    [i for i in range(181,190)],
    [i for i in range(191,200)],
    [i for i in range(201,210)],
    [i for i in range(211,220)],
    [i for i in range(221,230)],
    [i for i in range(231,240)],
    [i for i in range(241,250)],
    [i for i in range(251,260)],
    [i for i in range(261,270)],
    [i for i in range(271,280)],
    [i for i in range(281,290)],
    [i for i in range(291,300)]
    
    ]
import random
for i in matrix:
    random.shuffle(i)

import matplotlib.pyplot as plt
plt.matshow(matrix)
plt.axis("off")
plt.show()
plt.savefig("colors.png")