@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

set SCRIPT_DIR=%~dp0
set WORK_DIR=%SCRIPT_DIR%..

echo ============================================
echo 热点新闻口述稿生成Agent - 独立版
echo ============================================

if "%1"=="" (
    echo 用法: standalone_run.bat ^<模式^> [参数]
    echo.
    echo 模式:
    echo   http [端口]  - 启动HTTP服务 (默认端口5000)
    echo   flow [输入]  - 单次运行 (默认"你好")
    echo   chat         - 交互式聊天
    echo.
    echo 示例:
    echo   standalone_run.bat http
    echo   standalone_run.bat http 8080
    echo   standalone_run.bat flow "请写一篇关于AI的热点口述稿"
    echo   standalone_run.bat chat
    exit /b 1
)

set MODE=%1
set PARAM=%2

if "%MODE%"=="http" (
    if "%PARAM%"=="" set PARAM=5000
    echo 启动HTTP服务，端口: %PARAM%
    cd /d %WORK_DIR%\src
    python standalone_main.py -m http -p %PARAM%
) else if "%MODE%"=="flow" (
    if "%PARAM%"=="" set PARAM=你好
    cd /d %WORK_DIR%\src
    python standalone_main.py -m flow -i "%PARAM%"
) else if "%MODE%"=="chat" (
    cd /d %WORK_DIR%\src
    python standalone_main.py -m chat
) else (
    echo 未知模式: %MODE%
    echo 支持的模式: http, flow, chat
    exit /b 1
)
