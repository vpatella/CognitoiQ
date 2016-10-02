#!/usr/bin/python
import sys

def are_anagrams(str1,str2):
        if sorted(str1) == sorted(str2):
                return True
        else:
                return False

print("Enter the first word:")
str1 = sys.stdin.readline()
print("Enter the second word:")
str2 = sys.stdin.readline()
print(are_anagrams(str1,str2))
