import streamlit as st

# Ocultar menú superior, botón de GitHub y pie de página oficial de Streamlit
st.set_page_config(
    page_title="Asistente Multidiagnóstico para Jardinería", 
    page_icon="🌱", 
    layout="wide"
)

# Inyección de CSS para ajustar fuentes en móviles y ocultar la UI de Streamlit
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_container__1QS1A {display: none !important;}
    
    @media (max-width: 768px) {
        html, body, [class*="css"] {
            font-size: 14px !important;
        }
        h1 { font-size: 1.8rem !important; }
        h2 { font-size: 1.4rem !important; }
    }
    
    .nav-box {
        display: flex;
        justify-content: space-around;
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .nav-link {
        text-decoration: none;
        color: #1f77b4;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar state para controlar el reseteo de los checkboxes
if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0

def reset_all():
    st.session_state.reset_counter += 1

# Título de la aplicación
st.title("🌱 Asistente Multidiagnóstico para Jardinería")
st.write("Selecciona **todos los síntomas** que observes en la planta. Esta app identificará los problemas según las claves oficiales.")

# Enlaces de navegación interna optimizados para pantallas móviles
st.markdown("""
<div class="nav-box">
    <a class="nav-link" href="#hojas">🍃 Hojas</a>
    <a class="nav-link" href="#tallos">🪵 Tallos</a>
    <a class="nav-link" href="#cultivo">🧪 Cultivo</a>
</div>
""", unsafe_allow_html=True)

# Botón de Reset permanente en la barra superior
if st.button("🔄 Reiniciar Diagnósticos (Reset)", on_click=reset_all):
    st.rerun()

# Matriz Técnica Oficial Completa corregida
DICCIONARIO_TRATAMIENTOS = {
    "PULGÓN": "Tratamiento biológico con jabón potásico (2%) y aceite de neem. En ataques severos, emplear piretrinas naturales o fauna útil (adalia bipunctata). Eliminar brotes muy colapsados.",
    "CÁPSIDO VERDE COMÚN": "Monitorear las brotaciones. Al encontrar adultos, aplicar tratamientos al atardecer con jabón fosfórico o piretroides autorizados. Retirar malas hierbas colindantes.",
    "ABEJA ASERRADORA": "El daño suele ser puramente estético. No se recomiendan tratamientos químicos drásticos. Colocar barreras físicas o favorecer la biodiversidad para ahuyentarlas.",
    "BABOSAS / CARACOLES": "Colocar trampas de cerveza o barreras físicas de ceniza/tierra de diatomeas alrededor del tallo. En infestaciones graves, emplear cebos selectivos de fosfato férrico (ecológico).",
    "GORGOJOS ADULTOS": "Tratamiento nocturno (cuando están activos) sacudiendo las ramas sobre una manta. Aplicar nematodos entomopatógenos en el suelo para controlar las larvas si es necesario.",
    "ORUGAS": "Recogida manual en ataques iniciales. Tratamiento biológico altamente efectivo con Bacillus thuringiensis (var. kurstaki) aplicado sobre las hojas tiernas cuando la oruga es joven.",
    "ARAÑUELA ROJA": "Aumentar la humedad ambiental pulverizando agua (odian la humedad). Aplicar azufre mojable o tratamientos con aceite parafinado. En control biológico, introducir el ácaro depredador Phytoseiulus persimilis.",
    "MILDIU PULVERULENTO": "Eliminar y quemar restos afectados. Aplicar fungicidas a base de azufre, bicarbonato potásico o tratamientos preventivos con cola de caballo. Mejorar la aireación de la planta.",
    "BOTRITIS": "Reducir drásticamente la humedad foliar y el riego. Podar partes afectadas con herramientas desinfectadas. Aplicar fungicidas biológicos a base de Bacillus subtilis o cobre en casos graves.",
    "COCHINILLA": "Limpieza manual con alcohol de quemar y algodón en plantas pequeñas. En ataques generalizados, aplicar aceite de verano combinado con un insecticida sistémico autorizado (ej. deltametrina).",
    "VIRUS": "No existe tratamiento curativo. Se debe arrancar y destruir la planta afectada inmediatamente para evitar el contagio. Es fundamental controlar las plagas de pulgón o mosca blanca, que actúan como vectores.",
    "MOSCA BLANCA": "Colocar trampas cromáticas amarillas pegajosas. Tratar con jabón potásico combinado con aceite de neem. En invernaderos, introducir el parasitoide Encarsia formosa.",
    "EXCESO DE ABONO O LIMITACIÓN DE ESPACIO": "Realizar un lavado de suelo (riego abundante sin encharcar para arrastrar sales). Si la maceta se ha quedado pequeña, programar un trasplante de urgencia a un contenedor mayor.",
    "QUEMADURA DE LAS HOJAS POR EL VIENTO": "Instalar barreras cortavientos o reubicar la planta a una zona protegida. Incrementar los riegos en días de viento seco para evitar la deshidratación de los bordes.",
    "FALTA DE NITROGENO": "Aportar materia orgánica al suelo (humus de lombriz, compost o estiércol maduro). Aplicar un abonado de fondo rico en Nitrógeno (N) de liberación lenta.",
    "TIERRA ESTÉRIL": "Renovar la capa superior del sustrato. Incorporar abono orgánico completo microgranulado y bioestimulantes radiculares para reactivar la flora bacteriana del suelo.",
    "SUELO ALCALINO": "Aplicar quelatos de hierro (Fe) directamente al riego para corregir la clorosis férrica. A largo plazo, acidificar el sustrato aportando turba rubia o azufre elemental.",
    "PODREDUMBRE": "Suspender los riegos de inmediato. Mejorar el drenaje del terreno o maceta aportando perlita o arena. Si afecta a las raíces, aplicar un fungicida específico para cuello (ej. Fosetil-Al).",
    "DESHOJE NATURAL": "Proceso fisiológico normal en hojas viejas de la zona baja. No requiere acción. Mantener el mantenimiento habitual de la planta retirando las hojas secas caídas.",
    "PLANTA ESTRESADA": "Evitar mover la planta de sitio constantemente. Suspender el abono hasta que se dejen ver nuevos brotes. Mantener riegos moderados y estables sin saturar el suelo.",
    "FALTA DE LUZ NATURAL": "Trasladar la planta de forma progresiva a una ubicación con mayor exposición solar o iluminación indirecta brillante (evitar sol directo de golpe para no quemarla).",
    "FALTA DE POTASIO": "Aplicar un fertilizante rico en Potasio (K), como sulfato potásico o patasa, especialmente antes y durante la época de floración para fortalecer los tejidos y flores.",
    "LARVAS DE GORGOJO": "Aplicar nematodos entomopatógenos (Steinernema carpocapsae) al suelo mediante el riego en primavera u otoño para que parasiten las larvas que devoran las raíces.",
    "QUEMADURA DE LAS HOJAS": "Proporcionar sombreado provisional durante las horas centrales del día. Ajustar la frecuencia de riego para que la planta responda mejor a los picos de calor extremo.",
    "PODREDUMBRE APICAL": "Regular el suministro de agua para evitar fluctuaciones drásticas de humedad. Asegurar la asimilación de calcio mediante aportaciones de quelatos de calcio o enmiendas específicas.",
    "EXCESO DE AGUA": "Interrumpir el riego por completo y dejar secar el sustrato. Verificar que los agujeros de drenaje no estén obstruidos. Si es grave, extraer el cepellón y envolverlo en papel absorbente."
}

diagnosticos_detectados = {}

# Estructura en tres columnas fijas sin errores sintácticos
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div id="hojas"></div>', unsafe_allow_html=True)
    st.header("🍃 Síntomas en Hojas")
    
    if st.checkbox("Las hojas nuevas están deformadas + moho oscuro/polvoriento en hojas viejas", key=f"c1_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["PULGÓN"] = "PULGÓN"
    if st.checkbox("Las hojas nuevas están deformadas (sin moho oscuro)", key=f"c2_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "CÁPSIDO VERDE COMÚN"
    if st.checkbox("Tiene agujeros regulares en forma semicircular", key=f"c3_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["ABEJA ASERRADORA"] = "ABEJA ASERRADORA"
    if st.checkbox("Tiene agujeros grandes e irregulares con rastro plateado", key=f"c4_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["BABOSAS / CARACOLES"] = "BABOSAS / CARACOLES"
    if st.checkbox("Tiene agujeros grandes e irregulares (sin rastro plateado)", key=f"c5_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["GORGOJOS ADULTOS"] = "GORGOJOS ADULTOS"
    if st.checkbox("Tiene agujeros por toda la hoja (defoliación)", key=f"c6_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["ORUGAS"] = "ORUGAS"
    if st.checkbox("Tiene agujeros con el borde marrón", key=f"c7_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "CÁPSIDO VERDE COMÚN"
    if st.checkbox("Hojas moteadas/con manchas + pequeños insectos y puestas de huevos diminutos", key=f"c8_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["ARAÑUELA ROJA"] = "ARAÑUELA ROJA"
    if st.checkbox("Hojas moteadas/con manchas + brotes atrofiados o deformados", key=f"c9_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["VIRUS"] = "VIRUS"
    if st.checkbox("Hojas con grandes manchas + moho negro y polvoriento + hojas nuevas deformadas", key=f"c10_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["PULGÓN"] = "PULGÓN"
    if st.checkbox("Hojas con grandes manchas + moho negro y polvoriento (sin deformación)", key=f"c11_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["COCHINILLA"] = "COCHINILLA"
    if st.checkbox("Las hojas jaspeadas se vuelven marrones", key=f"c12_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["FALTA DE LUZ NATURAL"] = "FALTA DE LUZ NATURAL"
    if st.checkbox("La planta ya no florece", key=f"c13_{st.session_state.reset_counter}"): 
        diagnosticos_detectados["FALTA DE POTASIO"] = "FALTA DE POTASIO"
