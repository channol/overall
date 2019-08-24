#!/usr/bin/python3
import sys,os,re,time,logging
import requests

class Landslide():
    """
    landslide RESTful api
    method:get post
    action: start,stop,continue,abort
    """
    def __init__(self,ls_user,ls_password,library,case_name):
        self.ls_user = ls_user
        self.ls_password = ls_password
        self.library = library
        self.name = case_name

    def get_ls_run(ls_user='qinglong',ls_password='casa123'):
        session = requests.session()
        session.auth = (ls_user,ls_password)
        url = "http://10.133.6.19:8080/api/runningTests"
        rsp = session.get(url)
        logging.info('the url: '+rsp.url)
        if rsp.status_code == 200:
            logging.info('response is '+str(rsp.status_code))
            #logging.info(rsp.text)
            return True
        else:
            logging.error('check the url!')
            logging.error('response is '+rsp.status_code)
            logging.info(rsp.text)
            return False

    def case_start(case_name,ls_user='qinglong',ls_password='casa123',library='10828'):
        session = requests.session()
        session.auth = (ls_user,ls_password)
        payload = { "library": library, "name": case_name}
        url = "http://10.133.6.19:8080/api/runningTests"
        rsp = session.post(url,json=payload)
        logging.info('the url: '+rsp.url)
        logging.info(rsp)
        if rsp.status_code == 404:
            logging.error('check the test case name!')
            logging.error(rsp.text)
            return False
        elif rsp.status_code == 400:
            reason = rsp.json()['reason']
            test_id_old = re.search('\d\d\d\d',reason,re.M).group()
            logging.warning('old test id is: '+test_id_old)
            time.sleep(1)
            url_abort = url+'/'+test_id_old+"?action=abort"
            rsp_abort = session.post(url_abort)
            time.sleep(3)
            logging.info(rsp_abort.url)
            logging.info(rsp.text)
            return False
        elif rsp.status_code == 201:
            logging.info(rsp.text)
            test_id = rsp.json()['id']
            logging.info('test id is : '+test_id)
            return test_id
        else:
            logging.error('check the url and session')
            logging.info(rsp.text)
            return False















