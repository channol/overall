#!/usr/bin/python3
import pytest
from landslide import *
from config import get_parameter

def test_get_ls_run():
    step1 = Landslide.get_ls_run(get_parameter('ls_user'),get_parameter('ls_password'))
    assert step1 != False


