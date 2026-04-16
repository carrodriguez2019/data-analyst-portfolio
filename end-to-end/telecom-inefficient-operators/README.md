<p align="center">  
  <img src="images/callme_banner.png" alt="Banner del proyecto" width="50%" style="display: block; margin: 0 auto;">
</p>

<h1 align="center">📞 Telecom Analytics: Identificación de Operadores Ineficientes</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Data%20Analysis-blue">  
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
  <img src="https://img.shields.io/badge/Focus-Business%20Impact-critical">
</p>

---

**CallMeMaybe** (telefonía virtual) necesitaba detectar operadores con bajo desempeño para reducir llamadas perdidas y tiempos de espera.

---

## 🎯 Objetivo
Identificar operadores ineficientes mediante métricas operativas (tasa de pérdida, tiempo de espera, volumen saliente) y proponer mejoras.

---

## 📊 Dataset
Dos tablas simuladas con **1.092 operadores** y **50k+ registros**:
- `telecom_dataset_us.csv`: llamadas (entrantes/salientes/internas), duración, llamadas perdidas, operador.
- `telecom_clients_us.csv`: clientes, plan tarifario, fecha registro.

> Nota: Datos simulados para fines educativos.
---

## 🧩 Planificación y Ejecución del Proyecto
Metodología: Limpieza → EDA → Ingeniería de variables → KPIs → Validación estadística.  
Flujo: **EDA → Hipótesis → Validación → Insights**  
📓 Notebooks: [`01_task_breakdown.ipynb`](../notebooks/01_task_breakdown.ipynb) · [`02_implementation.ipynb`](/notebooks/02_implementation.ipynb)

---

## 🔍 Hallazgos clave
1. **El problema principal no es la atención entrante** (tasa pérdida media <2%), sino la **baja productividad saliente** (18% de operadores hacen <11 llamadas out en todo el período).
2. **19% de operadores** tienen alta tasa de pérdida (>10%) o alto tiempo de espera (>60s).  
3. Solo **3 casos críticos** combinan mala atención y baja productividad.

---

## 📈 Clasificación final

<p align="center">
  <img src="images/imagen_barras_clasificacion.png" alt="Distribución de operadores según clasificación integral" width="80%">
</p>

| Tipo | % |
|------|---|
| Eficiente | 63% |
| Mejorar atención | 19% |
| Mejorar productividad | 18% |
| Crítico | <1% |

## 🔍 Top 20 operadores con mayor tasa de pérdida (atención prioritaria)

<p align="center">
  <img src="images/top20_perdida.png" alt="Top 20 operadores con mayor tasa de pérdida entrante" width="80%">
</p>

---

## 💡 Recomendaciones
- Capacitación en gestión de espera para el 19% con problemas de atención.
- Metas semanales de llamadas salientes para el 18% con baja productividad.
- Intervención personalizada para los 3 casos críticos.

---

## 🧰 Tecnologías Utilizadas

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/pandas-2.0.3-blue.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/numpy-1.24.3-blue.svg)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/scipy-1.10.1-blue.svg)](https://scipy.org/)
[![Matplotlib](https://img.shields.io/badge/matplotlib-3.7.2-blue.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/seaborn-0.12.2-blue.svg)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg)](https://jupyter.org/)

---

## 👩‍💻 Autor
**Carolina Rodríguez Guerra** 

