#  Proyecto Store 1 - Programa de Fidelización.

## Contexto del Negocio
Store 1, empresa de comercio electrónico.

## Descripción del Proyecto

Análisis y preparación de datos de clientes para el nuevo Programa de Fidelización de Store 1. Este proyecto se enfoca en la limpieza, estandarización y preparación de datos para futuras campañas de marketing personalizadas.

## Objetivos

-  **Limpieza de Datos**: Estandarizar nombres, edades y categorías.
- **Cálculo de Métricas**: Gasto total por cliente, preferencias por categoría.
- **Validación**: Asegurar consistencia y calidad de datos.
- **Preparación para KPIs**: Estructurar datos para análisis futuro.


## Datos

El dataset contiene información de clientes con las siguientes columnas:
- `usuario_id`: Identificador único
- `usuario_nombre`: Nombre del usuario
- `usuario_edad`: Edad del usuario
- `categorias_fav_low`: Categorías favoritas de productos
- `gasto_por_categoria`: Gasto en cada categoría favorita.

## Proceso de Análisis
1. Limpieza de Datos
- Nombres: Estandarización de formato 
- Edades: Validación y corrección de valores atípicos
- Categorías: Normalización de nombres y formatos

2. Transformación
- Gasto Total: Suma del gasto por categorías
- Categoría Principal: Identificación de categoría favorita
- Segmentación: Agrupación por edad y gasto

3. KPIs Calculados
- Gasto promedio por cliente
- Distribución por grupos de edad
- Preferencias de categorías por segmento
- Clientes de alto valor identificados

## Resultados y Hallazgos
Los datos han sido procesados y están listos para:

- Segmentación de clientes
- Análisis de comportamiento de compra
- Diseño de campañas de marketing personalizadas

## Tecnologías Utilizadas
- Python 3.x
- Jupyter Notebook
- Pandas (para manipulación de datos)
- Numpy (para cálculos numéricos)

## Instalación  y Uso
1. Clona el repositorio
```bash
git clone 
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

## Habilidades Demostradas
- Limpieza de Datos: Pandas, transformaciones de texto
- Análisis Exploratorio: Estadísticas descriptivas, agrupaciones
- Visualización: Gráficos de distribución y tendencias
- Storytelling: Presentación clara de hallazgos
- Python: Programación orientada a análisis

## Autor
Carolina Rodríguez Guerra - Análisis de datos para Store 1

## Licencia
Este proyecto es parte del programa de formación en análisis de datos.

## Información Adicional
- Bootcamp: Análisis de Datos (Tripleten)
- Sprint: 1
- Fecha: 6 de Julio de 2025
- Estado: Completado

