#!/usr/bin/python3
import configparser
import sys,os,re,time,logging

###########################################
strftime = time.strftime('%Y_%m_%d_%H_%M_%S')
os.makedirs('/root/log/result{}'.format(strftime))
cap_file = '/root/log/result'+strftime+'/capture'+strftime+'.pcap'
smfsm_file = '/root/log/result'+strftime+'/smfsm'+strftime+'.log'
pfcp_file = '/root/log/result'+strftime+'/pfcp'+strftime+'.log'
###########################################
def get_parameter(parameter):
    config = configparser.ConfigParser()
    config.read('config.ini')
    parameter = config.get('global',parameter)
    return parameter

def capture_start():
    logging.info('===start to capture===')
    os.system("nohup tcpdump -i any -f 'net 172.24.14.0/24' -w %s &" %(cap_file))

def capture_stop():
    logging.info('===stop to capture===')
    os.system("killall tcpdump")

def get_log():
    os.chdir('/root/test/')
    print(cap_file)
    os.popen('dcomp logs smfsm > {}'.format(smfsm_file))
    os.popen('dcomp logs pfcp > {}'.format(pfcp_file))
    if os.path.exists(smfsm_file):
        logging.info('scp root@172.0.5.27:'+smfsm_file+' .')
        logging.info('vim scp://root@172.0.5.27/'+smfsm_file)
    else:
        logging.warning('The sm log is not exist!')
    if os.path.exists(pfcp_file):
        logging.info('scp root@172.0.5.27:'+pfcp_file+' .')
        logging.info('vim scp://root@172.0.5.27/'+pfcp_file)
    else:
        logging.warning('The pfcp log is not exist!')
    if os.path.exists(cap_file):
        logging.info('scp root@172.0.5.27:'+cap_file+' .')
    else:
        logging.warning('The capture file is not exist!')
    os.chdir('/root/overall/')
