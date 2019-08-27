# overall 
学习使用pytest+allure自动化框架来测试5GC

# 文件说明   
## config.ini
- config.ini 测试参数配置文件
- config.py 定义获取文件参数的函数

## landslide.py
定义关于landslide RESTful API相关类及函数

## pytest.ini
配置pytest运行参数文件，配置log相关参数

## NF.py
定义关于Network function 网元相关函数，包括smf，upf，docker等

## allure-report.sh
根据report文件内容生成allure web report脚本

# 部署步骤
## 软件基础
- python3.6
- pytest 5.1.1
- Allure Commandline 2.12.1
- jdk 1.8 "1.8.0_161"

```
root@ubuntu18:~/overall# pytest --version
This is pytest version 5.1.1, imported from /usr/local/lib/python3.6/dist-packages/pytest.py
setuptools registered plugins:
allure-pytest-2.8.0 at /usr/local/lib/python3.6/dist-packages/allure_pytest/plugin.py
root@ubuntu18:~/overall# java -version
java version "1.8.0_161"
Java(TM) SE Runtime Environment (build 1.8.0_161-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.161-b12, mixed mode)
```
## pytest 安装
```
pip3 install pytest
```

