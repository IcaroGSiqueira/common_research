import matplotlib.pyplot as plt
import numpy as np

plt.clf()

# using some dummy data for this example
xs = [1,2,3,4]
ys = [1,2,3,4]

plt.scatter(xs,ys)

# zip joins x and y coordinates in pairs
for x,y in zip(xs,ys):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,5,0.5))

plt.show()