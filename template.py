# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:28:02 2021

@author: ritwi
"""

import os

dirs= [
       os.path.join("data","raw"),
       os.path.join("data","processed"),
       "notebooks",
       "saved_models",
       "src"
       ]




for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True) #to make all the mentioned directories and exist_ok = true checks if it is already created or not.If already created then it wont create.
    with open(os.path.join(dir_ , ".gitkeep"),"w") as f:
        pass





file_ =[
        "dvc.yaml",
        "params.yaml",
        ".gitignore",
        os.path.join("src","__init__.py"),
        ]

for file in file_:
    with open(file,"w") as f:
        pass