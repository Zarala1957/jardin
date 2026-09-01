import streamlit as st
import urllib.parse

st.set_page_config(page_title="Asistente Multidiagnóstico para Jardinería", page_icon="🌱", layout="wide")

st.title("🌱 Asistente Multidiagnóstico para Jardinería")
st.write("Selecciona **todos los síntomas** que observes en la planta. Esta app permite identificar múltiples problemas simultáneos.")

# Función limpia y corregida para abrir Google Imágenes en pestaña nueva sin fallos
def boton_consulta_directa(diagnostico_txt):
    termino_busqueda = f"{diagnostico_txt} plantas sintomas tratamiento"
    url_codificada = urllib.parse.quote(termino_busqueda)
    # Dirección oficial corregida con /search?q=
    enlace_google = f"https://google.com{url_codificada}&tbm=isch"
    
    # Botón nativo oficial de Streamlit (abre en pestaña nueva automáticamente)
    st.link_button("🔍 Ver Fotos y Tratamiento", enlace_google, type="primary")

# Estructura visual en 3 columnas en paralelo
col1, col2, col3 = st.columns(3)

diagnosticos_detectados = {}

# ==================== COLUMNA 1: SÍNTOMAS EN HOJAS ====================
with col1:
    st.header("🍃 Síntomas en Hojas")
    
    if st.checkbox("Las hojas nuevas están deformadas y hay moho oscuro/polvoriento"):
        diagnosticos_detectados["PULGÓN"] = "Pulgon"
    elif st.checkbox("Las hojas nuevas están deformadas (sin moho oscuro)"):
        diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "Capsido verde comun"
        
    if st.checkbox("Tiene agujeros en los bordes"):
        diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "Capsido verde comun"
    if st.checkbox("Tiene agujeros regulares en forma semicircular"):
        diagnosticos_detectados["ABEJA ASERRADORA"] = "Abeja aserradora hojas"
    if st.checkbox("Tiene agujeros grandes e irregulares con rastro plateado"):
        diagnosticos_detectados["BABOSAS / CARACOLES / LIMACOS"] = "Limacos"
    if st.checkbox("Tiene agujeros grandes e irregulares (sin rastro plateado)"):
        diagnosticos_detectados["GORGOJOS ADULTOS"] = "Gorgojos adultos"
    if st.checkbox("Tiene agujeros por toda la hoja (o defoliación masiva)"):
        diagnosticos_detectados["ORUGAS (Ej. Oruga asiática)"] = "Orugas hojas"

    if st.checkbox("Hay agujeros con el borde marrón"):
        diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "Capsido verde comun"
    if st.checkbox("Hay pequeños insectos y puestas de huevos diminutos"):
        diagnosticos_detectados["ARAÑA ROJA"] = "Araña roja"
    if st.checkbox("Hay manchas blancas y aterciopeladas"):
        diagnosticos_detectados["MILDIU PULVERULENTO / OÍDIO"] = "Mildiu pulverulento"
    if st.checkbox("Hay manchas o parches moteados con brotes atrofiados"):
        diagnosticos_detectados["VIROSIS VEGETAL"] = "Virus de las plantas"
    if st.checkbox("Las hojas jaspeadas se vuelven marrones"):
        diagnosticos_detectados["FALTA DE LUZ NATURAL (Zona de umbría)"] = "Falta de luz"
    if st.checkbox("La planta ya no florece"):
        diagnosticos_detectados["CARENCIA DE POTASIO (K)"] = "Falta de potasio"

# ==================== COLUMNA 2: SÍNTOMAS EN TALLOS ====================
with col2:
    st.header("🪵 Síntomas en Tallos")
    
    if st.checkbox("Los tallos se marchitan y caen"):
        diagnosticos_detectados["LARVAS DE GORGOJO"] = "Larvas de gorgojo"
    if st.checkbox("Los tallos y hojas parecen 'quemados' y totalmente muertos"):
        diagnosticos_detectados["PODREDUMBRE APICAL / FITOTOXICIDAD"] = "Podredumbre apical"
    if st.checkbox("Los tallos/hojas están dañados/quemados pero la planta sobrevive"):
        diagnosticos_detectados["QUEMADURA DE LAS HOJAS"] = "Quemadura de las hojas"
    if st.checkbox("Hay moho negro y polvoriento en los tallos"):
        diagnosticos_detectados["COCHINILLA"] = "Cochinilla"
    if st.checkbox("Hay moho gris y aterciopelado en los tallos"):
        diagnosticos_detectados["BOTRITIS"] = "Botritis"
    if st.checkbox("Hay gotas de líquido marrón en los tallos"):
        diagnosticos_detectados["COCHINILLA"] = "Cochinilla"

# ==================== COLUMNA 3: PROBLEMAS DE CULTIVO ====================
with col3:
    st.header("🧪 Problemas de Cultivo")
    
    if st.checkbox("Las hojas se vuelven marrones sólo por la punta"):
        diagnosticos_detectados["EXCESO DE ABONO / LIMITACIÓN DE ESPACIO"] = "Exceso de abono"
    if st.checkbox("Las hojas se vuelven marrones por los bordes"):
        diagnosticos_detectados["QUEMADURA POR EL VIENTO"] = "Quemadura por viento"
    if st.checkbox("Las hojas son pálidas y demasiado pequeñas (generalizado)"):
        diagnosticos_detectados["TIERRA ESTÉRIL / CARENCIA DE NITRÓGENO (N)"] = "Falta de nitrogeno"
    if st.checkbox("Las hojas amarillean pero los nervios siguen verdes"):
        diagnosticos_detectados["SUELO ALCALINO / CLOROSIS FÉRRICA"] = "Clorosis ferrica"
    if st.checkbox("El suelo está visiblemente anegado o hay podredumbre radicular"):
        diagnosticos_detectados["EXCESO DE AGUA / TERRENO ANEGADO"] = "Podredumbre exceso agua"
    if st.checkbox("Hojas secas, crujientes o marchitamiento por falta de agua"):
        diagnosticos_detectados["AUSENCIA DE RIEGO"] = "Falta de riego"
    if st.checkbox("Hojas con caídas y amarilleamiento natural (hojas viejas)"):
        diagnosticos_detectados["DESHOJE NATURAL"] = "Deshoje natural"
    if st.checkbox("La planta ha perdido todas las hojas de golpe tras un cambio"):
        diagnosticos_detectados["PLANTA ESTRESADA"] = "Planta estresada"

# ==================== PANEL DE RESULTADOS SIMULTÁNEOS ====================
st.markdown("---")
st.subheader("📋 Panel de Diagnósticos Encontrados")

if diagnosticos_detectados:
    st.success(f"Se han detectado **{len(diagnosticos_detectados)} problema(s)** simultáneos en la planta:")
    
    for nombre_problema, termino_busqueda in diagnosticos_detectados.items():
        col_diag, col_bot = st.columns()
        with col_diag:
            st.warning(f"🚨 **{nombre_problema}**")
        with col_bot:
            boton_consulta_directa(termino_busqueda)
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
