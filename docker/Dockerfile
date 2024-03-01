# Usa la imagen base de Python 3.11.5
FROM python:3.11.5

# Clona el repositorio de GitHub en el contenedor en /app
RUN git clone https://github.com/JorgeMIng/PDF_ArticleAnlyzer.git /app

# Establece el directorio de trabajo en /app
WORKDIR /app

RUN cd /app

# Cambia al directorio del repositorio antes de instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Cambia al directorio del repositorio antes de actualizar los módulos desde GitHub
RUN git submodule update --init --recursive

# Comando para ejecutar tu aplicación
CMD ["python", "main.py", "visualize.word_cloud"] && ["python", "main.py", "visualize.stadistic"] && ["python", "main.py", "visualize.links_search"] && tail -f /dev/null