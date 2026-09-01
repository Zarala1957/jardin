import streamlit as st
import urllib.parse

st.set_page_config(page_title="Diagnóstico de Jardinería", page_icon="🌱")

st.title("🌱 Asistente de Diagnóstico para Jardinería")
st.write("Identifica las condiciones de tu jardín a partir de los síntomas detectados.")

# Función auxiliar para crear botones de consulta directa
def boton_consulta_directa(diagnostico_txt):
    # Formateamos el texto para la búsqueda en Google (ej: "Botritis plantas tratamiento")
    termino_busqueda = f"{diagnostico_txt} plantas sintomas tratamiento"
    url_codificada = urllib.parse.quote(termino_busqueda)
    enlace_google = f"https://google.com{url_codificada}"
    
    st.markdown(
        f'<a href="{enlace_google}" target="_blank">'
        f'<button style="background-color:#4CAF50; color:white; border:none; '
        f'padding:10px 20px; text-align:center; text-decoration:none; '
        f'display:inline-block; font-size:16px; margin:4px 2px; cursor:pointer; '
        f'border-radius:8px;">🔍 Consultar fotos y tratamientos en directo</button></a>',
        unsafe_allow_stdio=True, unsafe_allow_html=True
    )

# --- INICIO DEL FLUJO ---
zona = st.radio("¿Qué parte de la planta está más afectada?", ["Seleccione...", "Tallos", "Hojas"])

if zona == "Tallos":
    st.subheader("🔎 Analizando Tallos")
    
    if st.checkbox("¿Los tallos se marchitan y caen?"):
        st.error("🚨 Diagnóstico: LARVAS DE GORGOJO")
        boton_consulta_directa("Larvas de gorgojo")
        
    elif st.checkbox("¿Los tallos están secándose?"):
        if st.radio("¿Parece que los tallos y las hojas estén 'quemados' y totalmente muertos?", ["Selecciona...", "Sí", "No"]) == "Sí":
            st.error("🚨 Diagnóstico: PODREDUMBRE APICAL / PROBLEMAS DE CULTIVO")
            boton_consulta_directa("Podredumbre apical plantas")
        else:
            st.warning("⚠️ Diagnóstico: QUEMADURA DE LAS HOJAS (Pero la planta aún sobrevive)")
            boton_consulta_directa("Quemadura de hojas por viento plantas")
            
    elif st.checkbox("¿Hay moho en los tallos?"):
        tipo_moho = st.radio("¿Cómo es el moho?", ["Selecciona...", "Negro y polvoriento", "Gris y aterciopelado"])
        if tipo_moho == "Negro y polvoriento":
            st.error("🚨 Diagnóstico: COCHINILLA (Moho negro)")
            boton_consulta_directa("Cochinilla moho negro")
        elif tipo_moho == "Gris y aterciopelado":
            st.error("🚨 Diagnóstico: BOTRITIS")
            boton_consulta_directa("Botritis")
            
    elif st.checkbox("¿Hay gotas de líquido marrón en los tallos?"):
        st.error("🚨 Diagnóstico: COCHINILLA")
        boton_consulta_directa("Cochinilla de las plantas")

