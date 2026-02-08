"""
Configuración avanzada (OPCIONAL)
Solo edita este archivo si necesitas ajustar parámetros específicos
"""


class AdvancedConfig:
    """Configuración avanzada del sistema"""
    
    # ============================================================
    # OFFSETS DE MEMORIA COMPARTIDA
    # ============================================================
    # IMPORTANTE: Estos valores pueden necesitar ajuste según la versión
    # del juego. Si los valores mostrados son incorrectos, intenta
    # ajustar estos offsets.
    
    # Para encontrar los offsets correctos:
    # 1. Usa una herramienta como Cheat Engine
    # 2. Busca los valores de combustible mientras juegas
    # 3. Anota las direcciones de memoria
    # 4. Calcula el offset desde el inicio de la memoria compartida
    
    # Offsets alternativos para diferentes versiones (descomentar si es necesario)
    
    # Versión 1 (predeterminada - en config.py)
    # OFFSET_FUEL = 100
    # OFFSET_MAX_FUEL = 104
    # OFFSET_LAP = 200
    # OFFSET_TOTAL_LAPS = 204
    
    # Versión 2 (alternativa - descomenta si la versión 1 no funciona)
    # OFFSET_FUEL = 120
    # OFFSET_MAX_FUEL = 124
    # OFFSET_LAP = 220
    # OFFSET_TOTAL_LAPS = 224
    
    # Versión 3 (para builds más recientes)
    # OFFSET_FUEL = 150
    # OFFSET_MAX_FUEL = 154
    # OFFSET_LAP = 250
    # OFFSET_TOTAL_LAPS = 254
    
    # ============================================================
    # CONFIGURACIÓN DE CÁLCULOS
    # ============================================================
    
    # Número de vueltas a usar para calcular el promedio
    # Más vueltas = más estable pero menos reactivo
    # Menos vueltas = más reactivo pero menos estable
    LAPS_FOR_AVERAGE = 10
    
    # Multiplicador de consumo para ser más conservador
    # 1.0 = sin cambio
    # 1.05 = 5% más conservador (recomendado)
    # 1.10 = 10% más conservador
    CONSUMPTION_MULTIPLIER = 1.0
    
    # ============================================================
    # CONFIGURACIÓN DE ALERTAS
    # ============================================================
    
    # Activar sonido de alerta (requiere winsound en Windows o beep en Linux)
    ENABLE_SOUND_ALERTS = False
    
    # Activar alertas solo cuando el balance sea negativo
    ALERTS_ONLY_ON_DEFICIT = True
    
    # ============================================================
    # CONFIGURACIÓN DE REGISTRO (LOGGING)
    # ============================================================
    
    # Guardar log de cada sesión
    ENABLE_LOGGING = False
    
    # Ruta del archivo de log
    LOG_FILE_PATH = "fuel_monitor_log.txt"
    
    # Guardar CSV con histórico de vueltas
    SAVE_LAP_HISTORY_CSV = False
    
    # Ruta del CSV
    CSV_FILE_PATH = "lap_history.csv"
    
    # ============================================================
    # CONFIGURACIÓN DE INTERFAZ
    # ============================================================
    
    # Usar interfaz simplificada (menos información)
    SIMPLE_INTERFACE = False
    
    # Mostrar gráfico de tendencia de consumo (requiere matplotlib)
    SHOW_CONSUMPTION_GRAPH = False
    
    # Actualizar solo cuando cambia la vuelta (reduce uso de CPU)
    UPDATE_ONLY_ON_LAP_CHANGE = False
    
    # ============================================================
    # CONFIGURACIÓN DE DEBUG
    # ============================================================
    
    # Modo debug: muestra información técnica adicional
    DEBUG_MODE = False
    
    # Mostrar valores raw de memoria
    SHOW_RAW_MEMORY_VALUES = False
    
    # Guardar dumps de memoria para análisis
    SAVE_MEMORY_DUMPS = False


# ============================================================
# FUNCIONES DE UTILIDAD
# ============================================================

def apply_advanced_config():
    """
    Aplica la configuración avanzada al config principal
    Descomentar para usar
    """
    # from config import Config
    # config = Config()
    # config.SAFETY_MARGIN = 1.0  # Ejemplo
    pass


# Notas:
# - La mayoría de usuarios NO necesitan modificar este archivo
# - Solo cambia valores si sabes lo que estás haciendo
# - Guarda una copia de seguridad antes de hacer cambios
# - Si algo deja de funcionar, restaura los valores predeterminados