"""
Le Mans Ultimate - Monitor de Combustible
Monitoriza el consumo de combustible y calcula el balance para terminar la carrera
"""

import struct
import mmap
import time
from dataclasses import dataclass
from typing import Optional
from config import Config
from calculator import FuelCalculator
from display import Display


@dataclass
class TelemetryData:
    """Datos de telemetría del juego"""
    fuel: float = 0.0
    max_fuel: float = 0.0
    lap: int = 0
    total_laps: int = 0
    session_time: float = 0.0
    last_lap_time: float = 0.0


class LeMansUltimateConnector:
    """Conector para leer telemetría de Le Mans Ultimate mediante memoria compartida"""
    
    def __init__(self):
        self.shared_mem = None
        self.config = Config()
        
    def connect(self) -> bool:
        """Intenta conectar con la memoria compartida del juego"""
        try:
            # Le Mans Ultimate usa el mismo sistema que rFactor 2
            self.shared_mem = mmap.mmap(-1, self.config.SHARED_MEMORY_SIZE, 
                                       self.config.SHARED_MEMORY_NAME)
            return True
        except Exception as e:
            print(f"Error al conectar: {e}")
            return False
    
    def read_telemetry(self) -> Optional[TelemetryData]:
        """Lee los datos de telemetría actuales"""
        if not self.shared_mem:
            return None
        
        try:
            self.shared_mem.seek(0)
            data = TelemetryData()
            
            # Offsets para rFactor 2 / Le Mans Ultimate
            # Estos son aproximados y pueden necesitar ajuste
            self.shared_mem.seek(self.config.OFFSET_FUEL)
            data.fuel = struct.unpack('f', self.shared_mem.read(4))[0]
            
            self.shared_mem.seek(self.config.OFFSET_MAX_FUEL)
            data.max_fuel = struct.unpack('f', self.shared_mem.read(4))[0]
            
            self.shared_mem.seek(self.config.OFFSET_LAP)
            data.lap = struct.unpack('i', self.shared_mem.read(4))[0]
            
            self.shared_mem.seek(self.config.OFFSET_TOTAL_LAPS)
            data.total_laps = struct.unpack('i', self.shared_mem.read(4))[0]
            
            self.shared_mem.seek(self.config.OFFSET_SESSION_TIME)
            data.session_time = struct.unpack('d', self.shared_mem.read(8))[0]
            
            self.shared_mem.seek(self.config.OFFSET_LAST_LAP_TIME)
            data.last_lap_time = struct.unpack('f', self.shared_mem.read(4))[0]
            
            return data
        except Exception as e:
            print(f"Error leyendo telemetría: {e}")
            return None
    
    def disconnect(self):
        """Cierra la conexión"""
        if self.shared_mem:
            self.shared_mem.close()


class FuelMonitor:
    """Monitor principal del programa"""
    
    def __init__(self):
        self.connector = LeMansUltimateConnector()
        self.calculator = FuelCalculator()
        self.display = Display()
        self.running = False
        
    def start(self):
        """Inicia el monitor"""
        print("Iniciando Le Mans Ultimate Fuel Monitor...")
        
        if not self.connector.connect():
            print("No se pudo conectar con Le Mans Ultimate")
            print("Asegúrate de que el juego esté ejecutándose")
            return
        
        print("Conectado! Monitorizando combustible...")
        self.running = True
        self.run_loop()
    
    def run_loop(self):
        """Bucle principal del programa"""
        try:
            while self.running:
                telemetry = self.connector.read_telemetry()
                
                if telemetry and telemetry.lap > 0:
                    # Actualizar calculadora con datos actuales
                    self.calculator.update(
                        current_fuel=telemetry.fuel,
                        max_fuel=telemetry.max_fuel,
                        current_lap=telemetry.lap,
                        total_laps=telemetry.total_laps,
                        last_lap_time=telemetry.last_lap_time
                    )
                    
                    # Obtener análisis
                    analysis = self.calculator.get_analysis()
                    
                    # Mostrar información
                    self.display.update(telemetry, analysis)
                
                time.sleep(0.1)  # Actualizar 10 veces por segundo
                
        except KeyboardInterrupt:
            print("\nDeteniendo monitor...")
        finally:
            self.stop()
    
    def stop(self):
        """Detiene el monitor"""
        self.running = False
        self.connector.disconnect()
        print("Monitor detenido")


if __name__ == "__main__":
    monitor = FuelMonitor()
    monitor.start()