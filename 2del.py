#!/usr/bin/python3
import pytest
import time,sys,os,re,logging
from landslide import *
from config import *
from NF import *

def test_landslide_case_delete():
    #ids = [293,295,291]
    for idl in range(340,360):
        Landslide.case_delete(str(idl))

