def conversao(cm):
  Polegadas = cm/2.54
  arquivo= open('documento.txt', 'a+')
  arquivo.write(f'{cm} cintímetros é %.3f em polegadas.\n' %(Polegadas))