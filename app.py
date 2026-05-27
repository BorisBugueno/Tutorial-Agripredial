# -*- coding: utf-8 -*-
"""
================================================================================
 TUTORIAL INTERACTIVO AGRIPREDIAL  —  Rol "Jefe de Campo"
================================================================================
App educativa hecha en Streamlit que enseña, paso a paso, cómo usar la
plataforma externa "Agripredial" (https://www.agripredial.cl/).

IMPORTANTE: Esta aplicación es 100% independiente de Agripredial. NO se conecta
a ningún sistema real ni guarda datos. Su único objetivo es ser un tutorial
visual y amigable para "jefes de campo" (usuarios del sector agrícola).

Estructura del código (de arriba hacia abajo):
  1. Configuración general de la página
  2. Estilos (CSS) para letras grandes y diseño amigable
  3. CONTENIDO del tutorial (todo el texto vive en el diccionario MODULOS)
  4. Funciones de ayuda reutilizables (mostrar imagen, mostrar paso, etc.)
  5. Barra lateral de navegación
  6. Render de cada página según el módulo elegido
================================================================================
"""

import os
import streamlit as st

# ==============================================================================
# 1) CONFIGURACIÓN GENERAL DE LA PÁGINA
# ==============================================================================
# layout="wide" da más espacio; el ícono y el título aparecen en la pestaña.
st.set_page_config(
    page_title="Tutorial Agripredial · Jefe de Campo",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carpeta donde el usuario podrá ir guardando las capturas de pantalla reales.
CARPETA_IMAGENES = "img"

# URL real de la plataforma (solo para enlazar; la app NO se conecta a ella).
URL_AGRIPREDIAL = "https://www.agripredial.cl/"


# ==============================================================================
# 2) ESTILOS (CSS)  —  letras grandes, botones cómodos, look amigable
# ==============================================================================
# Inyectamos CSS personalizado para que la interfaz sea muy legible para
# usuarios no técnicos: tipografías grandes, buen contraste y tarjetas suaves.
st.markdown(
    """
    <style>
        /* Tamaño de texto general más grande para mejor lectura */
        html, body, [class*="css"] { font-size: 18px; }

        /* Títulos principales con color verde "campo" */
        h1 { color: #1b5e20; font-size: 2.4rem !important; }
        h2 { color: #2e7d32; font-size: 1.8rem !important; }
        h3 { color: #388e3c; font-size: 1.4rem !important; }

        /* Tarjeta de paso: caja blanca con borde verde y sombra suave */
        .tarjeta-paso {
            background-color: #ffffff;
            border-left: 8px solid #43a047;
            border-radius: 12px;
            padding: 18px 22px;
            margin-bottom: 14px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
            font-size: 1.15rem;
            line-height: 1.6;
            color: #1b1b1b;
        }
        /* Número grande del paso dentro de un círculo verde */
        .num-paso {
            display: inline-block;
            background-color: #43a047;
            color: white;
            font-weight: bold;
            border-radius: 50%;
            width: 38px; height: 38px;
            text-align: center; line-height: 38px;
            margin-right: 10px; font-size: 1.2rem;
        }
        /* Caja de "consejo / tip" en amarillo suave */
        .tip-box {
            background-color: #fff8e1;
            border-left: 6px solid #fbc02d;
            border-radius: 8px;
            padding: 12px 16px; margin: 6px 0 18px 0;
            font-size: 1.05rem;
        }
        /* Botones de Streamlit un poco más grandes */
        .stButton>button {
            font-size: 1.1rem; padding: 0.5rem 1rem; border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ==============================================================================
# 3) CONTENIDO DEL TUTORIAL
# ==============================================================================
# TODO el texto del tutorial vive aquí, organizado como datos (no mezclado con
# la lógica). Así, para corregir un texto solo se edita este diccionario.
#
# Estructura de cada módulo:
#   "titulo"  -> texto que se ve en el menú y como encabezado
#   "intro"   -> párrafo introductorio del módulo
#   "secciones": lista de bloques temáticos. Cada sección tiene:
#         "nombre" -> subtítulo
#         "pasos"  -> lista de pasos. Cada paso es un diccionario con:
#               "texto"  -> instrucción (obligatorio)
#               "imagen" -> nombre de archivo de la captura (opcional)
#               "tip"    -> consejo destacado (opcional)
# ==============================================================================

MODULOS = {

    # ----------------------------------------------------------------------
    "inicio": {
        "titulo": "🏠 Inicio",
        "es_especial": True,  # esta página tiene render propio
    },

    # ----------------------------------------------------------------------
    "conceptos": {
        "titulo": "📚 Conceptos básicos",
        "es_especial": True,  # render propio (muestra la jerarquía)
    },

    # ----------------------------------------------------------------------
    "acceso": {
        "titulo": "🔑 Módulo 1: Acceso al sistema",
        "intro": (
            "Aprende a **entrar** y **salir** de Agripredial de forma segura. "
            "Este es siempre el primer paso antes de hacer cualquier tarea."
        ),
        "secciones": [
            {
                "nombre": "✅ Ingresar al sistema",
                "pasos": [
                    {
                        "texto": (
                            f"Abre tu navegador (Chrome, Edge o Firefox) y entra a la "
                            f"dirección: **{URL_AGRIPREDIAL}**"
                        ),
                        "imagen": "acceso_1_url.png",
                        "tip": "Puedes guardar esta página en 'Favoritos' para entrar más rápido la próxima vez.",
                    },
                    {
                        "texto": "Escribe tu **correo electrónico** y tu **contraseña** en las casillas.",
                        "imagen": "acceso_2_login.png",
                    },
                    {
                        "texto": "Haz clic en el botón para **Ingresar** y ¡listo! Ya estás dentro del sistema.",
                        "imagen": "acceso_3_ingresar.png",
                    },
                ],
            },
            {
                "nombre": "🚪 Salir del sistema",
                "pasos": [
                    {
                        "texto": "Cuando termines tu trabajo, haz clic en el botón **Salir**.",
                        "imagen": "acceso_4_salir.png",
                        "tip": "Cerrar sesión protege tu cuenta, sobre todo si usas un computador compartido.",
                    },
                ],
            },
        ],
    },

    # ----------------------------------------------------------------------
    "campos": {
        "titulo": "🌾 Módulo 2: Campos",
        "intro": (
            "Un **campo** es un terreno de la empresa agrícola. Aquí aprenderás a "
            "**registrar**, **consultar/modificar** y **eliminar** campos. "
            "Para registrar necesitarás un **archivo KML** con el mapa del terreno."
        ),
        "secciones": [
            {
                "nombre": "➕ Registrar un campo",
                "pasos": [
                    {"texto": "Haz clic en la opción **Empresa** del menú.", "imagen": "campo_1_empresa.png"},
                    {"texto": "Selecciona la **empresa agrícola** a la que pertenece el campo y haz clic en **Nuevo campo**.", "imagen": "campo_2_nuevo.png"},
                    {"texto": "Escribe el **nombre del campo** y haz clic en **Subir archivo KML**.", "imagen": "campo_3_nombre.png",
                     "tip": "Un archivo KML es un mapa digital del terreno. Suele entregarlo el equipo técnico o se obtiene desde Google Earth."},
                    {"texto": "En tu computador, busca y selecciona el **archivo KML** y haz clic en **Abrir**.", "imagen": "campo_4_kml.png"},
                    {"texto": "Cuando aparezca la **imagen del campo** a la izquierda de la pantalla, haz clic en **Guardar**.", "imagen": "campo_5_guardar.png"},
                    {"texto": "Por último, haz clic en **De acuerdo** para confirmar el registro del campo.", "imagen": "campo_6_deacuerdo.png"},
                ],
            },
            {
                "nombre": "🔎 Consultar y modificar un campo",
                "pasos": [
                    {"texto": "Selecciona el **campo de la empresa** que quieres revisar.", "imagen": "campo_7_consultar.png"},
                    {"texto": "El sistema mostrará los datos del campo y permitirá editarlos.", "imagen": "campo_8_datos.png"},
                    {"texto": "Si necesitas cambiar algo, modifica los datos y haz clic en **Guardar**.", "imagen": "campo_9_modificar.png"},
                ],
            },
            {
                "nombre": "🗑️ Eliminar un campo",
                "pasos": [
                    {"texto": "Selecciona primero el campo (igual que al consultarlo).", "imagen": "campo_10_seleccionar.png"},
                    {"texto": "Haz clic en la opción **Eliminar campo**.", "imagen": "campo_11_eliminar.png"},
                    {"texto": "Marca **Estoy seguro de mi decisión** y haz clic en **Sí, eliminar**.", "imagen": "campo_12_confirmar.png",
                     "tip": "⚠️ Eliminar un campo borra también su información. Hazlo solo si estás completamente seguro."},
                    {"texto": "Haz clic en **De acuerdo** para finalizar.", "imagen": "campo_13_ok.png"},
                ],
            },
        ],
    },

    # ----------------------------------------------------------------------
    "sectores": {
        "titulo": "📍 Módulo 3: Sectores",
        "intro": (
            "Un **sector** es una parte dentro de un campo. Para crearlo necesitas "
            "su **nombre**, el **número de plantas** y un **archivo KML**."
        ),
        "secciones": [
            {
                "nombre": "➕ Registrar un sector",
                "pasos": [
                    {"texto": "Selecciona el **campo** al que pertenecerá el sector y haz clic en **Nuevo sector**.", "imagen": "sector_1_nuevo.png"},
                    {"texto": "Escribe el **nombre del sector**, el **número de plantas** y haz clic en **Subir archivo KML**.", "imagen": "sector_2_datos.png"},
                    {"texto": "Selecciona el **archivo KML** en tu computador y haz clic en **Abrir**.", "imagen": "sector_3_kml.png"},
                    {"texto": "Cuando aparezca la **imagen del sector** a la izquierda, haz clic en **Guardar**.", "imagen": "sector_4_guardar.png"},
                    {"texto": "Haz clic en **De acuerdo** para registrar el sector.", "imagen": "sector_5_ok.png"},
                ],
            },
            {
                "nombre": "🔎 Consultar y modificar un sector",
                "pasos": [
                    {"texto": "Selecciona el **sector** que quieres revisar.", "imagen": "sector_6_consultar.png"},
                    {"texto": "El sistema mostrará sus datos y te permitirá editarlos.", "imagen": "sector_7_datos.png"},
                    {"texto": "Modifica lo que necesites y haz clic en **Guardar**.", "imagen": "sector_8_guardar.png"},
                ],
            },
            {
                "nombre": "🗑️ Eliminar un sector",
                "pasos": [
                    {"texto": "Selecciona el sector y haz clic en la opción **Eliminar sector**.", "imagen": "sector_9_eliminar.png"},
                    {"texto": "Marca **Estoy seguro de mi decisión** y haz clic en **Sí, eliminar**.", "imagen": "sector_10_confirmar.png"},
                    {"texto": "Haz clic en **De acuerdo** para finalizar.", "imagen": "sector_11_ok.png"},
                ],
            },
        ],
    },

    # ----------------------------------------------------------------------
    "cuarteles": {
        "titulo": "🍇 Módulo 4: Cuarteles",
        "intro": (
            "Un **cuartel** es una subdivisión dentro de un sector. Para crearlo "
            "necesitas su **nombre**, el **código de certificación** y un **archivo KML**."
        ),
        "secciones": [
            {
                "nombre": "➕ Registrar un cuartel",
                "pasos": [
                    {"texto": "Selecciona el **sector** al que pertenecerá el cuartel y haz clic en **Nuevo cuartel**.", "imagen": "cuartel_1_nuevo.png"},
                    {"texto": "Escribe el **nombre del cuartel**, el **código de certificación** y haz clic en **Subir archivo KML**.", "imagen": "cuartel_2_datos.png",
                     "tip": "El código de certificación lo entrega la entidad certificadora. Si no lo tienes a mano, consúltalo antes de empezar."},
                    {"texto": "Selecciona el **archivo KML** y haz clic en **Abrir**.", "imagen": "cuartel_3_kml.png"},
                    {"texto": "Cuando aparezca la **imagen del cuartel** a la izquierda, haz clic en **Guardar**.", "imagen": "cuartel_4_guardar.png"},
                    {"texto": "Haz clic en **De acuerdo** para registrar el cuartel.", "imagen": "cuartel_5_ok.png"},
                ],
            },
            {
                "nombre": "🔎 Consultar y modificar un cuartel",
                "pasos": [
                    {"texto": "Selecciona el **cuartel** que quieres revisar.", "imagen": "cuartel_6_consultar.png"},
                    {"texto": "Modifica los datos necesarios y haz clic en **Guardar**.", "imagen": "cuartel_7_guardar.png"},
                ],
            },
            {
                "nombre": "🗑️ Eliminar un cuartel",
                "pasos": [
                    {"texto": "Selecciona el cuartel y haz clic en **Eliminar cuartel**.", "imagen": "cuartel_8_eliminar.png"},
                    {"texto": "Marca **Estoy seguro de mi decisión** y haz clic en **Sí, eliminar**.", "imagen": "cuartel_9_confirmar.png"},
                    {"texto": "Haz clic en **De acuerdo** para finalizar.", "imagen": "cuartel_10_ok.png"},
                ],
            },
        ],
    },

    # ----------------------------------------------------------------------
    "cultivos": {
        "titulo": "🌱 Módulo 5: Cultivos y variedades",
        "intro": (
            "Aquí registras qué se cultiva en cada sector (por ejemplo, *cerezos*) "
            "y sus **variedades** (por ejemplo, *Bing*, *Santina*)."
        ),
        "secciones": [
            {
                "nombre": "➕ Registrar un cultivo",
                "pasos": [
                    {"texto": "Haz clic en la opción **Cultivos y variedades**.", "imagen": "cultivo_1_menu.png"},
                    {"texto": "En el menú desplegable, selecciona la **empresa**.", "imagen": "cultivo_2_empresa.png"},
                    {"texto": "Selecciona el **campo** en el siguiente desplegable.", "imagen": "cultivo_3_campo.png"},
                    {"texto": "Selecciona el **sector** donde estará el cultivo.", "imagen": "cultivo_4_sector.png"},
                    {"texto": "Escribe el **nombre del nuevo cultivo** y haz clic en el botón **➕ (agregar)**.", "imagen": "cultivo_5_agregar.png"},
                ],
            },
            {
                "nombre": "🔎 Consultar / 🗑️ Eliminar un cultivo",
                "pasos": [
                    {"texto": "Repite la selección de **empresa → campo → sector** para ver la lista de cultivos registrados.", "imagen": "cultivo_6_lista.png"},
                    {"texto": "Para eliminar, haz clic en el botón **🗑️** del cultivo que ya no necesitas.", "imagen": "cultivo_7_eliminar.png"},
                    {"texto": "Marca **Estoy seguro de mi decisión**, haz clic en **Sí, eliminar** y luego en **De acuerdo**.", "imagen": "cultivo_8_confirmar.png"},
                ],
            },
            {
                "nombre": "🍒 Registrar una variedad",
                "pasos": [
                    {"texto": "Selecciona **empresa → campo → sector** (igual que para el cultivo).", "imagen": "variedad_1_seleccion.png"},
                    {"texto": "Elige el **cultivo**, escribe el **nombre de la variedad** y haz clic en el botón **➕**.", "imagen": "variedad_2_agregar.png"},
                    {"texto": "Completa los **datos solicitados** de la variedad y haz clic en **Guardar**.", "imagen": "variedad_3_datos.png"},
                    {"texto": "Haz clic en **De acuerdo** para registrar la variedad.", "imagen": "variedad_4_ok.png"},
                ],
            },
            {
                "nombre": "🔎 Consultar y modificar una variedad",
                "pasos": [
                    {"texto": "Selecciona **empresa → campo → sector** y luego el **cultivo**.", "imagen": "variedad_5_consultar.png"},
                    {"texto": "Elige la **variedad** que quieres revisar; el sistema mostrará y permitirá editar sus datos.", "imagen": "variedad_6_datos.png"},
                    {"texto": "Modifica lo necesario y haz clic en **Guardar**.", "imagen": "variedad_7_guardar.png"},
                ],
            },
        ],
    },

    # ----------------------------------------------------------------------
    "equipo": {
        "titulo": "👥 Módulo 6: Equipo de trabajo",
        "intro": (
            "Registra a las personas del equipo: los **jefes de campo** (responsables "
            "de un campo) y los **supervisores** (responsables de un sector)."
        ),
        "secciones": [
            {
                "nombre": "🧑‍🌾 Registrar un jefe de campo",
                "pasos": [
                    {"texto": "Haz clic en la opción **Jefes de campo**.", "imagen": "jefe_1_menu.png"},
                    {"texto": "Selecciona la **empresa** en el menú desplegable.", "imagen": "jefe_2_empresa.png"},
                    {"texto": "Escribe los **datos del jefe de campo** y haz clic en **Añadir**.", "imagen": "jefe_3_anadir.png"},
                    {"texto": "Selecciona el **campo** que le asignarás desde el menú desplegable.", "imagen": "jefe_4_asignar.png"},
                    {"texto": "Para quitarle un campo, haz clic en el botón **🗑️** junto al campo correspondiente.", "imagen": "jefe_5_desasignar.png"},
                ],
            },
            {
                "nombre": "👷 Registrar un supervisor",
                "pasos": [
                    {"texto": "Haz clic en la opción **Supervisores**.", "imagen": "super_1_menu.png"},
                    {"texto": "Selecciona la **empresa** y el **campo**, escribe los datos del supervisor y haz clic en **Añadir**.", "imagen": "super_2_anadir.png"},
                    {"texto": "Selecciona el **sector** del campo que le asignarás.", "imagen": "super_3_asignar.png"},
                    {"texto": "Para quitarle un sector, haz clic en el botón **🗑️** correspondiente.", "imagen": "super_4_desasignar.png"},
                ],
            },
            {
                "nombre": "🔎 Consultar el equipo",
                "pasos": [
                    {"texto": "Vuelve a **Jefes de campo** o **Supervisores** y selecciona la empresa para ver el listado completo y sus asignaciones.", "imagen": "equipo_1_lista.png"},
                ],
            },
        ],
    },

    # ----------------------------------------------------------------------
    "categorias": {
        "titulo": "🗂️ Módulo 7: Categorías de trabajo",
        "intro": (
            "Las **categorías** agrupan los tipos de labores agrícolas "
            "(por ejemplo: *Poda*, *Riego*, *Cosecha*). Se usan después en las planillas."
        ),
        "secciones": [
            {
                "nombre": "➕ Registrar una categoría",
                "pasos": [
                    {"texto": "Haz clic en la opción **Categorías de trabajos**.", "imagen": "categoria_1_menu.png"},
                    {"texto": "Selecciona la **empresa** en el menú desplegable.", "imagen": "categoria_2_empresa.png"},
                    {"texto": "Escribe el **nombre de la categoría** y haz clic en el botón **➕**.", "imagen": "categoria_3_agregar.png"},
                ],
            },
            {
                "nombre": "🔎 Consultar categorías",
                "pasos": [
                    {"texto": "Selecciona la empresa y el sistema mostrará todas las categorías registradas para ella.", "imagen": "categoria_4_lista.png"},
                ],
            },
        ],
    },

    # ----------------------------------------------------------------------
    "planillas": {
        "titulo": "📋 Módulo 8: Planillas de labores",
        "intro": (
            "La **planilla de labores** es el formulario que usará el equipo en terreno. "
            "Aquí defines qué datos se van a recopilar en cada labor. ¡Es el módulo más "
            "completo, tómalo con calma!"
        ),
        "secciones": [
            {
                "nombre": "🆕 Crear una planilla nueva",
                "pasos": [
                    {"texto": "Haz clic en la opción **Planilla de labores** y selecciona la **empresa**.", "imagen": "planilla_1_menu.png"},
                    {"texto": "Escribe el **nombre de la planilla** y haz clic en el botón **➕**.", "imagen": "planilla_2_nombre.png"},
                    {"texto": "Haz clic sobre el **nombre de la planilla** que acabas de crear para abrirla.", "imagen": "planilla_3_abrir.png"},
                    {"texto": "Elige la **Categoría**, el **Supervisor/a**, la **frecuencia**, el **nivel** (campo, sector o cuartel) y el **nombre del nivel**.", "imagen": "planilla_4_config.png",
                     "tip": "El 'nivel' indica dónde se realiza la labor. Por ejemplo, si es a nivel de cuartel, deberás indicar cuál cuartel."},
                    {"texto": "Escribe el **nombre del dato/parámetro** a recopilar y elige su **tipo de dato**.", "imagen": "planilla_5_parametro.png"},
                    {"texto": "Para agregar otro dato, haz clic en el botón **➕**. Repite por cada dato que necesites.", "imagen": "planilla_6_mas.png"},
                    {"texto": "Cuando termines, haz clic en **Guardar** y luego en **De acuerdo**.", "imagen": "planilla_7_guardar.png"},
                    {"texto": "Para borrar un dato agregado por error, haz clic en el botón **🗑️** junto a ese parámetro.", "imagen": "planilla_8_borrar_dato.png"},
                ],
            },
            {
                "nombre": "🔢 Tipos de datos disponibles",
                "pasos": [
                    {"texto": (
                        "Al crear un parámetro puedes elegir entre estos tipos de dato:\n\n"
                        "- **Entero** → números sin decimales (ej: cantidad de cajas)\n"
                        "- **Decimal** → números con decimales (ej: kilos: 12,5)\n"
                        "- **Texto** → palabras o comentarios libres\n"
                        "- **Sí/No** → respuesta de dos opciones\n"
                        "- **Opciones** → lista para elegir (ej: estado de la planta)\n"
                        "- **Hora** → una hora del día\n"
                        "- **Fecha** → un día del calendario"
                    )},
                ],
            },
            {
                "nombre": "🔘 Cómo crear un dato tipo 'Opción' (ejemplo)",
                "pasos": [
                    {"texto": "Escribe el **nombre del dato** y selecciona el tipo **Opción**.", "imagen": "opcion_1_tipo.png"},
                    {"texto": "Escribe el nombre de la **primera opción**.", "imagen": "opcion_2_primera.png"},
                    {"texto": "Para agregar otra opción, pon una **coma (,)** al final o presiona la tecla **Enter**.", "imagen": "opcion_3_coma.png",
                     "tip": "Truco: la coma y la tecla Enter hacen lo mismo: 'cierran' una opción y abren el espacio para la siguiente."},
                    {"texto": "Escribe la siguiente opción y vuelve a usar coma o Enter. Repite hasta tener todas tus opciones.", "imagen": "opcion_4_siguientes.png"},
                ],
            },
            {
                "nombre": "📑 Crear una planilla copiando otra",
                "pasos": [
                    {"texto": "Selecciona la planilla que quieres copiar y haz clic en el botón **copiar 📄**.", "imagen": "copia_1_copiar.png"},
                    {"texto": "En la copia, escribe un **nombre nuevo**, ajusta lo que necesites, haz clic en **Guardar** y luego en **De acuerdo**.", "imagen": "copia_2_guardar.png",
                     "tip": "Copiar una planilla parecida ahorra mucho tiempo: solo cambias lo distinto."},
                ],
            },
            {
                "nombre": "🔎 Consultar y 🗑️ eliminar planillas",
                "pasos": [
                    {"texto": "Para consultar: entra a **Planilla de labores**, selecciona la empresa y haz clic en el nombre de la planilla.", "imagen": "planilla_9_consultar.png"},
                    {"texto": "Para eliminar: ubica el cursor sobre el nombre de la planilla y haz clic en el botón **🗑️**.", "imagen": "planilla_10_eliminar.png"},
                ],
            },
        ],
    },

    # ----------------------------------------------------------------------
    "glosario": {
        "titulo": "❓ Glosario y ayuda",
        "es_especial": True,  # render propio
    },
}


# ==============================================================================
# 4) FUNCIONES DE AYUDA REUTILIZABLES
# ==============================================================================

def mostrar_imagen(nombre_archivo: str, descripcion: str = "") -> None:
    """
    Muestra una captura de pantalla si existe en la carpeta 'img/'.
    Si todavía no se ha agregado la imagen, muestra un recuadro guía indicando
    qué captura colocar y con qué nombre. Esto permite armar el tutorial primero
    y agregar las imágenes reales después, sin que la app se rompa.
    """
    ruta = os.path.join(CARPETA_IMAGENES, nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True)
    else:
        st.info(
            f"📷 **Aquí irá una captura de pantalla.**\n\n"
            f"Guárdala en la carpeta `{CARPETA_IMAGENES}/` con el nombre "
            f"**`{nombre_archivo}`** y aparecerá automáticamente."
        )


def mostrar_paso(numero: int, paso: dict) -> None:
    """Dibuja un paso individual: número grande + texto + (imagen) + (tip)."""
    # Tarjeta con número y texto de la instrucción
    st.markdown(
        f'<div class="tarjeta-paso">'
        f'<span class="num-paso">{numero}</span>{paso["texto"]}'
        f'</div>',
        unsafe_allow_html=True,
    )
    # Imagen (real o placeholder), solo si el paso la define
    if paso.get("imagen"):
        mostrar_imagen(paso["imagen"])
    # Consejo destacado, si existe
    if paso.get("tip"):
        st.markdown(
            f'<div class="tip-box">💡 <b>Consejo:</b> {paso["tip"]}</div>',
            unsafe_allow_html=True,
        )


def render_modulo_estandar(clave: str) -> None:
    """
    Dibuja un módulo "normal" (los que tienen 'secciones' y 'pasos').
    Cada sección se muestra dentro de un expander para no saturar la vista.
    """
    modulo = MODULOS[clave]
    st.title(modulo["titulo"])
    st.markdown(modulo["intro"])
    st.divider()

    # Cada sección se abre/cierra; la primera viene abierta por comodidad.
    for i, seccion in enumerate(modulo["secciones"]):
        with st.expander(seccion["nombre"], expanded=(i == 0)):
            for numero, paso in enumerate(seccion["pasos"], start=1):
                mostrar_paso(numero, paso)

    # Botón para marcar el módulo como completado (control de avance).
    st.divider()
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("✅ Marcar como aprendido", key=f"btn_{clave}"):
            st.session_state.completados.add(clave)
            st.balloons()  # pequeña celebración visual
    with col2:
        if clave in st.session_state.completados:
            st.success("¡Muy bien! Ya marcaste este módulo como aprendido. 🎉")


# ==============================================================================
# 5) ESTADO Y BARRA LATERAL DE NAVEGACIÓN
# ==============================================================================
# 'session_state' recuerda datos mientras la persona usa la app (ej: qué
# módulos ya completó). Lo inicializamos una sola vez.
if "completados" not in st.session_state:
    st.session_state.completados = set()

with st.sidebar:
    st.markdown("## 🌱 Tutorial Agripredial")
    st.caption("Guía para el **Jefe de Campo**")
    st.divider()

    # Menú de navegación: una opción por módulo. Usamos los títulos como
    # etiquetas visibles y guardamos la 'clave' interna correspondiente.
    etiquetas = [m["titulo"] for m in MODULOS.values()]
    claves = list(MODULOS.keys())
    seleccion = st.radio(
        "📖 Elige una sección:",
        options=claves,
        format_func=lambda c: MODULOS[c]["titulo"],
        label_visibility="visible",
    )

    st.divider()
    # Barra de progreso: cuántos de los módulos "de aprendizaje" se completaron.
    modulos_aprendizaje = [k for k, v in MODULOS.items() if not v.get("es_especial")]
    total = len(modulos_aprendizaje)
    hechos = len(st.session_state.completados & set(modulos_aprendizaje))
    st.markdown(f"**Tu progreso:** {hechos} de {total} módulos")
    st.progress(hechos / total if total else 0)

    if hechos == total and total > 0:
        st.success("🏆 ¡Completaste todo el tutorial!")

    st.divider()
    st.link_button("🌐 Ir a Agripredial (sitio real)", URL_AGRIPREDIAL)
    st.caption("Esta app es solo un tutorial y no guarda ningún dato.")


# ==============================================================================
# 6) RENDER DE LA PÁGINA SEGÚN LA SELECCIÓN
# ==============================================================================

# ---- Página: INICIO ----------------------------------------------------------
if seleccion == "inicio":
    st.title("🌱 Bienvenido/a al Tutorial de Agripredial")
    st.markdown(
        "### Aprende a usar **Agripredial** como Jefe de Campo, paso a paso y a tu ritmo."
    )
    st.markdown(
        "Esta guía interactiva te enseña a manejar el sistema sin miedo a "
        "equivocarte, porque **aquí nada es real**: es solo para practicar y aprender. 😊"
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 👀 Mira")
        st.write("Cada tarea se explica con pasos numerados y capturas de pantalla.")
    with col2:
        st.markdown("#### 🖱️ Practica")
        st.write("Cuando te sientas listo/a, abre Agripredial y repite los pasos.")
    with col3:
        st.markdown("#### ✅ Avanza")
        st.write("Marca cada módulo como aprendido y observa cómo crece tu progreso.")

    st.divider()
    st.markdown("#### 📚 ¿Cómo está organizado el tutorial?")
    st.markdown(
        "Usa el **menú de la izquierda** para moverte. Te recomendamos seguir este orden:"
    )
    for clave, modulo in MODULOS.items():
        if clave not in ("inicio",):
            st.markdown(f"- **{modulo['titulo']}**")

    st.info(
        "👉 **Primer paso recomendado:** revisa la sección "
        "**📚 Conceptos básicos** para entender cómo se organiza el sistema."
    )

# ---- Página: CONCEPTOS BÁSICOS -----------------------------------------------
elif seleccion == "conceptos":
    st.title("📚 Conceptos básicos")
    st.markdown(
        "Antes de empezar, entendamos cómo **Agripredial organiza la información**. "
        "Todo sigue una estructura de mayor a menor, como cajas dentro de cajas:"
    )

    # Representación visual sencilla de la jerarquía geográfica.
    st.markdown(
        """
        <div style="font-size:1.3rem; line-height:2.2; padding:10px 0;">
        🏢 <b>Empresa</b><br>
        &nbsp;&nbsp;&nbsp;⬇️<br>
        🌾 <b>Campo</b> &nbsp; <span style="color:#777;">(terreno, se sube con archivo KML)</span><br>
        &nbsp;&nbsp;&nbsp;⬇️<br>
        📍 <b>Sector</b> &nbsp; <span style="color:#777;">(parte del campo, tiene número de plantas)</span><br>
        &nbsp;&nbsp;&nbsp;⬇️<br>
        🍇 <b>Cuartel</b> &nbsp; <span style="color:#777;">(parte del sector, tiene código de certificación)</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    st.markdown("#### 🌱 Además, dentro de los sectores se registra:")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Cultivos y variedades**")
        st.write("Qué se planta (ej: cerezo) y sus variedades (ej: Bing, Santina).")
    with c2:
        st.markdown("**Personas del equipo**")
        st.write("Jefes de campo (responsables de un campo) y supervisores (de un sector).")

    st.divider()
    st.markdown("#### 📋 Y para organizar el trabajo en terreno:")
    c3, c4 = st.columns(2)
    with c3:
        st.markdown("**Categorías de trabajo**")
        st.write("Agrupan las labores: poda, riego, cosecha, etc.")
    with c4:
        st.markdown("**Planillas de labores**")
        st.write("Formularios para registrar los datos de cada labor.")

    st.info("💡 Recuerda esta estructura: te ayudará a no perderte en los próximos módulos.")

# ---- Página: GLOSARIO --------------------------------------------------------
elif seleccion == "glosario":
    st.title("❓ Glosario y ayuda")
    st.markdown("Términos que aparecen en el sistema, explicados de forma sencilla:")

    glosario = {
        "Archivo KML": "Un mapa digital del terreno. Dibuja los límites de un campo, sector o cuartel sobre un mapa.",
        "Campo": "Un terreno de la empresa agrícola.",
        "Sector": "Una parte dentro de un campo. Tiene un número de plantas.",
        "Cuartel": "Una parte dentro de un sector. Tiene un código de certificación.",
        "Cultivo": "Lo que se planta en un sector (por ejemplo, cerezo o uva).",
        "Variedad": "Un tipo específico dentro de un cultivo (por ejemplo, la variedad Bing del cerezo).",
        "Categoría de trabajo": "Grupo que clasifica las labores agrícolas (poda, riego, cosecha...).",
        "Planilla de labores": "Formulario para anotar los datos de una labor en terreno.",
        "Parámetro / Dato": "Cada cosa que se anota en una planilla (kilos, hora, estado de la planta...).",
        "Frecuencia": "Cada cuánto tiempo se realiza una labor.",
        "Nivel": "Indica si la labor se hace a nivel de campo, sector o cuartel.",
        "Supervisor": "Persona responsable de un sector.",
        "Jefe de campo": "Persona responsable de un campo (¡ese eres tú!).",
    }
    for termino, definicion in glosario.items():
        with st.expander(f"📌 {termino}"):
            st.write(definicion)

    st.divider()
    st.markdown("#### 🆘 ¿Necesitas más ayuda?")
    st.write(
        "Si tienes dudas que este tutorial no resuelve, contacta al equipo de soporte "
        "de tu empresa o al administrador del sistema Agripredial."
    )

# ---- Páginas: MÓDULOS ESTÁNDAR -----------------------------------------------
else:
    render_modulo_estandar(seleccion)
