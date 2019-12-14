import numpy as np
import matplotlib.pyplot as plt
 

height = [101, 262]
bars = ('Women','Men')
y_pos = np.arange(len(bars))
 

plt.barh(y_pos, height)
plt.yticks(y_pos, bars)
plt.xlabel("Men and Women's Total Medal Count")
plt.title("Canadian Men and Women's Total Medal Count in Ice Hockey since 1994")
plt.show()
