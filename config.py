"""
Configuración para el monitor de combustible
Contiene offsets de memoria compartida y constantes
"""


class Config:
    """Configuración del sistema"""
    
    # Nombre de la memoria compartida (rFactor 2 / Le Mans Ultimate)
    SHARED_MEMORY_NAME = "$rFactor2SMMP_Telemetry$"
    
    # Tamaño de la memoria compartida
    SHARED_MEMORY_SIZE = 2048
    
    # Offsets en la memoria compartida (estos pueden variar según versión)
    # Estos son valores aproximados y pueden necesitar ajuste
    OFFSET_FUEL = 100  # Combustible actual
    OFFSET_MAX_FUEL = 104  # Capacidad máxima del tanque
    OFFSET_LAP = 200  # Vuelta actual
    OFFSET_TOTAL_LAPS = 204  # Total de vueltas
    OFFSET_SESSION_TIME = 300  # Tiempo de sesión
    OFFSET_LAST_LAP_TIME = 400  # Tiempo última vuelta
    
    # Configuración del display
    DISPLAY_UPDATE_RATE = 0.1  # Segundos entre actualizaciones
    
    # Margen de seguridad (litros extra para tener en cuenta)
    SAFETY_MARGIN = 0.5
    
    # Configuración de colores para terminal
    COLOR_GREEN = '\033[92m'
    COLOR_YELLOW = '\033[93m'
    COLOR_RED = '\033[91m'
    COLOR_BLUE = '\033[94m'
    COLOR_RESET = '\033[0m'
    COLOR_BOLD = '\033[1m'
    
    # Umbrales para alertas
    THRESHOLD_CRITICAL = 0.5  # Litros - crítico
    THRESHOLD_WARNING = 2.0   # Litros - advertencia