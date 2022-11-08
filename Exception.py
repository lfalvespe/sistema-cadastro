try:

  a = 1
  b = 0
  c = a/b

# Executa se der erro.
except Exception as erro:

  print(f'Problema encontrado {erro.__class__}')

else:
  print(f'Resultado {c}') # executa se der certo

# Executa sempre independente se der certo ou se der erro.
finally:
  print('Volte sempre!!!') 
