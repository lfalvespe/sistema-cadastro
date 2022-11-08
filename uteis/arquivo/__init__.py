from uteis.dados import cabecalho

def arquivoExiste(nome):
  try:
    a = open(nome, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True

def criarArquivo(nome):
  try:
    a = open(nome, 'wt+')
    a.close()
  except:
    print('Erro na criação do arquivo')
  else:
    print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
  try:
    a = open(nome, 'rt')
  except:
    print('Erro ao ler o arquivo!')
  else:
    cabecalho('Usuários Cadastrados:')
    for linha in a:
      dado = linha.split(';')
      dado[1] = dado[1].replace('\n', '')
      print(f'{dado[0]:<33} {dado[1]:<3} Anos')
  finally:
    a.close()
      
def cadastrar(arq, nome='DESCONHECIDO', idade=0):
 
  try:
    a = open(arq, 'at')
  except:
    print('Houve um erro na abertura do arquivo!')
  else:
    try:
      a.write(f'{nome};{idade}\n')
    except:
      print('Houve um erro na hora de excrever no arquivo')
    else:
      print(f'Registro de {nome} efetuado com sucesso!')
      a.close()
