import math

x1,y1= map(float, input().split())
x2,y2= map(float, input().split())

DP=(x2-x1)**2 + (y2-y1)**2
x= math.sqrt(DP)

print("{:.4f}".format(x))