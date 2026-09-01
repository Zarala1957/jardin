import streamlit as st

st.set_page_config(page_title="Asistente Multidiagnóstico para Jardinería", page_icon="🌱", layout="wide")

st.title("🌱 Asistente Multidiagnóstico para Jardinería")
st.write("Selecciona **todos los síntomas** que observes en la planta. Esta app identificará los problemas y te dará el tratamiento fitosanitario inmediato.")

# Matriz completa de soluciones técnicas oficiales (MF0525_2)
DICCIONARIO_TRATAMIENTOS = {
    "PULGÓN": "Tratamiento biológico con jabón potásico (2%) y aceite de neem. En ataques severos, emplear piretrinas naturales o fauna útil (adalia bipunctata). Eliminar brotes muy colapsados.",
    "CÁPSIDO VERDE COMÚN": "Monitorear las brotaciones. Encontrando adultos, aplicar tratamientos al atardecer con jabón fosfórico o piretroides autorizados. Retirar malas hierbas colindantes.",
    "ABEJA ASERRADORA": "El daño suele ser puramente estético. No se recomiendan tratamientos químicos drásticos. Colocar barreras físicas o favorecer la biodiversidad para ahuyentarlas.",
    "BABOSAS / CARACOLES": "Colocar trampas de cerveza o barreras físicas de ceniza/tierra de diatomeas alrededor del tallo. En infestaciones graves, emplear cebos selectivos de fosfato férrico (ecológico).",
    "GORGOJOS ADULTOS": "Tratamiento nocturno (cuando están activos) sacudiendo las ramas sobre una manta. Aplicar nematodos entomopatógenos en el suelo para controlar las larvas si es necesario.",
    "ORUGAS": "Recogida manual en ataques iniciales. Tratamiento biológico altamente efectivo con Bacillus thuringiensis (var. kurstaki) aplicado sobre las hojas tiernas cuando la oruga es joven.",
    "ARAÑA ROJA": "Aumentar la humedad ambiental pulverizando agua (odian la humedad). Aplicar azufre mojable o tratamientos con aceite parafinado. En control biológico, introducir el ácaro depredador Phytoseiulus persimilis.",
    "MILDIU PULVERULENTO": "Eliminar y quemar restos afectados. Aplicar fungicidas a base de azufre, bicarbonato potásico o tratamientos preventivos con cola de caballo. Mejorar la aireación de la planta.",
    "BOTRITIS": "Reducir drásticamente la humedad foliar and el riego. Podar partes afectadas con herramientas desinfectadas. Aplicar fungicidas biológicos a base de Bacillus subtilis o cobre en casos graves.",
    "COCHINILLA": "Limpieza manual con alcohol de quemar y algodón en plantas pequeñas. En ataques generalizados, aplicar aceite de verano combinado con un insecticida sistémico autorizado (ej. deltametrina).",
    "VIRUS": "No existe tratamiento curativo. Se debe arrancar y destruir la planta afectada inmediatamente para evitar el contagio. Es fundamental controlar las plagas de pulgón o mosca blanca, que actúan como vectores.",
    "MOSCA BLANCA": "Colocar trampas cromáticas amarillas pegajosas. Tratar con jabón potásico combinado con aceite de neem. En invernaderos, introducir el parasitoide Encarsia formosa.",
    "EXCESO DE ABONO O LIMITACIÓN DE ESPACIO": "Realizar un lavado de suelo (riego abundante sin encharcar para arrastrar sales). Si la maceta se ha quedado pequeña, programar un trasplante de urgencia a un contenedor mayor.",
    "QUEMADURA DE LAS HOJAS POR EL VIENTO": "Instalar barreras cortavientos o reubicar la planta a una zona protegida. Incrementar los riegos en días de viento seco para evitar la deshidratación de los bordes.",
    "FALTA DE NITROGENO / TIERRA ESTÉRIL": "Aportar materia orgánica al suelo (humus de lombriz, compost o estiércol maduro). Aplicar un abonado de fondo rico en Nitrógeno (N) de liberación lenta o quelatos si es urgente.",
    "SUELO ALCALINO": "Aplicar quelatos de hierro (Fe) directamente al riego para corregir la clorosis férrica. A largo plazo, acidificar el sustrato aportando turba rubia, azufre elemental o agua de riego corregida.",
    "PODREDUMBRE": "Suspender los riegos de inmediato. Mejorar el drenaje del terreno o maceta aportando perlita o arena. Si afecta a las raíces, aplicar un fungicida específico para cuello (ej. Fosetil-Al).",
    "DESHOJE NATURAL": "Proceso fisiológico normal en hojas viejas de la zona baja. No requiere acción. Mantener el mantenimiento habitual de la planta retirando las hojas secas caídas.",
    "PLANTA ESTRESADA": "Evitar mover la planta de sitio constantemente. Suspender el abono hasta que se estabilice. Mantener riegos moderados y estables sin saturar el suelo hasta ver nuevos brotes.",
    "FALTA DE LUZ NATURAL": "Trasladar la planta de forma progresiva a una ubicación con mayor exposición solar o iluminación indirecta brillante (evitar sol directo de golpe para no quemarla).",
    "FALTA DE POTASIO": "Aplicar un fertilizante rico en Potasio (K), como sulfato potásico o patasa, especialmente antes y durante la época de floración para fortalecer los tejidos y flores.",
    "LARVAS DE GORGOJO": "Aplicar nematodos entomopatógenos (Steinernema carpocapsae) al suelo mediante el riego en primavera u otoño para que parasiten las larvas que devoran las raíces.",
    "QUEMADURA DE LAS HOJAS": "Proporcionar sombreado provisional durante las horas centrales del día. Ajustar la frecuencia de riego para que la planta responda mejor a los picos de calor extremo."
}

