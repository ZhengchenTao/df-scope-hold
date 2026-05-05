@echo off
REM 设置便携式Python路径和脚本路径
set PYTHON_PATH="%~dp0PortablePython\python.exe"
set SCRIPT_PATH="%~dp0script.py"

REM 动态传递所有参数给Python脚本
%PYTHON_PATH% %SCRIPT_PATH%