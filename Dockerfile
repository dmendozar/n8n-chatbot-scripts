# Empezamos desde la imagen oficial de n8n
FROM n8nio/n8n:latest

# Cambiamos al usuario root temporalmente para poder instalar paquetes
USER root

# El sistema base de n8n usa 'apk' para instalar.
# Instalamos python3, pip, y las librerías de Python usando el gestor del sistema 'apk'.
# Los nombres de los paquetes en Alpine son 'py3-requests' y 'py3-beautifulsoup4'.
RUN apk add --no-cache python3 py3-pip py3-requests py3-beautifulsoup4

# Por seguridad, volvemos al usuario 'node' con menos privilegios
USER node