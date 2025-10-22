#  Proyecto Store 1 - Programa de Fidelización.

## Contexto del Negocio
Store 1, empresa de comercio electrónico.

## Descripción del Proyecto

Análisis y preparación de datos de clientes para el nuevo Programa de Fidelización de Store 1. Este proyecto se enfoca en la limpieza, estandarización y preparación de datos para futuras campañas de marketing personalizadas.

## Objetivos

-  **Limpieza de Datos**: Estandarizar nombres, edades y categorías.
- **Cálculo de Métricas**: Gasto total por cliente.
- **Validación**: Asegurar consistencia y calidad de datos.
=======
- **Cálculo de Métricas**: Gasto total por cliente
- **Validación**: Asegurar consistencia y calidad de datos.
>>>>>>> f713a8fcf23e1c43174545b9562f69fdff519aa

## Datos

El dataset contiene información de clientes con las siguientes columnas:
- `usuario_id`: Identificador único
- `usuario_nombre`: Nombre del usuario
- `usuario_edad`: Edad del usuario
- `categorias_fav_low`: Categorías favoritas de productos
- `gasto_por_categoria`: Gasto por cada usuario.

## Proceso de Análisis
1. Limpieza de Datos
- Nombres: Estandarización de formato 
- Edades: Validación y corrección de valores atípicos
- Categorías: Normalización de nombres y formatos

2. Transformación
- Gasto Total: Suma del gasto por categorías

## Resultados y Hallazgos
Los datos han sido procesados y están listos para:

- Segmentación de clientes
- Análisis de comportamiento de compra
- Diseño de campañas de marketing personalizadas

## Tecnologías Utilizadas
- Python 3.12.10
- Jupyter Notebook
- Visual Studio Code

## Instalación  y Uso
1. Clona el repositorio
```bash
git clone projects/bootcamp/01-data-cleaning/sprint1-store1-fidelizacion
```
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
3. Ejecuta el notebook principal:
```bash
jupyter notebook notebooks/analisis_store1.ipynb
```

## Estructura del Proyecto

<img width="430" height="399" alt="image" src="https://github.com/user-attachments/assets/24654498-0e93-47ae-8bd6-24a8d4cc96bb" />


## Habilidades Demostradas
- Limpieza de Datos: Pandas, transformaciones de texto
- Python: Programación orientada a análisis

## Autor
Carolina Rodríguez Guerra - Análisis de datos para Store 1

## Licencia
Este proyecto es parte del programa de formación en análisis de datos.

## Información Adicional
- Bootcamp: Análisis de Datos (Tripleten)
- Sprint: 1
- Fecha: 23 de Junio de 2025
- Estado: Completado

