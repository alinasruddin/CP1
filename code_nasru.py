import random
from operator import itemgetter
import numpy
import matplotlib.pyplot as plt
import sys
import pygame

pygame.init()

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
green = (0,255,0)
Height = 512
Width = 1024
points = []



n = input("Enter Number of points:")
X = random.sample(range(1, Width-1), n)
Y = random.sample(range(1, Height-1), n)

i=0
while i<n:
	points.append([X[i],Y[i]])
	i = i + 1
print points


max = sys.maxint
min = -sys.maxint-1
leftMost = [max,max]
rightMost = [min,min]


for ptr in points:

	if ptr[0] < leftMost[0]:
		leftMost = ptr
	if ptr[0] > rightMost[0]:
		rightMost = ptr

print leftMost
print rightMost


def isUpper(L,R,P):
	if ((P[1]-L[1])*(R[0]-L[0]) - (P[0]-L[0])*(R[1]-L[1])) > 0:
		return 1
	return 0

upper = []
lower = []
for ptr in points:
	if ptr != leftMost and ptr != rightMost:
		if isUpper(ptr,leftMost,rightMost):
			upper.append(ptr)
		else:
			lower.append(ptr)

print ("upper")
print upper

print ("lower")
print lower
lower_size = len(lower)
upper_size = len(upper)

print "No of elements in upper="
print upper_size

print "No of elements in lower="
print lower_size


upper.sort(key = lambda x : x[0])
upper.reverse()
print ("Sorted upper")
print upper

lower.sort(key = lambda x : x[0])
print ("Sorted lower")
print lower

lower.insert(0,leftMost)
upper.insert(0,rightMost)

newpoints = [lower , upper]
print newpoints

x_lm, y_lm = leftMost
x_rm, y_rm = rightMost

x = [x[0] for x in newpoints]
y = [y[1] for y in newpoints]
Ax = [x[0] for x in lower]
Ay = [y[1] for y in lower]
Bx = [x[0] for x in upper]
By = [y[1] for y in upper]
plt.plot(Ax, Ay, 'o', c='orange') # below the line
plt.plot(Bx, By, 'o', c='blue') # above the line
plt.plot(x_lm, y_lm, 'o', c='green') # leftmost point
plt.plot(x_rm, y_rm, 'o', c='red') # rightmost point
x_plot = plt.plot([x_lm, x_rm], [y_lm, y_rm], linestyle=':', color='black', linewidth=0.5) # polygon's division line
x_plot = plt.plot(x , y , color='black', linewidth=1)

# # connect points by line in order of apperiance
plt.show()
"""
lower.insert(0,leftMost)
upper.insert(0,rightMost)
newpoints = lower + upper
#algortihm
#create a  list newPolygon with points in proper order


size = [Width,Height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CODING PROJECT")

done = False

clock = pygame.time.Clock();

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
	    done = True

    screen.fill(white)
    pygame.draw.polygon(screen, green, newpoints, 2)

    #for i in range(15):
    #    pygame.draw.line(screen, green, [i*10,100], [40,490],2)
    pygame.display.flip()


    clock.tick(20)
	"""
