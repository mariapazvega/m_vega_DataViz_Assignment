import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 


Gold= [0,0, 19, 19, 21, 21]
Silver= [0,20, 0, 0, 0, 0]
Bronze= [0,0, 0, 0, 0, 0]
Year = [1994,1998, 2002, 2006, 2010, 2014]


plt.plot(Year, Gold, color='yellow', label='Gold')
plt.plot(Year, Silver, color='grey', label='Silver')
plt.plot(Year, Bronze, color='brown', label='Bronze')




plt.title("Women's medal count")
plt.ylabel("Medal Counts Since 1994")
plt.xlabel("Year 1994-2014")
plt.legend()
plt.show()