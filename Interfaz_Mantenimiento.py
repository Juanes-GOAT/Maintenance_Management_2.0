"""
Interfaz Gráfica para Sistema de Gestión de Mantenimiento
Archivo: Interfaz_Mantenimiento.py
Autor: Juan Esteban Jaramillo González

Este módulo proporciona una interfaz gráfica usando Tkinter para el sistema
de gestión de mantenimiento, integrándose con Gestion_Mantenimiento.py
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog, filedialog
from datetime import datetime
import sys
import os
from datetime import datetime

# ---------------- RUTAS Y RECURSOS (compatible con PyInstaller) ----------------
def get_base_path():
    """Devuelve la ruta base del proyecto o del ejecutable si está 'frozen'."""
    if getattr(sys, "frozen", False):
        # PyInstaller unpackea recursos en sys._MEIPASS
        return getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))

def resource_path(rel_path: str) -> str:
    """Construye la ruta absoluta para un recurso relativo al proyecto/exe."""
    return os.path.join(get_base_path(), rel_path)

# Directorio de datos (APPDATA en Windows) para almacenar JSON y exportaciones
DATA_DIR = os.path.join(os.getenv("APPDATA") or get_base_path(), "Gestion_Mantenimiento")
os.makedirs(DATA_DIR, exist_ok=True)

# Forzar año a mostrar (usa 2025 como mínimo)
DEFAULT_YEAR = 2025
YEAR_DISPLAY = max(datetime.now().year, DEFAULT_YEAR)

# Importar las estructuras de datos y funciones del módulo principal
try:
    import Gestion_Mantenimiento as gm
except ImportError:
    messagebox.showerror("Error", "No se pudo importar Gestion_Mantenimiento.py\nAsegúrate de que el archivo esté en la misma carpeta.")
    sys.exit(1)

class SistemaMantenimientoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Mantenimiento v2.0")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f8f9fa")
        
        # Paleta de colores moderna
        self.colors = {
            'primary': '#667eea',      # Púrpura moderno
            'secondary': '#764ba2',    # Púrpura oscuro
            'accent': '#f093fb',       # Rosa suave
            'success': '#4facfe',      # Azul cielo
            'warning': '#ffd93d',      # Amarillo vibrante
            'danger': '#ff6b6b',       # Rojo coral
            'dark': '#2d3748',         # Gris oscuro
            'light': '#f8f9fa',        # Blanco humo
            'card_bg': '#ffffff',      # Blanco puro
            'text': '#2d3748'          # Texto oscuro
        }
        
        # Configurar estilo
        self.configurar_estilos()
        
        # Crear interfaz principal
        self.crear_interfaz()
        
    def configurar_estilos(self):
        """Configura los estilos de la interfaz con diseño moderno"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilo para botones principales con gradiente visual
        style.configure('Main.TButton', 
                       font=('Segoe UI', 10, 'bold'),
                       padding=12,
                       background=self.colors['primary'],
                       foreground='white',
                       borderwidth=0,
                       relief='flat')
        style.map('Main.TButton',
                 background=[('active', self.colors['secondary'])],
                 foreground=[('active', 'white')])
        
        # Estilo para frames con bordes redondeados simulados
        style.configure('Card.TFrame',
                       background=self.colors['card_bg'],
                       relief='flat',
                       borderwidth=0)
        
        # Estilo para labels
        style.configure('Modern.TLabel',
                       font=('Segoe UI', 10),
                       background=self.colors['card_bg'],
                       foreground=self.colors['text'])
        
        # Estilo para pestañas moderno
        style.configure('TNotebook', 
                       background=self.colors['light'],
                       borderwidth=0)
        style.configure('TNotebook.Tab', 
                       font=('Segoe UI', 11, 'bold'),
                       padding=[25, 12],
                       background=self.colors['light'],
                       foreground=self.colors['text'])
        style.map('TNotebook.Tab',
                 background=[('selected', self.colors['primary'])],
                 foreground=[('selected', 'white')],
                 expand=[('selected', [1, 1, 1, 0])])
        
        # Estilo para Treeview moderno
        style.configure('Treeview',
                       background=self.colors['card_bg'],
                       foreground=self.colors['text'],
                       fieldbackground=self.colors['card_bg'],
                       borderwidth=0,
                       font=('Segoe UI', 9))
        style.configure('Treeview.Heading',
                       font=('Segoe UI', 10, 'bold'),
                       background=self.colors['primary'],
                       foreground='white',
                       borderwidth=0)
        style.map('Treeview.Heading',
                 background=[('active', self.colors['secondary'])])
        style.map('Treeview',
                 background=[('selected', self.colors['success'])],
                 foreground=[('selected', 'white')])
        
        # Estilo para Entry y Combobox
        style.configure('Modern.TEntry',
                       fieldbackground=self.colors['card_bg'],
                       borderwidth=2,
                       relief='solid')
        style.configure('TCombobox',
                       fieldbackground=self.colors['card_bg'],
                       background=self.colors['card_bg'],
                       borderwidth=1)
        
        # Estilo para LabelFrame
        style.configure('Modern.TLabelframe',
                       background=self.colors['card_bg'],
                       borderwidth=0,
                       relief='flat')
        style.configure('Modern.TLabelframe.Label',
                       font=('Segoe UI', 12, 'bold'),
                       background=self.colors['card_bg'],
                       foreground=self.colors['primary'])
        
    def crear_interfaz(self):
        """Crea la interfaz principal con pestañas"""
        # Frame superior con título - gradiente simulado con degradado
        header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=90)
        header_frame.pack(fill='x', side='top')
        header_frame.pack_propagate(False)
        
        # Contenedor para centrar el título
        title_container = tk.Frame(header_frame, bg=self.colors['primary'])
        title_container.pack(expand=True)
        
        titulo = tk.Label(title_container, 
                         text="🔧 SISTEMA DE GESTIÓN DE MANTENIMIENTO",
                         font=('Segoe UI', 22, 'bold'),
                         bg=self.colors['primary'],
                         fg='white')
        titulo.pack(pady=10)
        
        subtitulo = tk.Label(title_container,
                           text="Versión 2.0 | Gestión Profesional de Equipos",
                           font=('Segoe UI', 10),
                           bg=self.colors['primary'],
                           fg='#e0e7ff')
        subtitulo.pack()
        
        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Crear pestañas
        self.crear_pestana_equipos()
        self.crear_pestana_ordenes()
        self.crear_pestana_tecnicos()
        self.crear_pestana_planificacion()
        self.crear_pestana_reportes()
        self.crear_pestana_about()
        
        # Cargar datos al iniciar
        gm.cargar_datos()
        self.actualizar_todas_las_listas()
        
    def actualizar_todas_las_listas(self):
        """Actualiza todas las listas de la interfaz"""
        self.actualizar_lista_equipos()
        self.actualizar_lista_ordenes()
        self.actualizar_lista_tecnicos()
    
    # ==================== PESTAÑA DE PLANIFICACIÓN ====================
    
    def crear_pestana_planificacion(self):
        """Crea la pestaña de planificación de mantenimiento"""
        tab_plan = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tab_plan, text='📅 Planificación')
        
        # Frame superior - Crear plan
        frame_form = ttk.LabelFrame(tab_plan, text="Crear Plan de Mantenimiento", 
                                   padding=20, style='Modern.TLabelframe')
        frame_form.pack(fill='x', padx=10, pady=10)
        
        # Primera fila
        frame_row1 = tk.Frame(frame_form, bg=self.colors['card_bg'])
        frame_row1.pack(fill='x', pady=8)
        
        ttk.Label(frame_row1, text="Equipo:", style='Modern.TLabel').pack(side='left', padx=8)
        self.combo_plan_equipo = ttk.Combobox(frame_row1, state='readonly', width=35,
                                             font=('Segoe UI', 10))
        self.combo_plan_equipo.pack(side='left', padx=8)
        
        ttk.Label(frame_row1, text="Tipo:", style='Modern.TLabel').pack(side='left', padx=8)
        self.combo_plan_tipo = ttk.Combobox(frame_row1,
                                           values=["Preventivo", "Correctivo", "Predictivo"],
                                           state='readonly', width=15,
                                           font=('Segoe UI', 10))
        self.combo_plan_tipo.pack(side='left', padx=8)
        self.combo_plan_tipo.set("Preventivo")
        
        ttk.Label(frame_row1, text="Mes:", style='Modern.TLabel').pack(side='left', padx=8)
        self.combo_plan_mes = ttk.Combobox(frame_row1,
                                          values=list(range(1, 13)),
                                          state='readonly', width=8,
                                          font=('Segoe UI', 10))
        self.combo_plan_mes.pack(side='left', padx=8)
        self.combo_plan_mes.set(datetime.now().month)
        
        ttk.Label(frame_row1, text="Año:", style='Modern.TLabel').pack(side='left', padx=8)
        self.entry_plan_anio = ttk.Entry(frame_row1, width=10, font=('Segoe UI', 10))
        self.entry_plan_anio.pack(side='left', padx=8)
        self.entry_plan_anio.insert(0, datetime.now().year)
        
        # Segunda fila - Descripción
        frame_row2 = tk.Frame(frame_form, bg=self.colors['card_bg'])
        frame_row2.pack(fill='x', pady=8)
        
        ttk.Label(frame_row2, text="Descripción:", style='Modern.TLabel').pack(side='left', padx=8)
        self.entry_plan_descripcion = ttk.Entry(frame_row2, width=80, font=('Segoe UI', 10))
        self.entry_plan_descripcion.pack(side='left', padx=8, fill='x', expand=True)
        
        # Botones
        frame_botones = tk.Frame(frame_form, bg=self.colors['card_bg'])
        frame_botones.pack(pady=15)
        
        btn_crear = tk.Button(frame_botones, text="➕ Crear Plan", 
                            command=self.crear_plan_mantenimiento,
                            font=('Segoe UI', 10, 'bold'),
                            bg=self.colors['success'], fg='white',
                            padx=20, pady=10, relief='flat', cursor='hand2')
        btn_crear.pack(side='left', padx=5)
        btn_crear.bind('<Enter>', lambda e: btn_crear.config(bg=self._darken_color(self.colors['success'])))
        btn_crear.bind('<Leave>', lambda e: btn_crear.config(bg=self.colors['success']))
        
        # Frame medio - Filtro de carga mensual
        frame_filtro = ttk.LabelFrame(tab_plan, text="Ver Carga de Trabajo Mensual",
                                     padding=15, style='Modern.TLabelframe')
        frame_filtro.pack(fill='x', padx=10, pady=10)
        
        filtro_container = tk.Frame(frame_filtro, bg=self.colors['card_bg'])
        filtro_container.pack(fill='x')
        
        ttk.Label(filtro_container, text="Mes:", style='Modern.TLabel').pack(side='left', padx=8)
        self.combo_filtro_mes = ttk.Combobox(filtro_container,
                                            values=list(range(1, 13)),
                                            state='readonly', width=8,
                                            font=('Segoe UI', 10))
        self.combo_filtro_mes.pack(side='left', padx=8)
        self.combo_filtro_mes.set(datetime.now().month)
        
        ttk.Label(filtro_container, text="Año:", style='Modern.TLabel').pack(side='left', padx=8)
        self.entry_filtro_anio = ttk.Entry(filtro_container, width=10, font=('Segoe UI', 10))
        self.entry_filtro_anio.pack(side='left', padx=8)
        self.entry_filtro_anio.insert(0, datetime.now().year)
        
        btn_filtrar = tk.Button(filtro_container, text="🔍 Ver Carga Mensual",
                              command=self.ver_carga_mensual,
                              font=('Segoe UI', 9, 'bold'),
                              bg=self.colors['primary'], fg='white',
                              padx=20, pady=8, relief='flat', cursor='hand2')
        btn_filtrar.pack(side='left', padx=8)
        
        btn_todos = tk.Button(filtro_container, text="📋 Ver Todos los Planes",
                            command=self.actualizar_lista_planes,
                            font=('Segoe UI', 9, 'bold'),
                            bg=self.colors['dark'], fg='white',
                            padx=20, pady=8, relief='flat', cursor='hand2')
        btn_todos.pack(side='left', padx=8)
        
        # Frame inferior - Lista de planes
        frame_lista = ttk.LabelFrame(tab_plan, text="Planes de Mantenimiento",
                                    padding=20, style='Modern.TLabelframe')
        frame_lista.pack(fill='both', expand=True, padx=10, pady=10)
        
        columnas = ('ID', 'Equipo', 'Tipo', 'Mes', 'Año', 'Estado', 'Descripción')
        self.tree_planes = ttk.Treeview(frame_lista, columns=columnas, show='headings', height=12)
        
        anchos = [50, 150, 120, 60, 60, 100, 300]
        for col, ancho in zip(columnas, anchos):
            self.tree_planes.heading(col, text=col)
            self.tree_planes.column(col, width=ancho)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient='vertical', command=self.tree_planes.yview)
        self.tree_planes.configure(yscrollcommand=scrollbar.set)
        
        self.tree_planes.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Botón para eliminar plan seleccionado
        btn_frame_plan = tk.Frame(frame_lista, bg=self.colors['card_bg'])
        btn_frame_plan.pack(fill='x', pady=10)
        btn_eliminar_plan = tk.Button(btn_frame_plan, text="🗑️ Eliminar Plan Seleccionado",
                                      command=self.eliminar_plan_mantenimiento,
                                      font=('Segoe UI', 10, 'bold'),
                                      bg=self.colors['danger'], fg='white',
                                      padx=20, pady=8, relief='flat', cursor='hand2')
        btn_eliminar_plan.pack(side='left', padx=5)
        btn_eliminar_plan.bind('<Enter>', lambda e: btn_eliminar_plan.config(bg=self._darken_color(self.colors['danger'])))
        btn_eliminar_plan.bind('<Leave>', lambda e: btn_eliminar_plan.config(bg=self.colors['danger']))
        
        self.actualizar_lista_planes()
        self.actualizar_combo_plan_equipos()
    
    def crear_plan_mantenimiento(self):
        """Crea un nuevo plan de mantenimiento"""
        if len(gm.equipos) == 0:
            messagebox.showwarning("Advertencia", "Debe registrar equipos antes de crear planes")
            return
        
        equipo_seleccionado = self.combo_plan_equipo.get()
        if not equipo_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un equipo")
            return
        
        descripcion = self.entry_plan_descripcion.get().strip()
        if not descripcion:
            messagebox.showwarning("Advertencia", "Ingrese una descripción")
            return
        
        try:
            mes = int(self.combo_plan_mes.get())
            anio = int(self.entry_plan_anio.get())
            
            if mes < 1 or mes > 12:
                messagebox.showwarning("Advertencia", "El mes debe estar entre 1 y 12")
                return
            
            # Obtener ID del equipo
            id_equipo = int(equipo_seleccionado.split(" - ")[0])
            equipo = next((e for e in gm.equipos if e["id"] == id_equipo), None)
            
            plan = {
                "id": len(gm.planes_mantenimiento) + 1,
                "equipo_id": id_equipo,
                "equipo_nombre": equipo['nombre'],
                "tipo": self.combo_plan_tipo.get(),
                "descripcion": descripcion,
                "mes": mes,
                "anio": anio,
                "estado": "Programado",
                "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            gm.planes_mantenimiento.append(plan)
            gm.guardar_datos()
            
            messagebox.showinfo("Éxito", f"Plan de mantenimiento #{plan['id']} creado correctamente")
            self.entry_plan_descripcion.delete(0, tk.END)
            self.actualizar_lista_planes()
            
        except ValueError:
            messagebox.showerror("Error", "Año inválido")
    
    def ver_carga_mensual(self):
        """Filtra planes por mes y año"""
        try:
            mes = int(self.combo_filtro_mes.get())
            anio = int(self.entry_filtro_anio.get())
            
            self.tree_planes.delete(*self.tree_planes.get_children())
            
            planes_filtrados = [p for p in gm.planes_mantenimiento 
                              if p['mes'] == mes and p['anio'] == anio]
            
            if len(planes_filtrados) == 0:
                messagebox.showinfo("Información", 
                                  f"No hay planes programados para {mes}/{anio}")
                return
            
            for p in planes_filtrados:
                self.tree_planes.insert('', 'end', values=(
                    p['id'],
                    p['equipo_nombre'],
                    p['tipo'],
                    p['mes'],
                    p['anio'],
                    p['estado'],
                    p['descripcion']
                ))
            
            messagebox.showinfo("Carga Mensual", 
                              f"Se encontraron {len(planes_filtrados)} planes para {mes}/{anio}")
            
        except ValueError:
            messagebox.showerror("Error", "Mes o año inválido")
    
    def actualizar_lista_planes(self):
        """Actualiza la lista de planes de mantenimiento"""
        self.tree_planes.delete(*self.tree_planes.get_children())
        
        for p in gm.planes_mantenimiento:
            self.tree_planes.insert('', 'end', values=(
                p['id'],
                p['equipo_nombre'],
                p['tipo'],
                p['mes'],
                p['anio'],
                p['estado'],
                p['descripcion']
            ))
    
    def actualizar_combo_plan_equipos(self):
        """Actualiza el combobox de equipos para planificación"""
        equipos_lista = [f"{eq['id']} - {eq['nombre']}" for eq in gm.equipos]
        self.combo_plan_equipo['values'] = equipos_lista
    
    # ==================== PESTAÑA ABOUT ====================
    
    def crear_pestana_about(self):
        """Crea la pestaña About con información del proyecto"""
        tab_about = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tab_about, text='ℹ️ About')
        
        # Contenedor principal centrado
        main_container = tk.Frame(tab_about, bg=self.colors['card_bg'])
        main_container.pack(expand=True, fill='both', padx=40, pady=40)
        
        # Título
        title_frame = tk.Frame(main_container, bg=self.colors['primary'], height=80)
        title_frame.pack(fill='x', pady=(0, 30))
        title_frame.pack_propagate(False)
        
        tk.Label(title_frame, 
                text="Sistema de Gestión de Mantenimiento",
                font=('Segoe UI', 20, 'bold'),
                bg=self.colors['primary'],
                fg='white').pack(expand=True)
        
        # Logos
        logos_frame = tk.Frame(main_container, bg=self.colors['card_bg'])
        logos_frame.pack(pady=20)
        
        # Intentar cargar logos
        try:
            from PIL import Image, ImageTk
            
            # Logo universidad
            logo_uni_frame = tk.Frame(logos_frame, bg=self.colors['card_bg'])
            logo_uni_frame.pack(side='left', padx=30)
            
            if os.path.exists(resource_path("unnamed.png")):
                img_uni = Image.open(resource_path("unnamed.png"))
                img_uni = img_uni.resize((150, 150), Image.Resampling.LANCZOS)
                photo_uni = ImageTk.PhotoImage(img_uni)
                label_uni = tk.Label(logo_uni_frame, image=photo_uni, bg=self.colors['card_bg'])
                label_uni.image = photo_uni
                label_uni.pack()
            
            tk.Label(logo_uni_frame, 
                    text="Fundación Universitaria\nTecnológico Comfenalco",
                    font=('Segoe UI', 10, 'bold'),
                    bg=self.colors['card_bg'],
                    fg=self.colors['text']).pack(pady=10)
            
            # Logo empresa
            logo_emp_frame = tk.Frame(logos_frame, bg=self.colors['card_bg'])
            logo_emp_frame.pack(side='right', padx=30)
            
            if os.path.exists(resource_path("LOGO OSCURO SIN FONDO.png")):
                img_emp = Image.open(resource_path("LOGO OSCURO SIN FONDO.png"))
                img_emp = img_emp.resize((150, 150), Image.Resampling.LANCZOS)
                photo_emp = ImageTk.PhotoImage(img_emp)
                label_emp = tk.Label(logo_emp_frame, image=photo_emp, bg=self.colors['card_bg'])
                label_emp.image = photo_emp
                label_emp.pack()
            
            tk.Label(logo_emp_frame,
                    text="Industrias Mecánicas\nAndinas SAS",
                    font=('Segoe UI', 10, 'bold'),
                    bg=self.colors['card_bg'],
                    fg=self.colors['text']).pack(pady=10)
                    
        except ImportError:
            tk.Label(logos_frame,
                    text="⚠ Instale Pillow para ver los logos: pip install Pillow",
                    font=('Segoe UI', 10),
                    bg=self.colors['card_bg'],
                    fg=self.colors['warning']).pack()
        
        # Información del proyecto (usar ScrolledText para que haga scroll)
        info_frame = tk.Frame(main_container, bg=self.colors['light'], relief='flat', bd=1)
        info_frame.pack(fill='both', expand=True, pady=30, padx=50)
        
        info_text = f"""
        
        👨‍💻 DESARROLLADOR
        Juan Esteban Jaramillo González
        
        🏢 EMPRESA
        Industrias Mecánicas Andinas SAS
        
        🎓 INSTITUCIÓN EDUCATIVA
        Fundación Universitaria Tecnológico Comfenalco
        
        📅 VERSIÓN
        2.0 - Sistema de Gestión de Mantenimiento
        
        📝 DESCRIPCIÓN
        Sistema desarrollado como proyecto académico para la gestión
        integral de mantenimiento industrial, incluyendo planificación,
        órdenes de trabajo, gestión de técnicos y reportes estadísticos.
        
        🔧 CARACTERÍSTICAS
        • Gestión de equipos y órdenes de trabajo
        • Planificación de mantenimiento preventivo, correctivo y predictivo
        • Gestión de técnicos y asignaciones
        • Persistencia de datos en JSON
        • Exportación a Excel
        • Reportes y estadísticas
        
        © {YEAR_DISPLAY} - Todos los derechos reservados
        """
        
        txt_info = scrolledtext.ScrolledText(info_frame,
                                            wrap='word',
                                            font=('Segoe UI', 11),
                                            bg=self.colors['light'],
                                            fg=self.colors['text'],
                                            bd=0,
                                            highlightthickness=0,
                                            padx=20,
                                            pady=20)
        txt_info.insert('1.0', info_text.strip())
        txt_info.configure(state='disabled')  # sólo lectura
        txt_info.pack(fill='both', expand=True)
        
        # Botón de cerrar
        btn_cerrar = tk.Button(main_container, text="✖ Cerrar",
                              command=lambda: self.notebook.select(0),
                              font=('Segoe UI', 10, 'bold'),
                              bg=self.colors['danger'], fg='white',
                              padx=30, pady=10, relief='flat', cursor='hand2')
        btn_cerrar.pack(pady=20)
        self.actualizar_combo_equipos()
        if hasattr(self, 'tree_planes'):
            self.actualizar_lista_planes()
        if hasattr(self, 'tree_historial'):
            self.actualizar_historial()
        if hasattr(self, 'label_stats'):
            self.actualizar_estadisticas()
        
    def crear_pestana_equipos(self):
        """Crea la pestaña de gestión de equipos"""
        tab_equipos = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tab_equipos, text='📦 Equipos')
        
        # Frame izquierdo - Formulario con estilo moderno
        frame_form = ttk.LabelFrame(tab_equipos, text="Registrar/Editar Equipo", 
                                   padding=20, style='Modern.TLabelframe')
        frame_form.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        # Campos del formulario con mejor espaciado
        campos = [
            ("Nombre:", "entry_equipo_nombre"),
            ("Ubicación:", "entry_equipo_ubicacion"),
            ("Descripción:", "entry_equipo_descripcion"),
            ("Marca:", "entry_equipo_marca"),
            ("Modelo:", "entry_equipo_modelo"),
            ("Número de Serie:", "entry_equipo_serie")
        ]
        
        for idx, (label_text, attr_name) in enumerate(campos):
            label = ttk.Label(frame_form, text=label_text, style='Modern.TLabel')
            label.grid(row=idx, column=0, sticky='w', pady=8, padx=5)
            
            entry = ttk.Entry(frame_form, width=35, font=('Segoe UI', 10))
            entry.grid(row=idx, column=1, pady=8, padx=5, sticky='ew')
            setattr(self, attr_name, entry)
        
        ttk.Label(frame_form, text="Prioridad:", style='Modern.TLabel').grid(
            row=6, column=0, sticky='w', pady=8, padx=5)
        self.combo_equipo_prioridad = ttk.Combobox(frame_form, 
                                                   values=["Alta", "Media", "Baja"],
                                                   state='readonly',
                                                   width=33,
                                                   font=('Segoe UI', 10))
        self.combo_equipo_prioridad.grid(row=6, column=1, pady=8, padx=5, sticky='ew')
        self.combo_equipo_prioridad.set("Media")
        
        frame_form.columnconfigure(1, weight=1)
        
        # Botones con iconos y colores modernos
        frame_botones = tk.Frame(frame_form, bg=self.colors['card_bg'])
        frame_botones.grid(row=7, column=0, columnspan=2, pady=25)
        
        botones = [
            ("➕ Registrar", self.registrar_equipo, self.colors['success']),
            ("🔄 Actualizar", self.actualizar_equipo, self.colors['primary']),
            ("🗑️ Eliminar", self.eliminar_equipo, self.colors['danger']),
            ("🆕 Limpiar", self.limpiar_formulario_equipo, self.colors['dark'])
        ]
        
        for texto, comando, color in botones:
            btn = tk.Button(frame_botones, text=texto, command=comando,
                          font=('Segoe UI', 10, 'bold'),
                          bg=color, fg='white',
                          padx=15, pady=10,
                          relief='flat',
                          cursor='hand2',
                          activebackground=self.colors['secondary'],
                          activeforeground='white')
            btn.pack(side='left', padx=5)
            
            # Efecto hover
            btn.bind('<Enter>', lambda e, b=btn, c=color: b.config(bg=self._darken_color(c)))
            btn.bind('<Leave>', lambda e, b=btn, c=color: b.config(bg=c))
        
        # Frame derecho - Lista de equipos
        frame_lista = ttk.LabelFrame(tab_equipos, text="Lista de Equipos", 
                                    padding=20, style='Modern.TLabelframe')
        frame_lista.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        
        # Buscador moderno
        frame_buscar = tk.Frame(frame_lista, bg=self.colors['card_bg'])
        frame_buscar.pack(fill='x', pady=(0, 15))
        
        search_container = tk.Frame(frame_buscar, bg=self.colors['light'], 
                                   relief='flat', bd=1)
        search_container.pack(side='left', fill='x', expand=True)
        
        ttk.Label(search_container, text="🔍", background=self.colors['light'],
                 font=('Segoe UI', 12)).pack(side='left', padx=8)
        self.entry_buscar_equipo = tk.Entry(search_container, 
                                           font=('Segoe UI', 10),
                                           bg=self.colors['light'],
                                           relief='flat',
                                           bd=0)
        self.entry_buscar_equipo.pack(side='left', fill='x', expand=True, pady=8)
        
        btn_buscar = tk.Button(frame_buscar, text="Buscar", command=self.buscar_equipo,
                              font=('Segoe UI', 9, 'bold'),
                              bg=self.colors['primary'], fg='white',
                              padx=15, pady=6, relief='flat', cursor='hand2')
        btn_buscar.pack(side='left', padx=5)
        
        btn_todos = tk.Button(frame_buscar, text="Mostrar Todos", 
                            command=self.actualizar_lista_equipos,
                            font=('Segoe UI', 9, 'bold'),
                            bg=self.colors['dark'], fg='white',
                            padx=15, pady=6, relief='flat', cursor='hand2')
        btn_todos.pack(side='left', padx=5)
        
        # Treeview para equipos
        columnas = ('ID', 'Nombre', 'Ubicación', 'Estado', 'Prioridad')
        self.tree_equipos = ttk.Treeview(frame_lista, columns=columnas, show='headings', height=20)
        
        for col in columnas:
            self.tree_equipos.heading(col, text=col)
            self.tree_equipos.column(col, width=120)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_lista, orient='vertical', command=self.tree_equipos.yview)
        self.tree_equipos.configure(yscrollcommand=scrollbar.set)
        
        self.tree_equipos.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Evento de selección
        self.tree_equipos.bind('<<TreeviewSelect>>', self.seleccionar_equipo)
        
        # Cargar equipos
        self.actualizar_lista_equipos()
        
    def crear_pestana_ordenes(self):
        """Crea la pestaña de órdenes de trabajo"""
        tab_ordenes = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tab_ordenes, text='🔧 Órdenes de Trabajo')
        
        # Frame superior - Formulario con estilo moderno
        frame_form = ttk.LabelFrame(tab_ordenes, text="Nueva Orden de Trabajo", 
                                   padding=20, style='Modern.TLabelframe')
        frame_form.pack(fill='x', padx=10, pady=10)
        
        # Primera fila con mejor diseño
        frame_row1 = tk.Frame(frame_form, bg=self.colors['card_bg'])
        frame_row1.pack(fill='x', pady=8)
        
        ttk.Label(frame_row1, text="Equipo:", style='Modern.TLabel').pack(side='left', padx=8)
        self.combo_ot_equipo = ttk.Combobox(frame_row1, state='readonly', width=35,
                                           font=('Segoe UI', 10))
        self.combo_ot_equipo.pack(side='left', padx=8)
        
        ttk.Label(frame_row1, text="Tipo:", style='Modern.TLabel').pack(side='left', padx=8)
        self.combo_ot_tipo = ttk.Combobox(frame_row1, 
                                         values=["Preventivo", "Correctivo", "Predictivo"],
                                         state='readonly', width=15,
                                         font=('Segoe UI', 10))
        self.combo_ot_tipo.pack(side='left', padx=8)
        self.combo_ot_tipo.set("Preventivo")
        
        ttk.Label(frame_row1, text="Prioridad:", style='Modern.TLabel').pack(side='left', padx=8)
        self.combo_ot_prioridad = ttk.Combobox(frame_row1,
                                              values=["Alta", "Media", "Baja"],
                                              state='readonly', width=12,
                                              font=('Segoe UI', 10))
        self.combo_ot_prioridad.pack(side='left', padx=8)
        self.combo_ot_prioridad.set("Media")
        
        # Segunda fila - Descripción
        frame_row2 = tk.Frame(frame_form, bg=self.colors['card_bg'])
        frame_row2.pack(fill='x', pady=8)
        
        ttk.Label(frame_row2, text="Descripción:", style='Modern.TLabel').pack(side='left', padx=8)
        self.entry_ot_descripcion = ttk.Entry(frame_row2, width=100, font=('Segoe UI', 10))
        self.entry_ot_descripcion.pack(side='left', padx=8, fill='x', expand=True)
        
        # Botones modernos
        frame_botones = tk.Frame(frame_form, bg=self.colors['card_bg'])
        frame_botones.pack(pady=15)
        
        botones = [
            ("➕ Crear Orden", self.crear_orden_trabajo, self.colors['success']),
            ("✅ Completar Orden", self.completar_orden_trabajo, self.colors['primary']),
            ("👷 Asignar Técnico", self.asignar_tecnico_orden, self.colors['warning']),
            ("🔄 Cambiar Estado", self.cambiar_estado_orden, self.colors['dark'])
        ]
        # Añadir botón Eliminar Orden al array de botones
        botones.append(("🗑️ Eliminar Orden", self.eliminar_orden_trabajo, self.colors['danger']))
        
        for texto, comando, color in botones:
            btn = tk.Button(frame_botones, text=texto, command=comando,
                          font=('Segoe UI', 10, 'bold'),
                          bg=color, fg='white',
                          padx=18, pady=10,
                          relief='flat',
                          cursor='hand2',
                          activebackground=self.colors['secondary'],
                          activeforeground='white')
            btn.pack(side='left', padx=5)
            btn.bind('<Enter>', lambda e, b=btn, c=color: b.config(bg=self._darken_color(c)))
            btn.bind('<Leave>', lambda e, b=btn, c=color: b.config(bg=c))
        
        # Frame inferior - Lista de órdenes
        frame_lista = ttk.LabelFrame(tab_ordenes, text="Órdenes de Trabajo", 
                                    padding=20, style='Modern.TLabelframe')
        frame_lista.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Filtro por estado moderno
        frame_filtro = tk.Frame(frame_lista, bg=self.colors['card_bg'])
        frame_filtro.pack(fill='x', pady=(0, 15))
        
        ttk.Label(frame_filtro, text="Filtrar por estado:", 
                 style='Modern.TLabel', font=('Segoe UI', 10, 'bold')).pack(side='left', padx=8)
        self.combo_filtro_estado = ttk.Combobox(frame_filtro,
                                               values=["Todos", "Pendiente", "En progreso", "Pausada", "Completada", "Cancelada"],
                                               state='readonly', width=18,
                                               font=('Segoe UI', 10))
        self.combo_filtro_estado.pack(side='left', padx=8)
        self.combo_filtro_estado.set("Todos")
        
        btn_filtrar = tk.Button(frame_filtro, text="🔍 Filtrar", 
                              command=self.filtrar_ordenes,
                              font=('Segoe UI', 9, 'bold'),
                              bg=self.colors['primary'], fg='white',
                              padx=20, pady=8, relief='flat', cursor='hand2')
        btn_filtrar.pack(side='left', padx=5)
        
        # Treeview para órdenes
        columnas = ('ID', 'Equipo', 'Tipo', 'Estado', 'Prioridad', 'Técnico')
        self.tree_ordenes = ttk.Treeview(frame_lista, columns=columnas, show='headings', height=15)
        
        for col in columnas:
            self.tree_ordenes.heading(col, text=col)
            self.tree_ordenes.column(col, width=150)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient='vertical', command=self.tree_ordenes.yview)
        self.tree_ordenes.configure(yscrollcommand=scrollbar.set)
        
        self.tree_ordenes.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Actualizar listas
        self.actualizar_combo_equipos()
        self.actualizar_lista_ordenes()
        
    def crear_pestana_tecnicos(self):
        """Crea la pestaña de gestión de técnicos"""
        tab_tecnicos = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tab_tecnicos, text='👷 Técnicos')
        
        # Frame izquierdo - Formulario moderno
        frame_form = ttk.LabelFrame(tab_tecnicos, text="Registrar Técnico", 
                                   padding=20, style='Modern.TLabelframe')
        frame_form.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        # Campos del formulario
        campos = [
            ("Nombre Completo:", "entry_tecnico_nombre"),
            ("Especialidad:", "entry_tecnico_especialidad"),
            ("Teléfono:", "entry_tecnico_telefono")
        ]
        
        for idx, (label_text, attr_name) in enumerate(campos):
            label = ttk.Label(frame_form, text=label_text, style='Modern.TLabel')
            label.grid(row=idx, column=0, sticky='w', pady=12, padx=5)
            
            entry = ttk.Entry(frame_form, width=40, font=('Segoe UI', 10))
            entry.grid(row=idx, column=1, pady=12, padx=5, sticky='ew')
            setattr(self, attr_name, entry)
        
        frame_form.columnconfigure(1, weight=1)
        
        # Botones modernos
        frame_botones = tk.Frame(frame_form, bg=self.colors['card_bg'])
        frame_botones.grid(row=3, column=0, columnspan=2, pady=25)
        
        botones = [
            ("➕ Registrar Técnico", self.registrar_tecnico, self.colors['success']),
            ("🆕 Limpiar", self.limpiar_formulario_tecnico, self.colors['dark'])
        ]
        # Añadir botón eliminar técnico
        botones.append(("🗑️ Eliminar Técnico", self.eliminar_tecnico, self.colors['danger']))
        
        for texto, comando, color in botones:
            btn = tk.Button(frame_botones, text=texto, command=comando,
                          font=('Segoe UI', 10, 'bold'),
                          bg=color, fg='white',
                          padx=20, pady=10,
                          relief='flat',
                          cursor='hand2',
                          activebackground=self.colors['secondary'],
                          activeforeground='white')
            btn.pack(side='left', padx=8)
            btn.bind('<Enter>', lambda e, b=btn, c=color: b.config(bg=self._darken_color(c)))
            btn.bind('<Leave>', lambda e, b=btn, c=color: b.config(bg=c))
        
        # Frame derecho - Lista de técnicos
        frame_lista = ttk.LabelFrame(tab_tecnicos, text="Lista de Técnicos", 
                                    padding=20, style='Modern.TLabelframe')
        frame_lista.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        
        columnas = ('ID', 'Nombre', 'Especialidad', 'Teléfono', 'Estado')
        self.tree_tecnicos = ttk.Treeview(frame_lista, columns=columnas, show='headings', height=20)
        
        for col in columnas:
            self.tree_tecnicos.heading(col, text=col)
            self.tree_tecnicos.column(col, width=120)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient='vertical', command=self.tree_tecnicos.yview)
        self.tree_tecnicos.configure(yscrollcommand=scrollbar.set)
        
        self.tree_tecnicos.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.actualizar_lista_tecnicos()
        
    def crear_pestana_reportes(self):
        """Crea la pestaña de reportes y estadísticas"""
        tab_reportes = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tab_reportes, text='📊 Reportes')
        
        # Frame superior - Estadísticas con diseño de card moderno
        frame_stats = ttk.LabelFrame(tab_reportes, text="Estadísticas Generales", 
                                    padding=25, style='Modern.TLabelframe')
        frame_stats.pack(fill='x', padx=10, pady=10)
        
        # Card de estadísticas con sombra simulada
        stats_card = tk.Frame(frame_stats, bg=self.colors['light'], relief='flat', bd=0)
        stats_card.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.label_stats = tk.Label(stats_card, 
                                    text="",
                                    font=('Segoe UI', 11),
                                    justify='left',
                                    bg=self.colors['light'],
                                    fg=self.colors['text'],
                                    padx=30,
                                    pady=25)
        self.label_stats.pack(fill='both', expand=True)
        
        # Botón de actualización moderno
        btn_actualizar = tk.Button(frame_stats, text="🔄 Actualizar Estadísticas",
                                  command=self.actualizar_estadisticas,
                                  font=('Segoe UI', 10, 'bold'),
                                  bg=self.colors['primary'], fg='white',
                                  padx=25, pady=12,
                                  relief='flat',
                                  cursor='hand2',
                                  activebackground=self.colors['secondary'],
                                  activeforeground='white')
        btn_actualizar.pack(pady=15)
        btn_actualizar.bind('<Enter>', lambda e: btn_actualizar.config(bg=self._darken_color(self.colors['primary'])))
        btn_actualizar.bind('<Leave>', lambda e: btn_actualizar.config(bg=self.colors['primary']))
        
        # Frame inferior - Historial
        frame_historial = ttk.LabelFrame(tab_reportes, text="Historial de Mantenimiento", 
                                        padding=20, style='Modern.TLabelframe')
        frame_historial.pack(fill='both', expand=True, padx=10, pady=10)
        
        columnas = ('ID', 'Equipo', 'Tipo', 'Fecha', 'Técnico')
        self.tree_historial = ttk.Treeview(frame_historial, columns=columnas, show='headings', height=15)
        
        for col in columnas:
            self.tree_historial.heading(col, text=col)
            self.tree_historial.column(col, width=180)
        
        scrollbar = ttk.Scrollbar(frame_historial, orient='vertical', command=self.tree_historial.yview)
        self.tree_historial.configure(yscrollcommand=scrollbar.set)
        
        self.tree_historial.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Botón de exportación
        btn_frame = tk.Frame(frame_historial, bg=self.colors['card_bg'])
        btn_frame.pack(pady=15)
        
        btn_exportar = tk.Button(btn_frame, text="📊 Exportar Todo a Excel",
                               command=self.exportar_a_excel,
                               font=('Segoe UI', 11, 'bold'),
                               bg=self.colors['success'], fg='white',
                               padx=30, pady=12, relief='flat', cursor='hand2')
        btn_exportar.pack(side='left', padx=5)
        btn_exportar.bind('<Enter>', lambda e: btn_exportar.config(bg=self._darken_color(self.colors['success'])))
        btn_exportar.bind('<Leave>', lambda e: btn_exportar.config(bg=self.colors['success']))
        
        btn_guardar = tk.Button(btn_frame, text="💾 Guardar Datos (JSON)",
                              command=self.guardar_datos_manual,
                              font=('Segoe UI', 11, 'bold'),
                              bg=self.colors['primary'], fg='white',
                              padx=30, pady=12, relief='flat', cursor='hand2')
        btn_guardar.pack(side='left', padx=5)
        btn_guardar.bind('<Enter>', lambda e: btn_guardar.config(bg=self._darken_color(self.colors['primary'])))
        btn_guardar.bind('<Leave>', lambda e: btn_guardar.config(bg=self.colors['primary']))
        
        self.actualizar_estadisticas()
        self.actualizar_historial()
    
    def guardar_datos_manual(self):
        """Guarda los datos manualmente"""
        if gm.guardar_datos():
            messagebox.showinfo("Éxito", "Datos guardados correctamente en datos_mantenimiento.json")
        else:
            messagebox.showerror("Error", "No se pudieron guardar los datos")
    
    def exportar_a_excel(self):
        """Exporta historial a Excel (requiere pandas + openpyxl)"""
        try:
            import pandas as pd
        except ImportError:
            messagebox.showwarning("Exportar", "Instale 'pandas' y 'openpyxl':\n\npip install pandas openpyxl")
            return

        if not gm.historial_mantenimiento:
            messagebox.showinfo("Exportar", "No hay datos en el historial para exportar")
            return

        try:
            df = pd.DataFrame(gm.historial_mantenimiento)
            # Guardar por defecto en DATA_DIR; puedes usar filedialog.asksaveasfilename si prefieres elegir ruta
            salida = os.path.join(DATA_DIR, "historial_mantenimiento.xlsx")
            df.to_excel(salida, index=False)
            messagebox.showinfo("Exportar", f"Historial exportado a:\n{salida}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar a Excel:\n{e}")
    
    # ==================== MÉTODOS DE EQUIPOS ====================
    
    def registrar_equipo(self):
        """Registra un nuevo equipo"""
        nombre = self.entry_equipo_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "El nombre del equipo es obligatorio")
            return
        
        equipo = {
            "id": len(gm.equipos) + 1,
            "nombre": nombre,
            "ubicacion": self.entry_equipo_ubicacion.get().strip(),
            "descripcion": self.entry_equipo_descripcion.get().strip(),
            "marca": self.entry_equipo_marca.get().strip(),
            "modelo": self.entry_equipo_modelo.get().strip(),
            "numero_serie": self.entry_equipo_serie.get().strip(),
            "prioridad": self.combo_equipo_prioridad.get(),
            "estado": "Operativo",
            "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        gm.equipos.append(equipo)
        messagebox.showinfo("Éxito", f"Equipo '{nombre}' registrado correctamente")
        gm.guardar_datos()  # Guardar automáticamente
        self.limpiar_formulario_equipo()
        self.actualizar_lista_equipos()
        self.actualizar_combo_equipos()
        self.actualizar_combo_plan_equipos()  # Actualizar también en planificación
        
    def actualizar_equipo(self):
        """Actualiza un equipo seleccionado"""
        seleccion = self.tree_equipos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un equipo de la lista")
            return
        
        item = self.tree_equipos.item(seleccion[0])
        id_equipo = int(item['values'][0])
        
        equipo = next((e for e in gm.equipos if e["id"] == id_equipo), None)
        if equipo:
            equipo['nombre'] = self.entry_equipo_nombre.get().strip()
            equipo['ubicacion'] = self.entry_equipo_ubicacion.get().strip()
            equipo['descripcion'] = self.entry_equipo_descripcion.get().strip()
            equipo['marca'] = self.entry_equipo_marca.get().strip()
            equipo['modelo'] = self.entry_equipo_modelo.get().strip()
            equipo['numero_serie'] = self.entry_equipo_serie.get().strip()
            equipo['prioridad'] = self.combo_equipo_prioridad.get()
            
            messagebox.showinfo("Éxito", "Equipo actualizado correctamente")
            gm.guardar_datos()  # Guardar automáticamente
            self.actualizar_lista_equipos()
            self.actualizar_combo_equipos()
            self.actualizar_combo_plan_equipos()
        
    def eliminar_equipo(self):
        """Elimina un equipo seleccionado"""
        seleccion = self.tree_equipos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un equipo de la lista")
            return
        
        item = self.tree_equipos.item(seleccion[0])
        id_equipo = int(item['values'][0])
        nombre_equipo = item['values'][1]
        
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar '{nombre_equipo}'?"):
            equipo = next((e for e in gm.equipos if e["id"] == id_equipo), None)
            if equipo:
                gm.equipos.remove(equipo)
                messagebox.showinfo("Éxito", "Equipo eliminado correctamente")
                gm.guardar_datos()  # Guardar automáticamente
                self.limpiar_formulario_equipo()
                self.actualizar_lista_equipos()
                self.actualizar_combo_equipos()
                self.actualizar_combo_plan_equipos()
    
    def buscar_equipo(self):
        """Busca equipos por nombre o ubicación"""
        termino = self.entry_buscar_equipo.get().strip().lower()
        if not termino:
            self.actualizar_lista_equipos()
            return
        
        self.tree_equipos.delete(*self.tree_equipos.get_children())
        
        for eq in gm.equipos:
            if termino in eq['nombre'].lower() or termino in eq['ubicacion'].lower():
                self.tree_equipos.insert('', 'end', values=(
                    eq['id'],
                    eq['nombre'],
                    eq['ubicacion'],
                    eq['estado'],
                    eq['prioridad']
                ))
    
    def seleccionar_equipo(self, event):
        """Carga los datos del equipo seleccionado en el formulario"""
        seleccion = self.tree_equipos.selection()
        if not seleccion:
            return
        
        item = self.tree_equipos.item(seleccion[0])
        id_equipo = int(item['values'][0])
        
        equipo = next((e for e in gm.equipos if e["id"] == id_equipo), None)
        if equipo:
            self.entry_equipo_nombre.delete(0, tk.END)
            self.entry_equipo_nombre.insert(0, equipo['nombre'])
            
            self.entry_equipo_ubicacion.delete(0, tk.END)
            self.entry_equipo_ubicacion.insert(0, equipo['ubicacion'])
            
            self.entry_equipo_descripcion.delete(0, tk.END)
            self.entry_equipo_descripcion.insert(0, equipo['descripcion'])
            
            self.entry_equipo_marca.delete(0, tk.END)
            self.entry_equipo_marca.insert(0, equipo['marca'])
            
            self.entry_equipo_modelo.delete(0, tk.END)
            self.entry_equipo_modelo.insert(0, equipo['modelo'])
            
            self.entry_equipo_serie.delete(0, tk.END)
            self.entry_equipo_serie.insert(0, equipo['numero_serie'])
            
            self.combo_equipo_prioridad.set(equipo['prioridad'])
    
    def limpiar_formulario_equipo(self):
        """Limpia el formulario de equipos"""
        self.entry_equipo_nombre.delete(0, tk.END)
        self.entry_equipo_ubicacion.delete(0, tk.END)
        self.entry_equipo_descripcion.delete(0, tk.END)
        self.entry_equipo_marca.delete(0, tk.END)
        self.entry_equipo_modelo.delete(0, tk.END)
        self.entry_equipo_serie.delete(0, tk.END)
        self.combo_equipo_prioridad.set("Media")
    
    def actualizar_lista_equipos(self):
        """Actualiza la lista de equipos en el TreeView"""
        self.tree_equipos.delete(*self.tree_equipos.get_children())
        
        for eq in gm.equipos:
            self.tree_equipos.insert('', 'end', values=(
                eq['id'],
                eq['nombre'],
                eq['ubicacion'],
                eq['estado'],
                eq['prioridad']
            ))
    
    # ==================== MÉTODOS DE ÓRDENAS ====================
    
    def crear_orden_trabajo(self):
        """Crea una nueva orden de trabajo"""
        if len(gm.equipos) == 0:
            messagebox.showwarning("Advertencia", "Debe registrar equipos antes de crear órdenes")
            return
        
        equipo_seleccionado = self.combo_ot_equipo.get()
        if not equipo_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un equipo")
            return
        
        descripcion = self.entry_ot_descripcion.get().strip()
        if not descripcion:
            messagebox.showwarning("Advertencia", "Ingrese una descripción")
            return
        
        # Obtener ID del equipo
        id_equipo = int(equipo_seleccionado.split(" - ")[0])
        equipo = next((e for e in gm.equipos if e["id"] == id_equipo), None)
        
        ot = {
            "id": len(gm.ordenes_trabajo) + 1,
            "equipo_id": id_equipo,
            "equipo_nombre": equipo['nombre'],
            "descripcion": descripcion,
            "tipo": self.combo_ot_tipo.get(),
            "prioridad": self.combo_ot_prioridad.get(),
            "estado": "Pendiente",
            "tecnico_asignado": None,
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "fecha_inicio": None,
            "fecha_finalizacion": None,
            "observaciones": ""
        }
        
        gm.ordenes_trabajo.append(ot)
        messagebox.showinfo("Éxito", f"Orden de trabajo #{ot['id']} creada correctamente")
        gm.guardar_datos()  # Guardar automáticamente
        self.entry_ot_descripcion.delete(0, tk.END)
        self.actualizar_lista_ordenes()
        self.actualizar_estadisticas()
        
    def completar_orden_trabajo(self):
        """Completa una orden de trabajo seleccionada"""
        seleccion = self.tree_ordenes.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una orden de la lista")
            return
        
        item = self.tree_ordenes.item(seleccion[0])
        id_orden = int(item['values'][0])
        
        orden = next((o for o in gm.ordenes_trabajo if o["id"] == id_orden), None)
        
        if not orden:
            messagebox.showwarning("Advertencia", "Orden no encontrada")
            return
        
        if orden['estado'] == "Completada":
            messagebox.showinfo("Información", "Esta orden ya está completada")
            return
        
        # Diálogo para observaciones
        observaciones = simpledialog.askstring("Observaciones",
                                               "Ingrese observaciones finales:",
                                               parent=self.root)
        
        orden['estado'] = "Completada"
        orden['fecha_finalizacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        orden['observaciones'] = observaciones if observaciones else ""
        
        # Agregar al historial
        gm.historial_mantenimiento.append({
            "orden_id": orden['id'],
            "equipo_nombre": orden['equipo_nombre'],
            "tipo": orden['tipo'],
            "fecha": orden['fecha_finalizacion'],
            "tecnico": orden['tecnico_asignado'],
            "observaciones": observaciones if observaciones else ""
        })
        
        # Liberar técnico
        if orden['tecnico_asignado']:
            for t in gm.tecnicos:
                if t['nombre'] == orden['tecnico_asignado']:
                    t['estado'] = "Disponible"
                    break
        
        messagebox.showinfo("Éxito", f"Orden #{orden['id']} completada exitosamente")
        gm.guardar_datos()  # Guardar automáticamente
        self.actualizar_lista_ordenes()
        self.actualizar_lista_tecnicos()
        self.actualizar_historial()
        self.actualizar_estadisticas()
    
    def asignar_tecnico_orden(self):
        """Asigna un técnico a una orden de trabajo"""
        if len(gm.tecnicos) == 0:
            messagebox.showwarning("Advertencia", "Debe registrar técnicos primero")
            return
        
        seleccion = self.tree_ordenes.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una orden de la lista")
            return
        
        item = self.tree_ordenes.item(seleccion[0])
        id_orden = int(item['values'][0])
        
        orden = next((o for o in gm.ordenes_trabajo if o["id"] == id_orden), None)
        if not orden:
            return
        
        # Ventana para seleccionar técnico
        ventana = tk.Toplevel(self.root)
        ventana.title("Asignar Técnico")
        ventana.geometry("400x300")
        
        ttk.Label(ventana, text="Seleccione un técnico:", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Lista de técnicos
        lista_tecnicos = tk.Listbox(ventana, height=10)
        lista_tecnicos.pack(fill='both', expand=True, padx=20, pady=10)
        
        for t in gm.tecnicos:
            lista_tecnicos.insert(tk.END, f"{t['id']} - {t['nombre']} ({t['especialidad']}) - {t['estado']}")
        
        def asignar():
            seleccion = lista_tecnicos.curselection()
            if not seleccion:
                messagebox.showwarning("Advertencia", "Seleccione un técnico")
                return
            
            idx = seleccion[0]
            tecnico = gm.tecnicos[idx]
            
            orden['tecnico_asignado'] = tecnico['nombre']
            tecnico['estado'] = "Ocupado"
            
            messagebox.showinfo("Éxito", f"Técnico {tecnico['nombre']} asignado correctamente")
            gm.guardar_datos()  # Guardar automáticamente
            ventana.destroy()
            self.actualizar_lista_ordenes()
            self.actualizar_lista_tecnicos()
        
        ttk.Button(ventana, text="Asignar", command=asignar, style='Main.TButton').pack(pady=10)
    
    def cambiar_estado_orden(self):
        """Cambia el estado de una orden de trabajo"""
        seleccion = self.tree_ordenes.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una orden de la lista")
            return

        item = self.tree_ordenes.item(seleccion[0])
        id_orden = int(item['values'][0])

        orden = next((o for o in gm.ordenes_trabajo if o["id"] == id_orden), None)
        if not orden:
            messagebox.showwarning("Advertencia", "Orden no encontrada")
            return

        # Ventana para cambiar estado
        ventana = tk.Toplevel(self.root)
        ventana.title("Cambiar Estado")
        ventana.geometry("350x200")

        ttk.Label(ventana, text=f"Estado actual: {orden['estado']}",
                  font=('Arial', 11, 'bold')).pack(pady=15)

        ttk.Label(ventana, text="Nuevo estado:").pack(pady=5)
        combo_estado = ttk.Combobox(ventana,
                                    values=["Pendiente", "En progreso", "Pausada", "Completada", "Cancelada"],
                                    state='readonly', width=20)
        combo_estado.pack(pady=10)
        combo_estado.set(orden['estado'])

        def cambiar():
            nuevo_estado = combo_estado.get()
            orden['estado'] = nuevo_estado

            if nuevo_estado == "En progreso" and not orden['fecha_inicio']:
                orden['fecha_inicio'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            messagebox.showinfo("Éxito", f"Estado actualizado a: {nuevo_estado}")
            gm.guardar_datos()  # Guardar automáticamente
            ventana.destroy()
            self.actualizar_lista_ordenes()

        ttk.Button(ventana, text="Cambiar Estado", command=cambiar, style='Main.TButton').pack(pady=15)
    
    def filtrar_ordenes(self):
        """Filtra órdenes por estado"""
        estado = self.combo_filtro_estado.get()
        
        self.tree_ordenes.delete(*self.tree_ordenes.get_children())
        
        for o in gm.ordenes_trabajo:
            if estado == "Todos" or o['estado'] == estado:
                tecnico = o['tecnico_asignado'] if o['tecnico_asignado'] else "Sin asignar"
                self.tree_ordenes.insert('', 'end', values=(
                    o['id'],
                    o['equipo_nombre'],
                    o['tipo'],
                    o['estado'],
                    o['prioridad'],
                    tecnico
                ))
    
    def actualizar_lista_ordenes(self):
        """Actualiza la lista de órdenes de trabajo"""
        self.tree_ordenes.delete(*self.tree_ordenes.get_children())
        
        for o in gm.ordenes_trabajo:
            tecnico = o['tecnico_asignado'] if o['tecnico_asignado'] else "Sin asignar"
            self.tree_ordenes.insert('', 'end', values=(
                o['id'],
                o['equipo_nombre'],
                o['tipo'],
                o['estado'],
                o['prioridad'],
                tecnico
            ))
    
    def actualizar_combo_equipos(self):
        """Actualiza el combobox de equipos"""
        equipos_lista = [f"{eq['id']} - {eq['nombre']}" for eq in gm.equipos]
        self.combo_ot_equipo['values'] = equipos_lista
    
    # ==================== MÉTODOS DE TÉCNICOS ====================
    
    def registrar_tecnico(self):
        """Registra un nuevo técnico"""
        nombre = self.entry_tecnico_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "El nombre del técnico es obligatorio")
            return
        
        tecnico = {
            "id": len(gm.tecnicos) + 1,
            "nombre": nombre,
            "especialidad": self.entry_tecnico_especialidad.get().strip(),
            "telefono": self.entry_tecnico_telefono.get().strip(),
            "estado": "Disponible"
        }
        
        gm.tecnicos.append(tecnico)
        messagebox.showinfo("Éxito", f"Técnico '{nombre}' registrado correctamente")
        gm.guardar_datos()  # Guardar automáticamente
        self.limpiar_formulario_tecnico()
        self.actualizar_lista_tecnicos()
    
    def limpiar_formulario_tecnico(self):
        """Limpia el formulario de técnicos"""
        self.entry_tecnico_nombre.delete(0, tk.END)
        self.entry_tecnico_especialidad.delete(0, tk.END)
        self.entry_tecnico_telefono.delete(0, tk.END)
    
    def actualizar_lista_tecnicos(self):
        """Actualiza la lista de técnicos"""
        self.tree_tecnicos.delete(*self.tree_tecnicos.get_children())
        
        for t in gm.tecnicos:
            self.tree_tecnicos.insert('', 'end', values=(
                t['id'],
                t['nombre'],
                t['especialidad'],
                t['telefono'],
                t['estado']
            ))
    
    # ==================== MÉTODOS DE REPORTES ====================
    
    def actualizar_estadisticas(self):
        """Actualiza las estadísticas generales con diseño moderno"""
        total_equipos = len(gm.equipos)
        total_ordenes = len(gm.ordenes_trabajo)
        total_tecnicos = len(gm.tecnicos)
        total_completadas = len(gm.historial_mantenimiento)
        
        pendientes = sum(1 for o in gm.ordenes_trabajo if o['estado'] == "Pendiente")
        en_progreso = sum(1 for o in gm.ordenes_trabajo if o['estado'] == "En progreso")
        completadas = sum(1 for o in gm.ordenes_trabajo if o['estado'] == "Completada")
        
        # Texto con mejor formato y emojis
        texto = f"""
    📦  EQUIPOS REGISTRADOS
         {total_equipos} equipos en el sistema
    
    🔧  ÓRDENAS DE TRABAJO
         Total: {total_ordenes}
         • Pendientes: {pendientes}
         • En Progreso: {en_progreso}
         • Completadas: {completadas}
    
    👷  TÉCNICOS REGISTRADOS
         {total_tecnicos} técnicos disponibles
    
    ✅  MANTENIMIENTOS COMPLETADOS
         {total_completadas} trabajos finalizados
        """
        
        self.label_stats.config(text=texto, 
                               font=('Segoe UI', 11),
                               bg=self.colors['card_bg'],
                               fg=self.colors['text'])
    
    def _darken_color(self, hex_color):
        """Oscurece un color hexadecimal para efectos hover"""
        # Convertir hex a RGB
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # Oscurecer (reducir cada componente en 20%)
        r = max(0, int(r * 0.8))
        g = max(0, int(g * 0.8))
        b = max(0, int(b * 0.8))
        
        # Convertir de vuelta a hex
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def actualizar_historial(self):
        """Actualiza el historial de mantenimiento"""
        self.tree_historial.delete(*self.tree_historial.get_children())
        
        for h in gm.historial_mantenimiento:
            tecnico = h['tecnico'] if h['tecnico'] else "Sin asignar"
            self.tree_historial.insert('', 'end', values=(
                h['orden_id'],
                h['equipo_nombre'],
                h['tipo'],
                h['fecha'],
                tecnico
            ))

    def eliminar_orden_trabajo(self):
        """Elimina la orden de trabajo seleccionada y libera técnico si aplica"""
        seleccion = self.tree_ordenes.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una orden de la lista")
            return

        item = self.tree_ordenes.item(seleccion[0])
        id_orden = int(item['values'][0])

        if not messagebox.askyesno("Confirmar", f"¿Eliminar la orden #{id_orden}? Esta acción no se puede deshacer."):
            return

        orden = next((o for o in gm.ordenes_trabajo if o["id"] == id_orden), None)
        if orden:
            # Liberar técnico asignado (si existe)
            if orden.get('tecnico_asignado'):
                for t in gm.tecnicos:
                    if t['nombre'] == orden['tecnico_asignado']:
                        t['estado'] = "Disponible"
                        break
            gm.ordenes_trabajo.remove(orden)
            gm.guardar_datos()
            messagebox.showinfo("Éxito", f"Orden #{id_orden} eliminada correctamente")
            self.actualizar_lista_ordenes()
            self.actualizar_lista_tecnicos()
            self.actualizar_estadisticas()
    
    def eliminar_tecnico(self):
        """Elimina el técnico seleccionado. Desasigna en las órdenes si aplica."""
        seleccion = self.tree_tecnicos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un técnico de la lista")
            return

        item = self.tree_tecnicos.item(seleccion[0])
        id_tecnico = int(item['values'][0])

        tecnico = next((t for t in gm.tecnicos if t["id"] == id_tecnico), None)
        if not tecnico:
            messagebox.showwarning("Advertencia", "Técnico no encontrado")
            return

        # Buscar órdenes activas asignadas
        asignadas = [o for o in gm.ordenes_trabajo if o.get('tecnico_asignado') == tecnico['nombre'] and o.get('estado') != "Completada"]
        if asignadas:
            if not messagebox.askyesno("Confirmar", f"El técnico está asignado a {len(asignadas)} orden(es) activas.\n¿Desea eliminar y desasignar de esas órdenes?"):
                return

        # Desasignar en todas las órdenes
        for o in gm.ordenes_trabajo:
            if o.get('tecnico_asignado') == tecnico['nombre']:
                o['tecnico_asignado'] = None

        gm.tecnicos.remove(tecnico)
        gm.guardar_datos()
        messagebox.showinfo("Éxito", f"Técnico '{tecnico['nombre']}' eliminado correctamente")
        self.actualizar_lista_tecnicos()
        self.actualizar_lista_ordenes()
        self.actualizar_estadisticas()
    
    def eliminar_plan_mantenimiento(self):
        """Elimina el plan de mantenimiento seleccionado"""
        seleccion = self.tree_planes.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un plan de la lista")
            return

        item = self.tree_planes.item(seleccion[0])
        id_plan = int(item['values'][0])

        if not messagebox.askyesno("Confirmar", f"¿Eliminar el plan #{id_plan}?"):
            return

        plan = next((p for p in gm.planes_mantenimiento if p["id"] == id_plan), None)
        if plan:
            gm.planes_mantenimiento.remove(plan)
            gm.guardar_datos()
            messagebox.showinfo("Éxito", f"Plan #{id_plan} eliminado correctamente")
            self.actualizar_lista_planes()
    
def main():
    # Debug: descomenta la línea siguiente si quieres ver mensajes en la consola
    # print("Iniciando GUI de Gestión de Mantenimiento...")
    root = tk.Tk()
    app = SistemaMantenimientoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()