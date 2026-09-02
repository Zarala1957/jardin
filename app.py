import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS CSS PERSONALIZADOS
st.set_page_config(
    page_title="Asistente Multidiagnóstico para Jardinería",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>
    /* Ocultar elementos nativos de Streamlit y GitHub */
    [data-testid="stHeader"] {visibility: hidden;}
    footer {visibility: hidden;}
    div[data-testid="stDecoration"] {display: none;}
    
    /* Fuentes responsivas para teléfonos móviles */
    @media (max-width: 768px) {
        html, body, [data-testid="stMarkdownContainer"] p {
            font-size: 14px !important;
        }
        h1 { font-size: 24px !important; }
        h2 { font-size: 20px !important; }
        h3 { font-size: 18px !important; }
    }
    
    /* Estilos personalizados para los paneles de resultados */
    .recuadro-problema {
        background-color: #e8f5e9; 
        padding: 14px; 
        border-left: 6px solid #2e7d32; 
        border-radius: 6px; 
        margin-bottom: 6px;
    }
    .recuadro-solucion {
        background-color: #f3e5f5; 
        padding: 14px; 
        border-left: 6px solid #6a1b9a; 
        border-radius: 6px; 
        margin-bottom: 24px;
    }
</style>
""", unsafe_allow_html=True)

# 2. BASE DE DATOS DE SÍNTOMAS, PROBLEMAS (VERDES) Y SOLUCIONES (LILA)
DIAGNOSTICOS_MASTER = {
    "Hojas": {
        "Las hojas nuevas están deformadas y hay moho oscuro/polvoriento": {
            "problema": "Pulgones acompañados de hongo Negrilla u Oídio",
            "solucion": "Aplicar un tratamiento combinado de jabón potásico seguido de un fungicida a base de cobre o azufre."
        },
        "Las hojas nuevas están deformadas (sin moho oscuro)": {
            "problema": "Ataque temprano de Ácaros o Trips",
            "solucion": "Tratar la planta pulverizando aceite de neem o un acaricida específico en las horas bajas de sol."
        },
        "Tiene agujeros regulares en los bordes": {
            "problema": "Ataque de Gorgojos de la corteza u Otiorrinco",
            "solucion": "Realizar tratamientos nocturnos dirigidos o aplicar nematodos beneficiosos al sustrato."
        },
        "Tiene agujeros regulares en forma semicircular": {
            "problema": "Abeja Cortadora de Hojas (Megachile)",
            "solucion": "Suele ser un daño estético menor. No se requiere un tratamiento químico severo; basta con proteger la planta físicamente."
        },
        "Tiene agujeros grandes o irregulares con rastro plateado": {
            "problema": "Presencia de Caracoles o Babosas",
            "solucion": "Instalar trampas de cerveza a ras de suelo o esparcir gránulos ecológicos de fosfato férrico."
        },
        "Tiene agujeros grandes e irregulares (sin rastro plateado)": {
            "problema": "Infestación por Orugas Defoliadoras",
            "solucion": "Pulverizar las hojas con Bacillus thuringiensis de forma foliar mojando bien el envés."
        },
        "Tiene agujeros por toda la hoja (o defoliación masiva)": {
            "problema": "Plaga severa de Escarabajos adultos o Larvas gregarias",
            "solucion": "Retirar manualmente los ejemplares visibles y aplicar pulverizaciones con piretrinas naturales."
        },
        "Hay agujeros con el borde marrón": {
            "problema": "Antracnosis o Infección Fúngica foliar localizada",
            "solucion": "Podar y retirar inmediatamente las hojas afectadas y aplicar un fungicida sistémico de amplio espectro."
        },
        "Hay pequeños insectos y puestas de huevos diminutos": {
            "problema": "Presencia activa e infestación de Mosca Blanca o Araña Roja",
            "solucion": "Colocar trampas cromáticas adhesivas de color amarillo e iniciar lavados semanales con jabón potásico."
        },
        "Hay manchas blancas y aterciopeladas": {
            "problema": "Aparición de Mildiu u Oídio foliar",
            "solucion": "Aumentar la separación entre plantas para mejorar la ventilación y realizar tratamientos con azufre soluble."
        },
        "Hay manchas o parches moteados con brotes atrofiados": {
            "problema": "Infección por el Virus del Mosaico",
            "solucion": "Esta patología no tiene cura. Es necesario aislar de inmediato o desechar la planta para evitar contagios a ejemplares sanos."
        },
        "Las hojas jaspeadas se vuelven marrones": {
            "problema": "Carencia nutricional severa de elementos clave (como Magnesio o Potasio)",
            "solucion": "Incorporar al agua de riego un fertilizante corrector de carencias rico en microelementos."
        },
        "La planta ya no florece": {
            "problema": "Exceso de Nitrógeno en el suelo o falta severa de Fósforo y Luz",
            "solucion": "Suspender los abonos nitrogenados, cambiar a un fertilizante alto en Fósforo y Potasio, y reubicar a una zona más soleada."
        },
        "Las hojas inferiores amarillean y terminan cayéndose": {
            "problema": "Clorosis por Exceso Continuo de Riego o Falta de Nitrógeno",
            "solucion": "Espaciar de inmediato los riegos permitiendo secar el sustrato y aplicar un fertilizante nitrogenado ligero."
        },
        "Aparición de costras marrones o masas algodonosas adheridas": {
            "problema": "Infestación por Cochinilla (Parda o Algodonosa)",
            "solucion": "Limpiar los tallos y hojas con un algodón empapado en alcohol e impregnar la planta con aceite de neem."
        },
        "Hojas con las puntas completamente quemadas y secas": {
            "problema": "Estrés hídrico crítico o exceso acumulado de sales/fertilizantes",
            "solucion": "Efectuar un lavado profundo de raíces regando con abundante agua limpia y suspender el abono durante un mes."
        },
        "Manchas circulares concéntricas de color café oscuro": {
            "problema": "Alternaria (Hongo de la mancha de la hoja)",
            "solucion": "Retirar y destruir los restos vegetales afectados y realizar una aplicación foliar de fungicida orgánico."
        },
        "Hojas pálidas acompañadas de finas telarañas en el envés": {
            "problema": "Plaga latente de Araña Roja (Tetraníquidos)",
            "solucion": "Elevar la humedad ambiental mediante pulverizaciones constantes de agua limpia y aplicar un acaricida selectivo."
        },
        "Las hojas toman un color verde oscuro opaco y tintes purpúreos": {
            "problema": "Deficiencia crítica de Fósforo asimilable",
            "solucion": "Enmendar el suelo añadiendo harina de huesos o aplicando un abono líquido específico rico en Fósforo."
        }
    },
    "Tallos": {
        "Los tallos se marchitan y caen": {
            "problema": "Damping-off o Caída fúngica de plántulas",
            "solucion": "Reducir la humedad drásticamente, optimizar el drenaje del semillero y aplicar un fungicida protector en el sustrato."
        },
        "Los tallos y hojas parecen 'quemados' y totalmente muertos": {
            "problema": "Ataque severo de Fuego Bacteriano o Fitóftora",
            "solucion": "Ejecutar una poda drástica eliminando todo el tejido dañado y desinfectar escrupulosamente las herramientas de corte entre pasadas."
        },
        "Los tallos/hojas están dañados/quemados pero la planta sobrevive": {
            "problema": "Fisiopatía debida a una Helada Temprana o Quemadura Solar directa",
            "solucion": "Cubrir el cultivo con una manta térmica protectora por las noches o trasladar temporalmente a semisombra."
        },
        "Hay moho negro y polvoriento en los tallos": {
            "problema": "Fumagina (Hongo de la Negrilla) asentado sobre melaza",
            "solucion": "Identificar y eliminar primero la plaga causante de la melaza (como pulgones o cochinillas) usando jabón potásico."
        },
        "Hay moho grey y aterciopelado en los tallos": {
            "problema": "Botritis (Podredumbre gris del tallo)",
            "solucion": "Cortar de inmediato las zonas afectadas del tallo, disminuir la humedad ambiental y pulverizar un fungicida específico anti-botritis."
        },
        "Hay gotas de líquido marrón en los tallos": {
            "problema": "Chancro bacteriano o desarrollo de Gomosis",
            "solucion": "Sanear la herida del tallo raspando suavemente hasta el tejido sano y sellar aplicando pasta cicatrizante con base de cobre."
        },
        "El tallo principal se vuelve blando, flácido y oscuro en la base": {
            "problema": "Podredumbre del cuello de la raíz (Rhizoctonia o Pythium)",
            "solucion": "Suspender los riegos de forma inmediata, mejorar la aireación del suelo y aplicar un fungicida sistémico radicular."
        }
    },
    "Cultivo": {
        "Las hojas se vuelven marrones sólo por la punta": {
            "problema": "Entorno con aire extremadamente seco o exposición a corrientes fuertes",
            "solucion": "Elevar la humedad ambiental alrededor de la planta mediante recipientes con agua o usando un humidificador."
        },
        "Las hojas se vuelven marrones por los bordes": {
            "problema": "Acumulación tóxica de cloro o sales minerales procedentes del agua de red",
            "solucion": "Utilizar agua de lluvia para el riego o permitir que el agua del grifo repose en un contenedor abierto durante 24 horas."
        },
        "Las hojas son pálidas y demasiado pequeñas (generalizado)": {
            "problema": "Carencia generalizada de macronutrientes o iluminación deficiente",
            "solucion": "Aportar nutrientes orgánicos como humus de lombriz al sustrato y mover la planta hacia una ubicación con mejor luz."
        },
        "Las hojas amarillean pero los nervios siguen verdes (Planta ácida)": {
            "problema": "Clorosis Férrica por bloqueo de Hierro debido a pH inadecuado",
