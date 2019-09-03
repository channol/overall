#!/usr/bin/python3
import pytest
import time,sys,os,re,logging
from landslide import *
from config import *
from NF import *

#a = time.time()
times = 5

def test_003_start():
    capture_start()

#def test_003_get_ls_run():
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
def ue_ip(get_test_id,smf_ip,times):
    if get_test_id and smf_ip:
        for i in range(times):
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
def test_003_landslide_case_start(get_test_id):
    assert get_test_id, "landslide is running a case!"

def test_003_smf_ip(smf_ip):
    assert smf_ip, "can not get smf ip!"

def test_003_ue_ip(ue_ip):
    assert ue_ip, "can not get ue ip!"

def test_003_upf_session_rule(child_upf,ue_ip):
    if ue_ip:
        rules = ['far','qer','pdr','urr']
        for rule in rules:
            NF.upf_session_rule(child_upf,ue_ip,rule)
    NF.upf_close(child_upf)

def test_003_landslide_case_measurements_1(get_test_id):
    if get_test_id:
        logging.info('post measurements of landslide case')
        ls = Landslide.case_measurements(get_test_id)
    else:
        return False

def test_003_smf_del_session(smf_ip):
    NF.smf_del_session(smf_ip,get_parameter('supi'),get_parameter('pdu_id'))

def test_003_landslide_case_continue(get_test_id,times):
    if get_test_id:
        for i in range(times):
            logging.info('try continue landslide case times: '+str(i))
            ls = Landslide.case_state(get_test_id)
            if ls == '5_Waiting':
                ls = Landslide.case_continue(get_test_id)
                if ls:
                    break
                time.sleep(10)
            else:
                time.sleep(10)
    else:
        return False

def test_003_landslide_case_measurements_2(get_test_id,times):
    if get_test_id:
        for i in range(times):
            logging.info('post measurements of landslide case times: '+str(i))
            ls = Landslide.case_state(get_test_id)
            if ls == 'COMPLETE' or ls == 'COMPLETE_ERROR':
                ls = Landslide.case_measurements(get_test_id)
                if ls:
                    break
                time.sleep(10)
            else:
                time.sleep(10)
    else:
        return False

def test_003_landslide_case_delete(get_test_id,times):
    if get_test_id:
        for i in range(times):
            logging.info('try delete landslide case times: '+str(i))
            ls = Landslide.case_state(get_test_id)
            if ls == 'COMPLETE' or ls == 'COMPLETE_ERROR':
                ls = Landslide.case_delete(get_test_id)
                if ls:
                    break
                time.sleep(10)
            else:
                time.sleep(10)
    else:
        return False
#############################################################
def test_003_stop():
    capture_stop()
    get_log()
    time.sleep(3)
#logging.info('spend time: '+str(time.time()-a))
