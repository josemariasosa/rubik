import pandas as pd
import rubik as rk

test = [
	{
		"id": 1,
		"name": "jose",
        "data": {
            "phone": "3333333333",
            "address": "somewhere over the rainbow."
        }
	},
	{
		"id": 2,
		"name": "maria",
        "data": {
            "phone": "4444444444",
            "address": "under the sea."
        }
	}
]
test = pd.DataFrame(test)
test = rk.ungroup_dict(test, 'data')

print(test)

