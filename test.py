import pandas as pd
import rubik as rk
import numpy as np

test = [
{   
        "id": 1,
        "name": "jose",
        "data": np.nan
    },
    {
        "id": 1,
        "name": "jose",
        "data": {'np.nan': 1}
    },
    {
        "id": 1,
        "name": "jose",
        "data": np.nan
    },
    {
        "id": 2,
        "name": "maria",
        "data": np.nan
    },
    {
        "id": 2,
        "name": "maria",
        "data": np.nan
    }
]
test = pd.DataFrame(test)
print(test)
test = rk.ungroup_dict(test, 'data')

print(test)

