Este código fue desarrollado durante el curso PyLatino 2025, con el objetivo de explorar cómo funcionan los softwares de gestión de mantenimiento en las empresas. En el proceso, tuve que migrar a Visual Studio Code (VSC) debido a fallos presentados en la consola de PyLatino, posiblemente relacionados con alguna extensión. Sin embargo, esta situación se convirtió en una oportunidad, ya que me permitió agregar más funciones al proyecto.

Entre las mejoras realizadas se destacan:

La creación de una interfaz gráfica utilizando la librería Tkinter.

La aplicación de la estrategia de Vibe Coding para optimizar el desarrollo.

La generación de un ejecutable mediante PyInstaller, lo que facilita la distribución y uso del software.


Configuracion: Debe ejecutarse el codigo de Inteaz_Mantenimiento ya que en este esta la interfaz visual que es intuitiva, tambien poner en pantalla completa la ventana emergente de la interfaz pues por resolucion puede que en ventana no se pueda ver el codigo completo ademas de si tiene escalado en su configuracion de pantalla escalado por windows ponerla en 100% para mejor visibilidad

---------------------------------------------------------------------------------------------------------------

Funcionamiento: Esta interfaz permite en una seccion la de equipos agregar, eliminar y modificar equipos ademas de actualziar la tabla de equipos tabla que cuenta con un buscador otra seccion llamada ordenes de trabajo permite crear ordenes de trabajo, completar estas ordenes, asignar tecnicos, cambiar estado de la orden, eliminarla y visualizar las ordenes de trabajo en una tabla ademas de filtrarlas por estado, en la seccion de tecnicos se pueden registar, modificar y eliminar los tecnicos que se encuentran dentro de la empresa ademas de una lista con los tecnicos ya presentes, en la seccion de planificacion encontramos para crear planes de mantenimiento para el futuro principalmente pensado para mantenimientos predictivos y preventivos pero sin excluir aquellos mantenimientos correctivos planificados con anticipacion se puede filtrar la carga del trabajo mensual por mes y año, de penultima se ven las estadisticas generales en reportes donde encontramos la cantidad de equipos registrados, ordenes de trabajo, tecncicos y mantenimientso completados ademas de la posibilidad de exportar a un excel y guardar datos en un .JSON para cuando se vuelva a abrir la aplicacion cuente con estos datos y por ultimo una seccion llamada About donde encontramos la empresa ficticia que utilice para la materia de gestion de mantenimiento, mi universidad y un par de datos como mi nombre en desarrollador, version, descripcion y caracteristicas

-------------------------------------------------------------------------------------

Como usar Pyinstaller (Recomendado para un mejor funcionamiento de el codigo):

Tutorial de PyInstaller


1. Instalar PyInstaller

Primero, asegúrate de tener PyInstaller instalado en tu sistema. Puedes instalarlo fácilmente con el siguiente comando:

pip install pyinstaller

2. Navegar al Directorio del Proyecto

Abre una terminal y navega al directorio donde se encuentra tu script principal de Python y sus dependencias:

cd /ruta/a/tu/proyecto

3. Crear el Ejecutable

Ejecuta PyInstaller para empaquetar tu aplicación. El siguiente comando genera un único archivo ejecutable:

pyinstaller --onefile --windowed --icon=favicon.ico --add-data "datos_mantenimiento.json;." --add-data "LOGO OSCURO SIN FONDO.png;." --add-data "unnamed.png;." Interfaz_Mantenimiento.py

La opción --onefile asegura que todas las dependencias se empaqueten en un solo archivo.

4. Localizar el Ejecutable

Una vez completado el proceso, encontrarás el ejecutable en la carpeta dist dentro del directorio de tu proyecto:

ls dist/

El archivo generado será algo como GestionMantenimiento.exe (en Windows)

![image alt](https://github.com/Juanes-GOAT/Maintenance_Management_2.0/blob/dd8febe6418f920401537b76447a2cfd91b52fe1/Equipos.png)
