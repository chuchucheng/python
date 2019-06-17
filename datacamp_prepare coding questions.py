# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:18:23 2019

@author: ccc
"""

################ List methods ###############

basket1 =['banana', 'kiwifruits', 'grapefruits', 'apples', 'apricots', 'nectarines', 'oranges', 'peaches', 'pears', 'lemons']
basket2 =['apples', 'grapes', 'apricots', 'dragonfruits', 'peaches', 'pears', 'limes', 'papaya']

# Remove fruits from basket2 that are present in basket1
for item in basket1:
    if item in basket2:
        basket2.remove(item)

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))

# Transfer fruits from basket1 to basket2 to make them length approximately equal
while len(basket2)<len(basket1):
    item_to_transfer = basket1.pop()
    basket2.append(item_to_transfer)

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))

################ Operations on sets ###############
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 7, 9, 11, 13, 15}
C = {1, 2, 8, 10, 11, 12, 13, 14, 15, 16, 17}
D = {1, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
E = {9, 10, 11, 12, 13, 14, 15}

A.union(B.intersection(C)) - D.intersection(E)



################ Store dictionary  ###############
range_x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
range_y = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

circ_parab = dict()

for x in range_x:
    for y in range_y:       
        # Calculate the value for z
        z = x**2 + y**2
        # Create a new key for the dictionary
        # key = (x, y)
        # Create a new key-value pair      
        circ_parab[(x, y)] = z
        
        circ_parab[(1.8,1.4)]

################ String indexing and concatenation ###############
alphabet ='abcdefghijklmnopqrstuvwxyz'       
        
def encrypt(text, key):
  
    result = ''

    # Fill in the blanks to create an encrypted text
    for char in text.lower():
        idx = (alphabet.index(char) + key) % len(alphabet)
        # for decription: idx = alphabet.index(char) - key
        result = result + alphabet[idx]

    return result

# Check the encryption function with the shift equals to 2
print(encrypt("datacamp", 2))    

################ String ###############
text ='StRing ObJeCts haVe mANy inTEResting pROPerTies'
# Create a word list from the string stored in 'text'
word_list = text.split()

# Make every other word uppercased; otherwise - lowercased
for i in range(len(word_list)):
    if (i + 1) % 2 == 0:
        word_list[i] = word_list[i].upper()
    else:
        word_list[i] = word_list[i].lower()
        
# Join the words back and form a new string
new_text = ' '.join(word_list)
print(new_text)

# fix string errors
heroes = ''
heroes['Hair color'] = ('No Hair','BLOND','BLACK')
heroes['Gender'] = ['Fmale','male']
# Make all the values in the 'Hair color' column lowercased
heroes['Hair color'] = heroes['Hair color'].str.lower()
  
# Check the values in the 'Hair color' column
print(heroes['Hair color'].value_counts())

# Substitute 'Fmale' with 'Female' in the 'Gender' column
heroes["Gender"] = heroes['Gender'].str.replace('Fmale','Female')

# Check if there is no occurences of 'Fmale'
print(heroes['Gender'].value_counts())


################ regular expression ###############
import re

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############


