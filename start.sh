#!/bin/bash
# Script de inicio para Le Mans Ultimate Fuel Monitor (Linux/Mac)

echo "========================================"
echo "Le Mans Ultimate - Monitor de Combustible"
echo "========================================"
echo ""

# Verificar que Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 no está instalado"
    echo "Por favor instala Python 3.8 o superior"
    exit 1
fi

echo "Python encontrado. Verificando versión..."
python3 --version

echo ""
echo "Opciones:"
echo "1. Iniciar monitor (requiere Le Mans Ultimate ejecutándose)"
echo "2. Ejecutar simulación de prueba"
echo ""

read -p "Selecciona una opción (1 o 2): " choice

if [ "$choice" = "1" ]; then
    echo ""
    echo "Iniciando monitor de combustible..."
    echo "¡Asegúrate de que Le Mans Ultimate esté ejecutándose!"
    echo ""
    sleep 2
    python3 fuel_monitor.py
elif [ "$choice" = "2" ]; then
    echo ""
    echo "Iniciando simulación..."
    echo ""
    sleep 1
    python3 test_simulation.py
else
    echo "Opción no válida"
fi

echo ""