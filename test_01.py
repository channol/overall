#!/usr/bin/python3
import pytest
import time
from landslide import *
from config import *

def test_get_ls_run():
    step1 = Landslide.get_ls_run(get_parameter('ls_user'),get_parameter('ls_password'))
    assert step1 != False

def test_capture_start():
    capture_start()
    time.sleep(5)

def test_case_start():
    test_id = Landslide.case_start(get_parameter('case_001'))
    assert test_id

def test_capture_stop():
    capture_stop()

def test_get_log():
    get_log()

