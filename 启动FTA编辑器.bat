@echo off
chcp 65001 >nul
title FTA/ETA Editor (中文版)
rem 切到本脚本所在目录（中文版目录）
cd /d "%~dp0"
rem 优先使用真实安装的 Python 3.11，避免命中应用商店占位符 python.exe 而无法启动
set "PY=python"
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    set "PY=%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
)
start "" "%PY%" src\FTA_Editor_UI.py
