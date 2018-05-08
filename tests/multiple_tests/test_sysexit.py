# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:08:44 2018

@author: laetitialachat
"""

import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        #pytest.raises(theExceptedException) --> sucessful if the right exception was produced
        f()