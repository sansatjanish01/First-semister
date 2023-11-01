import pandas as pd
import numpy as np

a = {
    'car':["nano","BMW","Volvo"],
    'age':[3,6,8]
}
data = pd.DataFrame(a)
print(data)

my = [[3,4,5,6,7],[54,65,43,32,5]]
p = np.array(my)
print(p)