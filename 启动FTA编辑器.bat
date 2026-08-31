@echo off
title FTA/ETA Editor (中文版)
rem 切到本脚本所在目录（中文版目录）
cd /d "%~dp0"

rem ============================================================
rem 自动选择可用的 Python：必须带 tkinter（图形界面必需）。
rem 某些软件自带的精简版 Python 没有 tkinter，会启动即崩溃，
rem 因此每个候选都先做 tkinter 检查，通过才使用。
rem ============================================================
set "PYCMD="

rem 1) Python 启动器 py（自动指向系统安装的最新官方 Python）
py -c "import tkinter" >nul 2>nul
if not errorlevel 1 for /f "delims=" %%E in ('py -c "import sys;print(sys.executable)"') do set "PYCMD=%%E"

rem 2) PATH 中的 python（若为缺 tkinter 的精简版则自动跳过）
if not defined PYCMD (
    python -c "import tkinter" >nul 2>nul
    if not errorlevel 1 for /f "delims=" %%E in ('python -c "import sys;print(sys.executable)"') do set "PYCMD=%%E"
)

rem 3) 常见安装位置的系统 Python（3.13 / 3.12 / 3.11 / 3.10）
if not defined PYCMD for %%V in (313 312 311 310) do (
    if not defined PYCMD if exist "%LocalAppData%\Programs\Python\Python%%V%\python.exe" (
        "%LocalAppData%\Programs\Python\Python%%V%\python.exe" -c "import tkinter" >nul 2>nul
        if not errorlevel 1 set "PYCMD=%LocalAppData%\Programs\Python\Python%%V%\python.exe"
    )
    if not defined PYCMD if exist "%ProgramFiles%\Python%%V%\python.exe" (
        "%ProgramFiles%\Python%%V%\python.exe" -c "import tkinter" >nul 2>nul
        if not errorlevel 1 set "PYCMD=%ProgramFiles%\Python%%V%\python.exe"
    )
)

if not defined PYCMD (
    echo [错误] 未找到带图形界面（tkinter）的可用 Python。
    echo.
    echo 常见原因：PATH 里的 Python 是某些软件自带的精简版（缺 tkinter），
    echo 或系统尚未安装官方版 Python。
    echo 请从 https://www.python.org/downloads/ 安装 Python 3.10 或更高版本，
    echo 安装时务必勾选 "Add python.exe to PATH"。
    echo.
    pause
    exit /b 1
)

echo 已选择 Python: %PYCMD%

rem 首次运行时自动安装依赖（已安装则跳过，秒过）
%PYCMD% -c "import PIL, graphviz, openpyxl, openai" >nul 2>nul
if errorlevel 1 (
    echo 检测到缺少依赖，正在自动安装（requirements.txt，仅首次需要）...
    %PYCMD% -m pip install -r requirements.txt
    if errorlevel 1 (
        echo [错误] 依赖安装失败，请检查网络后重试，或手动执行：
        echo    %PYCMD% -m pip install -r requirements.txt
        pause
        exit /b 1
    )
)

rem 启动图形界面（黑窗最小化保活：程序若意外退出，错误信息会显示在黑窗中）
start "FTA Editor" /min cmd /k ""%PYCMD%" src\FTA_Editor_UI.py & echo. & echo [程序已退出] 若上方有 Traceback 即启动失败原因；正常使用时可直接关闭本窗口 & pause"
exit /b 0
