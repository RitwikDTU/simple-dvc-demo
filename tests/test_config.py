# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:21:24 2021

@author: ritwi
"""
import pytest
class NotInRange(Exception):
    def __init__(self,message="value not in range"):
        self.message=message
        super().__init__(self.message)




def test_generic():
    a=5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
            
            
def test_something():
    a=1
    b=1
    assert a==b