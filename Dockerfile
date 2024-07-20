# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al directorio de trabajo
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
