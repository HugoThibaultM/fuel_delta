"""
Módulo de visualización para mostrar datos en consola
"""

import os
import sys
from typing import Optional
from config import Config


class Display:
    """Clase para mostrar información en consola"""
    
    def __init__(self):
        self.config = Config()
        self.last_display = ""
        
    def clear_screen(self):
        """Limpia la pantalla"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_color_for_status(self, status: str) -> str:
        """Devuelve el color según el estado"""
        if status == "CRITICAL":
            return self.config.COLOR_RED
        elif status == "WARNING":
            return self.config.COLOR_YELLOW
        else:
            return self.config.COLOR_GREEN
    
    def format_balance(self, balance: float) -> str:
        """Formatea el balance con color"""
        if balance < -0.5:
            color = self.config.COLOR_RED
            symbol = "⚠ "
        elif balance < 0:
            color = self.config.COLOR_YELLOW
            symbol = "⚠ "
        else:
            color = self.config.COLOR_GREEN
            symbol = "✓ "
        
        sign = "+" if balance >= 0 else ""
        return f"{color}{symbol}{sign}{balance:.2f}L{self.config.COLOR_RESET}"
    
    def create_progress_bar(self, current: float, maximum: float, width: int = 30) -> str:
        """Crea una barra de progreso"""
        if maximum == 0:
            return "█" * width
        
        percentage = min(current / maximum, 1.0)
        filled = int(width * percentage)
        empty = width - filled
        
        # Color según nivel
        if percentage > 0.5:
            color = self.config.COLOR_GREEN
        elif percentage > 0.25:
            color = self.config.COLOR_YELLOW
        else:
            color = self.config.COLOR_RED
        
        bar = f"{color}{'█' * filled}{'░' * empty}{self.config.COLOR_RESET}"
        return f"[{bar}] {percentage*100:.1f}%"
    
    def update(self, telemetry, analysis):
        """Actualiza el display con nueva información"""
        
        # Crear el display
        display_text = self._create_display(telemetry, analysis)
        
        # Solo actualizar si ha cambiado
        if display_text != self.last_display:
            self.clear_screen()
            print(display_text)
            self.last_display = display_text
    
    def _create_display(self, telemetry, analysis) -> str:
        """Crea el texto del display"""
        
        lines = []
        
        # Título
        lines.append("")
        lines.append(f"{self.config.COLOR_BOLD}{self.config.COLOR_BLUE}")
        lines.append("╔════════════════════════════════════════════════════════════╗")
        lines.append("║        LE MANS ULTIMATE - MONITOR DE COMBUSTIBLE          ║")
        lines.append("╚════════════════════════════════════════════════════════════╝")
        lines.append(self.config.COLOR_RESET)
        lines.append("")
        
        # Información de la carrera
        lines.append(f"{self.config.COLOR_BOLD}INFORMACIÓN DE CARRERA:{self.config.COLOR_RESET}")
        lines.append(f"  Vuelta actual:  {telemetry.lap} / {telemetry.total_laps}")
        lines.append(f"  Vueltas restantes: {analysis.laps_remaining}")
        lines.append("")
        
        # Información de combustible
        lines.append(f"{self.config.COLOR_BOLD}COMBUSTIBLE:{self.config.COLOR_RESET}")
        fuel_bar = self.create_progress_bar(telemetry.fuel, telemetry.max_fuel)
        lines.append(f"  Actual: {telemetry.fuel:.2f}L / {telemetry.max_fuel:.2f}L")
        lines.append(f"  {fuel_bar}")
        lines.append("")
        
        # Consumo
        lines.append(f"{self.config.COLOR_BOLD}CONSUMO:{self.config.COLOR_RESET}")
        lines.append(f"  Promedio por vuelta: {analysis.avg_consumption:.3f}L")
        if hasattr(analysis, 'laps_possible') and analysis.laps_possible > 0:
            lines.append(f"  Vueltas posibles: {analysis.laps_possible:.1f}")
        lines.append("")
        
        # Balance y estado
        status_color = self.get_color_for_status(analysis.status)
        lines.append(f"{self.config.COLOR_BOLD}ANÁLISIS:{self.config.COLOR_RESET}")
        lines.append(f"  Combustible necesario: {analysis.fuel_needed:.2f}L")
        lines.append(f"  Balance: {self.format_balance(analysis.fuel_balance)}")
        lines.append("")
        
        # Mensaje de estado
        lines.append(f"{self.config.COLOR_BOLD}ESTADO:{self.config.COLOR_RESET}")
        lines.append(f"  {status_color}{self.config.COLOR_BOLD}{analysis.message}{self.config.COLOR_RESET}")
        
        # Si hay que ahorrar, mostrar claramente
        if analysis.fuel_to_save_per_lap > 0:
            lines.append("")
            lines.append(f"{self.config.COLOR_RED}{self.config.COLOR_BOLD}")
            lines.append(f"  ► DEBES AHORRAR: {analysis.fuel_to_save_per_lap:.2f}L POR VUELTA ◄")
            lines.append(self.config.COLOR_RESET)
        
        lines.append("")
        lines.append(f"{self.config.COLOR_BLUE}{'─' * 60}{self.config.COLOR_RESET}")
        lines.append(f"Presiona Ctrl+C para salir")
        lines.append("")
        
        return "\n".join(lines)
    
    def show_error(self, message: str):
        """Muestra un mensaje de error"""
        print(f"\n{self.config.COLOR_RED}{self.config.COLOR_BOLD}ERROR:{self.config.COLOR_RESET} {message}\n")
    
    def show_info(self, message: str):
        """Muestra un mensaje informativo"""
        print(f"\n{self.config.COLOR_BLUE}ℹ {message}{self.config.COLOR_RESET}\n")