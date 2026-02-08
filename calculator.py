"""
Módulo de cálculo para análisis de combustible
"""

from dataclasses import dataclass
from typing import List, Optional
from config import Config


@dataclass
class FuelAnalysis:
    """Resultado del análisis de combustible"""
    avg_consumption: float = 0.0  # Consumo promedio por vuelta
    fuel_needed: float = 0.0  # Combustible necesario para terminar
    fuel_balance: float = 0.0  # Balance (positivo=sobra, negativo=falta)
    laps_remaining: int = 0  # Vueltas restantes
    laps_possible: float = 0.0  # Vueltas posibles con combustible actual
    fuel_to_save_per_lap: float = 0.0  # Combustible a ahorrar por vuelta
    status: str = "OK"  # Estado: OK, WARNING, CRITICAL
    message: str = ""  # Mensaje descriptivo


class FuelCalculator:
    """Calculadora de consumo de combustible"""
    
    def __init__(self):
        self.config = Config()
        self.consumption_history: List[float] = []
        self.fuel_history: List[float] = []
        self.last_fuel: Optional[float] = None
        self.last_lap: int = 0
        
        # Datos actuales
        self.current_fuel = 0.0
        self.max_fuel = 0.0
        self.current_lap = 0
        self.total_laps = 0
        
    def update(self, current_fuel: float, max_fuel: float, 
               current_lap: int, total_laps: int, last_lap_time: float):
        """Actualiza los datos y calcula consumo"""
        
        # Detectar nueva vuelta
        if current_lap > self.last_lap and self.last_fuel is not None:
            consumption = self.last_fuel - current_fuel
            if consumption > 0:  # Solo registrar consumos válidos
                self.consumption_history.append(consumption)
                # Mantener solo últimas 10 vueltas para promedio
                if len(self.consumption_history) > 10:
                    self.consumption_history.pop(0)
        
        # Actualizar datos
        self.current_fuel = current_fuel
        self.max_fuel = max_fuel
        self.current_lap = current_lap
        self.total_laps = total_laps
        self.last_fuel = current_fuel
        self.last_lap = current_lap
        
        # Guardar histórico de combustible
        self.fuel_history.append(current_fuel)
        if len(self.fuel_history) > 100:
            self.fuel_history.pop(0)
    
    def get_average_consumption(self) -> float:
        """Calcula el consumo promedio por vuelta"""
        if not self.consumption_history:
            return 0.0
        return sum(self.consumption_history) / len(self.consumption_history)
    
    def get_analysis(self) -> FuelAnalysis:
        """Realiza el análisis completo de combustible"""
        analysis = FuelAnalysis()
        
        # Calcular consumo promedio
        analysis.avg_consumption = self.get_average_consumption()
        
        if analysis.avg_consumption == 0 or self.total_laps == 0:
            analysis.message = "Esperando datos de consumo..."
            return analysis
        
        # Vueltas restantes
        analysis.laps_remaining = self.total_laps - self.current_lap
        
        if analysis.laps_remaining <= 0:
            analysis.message = "Carrera completada"
            return analysis
        
        # Combustible necesario para terminar
        analysis.fuel_needed = (analysis.avg_consumption * analysis.laps_remaining) + \
                              self.config.SAFETY_MARGIN
        
        # Balance de combustible
        analysis.fuel_balance = self.current_fuel - analysis.fuel_needed
        
        # Vueltas posibles con combustible actual
        if analysis.avg_consumption > 0:
            analysis.laps_possible = self.current_fuel / analysis.avg_consumption
        
        # Determinar estado y mensaje
        if analysis.fuel_balance < -self.config.THRESHOLD_CRITICAL:
            analysis.status = "CRITICAL"
            # Calcular cuánto debe ahorrar por vuelta
            deficit = abs(analysis.fuel_balance)
            analysis.fuel_to_save_per_lap = deficit / analysis.laps_remaining
            analysis.message = f"CRÍTICO: Debes ahorrar {analysis.fuel_to_save_per_lap:.2f}L por vuelta"
            
        elif analysis.fuel_balance < 0:
            analysis.status = "WARNING"
            deficit = abs(analysis.fuel_balance)
            analysis.fuel_to_save_per_lap = deficit / analysis.laps_remaining
            analysis.message = f"ADVERTENCIA: Debes ahorrar {analysis.fuel_to_save_per_lap:.2f}L por vuelta"
            
        elif analysis.fuel_balance < self.config.THRESHOLD_WARNING:
            analysis.status = "WARNING"
            analysis.message = f"Justo: Sobran {analysis.fuel_balance:.2f}L"
            
        else:
            analysis.status = "OK"
            analysis.message = f"OK: Sobran {analysis.fuel_balance:.2f}L"
        
        return analysis
    
    def get_consumption_trend(self) -> str:
        """Analiza la tendencia del consumo"""
        if len(self.consumption_history) < 3:
            return "Insuficientes datos"
        
        # Comparar últimas 3 vueltas con promedio general
        recent = sum(self.consumption_history[-3:]) / 3
        overall = self.get_average_consumption()
        
        diff = recent - overall
        
        if abs(diff) < 0.1:
            return "Estable"
        elif diff > 0:
            return f"Aumentando (+{diff:.2f}L)"
        else:
            return f"Disminuyendo ({diff:.2f}L)"