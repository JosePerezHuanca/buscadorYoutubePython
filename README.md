# Buscador youtube

Esta es una interfaz que se conecta a la api youtube  V3 para realizar búsquedas y que utiliza un reproductor externo (En este caso PotPlayer) para reproducir los videos.

## Requisitos

- Tener instalado Python
- Ir a [https://console.developers.google.com] para obtener una clave de api.
- Tener instalado PotPlayer.
- Agregar PotPlayer como variable de entorno en windows
- Clonar el repositorio: ` git clone https://github.com/JosePerezHuanca/buscadorYoutubePython `
- Crear un entorno virtual. Por ejemplo con virtualenv: `virtualenv env`
- Para activar el entorno virtual en windows el comando es: ` env\Scripts\activate `
- instalar las dependencias: ` pip install -r requirements.txt `
- La clave debe incluirse en un archivo llamado .env como valor de API_KEY. 
- ejecutar el script ` python main.py `
- Opcionalmente, compilar un ejecutable ya sea con nuitca o pyinstaller.

## Descripción breve de la interfaz

El programa consta de un cuadro de texto para escribir una búsqueda, el botón buscar, una lista de resultados (aproximadamente 50) y un botón para reproducir por cada item que se seleccione en la lista que habre el reproductor PotPlayer con el video.
