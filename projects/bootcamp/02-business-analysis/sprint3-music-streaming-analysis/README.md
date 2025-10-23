#  Sprint 3 - Análisis de Hábitos de Escucha de Música Online (Springfield vs. Shelbyville).

## Objetivo del proyecto

Explorar y procesar información sobre los hábitos de escucha de los usuarios y las usuarias en dos ciudades: Springfield y Shelbyville.

## Etapas Clave

### Etapa 1: Descripción de los datos.

Anotar observaciones de los datos entregados.

### Etapa 2:  Preprocesamiento de datos.

En esta etapa se limpian los datos examinados: los nombres de columnas, valores duplicados y ausentes.

### Etapa 3:  Análisis.

En esta etapa se analiza si la actividad de los usuarios y las usuarias presenta variaciones según el día de la semana y la ciudad.

## Cómo Ejecutar el Proyecto

Sigue estos pasos para clonar el repositorio, configurar tu entorno de desarrollo y ejecutar el análisis

1. Clonar el Repositorio. 

Abre tu terminal (o PowerShell) y usa git para descargar el proyecto en tu máquina local

```bash
git clone https://github.com/tu_usuario/music-streaming-analysis.git
cd music-streaming-analysis/
```
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
3. Ejecuta el notebook principal:
```bash
jupyter notebook notebooks/analisis_store1.ipynb
```


2. Crear un Entorno Virtual (Recomendado)Es crucial usar un entorno virtual para aislar las dependencias del proyecto de tu instalación global de Python.A. Crear el EntornoBash# Crea un entorno virtual llamado 'venv'
python -m venv venv
B. Activar el EntornoSistema OperativoComando de ActivaciónWindows (PowerShell).\venv\Scripts\Activate.ps1Windows (CMD).\venv\Scripts\activate.batLinux/macOSsource venv/bin/activate(Verás (venv) aparecer al inicio de tu línea de comandos, indicando que el entorno está activo.)3. Instalar DependenciasCon el entorno virtual activado, instala todas las bibliotecas de Python necesarias para el proyecto utilizando el archivo requirements.txt:Bashpip install -r requirements.txt
4. Ejecutar el AnálisisUna vez instaladas las dependencias, puedes iniciar Jupyter Lab o Jupyter Notebook para abrir y ejecutar el análisis:Bash# Inicia Jupyter Lab
jupyter lab

# O inicia Jupyter Notebook
# jupyter notebook
Navega a la carpeta notebooks/ y abre el archivo sprint_3_analisis_musica.ipynb para revisar y ejecutar el análisis.5. Desactivar el EntornoCuando termines tu sesión de trabajo, desactiva el entorno virtual:Bashdeactivate

## Fuente de Datos

Los datos se almacenan en el archivo music_project_en.csv

Descripción de las columnas:

- `usuario_id`: identifica de forma exclusiva a cada usuario o usuaria.
- `Track`:título de la canción
- `artist`:nombre del artista
- `genre`: género musical
- `City`: género musical
- `genre`: ciudad del usuario o la usuaria
- `City`: hora del día en la que se reprodujo
- `time`: hora del día en la que se reprodujo la pista (HH:MM:SS)
- `Day`: día de la semana.



