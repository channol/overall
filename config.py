#!/usr/bin/python3
import configparser

def get_parameter(parameter):
    config = configparser.ConfigParser()
    config.read('config.ini')
    parameter = config.get('global',parameter)
    return parameter

