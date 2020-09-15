#!/usr/bin/env python
import configparser,os
import pathlib
'''
Written by Emir Karamehmetoglu
Returns version number stored in first line of __init__.py
'''
def version_number():
    dir=pathlib.Path().parent.absolute()
    #print(dir)
    filename='__init__.py'
    with open(os.path.join(dir, filename),'r') as f:
        out=f.readline()
    #print(out.split('=')[-1].strip())
    return out.split('=')[-1].strip()

if __name__=="__main__":
    version_number()
