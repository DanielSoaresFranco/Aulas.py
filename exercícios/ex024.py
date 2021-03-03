city = str(input('Digite a cidade: ')).strip()
print('Essa cidade tem Santo no nome? {}'.format(city[:5].lower() == 'santo'))
