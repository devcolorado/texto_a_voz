"""Este programa sirve para convertir un artículo existente en un 
archivo de audio reproducible en formato mp3 por medio de la url
de dicho articulo"""

#Importamos los modulos que usaremos
from newspaper import Article
from gtts import gTTS
import nltk

#Descargamos el tokenizador nltk para ayudar al modulo newspaper con la 
#tokenizacion del texto del articulo y su posterior conversion a texto
#con el modulo gtts
nltk.download("punkt")

#pedimos la url de la pagina cuyo texto queremos convertir a audio
#presuponiendo que el articulo estará en español
articulo = Article(input("Ingresa la url de la pagina: "), language="es")

#Descagarmos y analizamos el contenido del articulo
articulo.download()
articulo.parse()

#Pasamos la variable de texto a audio con la funcion gtts
audio = gTTS(articulo.text, lang="es")

#Guardamos el audio con el formato mp3
audio.save("audio.mp3")