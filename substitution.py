#Pegar a chave
import sys
argumentos = sys.argv
#Validar a chave
    #Armazenando alfabeto em uma variável
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
    #Se houver mais de um argumento de linha ou 0 = fim do programa;
    #Se o tamanho do argumento for diferente de 26 = fim do programa;
    #Se o argumento não for alfabeto = fim do programa;
    #Se o argumento não conter os mesmo caracteres da variável alfabeto = fim do programa;
    #Método upper para comparar de igual se o argumento for passado como letra minúscula.
if len(argumentos) != 2 or len(argumentos[1]) != 26 or not argumentos[1].isalpha() or not set(argumentos[1].upper()) == set(alfabeto):#or argumentos[1].isdecimal():
    print('Usage: ./substitution KEY')
    sys.exit(1)
#Pegar plaintext
else: 
    plaintext = input('Plaintext: ')
#Encripitar
    #cyphertext iniciada
    cyphertext = ''
    #armazenando o argumento em arg1
    arg1 = argumentos[1]
    #armazenando o tamanho da variável alfabeto para o loop
    alfabetolen = len(alfabeto)
    #armazenando o tamanho da variável plaintext para o loop
    plaintextlen = len(plaintext)
    #percorrendo o plaintext e verificando se é upper ou lower
    for i in range (plaintextlen):
        if plaintext[i].isupper():
            #Percorrendo o alfabeto e verificando se tal caractere bate com o alfabeto
            #Se sim, faz a letra que está na posição j de arg1 virar upper e depois incrementa na variavel cyphertext
            for j in range (alfabetolen):
                if plaintext[i] == alfabeto[j]: 
                    cyphertext += arg1[j].upper()
        elif plaintext[i].islower():
            #Se lower, antes de incrementar em cyphertext, faz a letra na posição j de arg1 virar lower
            for j in range (alfabetolen):
                if plaintext[i].upper() == alfabeto[j]:
                    cyphertext += arg1[j].lower()
            #se a letra na posição i de plaintext não for alfabética, apenas incrementa na variavel cyphertext
        else:
            cyphertext += plaintext[i]
    #printar cyphertext
    print('Cypher: ',cyphertext)
