"""
Modo de prueba/simulación del monitor de combustible
Permite probar el programa sin tener Le Mans Ultimate ejecutándose
"""

import time
import random
from calculator import FuelCalculator
from display import Display


class FuelMonitorSimulation:
    """Simulación del monitor para pruebas"""
    
    def __init__(self):
        self.calculator = FuelCalculator()
        self.display = Display()
        
        # Configuración de la simulación
        self.total_laps = 20
        self.current_lap = 0
        self.max_fuel = 80.0
        self.current_fuel = 75.0
        
        # Consumo base (se puede ajustar)
        self.base_consumption = 3.5  # litros por vuelta
        self.consumption_variance = 0.3  # varianza en el consumo
        
    def simulate_lap(self):
        """Simula completar una vuelta"""
        self.current_lap += 1
        
        # Simular consumo con algo de variación
        consumption = self.base_consumption + random.uniform(
            -self.consumption_variance, 
            self.consumption_variance
        )
        
        self.current_fuel = max(0, self.current_fuel - consumption)
        
        return consumption
    
    def run_simulation(self):
        """Ejecuta la simulación completa"""
        print("=== MODO SIMULACIÓN ===")
        print(f"Carrera de {self.total_laps} vueltas")
        print(f"Combustible inicial: {self.current_fuel:.2f}L / {self.max_fuel:.2f}L")
        print(f"Consumo base simulado: ~{self.base_consumption:.2f}L por vuelta")
        print("\nIniciando simulación...\n")
        time.sleep(2)
        
        try:
            while self.current_lap < self.total_laps and self.current_fuel > 0:
                # Simular vuelta
                consumption = self.simulate_lap()
                
                # Actualizar calculadora
                self.calculator.update(
                    current_fuel=self.current_fuel,
                    max_fuel=self.max_fuel,
                    current_lap=self.current_lap,
                    total_laps=self.total_laps,
                    last_lap_time=90.0  # Tiempo de vuelta simulado
                )
                
                # Obtener análisis
                analysis = self.calculator.get_analysis()
                
                # Crear objeto telemetría simulada
                class SimTelemetry:
                    def __init__(self, fuel, max_fuel, lap, total_laps):
                        self.fuel = fuel
                        self.max_fuel = max_fuel
                        self.lap = lap
                        self.total_laps = total_laps
                        self.session_time = 0
                        self.last_lap_time = 90.0
                
                telemetry = SimTelemetry(
                    self.current_fuel,
                    self.max_fuel,
                    self.current_lap,
                    self.total_laps
                )
                
                # Mostrar display
                self.display.update(telemetry, analysis)
                
                # Pausa entre vueltas
                time.sleep(2)  # 2 segundos por vuelta en simulación
                
                # Simular repostaje si se queda sin combustible
                if self.current_fuel < 5.0 and self.current_lap < self.total_laps:
                    print("\n⛽ SIMULANDO REPOSTAJE...")
                    time.sleep(1)
                    self.current_fuel = self.max_fuel
            
            # Resultado final
            self.display.clear_screen()
            if self.current_lap >= self.total_laps:
                print(f"\n{self.display.config.COLOR_GREEN}{self.display.config.COLOR_BOLD}")
                print("🏁 ¡CARRERA COMPLETADA!")
                print(f"Combustible restante: {self.current_fuel:.2f}L")
                print(self.display.config.COLOR_RESET)
            else:
                print(f"\n{self.display.config.COLOR_RED}{self.display.config.COLOR_BOLD}")
                print("⚠️  TE QUEDASTE SIN COMBUSTIBLE")
                print(f"Vuelta {self.current_lap} de {self.total_laps}")
                print(self.display.config.COLOR_RESET)
            
        except KeyboardInterrupt:
            print("\n\nSimulación detenida por el usuario")


def run_test_scenarios():
    """Ejecuta varios escenarios de prueba"""
    
    print("╔════════════════════════════════════════════════════════════╗")
    print("║           ESCENARIOS DE PRUEBA DISPONIBLES                ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    print("1. Escenario OK - Suficiente combustible")
    print("2. Escenario WARNING - Ajustado")
    print("3. Escenario CRITICAL - Necesitas ahorrar")
    print("4. Escenario SIN COMBUSTIBLE - No llegas\n")
    
    choice = input("Selecciona un escenario (1-4) o Enter para escenario aleatorio: ")
    
    sim = FuelMonitorSimulation()
    
    if choice == "1":
        # Escenario OK
        sim.current_fuel = 75.0
        sim.base_consumption = 3.0
        sim.total_laps = 20
    elif choice == "2":
        # Escenario WARNING
        sim.current_fuel = 65.0
        sim.base_consumption = 3.2
        sim.total_laps = 20
    elif choice == "3":
        # Escenario CRITICAL
        sim.current_fuel = 58.0
        sim.base_consumption = 3.5
        sim.total_laps = 20
    elif choice == "4":
        # Escenario sin combustible
        sim.current_fuel = 45.0
        sim.base_consumption = 3.8
        sim.total_laps = 20
    else:
        # Aleatorio
        sim.current_fuel = random.uniform(50, 80)
        sim.base_consumption = random.uniform(2.5, 4.0)
        sim.total_laps = random.randint(15, 30)
    
    sim.run_simulation()


if __name__ == "__main__":
    run_test_scenarios()