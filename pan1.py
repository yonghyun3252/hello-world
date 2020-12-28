import pandas as pd


friend_list = [
    ['name', ['john', 'jenny', 'nate']],
    ['age', [20,30,40]],
    ['job', ['student', 'teacher', 'manager']]
]
df = pd.DataFrame.from_dict(dict(friend_list))
print(df)
