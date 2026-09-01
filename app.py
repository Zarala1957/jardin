import streamlit as st

st.set_page_config(page_title="Asistente Multidiagnóstico para Jardinería", page_icon="🌱", layout="wide")

st.title("🌱 Asistente Multidiagnóstico para Jardinería")
st.write("Selecciona **todos los síntomas** que observes en la planta. Esta app identifica múltiples problemas simultáneos y muestra fotos de referencia.")

# Base de datos corregida con enlaces estables de servidores botánicos y agronómicos abiertos
FOTOS_REFERENCIA = {
    "PULGÓN": "https://unsplash.com",
    "CÁPSIDO VERDE COMÚN": "https://wikimedia.org", # Servidor libre alternativo
    "ABEJA ASERRADORA": "https://unsplash.com",
    "BABOSAS / CARACOLES / LIMACOS": "https://unsplash.com",
    "GORGOJOS ADULTOS": "https://unsplash.com",
    "ORUGAS (Ej. Oruga asiática)": "https://unsplash.com",
    "ARAÑA ROJA": "https://unsplash.com",
    "MILDIU PULVERULENTO / OÍDIO": "https://unsplash.com",
    "BOTRITIS": "https://unsplash.com",
    "COCHINILLA": "https://unsplash.com",
    "VIROSIS VEGETAL": "https://unsplash.com",
    "SUELO ALCALINO / CLOROSIS FÉRRICA": "https://unsplash.com",
    "TIERRA ESTÉRIL / CARENCIA DE NITRÓGENO (N)": "https://unsplash.com",
    "CARENCIA DE POTASIO (K)": "https://unsplash.com"
}

# Estructura visual en 3 columnas en paralelo
col1, col2, col3 = st.columns(3)

diagnosticos_detectados = {}

# ==================== COLUMNA 1: SÍNTOMAS EN HOJAS ====================
with col1:
    st.header("🍃 Síntomas en Hojas")
    
    if st.checkbox("Las hojas nuevas están deformadas y hay moho oscuro/polvoriento"):
        diagnosticos_detectados["PULGÓN"] = "PULGÓN"
    elif st.checkbox("Las hojas nuevas están deformadas (sin moho oscuro)"):
        diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "CÁPSIDO VERDE COMÚN"
        
    if st.checkbox("Tiene agujeros en los bordes"):
        diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "CÁPSIDO VERDE COMÚN"
    if st.checkbox("Tiene agujeros regulares en forma semicircular"):
        diagnosticos_detectados["ABEJA ASERRADORA"] = "ABEJA ASERRADORA"
    if st.checkbox("Tiene agujeros grandes e irregulares con rastro plateado"):
        diagnosticos_detectados["BABOSAS / CARACOLES / LIMACOS"] = "BABOSAS / CARACOLES / LIMACOS"
    if st.checkbox("Tiene agujeros grandes e irregulares (sin rastro plateado)"):
        diagnosticos_detectados["GORGOJOS ADULTOS"] = "GORGOJOS ADULTOS"
    if st.checkbox("Tiene agujeros por toda la hoja (o defoliación masiva)"):
        diagnosticos_detectados["ORUGAS (Ej. Oruga asiática)"] = "ORUGAS (Ej. Oruga asiática)"

    if st.checkbox("Hay agujeros con el borde marrón"):
        diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "CÁPSIDO VERDE COMÚN"
    if st.checkbox("Hay pequeños insectos y puestas de huevos diminutos"):
        diagnosticos_detectados["ARAÑA ROJA"] = "ARAÑA ROJA"
    if st.checkbox("Hay manchas blancas y aterciopeladas"):
        diagnosticos_detectados["MILDIU PULVERULENTO / OÍDIO"] = "MILDIU PULVERULENTO / OÍDIO"
    if st.checkbox("Hay manchas o parches moteados con brotes atrofiados"):
        diagnosticos_detectados["VIROSIS VEGETAL"] = "VIROSIS VEGETAL"
    if st.checkbox("La planta ya no florece"):
        diagnosticos_detectados["CARENCIA DE POTASIO (K)"] = "CARENCIA DE POTASIO (K)"

# ==================== COLUMNA 2: SÍNTOMAS EN TALLOS ====================
with col2:
    st.header("🪵 Síntomas en Tallos")
    
    if st.checkbox("Los tallos se marchitan y caen"):
        diagnosticos_detectados["LARVAS DE GORGOJO"] = "GORGOJOS ADULTOS"
    if st.checkbox("Hay moho negro y polvoriento en los tallos"):
        diagnosticos_detectados["COCHINILLA"] = "COCHINILLA"
    if st.checkbox("Hay moho gris y aterciopelado en los tallos"):
        diagnosticos_detectados["BOTRITIS"] = "BOTRITIS"
    if st.checkbox("Hay gotas de líquido marrón en los tallos"):
        diagnosticos_detectados["COCHINILLA"] = "COCHINILLA"

# ==================== COLUMNA 3: PROBLEMAS DE CULTIVO ====================
with col3:
    st.header("🧪 Problemas de Cultivo")
    
    if st.checkbox("Las hojas se vuelven marrones sólo por la punta"):
        diagnosticos_detectados["EXCESO DE ABONO / LIMITACIÓN DE ESPACIO"] = "EXCESO DE ABONO / LIMITACIÓN DE ESPACIO"
    if st.checkbox("Las hojas son pálidas y demasiado pequeñas (generalizado)"):
        diagnosticos_detectados["TIERRA ESTÉRIL / CARENCIA DE NITRÓGENO (N)"] = "TIERRA ESTÉRIL / CARENCIA DE NITRÓGENO (N)"
    if st.checkbox("Las hojas amarillean pero los nervios siguen verdes"):
        diagnosticos_detectados["SUELO ALCALINO / CLOROSIS FÉRRICA"] = "SUELO ALCALINO / CLOROSIS FÉRRICA"

# ==================== PANEL DE RESULTADOS EN VIVO ====================
st.markdown("---")
st.subheader("📋 Panel de Diagnósticos Encontrados")

if diagnosticos_detectados:
    st.success(f"Se han detectado **{len(diagnosticos_detectados)} problema(s)** simultáneos en la planta:")
    
    for nombre_problema, clave_foto in diagnosticos_detectados.items():
        st.warning(f"🚨 **{nombre_problema}**")
        
        # Carga la imagen de forma nativa desde servidores abiertos estables
        if clave_foto in FOTOS_REFERENCIA:
            st.image(FOTOS_REFERENCIA[clave_foto], caption=f"Imagen de referencia para {nombre_problema}", width=500)
        else:
            st.info("Utilice su cuaderno de campo para contrastar las muestras físicas.")
        st.markdown("") 
else:
    st.info("No se ha marcado ningún síntoma. Revisa la planta y marca las casillas correspondientes.")

# ==================== PIE DE PÁGINA COMERCIAL Y LEGAL ====================
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666666; font-size: 14px; padding: 20px;">
        <p>📋 <b>Módulo Formativo MF0525_2: Control Fitosanitario</b></p>
        <p>© 2024 - 2026 Asistente de Diagnóstico Fitosanitario Avanzado. Todos los derechos reservados.</p>
        <p><i>Desarrollado de forma privada para Prácticas de Identificación de Problemas en las Plantas.</i></p>
    </div>
    """, 
    unsafe_allow_html=True
)
