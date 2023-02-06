import csv
import matplotlib.pyplot as plt
import numpy as np
import time

with open('Homework 1\SmallMap.csv', newline='') as f:
    reader = csv.reader(f)
    mapList = list(reader)

height = len(mapList)
width = len(mapList[1])
#print('{} {}'.format(height,width))

plt.ion()
plt.show()

rowCounter = 0
entryCounter = 0
for row in mapList:
    rowCounter += 1
    for entry in row:
        entryCounter += 1
        if entry == '1':
            plt.plot(entryCounter, height-rowCounter, 'ko')
        elif entry == '2':
            plt.plot(entryCounter, height-rowCounter, 'bx')
        elif entry == '3':
            plt.plot(entryCounter, height-rowCounter, 'gx')
    entryCounter = 0
plt.axis('equal')
point = plt.plot(0, 0, 'rx')[0]

start_time = time.time()
t = 0
while t < 4:
    end_time = time.time()
    t = end_time - start_time
    point.set_data(t, t)
    plt.pause(1e-10)