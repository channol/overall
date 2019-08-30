#!/usr/bin/python3
import os,sys,time

print('*******start capture and you can ctrl+c to stop wireshark!')
pcapf='capture'+time.strftime('%Y_%m_%d_%H_%M_%S')+'.pcap'
logf='smfsm'+time.strftime('%Y_%m_%d_%H_%M_%S')+'.log'
plogf='pfcp'+time.strftime('%Y_%m_%d_%H_%M_%S')+'.log'
os.system('tcpdump -i any -w /root/log/{}'.format(pcapf))
time.sleep(1)
print('******copy log file to /root/log/******')
os.chdir('/root/dcomp_test/')
os.popen('dcomp logs smfsm > /root/log/{}'.format(logf))
time.sleep(3)
os.popen('dcomp logs pfcp > /root/log/{}'.format(plogf))
time.sleep(3)
print('******bye!******')
print('\n')
#print('log file name is:',logf)
print('scp root@172.0.5.27:/root/log/{} .'.format(logf))
print('vim scp://root@172.0.5.27//root/log/{}'.format(logf))
print('scp root@172.0.5.27:/root/log/{} .'.format(plogf))
print('vim scp://root@172.0.5.27//root/log/{}'.format(plogf))
print('\n')
#print('pcap file name is:',pcapf)
print('scp root@172.0.5.27:/root/log/{} .'.format(pcapf))
print('\n')
