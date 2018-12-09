import numpy as np
from scipy.stats import mode

ins = np.genfromtxt('data/day6.csv', delimiter=',', dtype=np.int)
# print(ins)

# print(ins[:,1])
# set up

minx = min(ins[:,0])
miny = min(ins[:,1])
maxx = max(ins[:,0])
maxy = max(ins[:,0])
xrange = maxx-minx
yrange = maxy-miny
num_points = len(ins[:,0])
#
field = np.zeros((xrange,yrange))
print(field)

def manhattan_dist(arr1,arr2):
    """

    :param arr: n-d vectors of same dim
    :return: absolute value manhattan distance
    """
    sub = arr1-arr2
    dist = np.sum(sub)
    return abs(dist)

# debug...
# a = manhattan_dist(minx,miny)
# print(a)
# print(maxx)
# print(maxy)
# print(yrange)
# print(miny)

#wrap in fuction to go over all of input array (generate xrange/yrange) then subtract two different sized fields to
# determine which are infinite and not

for x in range(xrange): # # SLOW... :(
    for y in range(yrange):
        dists = [999999] #placeholder for ties and shifts index of points to start at 1
        for i in ins:
            dists.append(manhattan_dist((x,y),i))
            min_dist = min(dists)
            #ties
            if dists.count(min_dist) > 1:
                field[x,y] = 999999
                break
            field[x,y] = dists.index(min_dist)
            # print(dists)
            # print(field[x,y])
        # print(x,y)
print(field)
print(mode(field, axis = None)) #drop 999999 somehow..