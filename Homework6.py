my_dict={'Anton':1988, 'Masha':1987,'Petya':1999}
print('Dict:',my_dict)
print('Existing value:', my_dict.get('Masha'))
print('Not existing value:',my_dict.get('Pasha'))
my_dict.update({'Slava':2005,
"Misha":2000})
print(my_dict)
p=my_dict.pop("Petya")
print('Deleted value:',p)
print('Modified dictionary:',my_dict)
my_set={1,2,3,4,'Груша',5,3,4,4,45.56}
print('Set:',my_set)
my_set.add("Petya")
my_set.add(100.57)
print('Modified set:',my_set)
