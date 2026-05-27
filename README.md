# 🌱 Tutorial Interactivo Agripredial — Jefe de Campo

Aplicación web hecha con **Python + Streamlit** que funciona como un **tutorial
interactivo** para enseñar a los *jefes de campo* (sector agrícola) a usar la
plataforma externa **Agripredial** ([https://www.agripredial.cl/](https://www.agripredial.cl/)).

> ⚠️ Esta aplicación es **independiente** de Agripredial. Su único fin es
> **educativo**: no se conecta a ningún sistema real ni guarda datos.

---

## 📋 ¿Qué enseña?

El tutorial está dividido en módulos basados en el manual oficial del rol
"Jefe de Campo":

1. 🏠 **Inicio** — bienvenida y cómo usar la guía.
2. 📚 **Conceptos básicos** — la jerarquía Empresa → Campo → Sector → Cuartel.
3. 🔑 **Acceso al sistema** — ingresar y salir.
4. 🌾 **Campos** — registrar, consultar, modificar y eliminar.
5. 📍 **Sectores** — gestión completa.
6. 🍇 **Cuarteles** — gestión completa.
7. 🌱 **Cultivos y variedades**.
8. 👥 **Equipo de trabajo** — jefes de campo y supervisores.
9. 🗂️ **Categorías de trabajo**.
10. 📋 **Planillas de labores** — el módulo más completo.
11. ❓ **Glosario y ayuda**.

---

## 🗂️ Estructura del proyecto

```
tutorial-agripredial/
├── app.py              # Código principal de la aplicación Streamlit
├── requirements.txt    # Dependencias (Streamlit)
├── .gitignore          # Archivos que Git debe ignorar
├── README.md           # Este archivo
└── img/                # Carpeta para las capturas de pantalla del tutorial
    └── .gitkeep
```

---

## 🖼️ Cómo agregar las capturas de pantalla

La app ya muestra **recuadros guía** indicando qué imagen va en cada paso y con
qué **nombre exacto** guardarla. Para que aparezca una captura real:

1. Toma la captura de pantalla del paso correspondiente en Agripredial.
2. Guárdala en la carpeta `img/` **con el nombre que indica el recuadro**
   (por ejemplo, `campo_1_empresa.png`).
3. Súbela al repositorio. La imagen aparecerá automáticamente; no hay que tocar
   el código.

Formatos recomendados: `.png` o `.jpg`.

---

## ▶️ Ejecución local (opcional)

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🚀 Despliegue en Streamlit Community Cloud

Ver la sección de despliegue en la conversación o en el manual de entrega.
Resumen: subir este repositorio a GitHub → entrar a
[share.streamlit.io](https://share.streamlit.io) → conectar el repo →
indicar `app.py` como archivo principal → *Deploy*.

---

## 🧩 Personalización

Todo el **texto del tutorial vive en el diccionario `MODULOS`** dentro de
`app.py`. Para cambiar una instrucción, agregar un paso o un consejo, solo se
edita ese diccionario; no es necesario tocar la lógica de la aplicación.
