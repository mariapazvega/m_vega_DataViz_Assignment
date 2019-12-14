import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 

Men = [12,0, 23, 23, 23, 25]
Women = [0,20, 20, 19, 21, 21]
Year = [1994,1998, 2002, 2006, 2010, 2014]


plt.plot(Year, Women, color='pink', label='Women')
plt.plot(Year, Men, color='blue', label='Men')



plt.title("Comparison between Canadian Men and Women's medal count")
plt.ylabel("Medal Counts Since 1994")
plt.xlabel("Year 1994-2014")
plt.legend()
plt.show()