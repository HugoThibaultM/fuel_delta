import mmap
import struct
import time
import ctypes

def escanear_memoria():
    print("--- ESCÁNER DE FRECUENCIA LMU ---")
    print("Manten SimHub abierto y las agujas moviéndose...")
    
    # Las 3 posibles "frecuencias" (nombres de memoria) que usa el juego
    posibles_mapas = [
        "$rFactor2Shared$",          # Estándar
        "$rFactor2Extended$",        # Plugin extendido
        "$rFactor2Shared$Scoring$"   # Datos de tiempos/vueltas
    ]

    mapas_activos = []

    # 1. Identificar qué mapas existen en Windows ahora mismo
    for nombre in posibles_mapas:
        try:
            shmem = mmap.mmap(-1, 16000, nombre, access=mmap.ACCESS_READ)
            mapas_activos.append((nombre, shmem))
            print(f"✅ SEÑAL ENCONTRADA en: {nombre}")
        except FileNotFoundError:
            print(f"❌ Sin señal en: {nombre}")

    if not mapas_activos:
        print("\n⚠️ CRÍTICO: Windows no encuentra la memoria. ¿SimHub se está ejecutando como Administrador y Python no?")
        return

    print("\n--- ANALIZANDO FLUJO DE DATOS ---")
    try:
        while True:
            salida = ""
            for nombre, shmem in mapas_activos:
                shmem.seek(0)
                # Leemos los primeros 64 bytes
                data = shmem.read(64)
                
                # Convertimos a hex para ver si cambian (si hay FF, 01, A3... hay vida)
                hex_str = data[:8].hex()
                
                # Intentamos leer el Combustible (Offset típico 84-88 en Standard)
                if "Shared$" in nombre and not "Scoring" in nombre:
                    shmem.seek(84) # Offset v1
                    fuel_bytes = shmem.read(8)
                    val_fuel = struct.unpack('d', fuel_bytes)[0]
                    salida += f"[{nombre}] Hex:{hex_str} | Fuel(est): {val_fuel:.2f}  ||  "
                else:
                    salida += f"[{nombre}] Hex:{hex_str}  ||  "

            print(f"\r{salida}", end="")
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nEscaneo finalizado.")

if __name__ == "__main__":
    escanear_memoria()
