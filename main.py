from uteis.dados import *
from uteis.arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoExiste(arq):  
  criarArquivo(arq)

while True:
  resposta = menu(['Mostrar lista de usuários',
     'Cadastrar novo usuário',
     'Sair'])
  
  if resposta == 1:
    # Opção de listar o conteúdo de um arquivo
    lerArquivo(arq)
  elif resposta == 2:
    cabecalho('Novo Cadastro')
    nome = str(input('Nome: '))
    idade = leiaint('Idade: ')
    cadastrar(arq, nome, idade )
  elif resposta == 3:
    cabecalho('Saindo do sistema...Até logo!')
    break
  else:
    print('\n \033[31mErro: Digite uma opção válida!\033[m \n')
  sleep(1.5)
