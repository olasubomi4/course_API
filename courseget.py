# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:13:01 2022

@author: olasubomi
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class course(BaseModel):
    coursename: str 
   