import numpy as np
import matplotlib.pyplot as plt
 

height = [101,0]
bars = ('Women','')
y_pos = np.arange(len(bars))
 

plt.barh(y_pos, height)
plt.yticks(y_pos, bars)
plt.xlabel("Total Medal Count")
plt.title("Canadian Women's Total Medal Count in Ice Hockey since 1994")
plt.show()
