import matplotlib.pyplot as plt
import  numpy as np
import pandas as pd
plt.title("Test Plot",fontdict= {"fontsize":15})
plt.figure(figsize=(3,3), dpi=300)
plt.xlabel("X")
plt.ylabel("Y")
plt.xticks([0,1,2,3])
plt.yticks([0,5,100])



plt.plot([1,2,3],[2,4,6],marker= '.' , markersize=10)

plt.savefig("mygraph.png",dpi=500)
plt.show()

#