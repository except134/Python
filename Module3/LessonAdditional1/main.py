data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(ds):
    ret = []
    for i in ds:
        if isinstance(i, int):
            ret.append(i)
        elif isinstance(i, str):
            ret.append(len(i))
        elif isinstance(i, dict):
            if len(i) > 0:
                ret.append(calculate_structure_sum(list(i.keys())))
                ret.append(calculate_structure_sum(list(i.values())))
        else:
            if len(i) > 0:
                ret.append(calculate_structure_sum(i))
    else:
        return sum(ret)
    
result = calculate_structure_sum(data_structure)
print(result)



