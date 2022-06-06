#1. What does an empty dictionary's code look like?
empdict = {}
print(empdict)
#2. What is the value of a dictionary value with the key 'foo' and the value 42?
mydict = {'foo':42}
print(mydict)
#3. What is the most significant distinction between a dictionary and a list?
 ''' 
    --> List are ordered collections but dictionary is an unordered collections.
    --> List items are access by index position but dictionary items are access by its keys and value.
'''
#4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
'''It gives a KeyError'''
#5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
''' There is no difference. The in operator checks whether a value exists as a key in the dictionary.'''
#6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
''' 'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.'''
#7. What is a shortcut for the following code?if 'color' not in spam: spam['color'] = 'black'
''' spam.setdefault('color', 'black') '''
#8. How do you "pretty print" dictionary values using which module and function?
''' pprint.pprint() '''