from urllib import request, error

try:
    site = request.urlopen('http://pudim.com.br/')
except error.URLError:
    print('\033[1;31mNão consegui acessar o site do pudim :(')
else:
    print('\033[1;32mConsegui acessar o site do pudim!')
