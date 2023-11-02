import pandas as pd
import numpy as np

dat = {
    'car':["BMW","Volvo","Shift","Nishan"],
    'age':[3,5,4,3],
    'model':[2021,2018,2023,2020],
    'color':["red","green","black","white"]
}
vari = pd.DataFrame(dat)
print(vari)
print(type(vari))
print(type(dat))