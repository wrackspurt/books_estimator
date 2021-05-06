import pandas as pd
genres_dict = {"16th Century": [0],
"18th Century": [0],
"19th Century": [0],
"20th Century": [0],
"21st Century": [0]}

#ulist = ["16th Century", "20th Century", "None"]
ulist = ['None']

print(ulist)

"""for u in ulist:
    if u in genres_dict.keys():
        genres_dict[u][0] += 1

print(genres_dict)"""

if "None" in ulist:
    ulist.remove("None")

if len(ulist) == 0:
    print('sad')

df1 = {'r1': [1], 'r2': [2], 'r3': [3]}
df2 = {'r4': [4], 'r5': [5]}

ds = pd.DataFrame({**df1, **df2})
print(ds)


