# Usa una imagen de Node.js
FROM node:14

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia package.json y package-lock.json
COPY package*.json /app/

# Instala las dependencias
RUN npm install

# Copia el resto del código del frontend
COPY . /app

# Construye la aplicación
RUN npm run build

# Usa una imagen de servidor web para servir la app
FROM nginx:alpine

# Copia los archivos de build de React a nginx
COPY --from=0 /app/build /usr/share/nginx/html

# Expone el puerto 80
EXPOSE 80

# Inicia el servidor
CMD ["nginx", "-g", "daemon off;"]
