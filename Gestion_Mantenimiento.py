"""
Mi proyecto consiste en el desarrollo de un software de gestion de mantenimiento
como parte de una materia que estoy cursando en mi carrera. Actualmente, mi universidad
no cuenta con este tipo de herramienta, ya que suelen ser costosas y se consideran un 
gasto innecesario para una sola asignatura de corta duracion.

Sin embargo, quienes nos interesamos en la materia vemos necesario contar, al menos
con un ejemplo practico. Por ello, he creado una version inicial muy basica, que funciona
como borrador. Mi objetivo es seguir mejorandola hasta convertirla en una aplicacion mas profesional
y completa, capaz de ejecutarse de manera independiente y sin depender de la consola

Juan Esteban Jaramillo Gonzalez
"""

import os
import sys
import json
from datetime import datetime

# Forzar salida UTF-8 en consola Windows para evitar UnicodeEncodeError al imprimir emojis
if os.name == "nt":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        # Fallback: asegurar variable de entorno (toma efecto si se reinicia el intérprete)
        os.environ.setdefault("PYTHONIOENCODING", "utf-8")

# Estructuras de datos globales
equipos = []
ordenes_trabajo = []
tecnicos = []
historial_mantenimiento = []
planes_mantenimiento = []

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(os.getenv('APPDATA') or get_base_path(), "Gestion_Mantenimiento")
os.makedirs(DATA_DIR, exist_ok=True)

ARCHIVO_DATOS = os.path.join(DATA_DIR, "datos_mantenimiento.json")

# ==================== PERSISTENCIA DE DATOS ====================

def guardar_datos():
    """Guarda todos los datos en un archivo JSON"""
    datos = {
        "equipos": equipos,
        "ordenes_trabajo": ordenes_trabajo,
        "tecnicos": tecnicos,
        "historial_mantenimiento": historial_mantenimiento,
        "planes_mantenimiento": planes_mantenimiento
    }
    
    try:
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar datos: {e}")
        return False

def cargar_datos():
    """Carga todos los datos desde el archivo JSON"""
    global equipos, ordenes_trabajo, tecnicos, historial_mantenimiento, planes_mantenimiento
    
    if not os.path.exists(ARCHIVO_DATOS):
        print("No se encontró archivo de datos. Se iniciará con datos vacíos.")
        return False
    
    try:
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            
        equipos = datos.get("equipos", [])
        ordenes_trabajo = datos.get("ordenes_trabajo", [])
        tecnicos = datos.get("tecnicos", [])
        historial_mantenimiento = datos.get("historial_mantenimiento", [])
        planes_mantenimiento = datos.get("planes_mantenimiento", [])
        
        print("Datos cargados correctamente.")
        return True
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return False

# ==================== FUNCIONES DE GESTIÓN ====================

def menu_principal():
    print("\n" + "="*60)
    print("   SISTEMA DE GESTIÓN DE MANTENIMIENTO - VERSIÓN 2.0")
    print("="*60)
    print("📦 EQUIPOS")
    print("  1. Registrar equipo")
    print("  2. Listar equipos")
    print("  3. Buscar equipo")
    print("  4. Editar equipo")
    print("  5. Eliminar equipo")
    print("\n🔧 ÓRDENAS DE TRABAJO")
    print("  6. Crear orden de trabajo")
    print("  7. Ver órdenes de trabajo")
    print("  8. Actualizar estado de orden")
    print("  9. Asignar técnico a orden")
    print("  10. Completar orden de trabajo")
    print("\n👷 TÉCNICOS")
    print("  11. Registrar técnico")
    print("  12. Listar técnicos")
    print("\n📅 PLANIFICACIÓN")
    print("  13. Crear plan de mantenimiento")
    print("  14. Ver planes de mantenimiento")
    print("  15. Ver carga de trabajo mensual")
    print("\n📊 REPORTES")
    print("  16. Historial de mantenimiento")
    print("  17. Estadísticas generales")
    print("  18. Órdenes por estado")
    print("\n💾 DATOS")
    print("  19. Guardar datos")
    print("  20. Cargar datos")
    print("\n  0. Salir")
    print("="*60)

