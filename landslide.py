#!/usr/bin/python3
import sys,os,re,time,logging
import requests

class Landslide():
    """
    landslide resful api
    method:get post
    action: start,stop,continue,abort
    """
    def __init__(self,ls_user,ls_password,library,case_name):
        self.ls_user = ls_user
        self.ls_password = ls_password
        self.library = library
        self.name = case_name

    def get_ls_run(ls_user,ls_password):
        session = requests.session()
        session.auth = (ls_user,ls_password)
        url = "http://10.133.6.19:8080/api/runningTest"
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