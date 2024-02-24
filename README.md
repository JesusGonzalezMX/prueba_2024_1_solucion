# Iniciativa en Ciencia de Decisiones | Solución a la Prueba - 2024-1
### Jesús González Godoy, PhD | 23-02-2024

### Estructura del repositorio:
- En el folder “.devcontainer” se encuentran las configuraciones necesarias para hacer de este proyecto reproducible, consistente y fácil de compartir, de esto se hablara mas adelante.
- En el folder data están los recursos descargados y los archivos generados al procesar estos recursos, en formato long y wide.
- Finalmente en el folder scripts, como su nombre lo indica esta el código que da solución a los requerimientos del problema.
- Cabe destacar que existe un documento de requerimientos “requirements.txt” que será usado para crear el contenedor con todo lo necesario para correr los scripts de la solución.

### Entorno de desarrollo
Para tener una solución exitosa se usó un “Developer container” o “Dev Container”, una herramienta que asegura consistencia reproducibilidad y facilita la colaboración. Los Dev containers son una forma de usar Docker para crear ambientes de desarrollo contenidos en un solo espacio de trabajo organizado y colaborativo, con el cual tenemos las siguientes ventajas:
- Consistencia: Estos contenedores aseguran que todos los desarrolladores trabajan con el mismo ambiente sin importar sus configuraciones locales, reduciendo problemas de compatibilidad.
- Aislamiento: Estos contenedores están encapsulados y aislados del sistema principal y de otros contenedores, por lo que los cambios hechos en el contenedor de un proyecto no afectan a los demás proyectos, es decir que se pueden tener diferentes bibliotecas, aplicaciones y herramientas en cada contenedor.
- Reproducibilidad: Se facilita reproducir el ambiente de trabajo en diferentes máquinas y tener distintas etapas de desarrollo.

Este contenedor es muy fácil e intuitivo de usar desde visual studio code, pues basta con clonar el repositorio allí y automáticamente una ventana pregunta si se desea abrir el repositorio usando el contenedor, los únicos requisitos además de tener visual studio code, es tener instalado Docker y la extensión “Dev containers” para visual studio.

### Solucion
Para mas detalles de la solucion se puede revisar la documentacion:
- [Solución a la Prueba - 2024-1](https://github.com/JesusGonzalezMX/prueba_2024_1_solucion/blob/main/docs/documentacion.pdf).
Las visualizaciones generadas estan tambien en esta carpeta:
- [visualizacion · Streamlit](https://github.com/JesusGonzalezMX/prueba_2024_1_solucion/blob/main/docs/visualizacion.pdf).


