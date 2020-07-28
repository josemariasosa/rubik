import pandas as pd
import rubik as rk

test = [
{   
        "id": 1,
        "name": "jose",
        "data": None
    },
    {
        "id": 1,
        "name": "jose",
        "data": None
    },
    {
        "id": 1,
        "name": "jose",
        "data": None
    },
    {
        "id": 2,
        "name": "maria",
        "data": {}
    },
    {
        "id": 2,
        "name": "maria",
        "data": None
    }
]
test = pd.DataFrame(test)
test = rk.ungroup_dict(test, 'data')

print(test)

