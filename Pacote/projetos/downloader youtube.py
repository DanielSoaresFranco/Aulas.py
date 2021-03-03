from webbrowser import open

url = str(input('Cole a URL do vídeo aqui: '))
https = 'https://' in url
www = 'www.' in url

if https is True and www is True:
    num = 12
elif https is False and www is True:
    num = 4
elif https is True and www is False:
    num = 8
else:
    num = 0

downlod = url[:num] + "ss" + url[num:]

open(downlod)

print('O seu vídeo já será baixado!')
