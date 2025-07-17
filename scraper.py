# scraper.py
import sys
import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    """
    Toma una URL, descarga su contenido HTML, extrae el texto principal
    y lo imprime en la consola.
    """
    try:
        # Usamos un User-Agent común para parecer un navegador real y evitar bloqueos.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Hacemos la petición GET a la URL con un tiempo de espera de 10 segundos.
        response = requests.get(url, headers=headers, timeout=10)
        # Lanza un error si la petición falla (ej. error 404 o 500).
        response.raise_for_status()

        # Usamos BeautifulSoup para procesar el HTML.
        soup = BeautifulSoup(response.content, 'html.parser')

        # Buscamos la etiqueta <main>, que usualmente contiene el contenido principal.
        # Si no la encuentra, busca <article>. Como último recurso, usa todo el <body>.
        if soup.main:
            main_content = soup.main
        elif soup.article:
            main_content = soup.article
        else:
            main_content = soup.body

        # Extraemos el texto, usando un espacio como separador y eliminando espacios extra.
        content_text = main_content.get_text(separator=' ', strip=True)
        
        # Imprimimos el texto limpio. N8N capturará esta salida.
        print(content_text)

    except requests.exceptions.RequestException as e:
        # En caso de error de conexión, lo imprimimos a la salida de error
        # para que no se mezcle con los resultados correctos en n8n.
        print(f"Error al acceder a la URL: {e}", file=sys.stderr)
        sys.exit(1) # Salimos del script con un código de error

# --- Punto de Entrada del Script ---
if __name__ == '__main__':
    # El script espera recibir la URL como un argumento desde la línea de comandos.
    # sys.argv[0] es el nombre del script, sys.argv[1] es el primer argumento.
    if len(sys.argv) > 1:
        url_to_scrape = sys.argv[1]
        scrape_url(url_to_scrape)
    else:
        print("Error: No se proporcionó una URL como argumento.", file=sys.stderr)
        sys.exit(1) # Salimos del script con un código de error