# Estructura de las 3 grandes columnas del libro
col1, col2, col3 = st.columns(3)
diagnosticos_detectados = {}

with col1:
    st.header("🍃 Síntomas en Hojas")
    if st.checkbox("Las hojas nuevas están deformadas y hay moho oscuro/polvoriento"): diagnosticos_detectados["PULGÓN"] = "PULGÓN"
    if st.checkbox("Las hojas nuevas están deformadas (sin moho oscuro)"): diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "CÁPSIDO VERDE COMÚN"
    if st.checkbox("Tiene agujeros en los bordes"): diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "CÁPSIDO VERDE COMÚN"
    if st.checkbox("Tiene agujeros regulares en forma semicircular"): diagnosticos_detectados["ABEJA ASERRADORA"] = "ABEJA ASERRADORA"
    if st.checkbox("Tiene agujeros grandes e irregulares con rastro plateado"): diagnosticos_detectados["BABOSAS / CARACOLES"] = "BABOSAS / CARACOLES"
    if st.checkbox("Tiene agujeros grandes e irregulares (sin rastro plateado)"): diagnosticos_detectados["GORGOJOS ADULTOS"] = "GORGOJOS ADULTOS"
    if st.checkbox("Tiene agujeros por toda la hoja (o defoliación masiva)"): diagnosticos_detectados["ORUGAS"] = "ORUGAS"
    if st.checkbox("Hay agujeros con el borde marrón"): diagnosticos_detectados["CÁPSIDO VERDE COMÚN"] = "CÁPSIDO VERDE COMÚN"
    if st.checkbox("Hay pequeños insectos y puestas de huevos diminutos"): diagnosticos_detectados["ARAÑA ROJA"] = "ARAÑA ROJA"
    if st.checkbox("Hay manchas blancas y aterciopeladas"): diagnosticos_detectados["MILDIU PULVERULENTO"] = "MILDIU PULVERULENTO"
    if st.checkbox("Hay manchas o parches moteados con brotes atrofiados"): diagnosticos_detectados["VIRUS"] = "VIRUS"
    if st.checkbox("Las hojas jaspeadas se vuelven marrones"): diagnosticos_detectados["FALTA DE LUZ NATURAL"] = "FALTA DE LUZ NATURAL"
    if st.checkbox("La planta ya no florece"): diagnosticos_detectados["FALTA DE POTASIO"] = "FALTA DE POTASIO"

