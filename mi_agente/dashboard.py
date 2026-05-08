import streamlit as st
import pandas as pd
import plotly.express as px

#-------------Configuracion de la pagina-------------
st.set_page_config(
    page_title = "Music Analytics Dashboard",
    page_icon = "🎵",
    layout = "wide"
)

#-------------Cargar Datos-------------
@st.cache_data

def cargar_datos():
    df = pd.read_csv("music_project_en_limpio.csv")
    df["hora"] = df["time"].split(':',, expand=True)[0].astype(int)
    def asignar_franja_horaria(hora):
        if df["hora"] <= 11: return 'Morning'
        elif df['hora'] <= 6: return 'Afternoon'
        else:  return 'Night'
    df['franja'] = df['hora'].apply(asignar_franja_horaria)
    return df
        
df = cargar_datos()
orden_dias = ['Monday', 'Wednesday', 'Friday']
orden_franja = ['Morning','Afternoon','Night']

#-------------SIDERBAR-------------
with st.sidebar:
    st.title("🎛️ Filtros")
    st.divider()
    ciudad_filtro = st.multiselect("🏙️ Ciudad", option=sorted(df['city'].unique()))
    dia_filtro = st.multiselect("📅 Día", option=orden_dias,default=orden_dias)
    franja_filtro = st.multiselect("🕐 Franja", option=orden_franja,default=orden_franja)
    st.divider()
    st.caption("🎵 Springfield vs Shelbyville\nHábitos de escucha musical")

df_f = df[df[df['city'].isin(ciudad_filtro) & df['day'].isin(dia_filtro) & df['franja'].isin(franja_filtro)]].copy()

#-------------Titulo-------------
st.title("🎵 Music Analytics Dashboard")
st.caption("Springfield vs Shelbyville — Hábitos de escucha")
st.divider()

#-------------KPIs-------------
col1, col2, col3,col4 =  st.columns(4)

with col1:
   st.metric("🎵 Total reproducciones", f"{len(df_f):,}") 
    
with col2:
    st.metric("🏙️ Ciudad más activa", df['city'].mode()[0] if len(df_f) > 0 else "—")

with col3:
    st.metric("🎸 Género más escuchado", df['genre'].mode()[0] if len(df_f) > 0 else "—")

with col4:
    st.metric("🎤 Artista top", df['artist'].mode()[0] if len(df_f) > 0 else "—")

st.divider()

#-------------Tabs-------------
tab1, tab2, tab3, tab4= st.tabs(["📊 Géneros","🔥 Heatmap horario", "📅 Actividad por día", "🏙️ Comparativa ciudades"])

#-------------TAB 1 -------------
with tab1:
    st.subheader("Top géneros  por ciudad")
    
    conteo = df_f['genre'].value_counts().head(10)
    top_generos = pd.DataFrame({
        'genre':          conteo.index,
        'reproducciones': conteo.values
    })
    
    fig1 = px.bar(
        top_generos,
        x   =   'reproducciones',
        y   =   'genre',
        orientation = 'h',
        color = 'reproducciones',
        color_continuous_scale = 'Viridis',
        title = f"Top 10 géneros"        
    )
    
    fig1.update_layout(yaxis={'categoryorder':'total ascending'}, height=420)
    st.plotly_chart(fig1, use_container_width=True)

#-------------TAB 2 -------------
with tab2:
    st.subheader("¿A qué hora escucha música cada ciudad?")
    col_a, col_b = st.columns(2)
    for ciudad_nombre, col in zip(['Springfield','Shelbyville'],[col_a, col_b]):
        with col:
            pivot = df_f[df_f['city']==ciudad_nombre].groupby(['hora','day']).size().reset_index(name='reproducciones')
            fig_h = px.density_heatmap(pivot, x='day', y='hora', z='reproducciones', 
                                       category_orders={'day': orden_dias}, 
                                       color_continuous_scale='Viridis',
                                       title=f"🏙️ {ciudad_nombre}", nbinsy=24
                                    )
            fig_h.update_layout(height=450)
            st.plotly_chart(fig_h, use_container_width=True)
            st.divider()
            st.subheader("Distribución por franja horaria")
            franja_ciudad = df_f.groupby(['franja','city']).size().reset_index(name='reproducciones')

with tab3:
    st.subheader("Reproducciones por día de la semana")
    
    orden_dias =  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    actividad_dia = (df.groupby(['day','city'])
                     .size()
                     .reset_index(name='reproducciones')
                     )
    
   
    fig2 = px.bar(
        actividad_dia,
        x   =   'day',
        y   =   'reproducciones',
        color = 'city',
        barmode   = 'group',
        category_orders = {'day': orden_dias},
        title     = "Actividad por día — Springfield vs Shelbyville",
         color_discrete_map = {'Springfield': '#7C3AED', 'Shelbyville': '#2563EB'}       
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # ── TAB 3: Comparativa ciudades ───────────────────────────
with tab3:
    st.subheader("¿Qué escucha cada ciudad?")
 
    col_a, col_b = st.columns(2)
 
    for ciudad_nombre, col in zip(['Springfield', 'Shelbyville'], [col_a, col_b]):
        with col:
            st.markdown(f"### 🏙️ {ciudad_nombre}")
            top = (df[df['city'] == ciudad_nombre]['genre']
                   .value_counts()
                   .head(5)
                   .reset_index())
            top.columns = ['género', 'reproducciones']
 
            fig = px.pie(
                top,
                names  = 'género',
                values = 'reproducciones',
                title  = f"Top 5 géneros",
                hole   = 0.4
            )
            st.plotly_chart(fig, use_container_width=True)