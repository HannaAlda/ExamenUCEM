# Usa una imagen de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt en /app
COPY requirements.txt /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del backend
COPY . /app

# Expone el puerto en el que corre Flask (5000)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
