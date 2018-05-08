# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:31:05 2018

@author: laetitialachat
"""

import pytest

def isEven(number):
    if isinstance(number, str) and float(number)%2==0.0:
        return True
    elif isinstance(number, (int,float)) and float(number)%2==0.0:
        return True
    return False

def test_even_numerical():
	assert isEven(12)
	assert isEven(12.0)
	assert isEven(13) == False
	assert isEven(13.5) == False

"""def test_even_string():
	assert isEven("12")
	assert isEven("12.0")
	with pytest.raises(ValueError):
		isEven("abc")"""
