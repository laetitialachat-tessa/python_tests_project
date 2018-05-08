# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:21:04 2018

@author: laetitialachat
"""
class Student:
	name = 'Marie'
	check = True

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = Student
        assert hasattr(x, 'check')