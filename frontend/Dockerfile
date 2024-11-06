# Usamos una imagen base de Node.js para construir el proyecto
FROM node:14 AS build

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos package.json y package-lock.json para instalar dependencias
COPY package*.json ./

# Instalamos las dependencias
RUN npm install

# Copiamos el resto del código de la aplicación
COPY . .

# Construimos la aplicación para producción
RUN npm run build

# Usamos una imagen base de Nginx para servir la aplicación
FROM nginx:alpine

# Copiamos los archivos de la build de React generados al directorio de Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Exponemos el puerto 80 para que Nginx sirva la aplicación
EXPOSE 80

# Comando por defecto para ejecutar Nginx
CMD ["nginx", "-g", "daemon off;"]
