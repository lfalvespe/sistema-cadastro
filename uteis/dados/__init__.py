def leiaint(msg):
  try:
    n = int(input(msg))
  except (ValueError, TypeError):
    print('\033[31mErro: Digite um número inteiro válido.\033[m')
  except(KeyboardInterrupt):
    print('\033[31mO usuário cancelou a digitação.\033[m')
    return 0
  else:
    return n

def linha(tam = 38):
  return '-'*tam

def cabecalho(texto):
  print(linha())
  print(texto.center(42))
  print(linha())

def menu(lista):
  cabecalho('\033[30;47mMenu Principal:\033[m')
  c = 1
  for item in lista:
    print(f'\033[31m{c}\033[m - \033[34m{item}\033[m')
    c +=1
  print(linha())
  
  opcao = leiaint('\033[32mSua opção: \033[m')
  return opcao


