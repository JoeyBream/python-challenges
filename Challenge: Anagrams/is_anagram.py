### A program which compares two strings, and returns True if they are anagrams of eachother.

def is_anagram(string1,string2):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        j = letters[i]
        if string1.count(j) != string2.count(j):
            return False
            break
    return True