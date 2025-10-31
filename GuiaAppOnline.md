📄 Contenido para guia_streamlit.md
(copia desde aquí hasta el final)
# 📘 GUÍA PASO A PASO  
## Despliegue de una App de Streamlit en Streamlit Community Cloud  
### (Windows y macOS)

---

## 🧭 Índice
1. Introducción  
2. Crear un entorno virtual  
3. Instalar librerías necesarias  
4. Crear la app de Streamlit  
5. Generar el archivo `requirements.txt`  
6. Crear un repositorio en GitHub  
7. Subir tu app a GitHub  
8. Desplegar tu app en Streamlit Cloud  
9. Sincronizar cambios futuros  
10. Recomendaciones finales  

---

## 1️⃣ Introducción

En esta guía aprenderás a **subir tu aplicación de Streamlit a Internet** usando el servicio gratuito **Streamlit Community Cloud**, paso a paso.  
Cada estudiante desplegará **su propia app individual**, creada desde cero.  

**Requisitos previos:**
- Tener **Python 3.8 o superior** instalado.  
- Tener **Visual Studio Code (VS Code)** instalado.  
- Saber ejecutar apps de Streamlit localmente (`streamlit run app.py`).  

---

## 2️⃣ Crear un entorno virtual

El entorno virtual te permite aislar las librerías de tu proyecto.

Abre **VS Code** y crea una **carpeta nueva** (por ejemplo: `mi_app_streamlit`).

Luego abre una **terminal** en esa carpeta (`Ctrl + ñ` o `View → Terminal`).

### 🔹 En Windows:
```bash
python -m venv venv
venv\Scripts\activate

🔹 En macOS:
python3 -m venv venv
source venv/bin/activate

Cuando el entorno esté activo, verás (venv) al inicio de la línea en la terminal.

3️⃣ Instalar librerías necesarias
Con el entorno activado, instala las librerías base para tu app:
pip install streamlit yfinance matplotlib

Verifica las instalaciones con:
pip list


4️⃣ Crear la app de Streamlit
Crea un archivo llamado app.py dentro de tu carpeta del proyecto y copia este código:
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("📈 Mi Primera App de Datos Financieros")

ticker = st.text_input("Ingresa el símbolo de una acción (ejemplo: AAPL, MSFT, TSLA):", "AAPL")

if ticker:
    data = yf.download(ticker, period="1y")
    st.write(f"Datos de {ticker}:")
    st.dataframe(data.tail())

    fig, ax = plt.subplots()
    ax.plot(data.index, data["Close"], label="Cierre", color="blue")
    ax.set_title(f"Precio de cierre de {ticker} - Último año")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Precio (USD)")
    ax.legend()
    st.pyplot(fig)

Guarda el archivo y pruébalo en local:
streamlit run app.py


5️⃣ Generar el archivo requirements.txt
Este archivo le dirá a Streamlit Cloud qué librerías instalar.
Ejecuta en la terminal:
pip freeze > requirements.txt

Verifica que el archivo requirements.txt aparezca en tu carpeta.

6️⃣ Crear un repositorio en GitHub


Ve a https://github.com.


Crea una cuenta (si no la tienes).


Pulsa New repository.


Ponle nombre, por ejemplo: mi-app-streamlit.


Marca la opción “Add a README file”.


Haz clic en Create repository.



7️⃣ Subir tu app a GitHub (desde VS Code)


En VS Code, abre la paleta de comandos (Ctrl + Shift + P).


Escribe: Git: Initialize Repository → selecciona tu carpeta del proyecto.


Luego usa: Git: Add Remote y pega la URL de tu repositorio GitHub (algo como https://github.com/tuusuario/mi-app-streamlit.git).


Agrega tus archivos:
git add .
git commit -m "Primera versión de mi app"
git push -u origin main




💡 Si Git no está configurado en tu PC, VS Code te pedirá iniciar sesión con GitHub. Acepta y sigue las instrucciones en pantalla.


8️⃣ Desplegar tu app en Streamlit Cloud


Ve a https://share.streamlit.io.


Inicia sesión con tu cuenta de GitHub.


Pulsa “New app”.


Selecciona tu repositorio y elige:


Branch: main


File path: app.py




Haz clic en Deploy 🚀


Tu app se desplegará en línea (puede tardar unos 2 minutos).
Obtendrás una URL del tipo:
https://nombreusuario-mi-app-streamlit.streamlit.app


9️⃣ Sincronizar cambios futuros
Cada vez que modifiques tu app en VS Code:
git add .
git commit -m "Actualización del gráfico"
git push

Streamlit Cloud detectará el cambio automáticamente y actualizará tu app en línea.

🔟 Recomendaciones finales
✅ Usa un entorno virtual por cada proyecto.
✅ No subas el directorio venv a GitHub (Git lo ignora automáticamente).
✅ Evita usar archivos grandes o datos privados.
✅ Puedes cambiar el título, colores o estructura de tu app para personalizarla.

🎓 Conclusión
Ahora cada alumno puede tener su app de Streamlit en línea, mostrando datos reales de Yahoo Finance, sin pagar servidores ni usar Docker.
Este flujo es el mismo que usan los desarrolladores para publicar prototipos de análisis de datos y dashboards interactivos.

---

¿Deseas que te agregue al final del documento una **portada personalizada** con el logo de tu institución o tu nombre como docente (por ejemplo, “Guía elaborada por [Tu Nombre] – Curso de Programación de Datos”)?  
Puedo generarte esa portada en formato Markdown o imagen para que aparezca en el PDF.
