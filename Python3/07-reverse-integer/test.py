dict1 = {'key1':{'a': 1, 'b': 2},'key2':{'a': 3, 'b': 4},'key3':{'a': 5, 'b': 6}}

print(sum(i['b'] for i in dict1.values()))

