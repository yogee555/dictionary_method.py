# Dictionary Method

# copy()
# creating original dictionary
original_dictionary = {"name":"yogi","age":29,"city":"new york"}
# creating a shallow copy using the copy() method
copied_dictionary = original_dictionary.copy()
print("original_dictionary:",original_dictionary)
print("copied_dictionary:",copied_dictionary)

# clear()
emp = {'name':'john','age':25,'job':'HR','sal':725000}
print("Dictionary:",emp)
print("Dictionary Length:",len(emp))
emp.clear()
print("\nDictionary:",emp)
print("Dictionary Length:",len(emp))

# pop
mydict={1:'apple',2:'banana',3:'orange',4:'kiwi'}
print('dictionary items:',mydict)
# pop values
print('\nremoved items:',mydict.pop(3))
print('dictionary items:',mydict)
# pop values
print('\nremoved items:',mydict.pop(1))
print('dictionary items:',mydict)

# values
emp = {'name':'kevin','age':25,'job':'HR','sal':725000}
print("dictionary:",emp)
# print values
print("dictionary values:",emp.values())
employ = {}
print("\ndictionary:",employ)
# print values
print("dictionary values:",employ.values())

# items
emp = {'name':'kevin','age':25,'job':'HR','sal':725000}
print("dictionary:",emp)
# print items
print("dictionary items:",emp.items())
# creating empty dictinory
employ = {}
print("\ndictionary:",employ)
# print items
print("dictionary items:",employ.items())

# keys
emp = {'name':'kevin','age':25,'job':'HR','sal':725000}
print("dictionary:",emp)
# print keys
print("dictionary keys:",emp.keys())
# creating empty dictinory
employ = {}
print("\ndictionary:",employ)
# print keys
print("dictionary keys:",employ.keys())

# get
dname = {1:'apple',2:'banana',3:'orange',4:'kiwi'}
print("available items:",dname)
print("\nvalue of key2:",dname.get(2))
print("value of key3:",dname.get(3))
print("value of key4:",dname.get(4))
print("value of key1:",dname.get(1))

# fromkeys
# 1
keys = {'a','b','c','d','e'}
mydict = dict.fromkeys(keys)
print("dictionary keys:",mydict)
#2
l=[2,4,6,8,10,12]
d1=dict.fromkeys(l)
print(d1)
d2=dict.fromkeys(l,"even")
print(d2)
#3
seq=('name','age','sex')
dict=dict.fromkeys(seq)
print("new dictionary:%s"%str(dict))
dict=dict.fromkeys(seq,10)
print("new dictionary:%s"%str(dict))

# popitems
mydict = {1:'apple',2:'banana',3:'orange',4:'kiwi'}
print("dictionary items:",mydict)
# popitems
print("\nremoved items:",mydict.popitem())
print("dictionary items:",mydict)
# add new item
mydict[5]='mango'
print("\ndictionary items:",mydict)
# popitems
print("\nremoved items:",mydict.popitem())
print("dictionary items:",mydict)

# update
mydict = {1:'apple',2:'banana'}
mynewdict = {3:'orange',4:'banana'}
print("dictionary item:",mydict)
print("new dictionary item:",mynewdict)
# update items
mydict.update(mynewdict)
print("\ndictionary item:",mydict)

# setdefault
#1
# creating dictionary
a_dict={1:'one',2:'two',3:'three'}
print(a_dict)
# add new value by passing key & value
print(a_dict.setdefault(4,'four'))
print(a_dict)
print(a_dict.setdefault(2,'two-update'))
print(a_dict)
# new key without value
print(a_dict.setdefault(5))
print(a_dict)
#2
emp={'name':'kevin','age':25,'sal':725000}
print('dictionary:',emp)
# print value using key
print("\n dictionary value:",emp.setdefault('age',None))
print("\n dictionary value:",emp.setdefault('job',None))
print("\n dictionary value:",emp.setdefault('sex',None))
print("\n dictionary value:",emp.setdefault('name',None))

# print min & max value
r1={'a':25,'b':65,'h':10}
e=min(r1.values())
k=max(r1.values())
print(e)
print(k)

