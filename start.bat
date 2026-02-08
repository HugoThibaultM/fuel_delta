@echo off
REM Script de inicio para Le Mans Ultimate Fuel Monitor (Windows)

echo ========================================
echo Le Mans Ultimate - Monitor de Combustible
echo ========================================
echo.

REM Verificar que Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Por favor instala Python 3.8 o superior desde https://www.python.org
    pause
    exit /b 1
)

echo Python encontrado. Verificando version...
python --version

echo.
echo Opciones:
echo 1. Iniciar monitor (requiere Le Mans Ultimate ejecutandose)
echo 2. Ejecutar simulacion de prueba
echo.

set /p choice="Selecciona una opcion (1 o 2): "

if "%choice%"=="1" (
    echo.
    echo Iniciando monitor de combustible...
    echo Asegurate de que Le Mans Ultimate este ejecutandose!
    echo.
    timeout /t 2 /nobreak >nul
    python fuel_monitor.py
) else if "%choice%"=="2" (
    echo.
    echo Iniciando simulacion...
    echo.
    timeout /t 1 /nobreak >nul
    python test_simulation.py
) else (
    echo Opcion no valida
)

echo.
pause