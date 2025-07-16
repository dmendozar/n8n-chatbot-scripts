# Empezamos desde la imagen oficial de n8n
FROM n8nio/n8n:latest

# Cambiamos al usuario root temporalmente para poder instalar paquetes
USER root

# El sistema base de n8n usa 'apk' para instalar.
# Instalamos python3 y pip, además de las herramientas de compilación necesarias para algunas librerías.
RUN apk add --no-cache python3 py3-pip build-base

# Ahora usamos pip para instalar las librerías de Python que nuestro script necesita
RUN pip3 install requests beautifulsoup4

# Por seguridad, volvemos al usuario 'node' con menos privilegios
USER node