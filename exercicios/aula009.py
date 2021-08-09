frase = str('Curso em Vídeo Python')
print(frase[3]) 
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.split())
print('''Lorem Ipsum is simply dummy text of the printing 
  and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s,
      when an unknown printer took a galley of type and
         scrambled it to make a type specimen book. It
            has survived not only five centuries, but also 
               the leap into electronic typesetting, remaining
                  .''') # improme no shape do texto
print(frase.count('o')) # Case sensitive (o != O)
print(frase.upper().count('O')) # joga tudo Upper e procura quantos 'O' tem
print(len(frase.strip())) # comprimento da string com espaços excedentes retirados
print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Android') # transformação de string com atribuição a variável principal
print(frase)
print('Curso' in frase)
print(frase.find('Curso')) #mostra a posição inicial da palavra
print(frase.find('Vídeo'))
print(frase.find('vídeo')) # -1 não existe
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido)
print(dividido[0]) # printar o split do índice 0
print(dividido[2][3]) # dentro do split de índice 2; mostrar a letra de índice 3
print(len(frase)) # comprimento
print(len(dividido)) # comprimento dos índices split (quantos tem)