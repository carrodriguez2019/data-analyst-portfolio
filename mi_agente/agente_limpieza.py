# ============================================================
# AGENTE DE LIMPIEZA DE DATOS — con LLM (Groq)
# Construido paso a paso: Pandas/notebooks → Agentes IA
# ============================================================

import pandas as pd
import json
from groq import Groq

# ── 1. HERRAMIENTAS (las manos del agente) ───────────────────

def inspect_dataframe(df):
    """Observa el estado actual del DataFrame."""
    reporte = {}
    reporte['filas_columnas'] = df.shape
    reporte['columnas']       = df.columns.tolist()
    reporte['nulos_%']        = df.isna().mean() * 100
    reporte['duplicados']     = df.duplicated().sum()
    return reporte

def fix_column_names(df):
    """Estandariza nombres: sin espacios, minúsculas, snake_case."""
    df.columns = (df.columns
                    .str.strip()
                    .str.lower()
                    .str.replace(' ', '_'))
    return df

def fix_nulls(df):
    """
    Regla: si nulos > 50% → imputa con moda.
           si nulos <= 50% → elimina filas.
    """
    for columna in df.columns:
        porcentaje = df[columna].isna().sum() / len(df) * 100
        if porcentaje > 50:
            df[columna] = df[columna].fillna('unknown')
        else:
            df = df.dropna(subset=[columna])
    return df

def fix_duplicates(df):
    """Elimina filas duplicadas y resetea el índice."""
    df = df.drop_duplicates().reset_index(drop=True)
    return df

# Mapa: nombre → función
TOOLS = {
    'fix_column_names': fix_column_names,
    'fix_nulls':        fix_nulls,
    'fix_duplicates':   fix_duplicates
}

# ── 2. PROMPT (lo que el LLM lee) ────────────────────────────

def build_prompt(reporte):
    return f"""
Eres un agente experto en limpieza de datos.
Analiza el siguiente reporte de un DataFrame:

- Dimensiones: {reporte['filas_columnas']}
- Columnas: {reporte['columnas']}
- Nulos por columna (%): {reporte['nulos_%'].round(2).to_dict()}
- Filas duplicadas: {reporte['duplicados']}

Tienes disponibles estas herramientas:
  - fix_column_names : limpia espacios y estandariza nombres a snake_case
  - fix_nulls        : imputa o elimina nulos según el porcentaje
  - fix_duplicates   : elimina filas duplicadas

Responde ÚNICAMENTE con una lista JSON con las herramientas a ejecutar.
Si el dataset ya está limpio, responde con una lista vacía: []

Ejemplo de respuesta:
["fix_column_names", "fix_nulls", "fix_duplicates"]
"""

# ── 3. CEREBRO (el LLM toma las decisiones) ──────────────────

def llamar_llm(prompt, api_key):
    cliente   = Groq(api_key=api_key)
    respuesta = cliente.chat.completions.create(
        model    = "llama-3.3-70b-versatile",
        messages = [{"role": "user", "content": prompt}]
    )
    return respuesta.choices[0].message.content

# ── 4. LOOP ReAct (observar → decidir → actuar → verificar) ──

def agente_limpieza(ruta_csv, api_key):
    df = pd.read_csv(ruta_csv)

    print("=" * 55)
    print("   AGENTE DE LIMPIEZA INICIADO")
    print("=" * 55)

    iteracion = 0
    while True:
        iteracion += 1
        print(f"\n── Iteración {iteracion} ──────────────────────────")

        # OBSERVAR
        print("  [1] Observando dataset...")
        reporte = inspect_dataframe(df)

        # DECIDIR
        print("  [2] Consultando al LLM...")
        prompt            = build_prompt(reporte)
        respuesta_llm     = llamar_llm(prompt, api_key)

        # Parsear JSON de la respuesta
        try:
            tools_a_ejecutar = json.loads(respuesta_llm.strip())
        except json.JSONDecodeError:
            # Si el LLM añade texto extra, extraemos el JSON
            inicio = respuesta_llm.find('[')
            fin    = respuesta_llm.rfind(']') + 1
            tools_a_ejecutar = json.loads(respuesta_llm[inicio:fin])

        print(f"  [2] LLM decidió: {tools_a_ejecutar}")

        # CONDICIÓN DE PARADA
        if not tools_a_ejecutar:
            print("\n✅ El LLM confirma que el dataset está limpio.")
            break

        # ACTUAR
        print("  [3] Ejecutando herramientas...")
        for tool_name in tools_a_ejecutar:
            print(f"      → {tool_name}")
            df = TOOLS[tool_name](df)

        # VERIFICAR
        reporte_post  = inspect_dataframe(df)
        nulos_totales = reporte_post['nulos_%'].sum()
        duplicados    = reporte_post['duplicados']

        print(f"  [4] Verificando...")
        print(f"      Nulos restantes  : {nulos_totales:.2f}%")
        print(f"      Duplicados       : {duplicados}")
        print(f"      Filas actuales   : {reporte_post['filas_columnas']}")

        if nulos_totales == 0 and duplicados == 0:
            print("\n✅ Dataset limpio verificado. STOP.")
            break

    # Guardar resultado
    salida = ruta_csv.replace('.csv', '_limpio.csv')
    df.to_csv(salida, index=False)
    print(f"\n💾 Dataset guardado en: {salida}")
    print(f"   Columnas finales: {df.columns.tolist()}")
    print(f"   Dimensiones finales: {df.shape}")

    return df


# ── 5. EJECUTAR ───────────────────────────────────────────────

if __name__ == "__main__":
    API_KEY  = "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"   # ← pega tu key aquí
    RUTA_CSV = "music_project_en.csv"       # ← o cualquier otro CSV

    df_limpio = agente_limpieza(RUTA_CSV, API_KEY)
