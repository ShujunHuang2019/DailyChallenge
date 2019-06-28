import pandas as pd
from pandas import Series, DataFrame
mjp= Series([5,4,3,2,1])
mjp
mjp.values
mjp.index

jeeva = Series([5,4,3,2,1,-7,-29], index =['a','b','c','d','e','f','h'])
jeeva
jeeva["d"]
jeeva[["a", "d", "h"]]

import numpy as np
np.mean(jeeva)

print("b" in jeeva)
print("z" in jeeva)

player_salary = {"john": 30000, "davie": 40000, "seb": 90000}
player_salary
player_salary["john"]
player_salary.keys
new_player = Series(player_salary)

players = ["Klose", "Messi", "Rona"]
players

states = {'State' :['Gujarat', 'Tamil Nadu', ' Andhra', 'Karnataka', 'Kerala'], 'Population': [36, 44, 67,89,34],'Language' :['Gujarati', 'Tamil', 'Telugu', 'Kannada', 'Malayalam']}
india = DataFrame(states) # creating a data frame
india

DataFrame(states, columns=['State', 'Language', 'Population'])

new_farme = DataFrame(states,
columns=['State', 'Language', 'Population', 'Per Capita Income'],
index =['a','b','c','d','e'])

print new_farme.columns

new_farme.Population
new_farme.ix[3]

new_farme.head(3)
new_farme.tail(3)
new_farme.index
new_farme.columns
new_farme.values
type(new_farme.describe)
