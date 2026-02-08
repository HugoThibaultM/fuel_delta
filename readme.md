# Le Mans Ultimate - Monitor de Combustible

Monitor en tiempo real del consumo de combustible para Le Mans Ultimate que te indica si llegarás al final de la carrera y cuánto necesitas ahorrar.

## 📋 Características

- **Monitorización en tiempo real** del combustible
- **Cálculo automático** del consumo promedio por vuelta
- **Balance de combustible**: te dice si sobra o falta combustible
- **Alertas visuales** con códigos de color
- **Indicación clara** de cuánto ahorrar por vuelta si no llegas

## 🚀 Instalación

1. Asegúrate de tener Python 3.8 o superior instalado
2. No requiere librerías externas (usa solo librerías estándar de Python)

## 📁 Estructura de archivos

```
fuel_monitor.py    # Programa principal
config.py          # Configuración y constantes
calculator.py      # Lógica de cálculo de combustible
display.py         # Visualización en consola
README.md          # Este archivo
```

## 💻 Uso

1. Inicia Le Mans Ultimate y entra en una carrera
2. Ejecuta el programa:
   ```bash
   python fuel_monitor.py
   ```
3. El monitor comenzará a mostrar información en tiempo real

## 📊 Interpretación de resultados

### Balance de combustible:
- **Verde (+X.XX L)**: Sobra combustible, puedes estar tranquilo
- **Amarillo (-X.XX L)**: Falta combustible, necesitas ahorrar
- **Rojo (-X.XX L)**: Situación crítica, debes ahorrar urgentemente

### Estados:
- **OK**: Llegarás sin problemas
- **WARNING**: Situación ajustada, controla el consumo
- **CRITICAL**: No llegarás si sigues consumiendo igual

### Ejemplo de salida:

Si el programa muestra:
```
Balance: ⚠ -0.3L
DEBES AHORRAR: 0.03L POR VUELTA
```

Significa que te faltan 0.3 litros para llegar al final, por lo que debes ahorrar 0.03L en cada una de las vueltas restantes.

## ⚙️ Configuración

Puedes ajustar parámetros en `config.py`:

- `SAFETY_MARGIN`: Margen de seguridad en litros (default: 0.5L)
- `THRESHOLD_WARNING`: Umbral de advertencia (default: 2.0L)
- `THRESHOLD_CRITICAL`: Umbral crítico (default: 0.5L)

## 🔧 Solución de problemas

### "No se pudo conectar con Le Mans Ultimate"
- Asegúrate de que el juego esté ejecutándose
- Verifica que estés en una sesión activa (no en menús)
- En algunos casos, puede ser necesario ejecutar el programa como administrador

### Los valores parecen incorrectos
- Los offsets de memoria pueden variar según la versión del juego
- Puede ser necesario ajustar los valores en `config.py` → `OFFSET_*`
- Espera a completar al menos 2-3 vueltas para obtener datos precisos

### El programa no muestra datos
- Verifica que estés en una carrera, no en clasificación o entrenamientos
- Asegúrate de haber completado al menos una vuelta

## 📝 Notas importantes

- El consumo promedio se calcula con las últimas 10 vueltas
- Se incluye un margen de seguridad de 0.5L por defecto
- Los cálculos son más precisos después de 3-4 vueltas
- El programa solo funciona mientras Le Mans Ultimate está ejecutándose

## 🎯 Consejos para ahorrar combustible

Si el programa indica que debes ahorrar:
- Reduce las aceleraciones bruscas
- Usa motor brake mapping más bajo
- Levanta antes del acelerador en curvas
- Mantén una conducción más suave
- Reduce el tiempo en lift & coast

## ⚠️ Limitaciones

- Requiere que Le Mans Ultimate esté usando memoria compartida
- Los offsets pueden cambiar con actualizaciones del juego
- No funciona con todas las versiones del juego (compatible con rFactor 2 engine)

## 📄 Licencia

Proyecto de código abierto para la comunidad de Le Mans Ultimate.

## 🤝 Contribuciones

Si encuentras problemas o tienes sugerencias, siéntete libre de mejorar el código.

---

**Disfruta de tus carreras y que nunca te quedes sin combustible! 🏁**