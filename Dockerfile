# Empezamos desde la imagen oficial de n8n
FROM n8nio/n8n:latest

# Cambiamos al usuario root para instalar paquetes
USER root

# Instalamos python3 y las librerías necesarias
RUN apk add --no-cache python3 py3-pip py3-requests py3-beautifulsoup4

# --- CAMBIO IMPORTANTE ---
# Copiamos el script al directorio de datos principal de n8n, llamado /data
COPY scraper.py /data/

# Volvemos al usuario normal de n8n
USER node