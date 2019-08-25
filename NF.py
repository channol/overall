#!/usr/bin/python3
import sys,os,re,time,logging
import requests
import pexpect
import jsonpath

class NF():
    """
    Network function api
    method:get post delete
    NF: smf,upf,docker
    """
    def __init__(self,container):
        self.container = container
        self.smf_ip = smf_ip
        self.supi = supi
        self.pdu_id = pdu_id


    def get_ip(container):
        getip = os.popen("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' %s" %(container))
        ip = getip.read().replace('\n',"")
        return ip

    def smf_get_session(smf_ip,supi,pdu_id):
        if len(smf_ip) == 0:
            logging.error('check the smf ip')
            return False
        else:
            url = 'http://{}:80/mgmt/v1/session/{}/{}'.format(smf_ip,supi,pdu_id)
            headers = {"Accept": "application/json","Content-type": "application/json"}
            rsp = requests.get(url,headers=headers)
            logging.info(rsp.url)
            if rsp.status_code == 200:
                logging.debug(rsp.text)
                ue_ip_bak = jsonpath.jsonpath(rsp.json(),'$..ipaddr')
                pattern_ip = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
                ue_ip = pattern_ip.search(str(ue_ip_bak))
                logging.info('ue ip: '+str(ue_ip.group()))
                fsmstate = rsp.json()['fsmState']
                logging.info('fsmState: '+fsmstate)
                return ue_ip.group()
            else:
                logging.error('get smf ue session failure!')
                logging.error(rsp.text)
                return False

    def smf_del_session(smf_ip,supi,pdu_id):
        url = 'http://{}:80/mgmt/v1/session/{}/{}'.format(smf_ip,supi,pdu_id)
        headers = {"Accept": "application/json","Content-type": "application/json"}
        rsp = requests.delete(url,headers=headers)
        logging.info(rsp.url)
        if r.status_code == 200:
            logging.info('smf delete session successful!')
            logging.info(rsp.text)
            return True

        else:
            logging.error('smf delete session failure!')
            logging.error(rsp.text)
            return False

    def upf_connect():
        upf_login = "ssh test@172.0.5.38"
        child_upf = pexpect.spawn(upf_login)
        index_upf = child_upf.expect(['password: ',pexpect.EOF,pexpect.TIMEOUT])
        if index_upf != 0:
            logging.error('connect to upf failure!')
            child_upf.close()
            return False
        else:
            child_upf.sendline('testcasa')
            time.sleep(1)
            child_upf.expect('CASA-MOBILE>')
            time.sleep(1)
            child_upf.sendline('page-off')
            time.sleep(1)
            child_upf.expect('CASA-MOBILE>')
            time.sleep(1)
            return child_upf


    def upf_close(child_upf):
        if child_upf:
            child_upf.close()

    def upf_session_rule(child_upf,ue_ip,rule):
        #send cli to upf
        child_upf.buffer
        time.sleep(1)
        child_upf.sendline("show upf session ue-ip {} {}".format(ue_ip,rule))
        time.sleep(1)
        index_ue = child_upf.expect(['session not found','CASA-MOBILE>'])
        time.sleep(1)
        if index_ue == 0:
            logging.error('UPF can not find the session')
            return False
        else:
            logging.info(child_upf.before.decode(encoding='utf-8'))
            return True
