import sys
#armazenando argv em uma variável
argumentos = sys.argv
#Verificando se há apenas um inteiro positivo como argumento de linha
if len(argumentos) !=2 or not argumentos[1].isdigit():
    print('Usage: ./caesar key')
    sys.exit(1)
else:
#Armazenando o argumento na variável key
    key = int(argumentos[1])
    alphaASCII = 0
    cyphertext = ''
#Input do usuário
    plaintext = input('Plaintext: ')
#Percorrendo plaintext verificando se é alfabeto
    for i in plaintext:
        if i.isalpha():
#Verificando se é maiúsculo e aplicando a formula para conversão
            if i.isupper():
                i = ord(i)-65
                alphaASCII = (i + key) % 26
                cyphertext+=chr(alphaASCII+65)
#Verificando se é minúsculo e aplicando a formula para conversão
            else:
                i = ord(i) - 97
                alphaASCII = (i + key) % 26
                cyphertext+=chr(alphaASCII + 97)
#Se não for alfabeto apenas armazena o char sem converter
        else:
            cyphertext += i
#imprimindo o resultado
    print('Cyphertext: %s'% cyphertext)