with col2:
    st.header("🪵 Síntomas en Tallos")
    if st.checkbox("Los tallos se marchitan y caen"): diagnosticos_detectados["LARVAS DE GORGOJO"] = "LARVAS DE GORGOJO"
    if st.checkbox("Los tallos y hojas parecen 'quemados' y totalmente muertos"): diagnosticos_detectados["PODREDUMBRE APICAL"] = "PODREDUMBRE APICAL"
    if st.checkbox("Los tallos/hojas están dañados/quemados pero la planta sobrevive"): diagnosticos_detectados["QUEMADURA DE LAS HOJAS"] = "QUEMADURA DE LAS HOJAS"
    if st.checkbox("Hay moho negro y polvoriento en los tallos"): diagnosticos_detectados["COCHINILLA"] = "COCHINILLA"
    if st.checkbox("Hay moho gris y aterciopelado en los tallos"): diagnosticos_detectados["BOTRITIS"] = "BOTRITIS"
    if st.checkbox("Hay gotas de líquido marrón en los tallos"): diagnosticos_detectados["COCHINILLA"] = "COCHINILLA"

with col3:
    st.header("🧪 Problemas de Cultivo")
    if st.checkbox("Las hojas se vuelven marrones sólo por la punta"): diagnosticos_detectados["EXCESO DE ABONO O LIMITACIÓN DE ESPACIO"] = "EXCESO DE ABONO O LIMITACIÓN DE ESPACIO"
    if st.checkbox("Las hojas se vuelven marrones por los bordes"): diagnosticos_detectados["QUEMADURA DE LAS HOJAS POR EL VIENTO"] = "QUEMADURA DE LAS HOJAS POR EL VIENTO"
    if st.checkbox("Las hojas son pálidas y demasiado pequeñas (generalizado)"): diagnosticos_detectados["FALTA DE NITROGENO / TIERRA ESTÉRIL"] = "FALTA DE NITROGENO / TIERRA ESTÉRIL"
    if st.checkbox("Las hojas amarillean pero los nervios siguen verdes (Planta ácida)"): diagnosticos_detectados["SUELO ALCALINO"] = "SUELO ALCALINO"
    if st.checkbox("El suelo está visiblemente anegado o hay podredumbre radicular"): diagnosticos_detectados["PODREDUMBRE"] = "PODREDUMBRE"
    if st.checkbox("Hojas con caídas y amarilleamiento natural (hojas viejas)"): diagnosticos_detectados["DESHOJE NATURAL"] = "DESHOJE NATURAL"
    if st.checkbox("La planta ha perdido todas las hojas de golpe tras un cambio"): diagnosticos_detectados["PLANTA ESTRESADA"] = "PLANTA ESTRESADA"
    if st.checkbox("Hay grandes manchas o parches con pequeños insectos con forma de polilla"): diagnosticos_detectados["MOSCA BLANCA"] = "MOSCA BLANCA"

# Panel de resultados blindado en plano contra errores de indentación
st.markdown("---")
st.subheader("📋 Panel de Diagnósticos Encontrados")

if not diagnosticos_detectados:
    st.info("No se ha marcado ningún síntoma. Revisa la planta y marca las casillas correspondientes.")
else:
    st.success(f"Se han detectado {len(diagnosticos_detectados)} problema(s) simultáneos en la planta:")
    for prob, clave en diagnosticos_detectados.items():
        st.warning(f"🚨 **{prob}**")
        sol = DICCIONARIO_TRATAMIENTOS.get(clave, "Consulte el cuaderno de campo del Módulo MF0525_2.")
        st.info(f"🛠️ **Tratamiento:** {sol}")

# Pie de página unificado y limpio
st.markdown("---")
