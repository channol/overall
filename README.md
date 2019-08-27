# overall概述
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
pip3 install -U pytest
```
## pytest allure插件安装
```
pip3 install allure-pytest
```  
## jdk 1.8+安装
- 下载jdk软件，jdk-8u161-linux-x64.tar.gz
- 复制到/opt，解压： `tar -zxvf jdk-8u161-linux-x64.tar.gz`  
- 创建软连接： `ln -snf /opt/jdk1.8.0_161 /opt/jdk`  
- 环境变量配置/etc/profile  
```
export JAVA_HOME=/opt/jdk
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib
export PATH=$PATH:$JAVA_HOME/bin
```
- 应用配置： `source /etc/profile`  
## Allure Commandline安装
- 解压: `unzip allure-commandline-2.12.1.zip`
- 直接调用（可优化）： `/root/allure-2.12.1/bin/allure'

# 效果图
![image](https://github.com/channol/overall/blob/master/log/TIM%E5%9B%BE%E7%89%8720190827100603.png)
