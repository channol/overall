#!/usr/bin/python3
import pytest
import time,sys,os,re,logging
from landslide import *
from config import *
from NF import *

a = time.time()

#def test_capture_start():
#    capture_start()

#def test_get_ls_run():
#    Landslide.get_ls_run()

#############################################################
#@pytest.fixture(scope = 'module')
def test_id():
    test_id = Landslide.case_start(get_parameter('case_001'))
    return test_id

#def test_landslide_case_continue(get_test_id):
#    Landslide.case_continue(get_test_id)

#time.sleep(30)
#def test_landslide_case_delete(get_test_id):
#    Landslide.case_delete(get_test_id)

#############################################################

#def test_capture_stop():
#    capture_stop()

#def test_get_log():
#    get_log()

logging.info('spend time: '+str(time.time()-a))
