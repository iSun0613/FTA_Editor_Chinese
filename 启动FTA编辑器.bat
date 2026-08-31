@echo off
chcp 65001 >nul
title FTA/ETA Editor (中文版)
rem 切到本脚本所在目录（中文版目录）
cd /d "%~dp0"
rem 优先使用 PATH 中的 python，避免硬编码特定版本路径
set "PY=python"
where python >nul 2>nul
if errorlevel 1 (
    echo 未在 PATH 中找到 python，请先安装 Python 3.10 或更高版本并加入 PATH。
    pause
    exit /b 1
)
start "" "%PY%" src\FTA_Editor_UI.py