elif zona == "Hojas":
    st.subheader("🔎 Analizando Hojas")
    
    sintoma = st.selectbox("¿Cuál es el síntoma principal en las hojas?", 
                            ["Selecciona...", 
                             "Se vuelven marrones", 
                             "Se vuelven amarillas", 
                             "Tienen agujeros", 
                             "Se caen", 
                             "Tienen marcas / manchas / moho"])

    # 1. MARRONES (Problemas de cultivo principales)
    if sintoma == "Se vuelven marrones":
        donde = st.radio("¿En qué parte de la hoja?", ["Selecciona...", "Sólo por la punta", "Por los bordes"])
        if donde == "Sólo por la punta":
            st.warning("⚠️ PROBLEMA DE CULTIVO: EXCESO DE ABONO O LIMITACIÓN DE ESPACIO")
            boton_consulta_directa("Exceso de abono puntas marrones")
        elif donde == "Por los bordes":
            st.warning("⚠️ PROBLEMA DE CULTIVO: QUEMADURA DE LAS HOJAS POR EL VIENTO")
            boton_consulta_directa("Quemadura por viento plantas")

    # 2. AMARILLAS
    elif sintoma == "Se vuelven amarillas":
        if st.checkbox("¿Las hojas son pálidas y demasiado pequeñas?"):
            st.warning("⚠️ PROBLEMA DE CULTIVO: TIERRA ESTÉRIL / FALTA DE NITRÓGENO")
            boton_consulta_directa("Falta de nitrogeno plantas")
        elif st.checkbox("¿Es una planta ácida?"):
            st.error("🚨 Diagnóstico: SUELO ALCALINO (Clorosis férrica)")
            boton_consulta_directa("Suelo alcalino clorosis ferrica")
        elif st.checkbox("¿El suelo de la planta está anegado?"):
            st.error("🚨 Diagnóstico: PODREDUMBRE POR EXCESO DE AGUA")
            boton_consulta_directa("Podredumbre raices exceso agua")

    # 3. AGUJEROS
    elif sintoma == "Tienen agujeros":
        if st.radio("¿Los bordes son la parte más afectada?", ["No", "Sí"]) == "Sí":
            st.error("🚨 Diagnóstico: CÁPSIDO VERDE COMÚN")
            boton_consulta_directa("Capsido verde comun")
        elif st.radio("¿Los agujeros son regulares y en forma semicircular?", ["No", "Sí"]) == "Sí":
            st.error("🚨 Diagnóstico: ABEJA ASERRADORA")
            boton_consulta_directa("Abeja aserradora hojas")
        elif st.radio("¿Son agujeros grandes e irregulares?", ["No", "Sí"]) == "Sí":
            if st.radio("¿Hay un rastro plateado?", ["No", "Sí"]) == "Sí":
                st.error("🚨 Diagnóstico: BABOSAS / CARACOLES")
                boton_consulta_directa("Babosas caracoles jardin")
            else:
                st.error("🚨 Diagnóstico: GORGOJOS ADULTOS u ORUGAS")
                boton_consulta_directa("Gorgojos adultos orugas hojas")
        elif st.radio("¿Hay agujeros por toda la hoja?", ["No", "Sí"]) == "Sí":
            st.error("🚨 Diagnóstico: ORUGAS EN HOJAS")
            boton_consulta_directa("Orugas hojas jardin")

    # 4. SE CAEN
    elif sintoma == "Se caen":
        if st.radio("¿Primero se vuelven amarillas?", ["No", "Sí"]) == "Sí":
            st.success("🍃 Proceso Natural: DESHOJE NATURAL")
            boton_consulta_directa("Deshoje natural plantas")
        elif st.radio("¿Primero se vuelven marrones?", ["No", "Sí"]) == "Sí":
            st.warning("⚠️ PROBLEMA DE CULTIVO: EXCESO DE AGUA")
            boton_consulta_directa("Caida hojas exceso de agua")
        elif st.radio("¿La planta ha perdido todas las hojas de golpe?", ["No", "Sí"]) == "Sí":
            st.warning("⚠️ Diagnóstico: PLANTA ESTRESADA")
            # Enlace de búsqueda para plantas estresadas por cambio de sitio o clima
            boton_consulta_directa("Planta estresada caida hojas")

    # 5. MARCAS / MANCHAS / MOHO
    elif sintoma == "Tienen marcas / manchas / moho":
        if st.checkbox("¿Hay agujeros con el borde marrón?"):
            st.error("🚨 Diagnóstico: CÁPSIDO VERDE COMÚN")
            boton_consulta_directa("Capsido verde comun")
        elif st.checkbox("¿Hay pequeños insectos y puestas de huevos diminutos?"):
            st.error("🚨 Diagnóstico: ARAÑUELA ROJA")
            boton_consulta_directa("Arañuela roja")
        elif st.checkbox("¿Hay manchas blancas y aterciopeladas?"):
            st.error("🚨 Diagnóstico: MILDIU PULVERULENTO")
            boton_consulta_directa("Mildiu pulverulento")
        elif st.checkbox("¿Hay un moho gris y aterciopelado?"):
            st.error("🚨 Diagnóstico: BOTRITIS")
            boton_consulta_directa("Botritis plantas")
        elif st.checkbox("¿Las hojas están moteadas o tienen manchas?"):
            if st.checkbox("¿Hay brotes atrofiados o deformados?"):
                st.error("🚨 Diagnóstico: VIRUS VEGETAL")
                boton_consulta_directa("Virus de las plantas")
            elif st.checkbox("¿Las hojas tienen grandes manchas o parches?"):
                if st.checkbox("¿Hay un moho negro y polvoriento?"):
                    if st.checkbox("¿Las hojas nuevas están deformadas?"):
                        st.error("🚨 Diagnóstico: PULGÓN")
                        boton_consulta_directa("Pulgon plantas")
                    else:
                        st.error("🚨 Diagnóstico: COCHINILLA")
                        boton_consulta_directa("Cochinilla plantas")
                elif st.checkbox("¿Hay pequeños insectos con forma de polilla sobre las hojas?"):
                    st.error("🚨 Diagnóstico: MOSCA BLANCA")
                    boton_consulta_directa("Mosca blanca jardin")