def registrar_equipo():
    print("\n--- REGISTRAR EQUIPO ---")
    nombre = input("Nombre del equipo: ").strip()
    if not nombre:
        print("⚠ El nombre no puede estar vacío.")
        return

    ubicacion = input("Ubicación: ").strip()
    descripcion = input("Descripción: ").strip()
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    numero_serie = input("Número de serie: ").strip()

    while True:
        prioridad = input("Prioridad (Alta/Media/Baja): ").strip().capitalize()
        if prioridad in ["Alta", "Media", "Baja"]:
            break
        print("⚠ Prioridad inválida. Use: Alta, Media o Baja")

    equipo = {
        "id": len(equipos) + 1,
        "nombre": nombre,
        "ubicacion": ubicacion,
        "descripcion": descripcion,
        "marca": marca,
        "modelo": modelo,
        "numero_serie": numero_serie,
        "prioridad": prioridad,
        "estado": "Operativo",
        "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    equipos.append(equipo)
    print(f"✔ Equipo '{nombre}' registrado correctamente con ID: {equipo['id']}")
    guardar_datos()

def listar_equipos():
    print("\n--- LISTA DE EQUIPOS ---")
    if len(equipos) == 0:
        print("No hay equipos registrados.")
        return
    
    print(f"{'ID':<5} {'Nombre':<20} {'Ubicación':<15} {'Estado':<12} {'Prioridad':<10}")
    print("-" * 70)
    for eq in equipos:
        print(f"{eq['id']:<5} {eq['nombre']:<20} {eq['ubicacion']:<15} {eq['estado']:<12} {eq['prioridad']:<10}")

def buscar_equipo():
    print("\n--- BUSCAR EQUIPO ---")
    termino = input("Ingrese nombre o ubicación del equipo: ").strip().lower()

    resultados = [eq for eq in equipos if termino in eq['nombre'].lower() or termino in eq['ubicacion'].lower()]

    if len(resultados) == 0:
        print("⚠ No se encontraron equipos con ese criterio.")
        return
    
    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    for eq in resultados:
        print(f"\nID: {eq['id']}")
        print(f"Nombre: {eq['nombre']}")
        print(f"Ubicación: {eq['ubicacion']}")
        print(f"Marca: {eq['marca']} - Modelo: {eq['modelo']}")
        print(f"Estado: {eq['estado']} | Prioridad: {eq['prioridad']}")

def editar_equipo():
    print("\n--- EDITAR EQUIPO ---")
    if len(equipos) == 0:
        print("⚠ No hay equipos registrados.")
        return
    
    listar_equipos()
    try:
        id_eq = int(input("\nSeleccione ID del equipo a editar: "))
        equipo = next((e for e in equipos if e["id"] == id_eq), None)

        if not equipo:
            print("⚠ Equipo no encontrado.")
            return

        print(f"\nEditando equipo: {equipo['nombre']}")
        print("(Deje en blanco para mantener el valor actual)")

        nombre = input(f"Nombre [{equipo['nombre']}]: ").strip()
        ubicacion = input(f"Ubicación [{equipo['ubicacion']}]: ").strip()
        estado = input(f"Estado [{equipo['estado']}]: ").strip()
        
        if nombre:
            equipo['nombre'] = nombre
        if ubicacion:
            equipo['ubicacion'] = ubicacion
        if estado:
            equipo['estado'] = estado

        print("✔ Equipo actualizado correctamente.")
        guardar_datos()
    except ValueError:
        print("⚠ ID inválido.")

def eliminar_equipo():
    print("\n--- ELIMINAR EQUIPO ---")
    if len(equipos) == 0:
        print("⚠ No hay equipos registrados.")
        return
    
    listar_equipos()
    try:
        id_eq = int(input("\nSeleccione ID del equipo a eliminar: "))
        equipo = next((e for e in equipos if e["id"] == id_eq), None)
        
        if not equipo:
            print("⚠ Equipo no encontrado.")
            return

        confirmacion = input(f"¿Está seguro de eliminar '{equipo['nombre']}'? (s/n): ").lower()
        if confirmacion == 's':
            equipos.remove(equipo)
            print("✔ Equipo eliminado correctamente.")
            guardar_datos()
        else:
            print("Operación cancelada.")
    except ValueError:
        print("⚠ ID inválido.")

def crear_ot():
    print("\n--- CREAR ORDEN DE TRABAJO ---")
    if len(equipos) == 0:
        print("⚠ Debes registrar equipos antes de crear órdenes.")
        return

    listar_equipos()
    try:
        id_eq = int(input("\nSeleccione ID del equipo: "))
        equipo = next((e for e in equipos if e["id"] == id_eq), None)
        
        if not equipo:
            print("⚠ Equipo no encontrado.")
            return
        
        descripcion = input("Descripción del trabajo a realizar: ").strip()
        if not descripcion:
            print("⚠ La descripción no puede estar vacía.")
            return
        
        while True:
            tipo = input("Tipo de mantenimiento (Preventivo/Correctivo/Predictivo): ").strip().capitalize()
            if tipo in ["Preventivo", "Correctivo", "Predictivo"]:
                break
            print("⚠ Tipo inválido.")
        
        while True:
            prioridad = input("Prioridad (Alta/Media/Baja): ").strip().capitalize()
            if prioridad in ["Alta", "Media", "Baja"]:
                break
            print("⚠ Prioridad inválida.")
        
        ot = {
            "id": len(ordenes_trabajo) + 1,
            "equipo_id": id_eq,
            "equipo_nombre": equipo['nombre'],
            "descripcion": descripcion,
            "tipo": tipo,
            "prioridad": prioridad,
            "estado": "Pendiente",
            "tecnico_asignado": None,
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "fecha_inicio": None,
            "fecha_finalizacion": None,
            "observaciones": ""
        }

        ordenes_trabajo.append(ot)
        print(f"✔ Orden de trabajo #{ot['id']} creada correctamente.")
        guardar_datos()
    except ValueError:
        print("⚠ ID inválido.")

def ver_ordenes():
    print("\n--- ÓRDENAS DE TRABAJO ---")
    if len(ordenes_trabajo) == 0:
        print("No hay órdenes registradas.")
        return

    print(f"{'ID':<5} {'Equipo':<20} {'Tipo':<12} {'Estado':<15} {'Prioridad':<10} {'Técnico':<15}")
    print("-" * 90)
    for o in ordenes_trabajo:
        tecnico = o['tecnico_asignado'] if o['tecnico_asignado'] else "Sin asignar"
        print(f"{o['id']:<5} {o['equipo_nombre']:<20} {o['tipo']:<12} {o['estado']:<15} {o['prioridad']:<10} {tecnico:<15}")

def actualizar_estado_orden():
    print("\n--- ACTUALIZAR ESTADO DE ORDEN ---")
    if len(ordenes_trabajo) == 0:
        print("⚠ No hay órdenes registradas.")
        return
    
    ver_ordenes()
    try:
        id_ot = int(input("\nSeleccione ID de la orden: "))
        orden = next((o for o in ordenes_trabajo if o["id"] == id_ot), None)
        
        if not orden:
            print("⚠ Orden no encontrada.")
            return
        
        print(f"\nEstado actual: {orden['estado']}")
        print("Estados disponibles: Pendiente, En Progreso, Pausada, Completada, Cancelada")
        nuevo_estado = input("Nuevo estado: ").strip().capitalize()
        
        if nuevo_estado in ["Pendiente", "En progreso", "Pausada", "Completada", "Cancelada"]:
            orden['estado'] = nuevo_estado
            
            if nuevo_estado == "En progreso" and not orden['fecha_inicio']:
                orden['fecha_inicio'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"✔ Estado actualizado a: {nuevo_estado}")
            guardar_datos()
        else:
            print("⚠ Estado inválido.")
    except ValueError:
        print("⚠ ID inválido.")
            
def registrar_tecnico():
    print("\n--- REGISTRAR TÉCNICO ---")
    nombre = input("Nombre completo del técnico: ").strip()
    if not nombre:
        print("⚠ El nombre no puede estar vacío.")
        return
    
    especialidad = input("Especialidad: ").strip()
    telefono = input("Teléfono: ").strip()
    
    tecnico = {
        "id": len(tecnicos) + 1,
        "nombre": nombre,
        "especialidad": especialidad,
        "telefono": telefono,
        "estado": "Disponible"
    }
    
    tecnicos.append(tecnico)
    print(f"✔ Técnico '{nombre}' registrado correctamente.")
    guardar_datos()

def listar_tecnicos():
    print("\n--- LISTA DE TÉCNICOS ---")
    if len(tecnicos) == 0:
        print("No hay técnicos registrados.")
        return
    
    print(f"{'ID':<5} {'Nombre':<25} {'Especialidad':<20} {'Estado':<12}")
    print("-" * 65)
    for t in tecnicos:
        print(f"{t['id']:<5} {t['nombre']:<25} {t['especialidad']:<20} {t['estado']:<12}")

def asignar_tecnico():
    print("\n--- ASIGNAR TÉCNICO A ORDEN ---")
    if len(ordenes_trabajo) == 0:
        print("⚠ No hay órdenes registradas.")
        return
    
    if len(tecnicos) == 0:
        print("⚠ No hay técnicos registrados.")
        return
    
    ver_ordenes()
    try:
        id_ot = int(input("\nSeleccione ID de la orden: "))
        orden = next((o for o in ordenes_trabajo if o["id"] == id_ot), None)
        
        if not orden:
            print("⚠ Orden no encontrada.")
            return
        
        listar_tecnicos()
        id_tec = int(input("\nSeleccione ID del técnico: "))
        tecnico = next((t for t in tecnicos if t["id"] == id_tec), None)
        
        if not tecnico:
            print("⚠ Técnico no encontrado.")
            return
        
        orden['tecnico_asignado'] = tecnico['nombre']
        tecnico['estado'] = "Ocupado"
        print(f"✔ Técnico {tecnico['nombre']} asignado a la orden #{orden['id']}")
        guardar_datos()
    except ValueError:
        print("⚠ ID inválido.")

def completar_orden():
    print("\n--- COMPLETAR ORDEN DE TRABAJO ---")
    if len(ordenes_trabajo) == 0:
        print("⚠ No hay órdenes registradas.")
        return
    
    ver_ordenes()
    try:
        id_ot = int(input("\nSeleccione ID de la orden a completar: "))
        orden = next((o for o in ordenes_trabajo if o["id"] == id_ot), None)
        
        if not orden:
            print("⚠ Orden no encontrada.")
            return
        
        if orden['estado'] == "Completada":
            print("⚠ Esta orden ya está completada.")
            return
        
        observaciones = input("Observaciones finales: ").strip()
        
        orden['estado'] = "Completada"
        orden['fecha_finalizacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        orden['observaciones'] = observaciones
        
        historial_mantenimiento.append({
            "orden_id": orden['id'],
            "equipo_nombre": orden['equipo_nombre'],
            "tipo": orden['tipo'],
            "fecha": orden['fecha_finalizacion'],
            "tecnico": orden['tecnico_asignado'],
            "observaciones": observaciones
        })
        
        if orden['tecnico_asignado']:
            for t in tecnicos:
                if t['nombre'] == orden['tecnico_asignado']:
                    t['estado'] = "Disponible"
                    break
        
        print(f"✔ Orden #{orden['id']} completada exitosamente.")
        guardar_datos()
    except ValueError:
        print("⚠ ID inválido.")

def crear_plan_mantenimiento():
    print("\n--- CREAR PLAN DE MANTENIMIENTO ---")
    if len(equipos) == 0:
        print("⚠ Debes registrar equipos antes de crear planes.")
        return
    
    listar_equipos()
    try:
        id_eq = int(input("\nSeleccione ID del equipo: "))
        equipo = next((e for e in equipos if e["id"] == id_eq), None)
        
        if not equipo:
            print("⚠ Equipo no encontrado.")
            return
        
        while True:
            tipo = input("Tipo (Preventivo/Correctivo/Predictivo): ").strip().capitalize()
            if tipo in ["Preventivo", "Correctivo", "Predictivo"]:
                break
            print("⚠ Tipo inválido.")
        
        descripcion = input("Descripción del plan: ").strip()
        mes = input("Mes programado (1-12): ").strip()
        anio = input("Año (YYYY): ").strip()
        
        plan = {
            "id": len(planes_mantenimiento) + 1,
            "equipo_id": id_eq,
            "equipo_nombre": equipo['nombre'],
            "tipo": tipo,
            "descripcion": descripcion,
            "mes": int(mes),
            "anio": int(anio),
            "estado": "Programado",
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        planes_mantenimiento.append(plan)
        print(f"✔ Plan de mantenimiento #{plan['id']} creado correctamente.")
        guardar_datos()
    except ValueError:
        print("⚠ Entrada inválida.")

def ver_planes():
    print("\n--- PLANES DE MANTENIMIENTO ---")
    if len(planes_mantenimiento) == 0:
        print("No hay planes registrados.")
        return
    
    print(f"{'ID':<5} {'Equipo':<20} {'Tipo':<15} {'Mes':<8} {'Año':<8} {'Estado':<12}")
    print("-" * 80)
    for p in planes_mantenimiento:
        print(f"{p['id']:<5} {p['equipo_nombre']:<20} {p['tipo']:<15} {p['mes']:<8} {p['anio']:<8} {p['estado']:<12}")

def ver_carga_mensual():
    print("\n--- CARGA DE TRABAJO MENSUAL ---")
    mes = int(input("Ingrese el mes (1-12): "))
    anio = int(input("Ingrese el año (YYYY): "))
    
    planes_mes = [p for p in planes_mantenimiento if p['mes'] == mes and p['anio'] == anio]
    
    if len(planes_mes) == 0:
        print(f"No hay planes programados para {mes}/{anio}")
        return
    
    print(f"\n--- PLANES PROGRAMADOS PARA {mes}/{anio} ---")
    print(f"{'ID':<5} {'Equipo':<20} {'Tipo':<15} {'Descripción':<30}")
    print("-" * 75)
    for p in planes_mes:
        print(f"{p['id']:<5} {p['equipo_nombre']:<20} {p['tipo']:<15} {p['descripcion']:<30}")

def ver_historial():
    print("\n--- HISTORIAL DE MANTENIMIENTO ---")
    if len(historial_mantenimiento) == 0:
        print("No hay registros en el historial.")
        return
    
    print(f"{'ID':<5} {'Equipo':<20} {'Tipo':<12} {'Fecha':<20} {'Técnico':<15}")
    print("-" * 80)
    for h in historial_mantenimiento:
        print(f"{h['orden_id']:<5} {h['equipo_nombre']:<20} {h['tipo']:<12} {h['fecha']:<20} {h['tecnico']:<15}")

def estadisticas_generales():
    print("\n--- ESTADÍSTICAS GENERALES ---")
    print(f"Total de equipos registrados: {len(equipos)}")
    print(f"Total de órdenes de trabajo: {len(ordenes_trabajo)}")
    print(f"Total de técnicos: {len(tecnicos)}")
    print(f"Mantenimientos completados: {len(historial_mantenimiento)}")
    print(f"Planes de mantenimiento: {len(planes_mantenimiento)}")
    
    if len(ordenes_trabajo) > 0:
        pendientes = sum(1 for o in ordenes_trabajo if o['estado'] == "Pendiente")
        en_progreso = sum(1 for o in ordenes_trabajo if o['estado'] == "En progreso")
        completadas = sum(1 for o in ordenes_trabajo if o['estado'] == "Completada")
        
        print(f"\nÓrdenes pendientes: {pendientes}")
        print(f"Órdenes en progreso: {en_progreso}")
        print(f"Órdenes completadas: {completadas}")

def ordenes_por_estado():
    print("\n--- FILTRAR ÓRDENES POR ESTADO ---")
    if len(ordenes_trabajo) == 0:
        print("⚠ No hay órdenes registradas.")
        return
    
    print("Estados: Pendiente, En progreso, Pausada, Completada, Cancelada")
    estado = input("Ingrese el estado a filtrar: ").strip().capitalize()
    
    filtradas = [o for o in ordenes_trabajo if o['estado'].lower() == estado.lower()]
    
    if len(filtradas) == 0:
        print(f"No hay órdenes con estado '{estado}'.")
        return
    
    print(f"\n--- ÓRDENES CON ESTADO: {estado.upper()} ---")
    print(f"{'ID':<5} {'Equipo':<20} {'Tipo':<12} {'Prioridad':<10} {'Técnico':<15}")
    print("-" * 70)
    for o in filtradas:
        tecnico = o['tecnico_asignado'] if o['tecnico_asignado'] else "Sin asignar"
        print(f"{o['id']:<5} {o['equipo_nombre']:<20} {o['tipo']:<12} {o['prioridad']:<10} {tecnico:<15}")

def main():
    # Cargar datos al iniciar
    cargar_datos()
    
    while True:
        menu_principal()
        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:
            case "1":
                registrar_equipo()
            case "2":
                listar_equipos()
            case "3":
                buscar_equipo()
            case "4":
                editar_equipo()
            case "5":
                eliminar_equipo()
            case "6":
                crear_ot()
            case "7":
                ver_ordenes()
            case "8":
                actualizar_estado_orden()
            case "9":
                asignar_tecnico()
            case "10":
                completar_orden()
            case "11":
                registrar_tecnico()
            case "12":
                listar_tecnicos()
            case "13":
                crear_plan_mantenimiento()
            case "14":
                ver_planes()
            case "15":
                ver_carga_mensual()
            case "16":
                ver_historial()
            case "17":
                estadisticas_generales()
            case "18":
                ordenes_por_estado()
            case "19":
                if guardar_datos():
                    print("✔ Datos guardados correctamente.")
                else:
                    print("⚠ Error al guardar datos.")
            case "20":
                if cargar_datos():
                    print("✔ Datos cargados correctamente.")
                else:
                    print("⚠ Error al cargar datos.")
            case "0":
                print("\n" + "="*60)
                print("   Gracias por usar el Sistema de Gestión de Mantenimiento")
                print("   ¡Hasta pronto! 👋")
                print("="*60 + "\n")
                # Guardar automáticamente al salir
                guardar_datos()
                break
            case _:
                print("⚠ Opción inválida. Por favor, seleccione una opción válida.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()