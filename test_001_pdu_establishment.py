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
@pytest.fixture(scope = 'module')
def get_test_id():
    test_id = Landslide.case_start(get_parameter('case_001'))
    return test_id

@pytest.fixture(scope = 'module')
def smf_ip():
    smf_ip = NF.get_ip(get_parameter('container_smfsm'))
    logging.info('smf ip: '+str(smf_ip))
    return smf_ip

@pytest.fixture(scope = 'module')
def child_upf():
    child_upf = NF.upf_connect()
    return child_upf

#@pytest.fixture
@pytest.fixture(scope = 'module')
def ue_ip(get_test_id,smf_ip):
    if get_test_id and smf_ip:
        for i in range(10):
            logging.info('try get ue ip times: '+str(i))
            ue_ip = NF.smf_get_session(smf_ip,get_parameter('supi'),get_parameter('pdu_id'))
            if ue_ip:
                break
            time.sleep(10)
        logging.info('ue ip: '+str(ue_ip))
        return ue_ip
    else:
        return False
#############################################################
def test_landslide_case_start(get_test_id):
    assert get_test_id, "landslide is running a case!"

def test_ue_ip(ue_ip):
    assert ue_ip, "can not get ue ip!"

def test_upf_session_rule(child_upf,ue_ip):
    if ue_ip:
        rules = ['far','qer','pdr','urr']
        for rule in rules:
            NF.upf_session_rule(child_upf,ue_ip,rule)
    NF.upf_close(child_upf)

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
