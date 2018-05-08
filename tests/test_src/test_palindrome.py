# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:31:47 2018

@author: laetitialachat
"""

def isPalindrome(word):
    if str(word).lower()==str(word)[::-1].lower():
        return True
    return False

def test_palindrome_string():
	assert isPalindrome("abba")
	assert isPalindrome("Abba")

def test_palindrome_int():
	assert isPalindrome(121)
	assert isPalindrome(1213)==False
