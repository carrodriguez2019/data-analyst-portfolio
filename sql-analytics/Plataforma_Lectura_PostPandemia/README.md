<p align="center">
  <img src="Banner.svg" alt="Banner del proyecto" width="100%" style="display: block; margin: 0 auto;">
</p>

<h1 align="center">📚 Análisis SQL: Plataforma de Lectura Post‑Pandemia</h1>

<p align="center">
  <img src="https://img.shields.io/badge/SQL-PostgreSQL-blue">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
  <img src="https://img.shields.io/badge/Focus-Database%20Analysis-critical">
  <img src="https://img.shields.io/badge/Method-Joins%20%7C%20Subqueries%20%7C%20Aggregations-orange">
</p>

---

La pandemia transformó los hábitos de consumo cultural: más personas se quedaron en casa leyendo libros, atrayendo la atención de startups que se apresuraron a desarrollar aplicaciones para los amantes de la lectura. Este proyecto analiza la base de datos de uno de esos servicios —que contiene libros, autores, editoriales, calificaciones y reseñas— para fundamentar la propuesta de valor de un nuevo producto digital.

---

## 🎯 Objetivo

Extraer insights accionables de la base de datos del servicio de lectura para:

- Cuantificar el **volumen de contenido reciente** disponible para recomendar.
- Analizar la relación entre **popularidad y satisfacción** de los libros.
- Identificar **editoriales y autores estratégicos** para alianzas comerciales.
- Detectar **segmentos de usuarios de alto valor** que generan contenido cualitativo.

---

## 📋 Especificación Técnica

| Parámetro | Detalle |
|-----------|---------|
| Motor de base de datos | PostgreSQL (Yandex Cloud) |
| Conexión | SQLAlchemy + psycopg2 (SSL) |
| Lenguaje de análisis | SQL (consultas) + Python (presentación) |
| Tablas analizadas | 5 (`books`, `authors`, `publishers`, `ratings`, `reviews`) |
| Registros totales | 1.000 libros · 636 autores · 340 editoriales · 6.456 ratings · 2.793 reseñas |

---

## 📊 Dataset

Cinco tablas relacionadas con datos del servicio de lectura:

- **`books`**: catálogo de libros (`book_id`, `author_id`, `title`, `num_pages`, `publication_date`, `publisher_id`).
- **`authors`**: autores y autoras (`author_id`, `author`).
- **`publishers`**: editoriales (`publisher_id`, `publisher`).
- **`ratings`**: calificaciones de usuarios (`rating_id`, `book_id`, `username`, `rating`).
- **`reviews`**: reseñas en texto de usuarios (`review_id`, `book_id`, `username`, `text`).

> Nota: Datos provistos para fines educativos (Practicum / TripleTen).

### Diagrama de la base de datos

<p align="center">
  <img src="BD.png" alt="Esquema relacional de las tablas" width="70%">
</p>

---

## 🧩 Planificación y Ejecución del Proyecto

Metodología: Conexión a la base → Exploración inicial de tablas → Diseño de consultas SQL → Ejecución y validación → Interpretación de resultados → Conclusiones de producto.

Flujo: **Conexión PostgreSQL → EDA de tablas → 5 consultas SQL (JOIN, subqueries, agregaciones, HAVING) → Insights de negocio → Recomendaciones**

📓 Notebook:
- [Notebook: Análisis SQL completo](Proyecto%20SQL.ipynb)

---

## 🔍 Hallazgos clave

1. **Catálogo actualizado**: 819 de 1.000 libros (≈82%) fueron publicados después del 1 de enero de 2000, garantizando contenido contemporáneo para recomendar.
2. **Popularidad ≠ satisfacción**: el libro más reseñado (*Twilight*, 7 reseñas) tiene una calificación moderada (3,66), mientras que el mejor valorado (*Misty of Chincoteague*, 5,00) tiene pocas reseñas.
3. **Penguin Books domina el catálogo extenso**: 42 títulos con más de 50 páginas, posicionándose como la editorial líder y candidata a alianzas estratégicas.
4. **J.K. Rowling/Mary GrandPré lidera en satisfacción**: calificación promedio de 4,29 entre libros con al menos 50 calificaciones.
5. **Usuarios super activos generan más contenido cualitativo**: quienes han calificado más de 50 libros escriben en promedio 24,33 reseñas (1,4× la media de 17,46).

---

## 📈 Resultados de las consultas

| # | Tarea | Resultado |
|---|-------|-----------|
| 1 | Libros publicados después del 01/01/2000 | **819 libros** |
| 2 | Libro con más reseñas / mejor calificación | *Twilight* (7 reseñas) · *Misty of Chincoteague* (5,00) |
| 3 | Editorial líder en libros >50 páginas | **Penguin Books** (42 títulos) |
| 4 | Autor mejor calificado (≥50 ratings) | **J.K. Rowling/Mary GrandPré** (4,29) |
| 5 | Promedio de reseñas en usuarios activos (>50 ratings) | **24,33 reseñas** vs. 17,46 (media) |

---

## 💡 Recomendaciones para el producto

- **Dashboard de descubrimiento dual**: pestañas "Más comentados" y "Mejor valorados" para que el usuario explore por popularidad o por satisfacción.
- **Métrica híbrida "Top Trending"**: combinar volumen de reseñas y rating promedio para priorizar títulos con tracción real.
- **Alianza estratégica con Penguin Books**: negociar una sección destacada o acceso anticipado a novedades a cambio de visibilidad en la app.
- **Colección "Lecturas imprescindibles"**: curar autores con calificaciones promedio altas (como J.K. Rowling) y usarlos como gancho en campañas de suscripción.
- **Programa "Crítico Élite"**: gamificar a los usuarios con más de 50 calificaciones (insignias, acceso beta, descuentos) para fidelizar a la fuente principal de contenido generado por el usuario.

---

## 🧰 Tecnologías Utilizadas

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)](https://www.postgresql.org/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)](https://www.sqlalchemy.org/)
[![Pandas](https://img.shields.io/badge/pandas-2.0.3-blue.svg)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg)](https://jupyter.org/)

---

## 👩‍💻 Autor

**Carolina Rodríguez Guerra**
