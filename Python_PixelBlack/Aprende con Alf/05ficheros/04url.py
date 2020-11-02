def palabras(url):
    '''
    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    
    try:
        file=request.urlopen(url)
        print(file)
    except(URLError):
        return('La URL {0} no existe.'.format(url))

    else:
        content = file.read()
        return(len(content.split()))
a='Aprende con Alf/05ficheros/url.txt'
b=open(a)
palabras(b.readline())
