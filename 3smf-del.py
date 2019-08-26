#!/usr/bin/python3
import pytest
import time,sys,os,re,logging
from landslide import *
from config import *
from NF import *

def test_smf_del_session():
    NF.smf_del_session("172.24.14.11",get_parameter('supi'),get_parameter('pdu_id'))
