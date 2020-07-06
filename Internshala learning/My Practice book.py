# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:00:11 2020

@author: Gaurav
"""

import keyword
keyword.kwlist

#The purpose of this program is to display some text.#

print ("Hello World")
print ("Welcome to Internshala") #Author Internshala


Pattern = int(input())
#1ST pattern
print(end="*")
for i in range(1,int((Pattern-3)/2)+1):
    print(end=" ")
for i in range(1,int((Pattern+1)/2)+1):
    print(end="*")
print()
#2nd and 3rd pattern
for j in range(int((Pattern-3)/2)):
	print(end="*")
	for i in range(1,int((Pattern-3)/2)+1):
		print(end=" ")
	print('*')
#4rd pattern
for i in range(Pattern):
	print(end="*")
print()

#5th and 6th pattern
for j  in range(int((Pattern-3)/2)):
	for i in range(int((Pattern-3)/2)+1):
		print(end=" ")
	print(end="*")
	for i in range(1,int((Pattern-3)/2)+1):
		print(end=" ")
	print(end="*\n")
#7th pattern
for i in range(int((Pattern+1)/2)+1):
	print(end="*")
for i in range(int((Pattern-3)/2)+1):
	print(end=" ")
print(end="*")

for _ in range(int(input())):
    