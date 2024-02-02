#input do usuário
texto = input('Texto: ')
#Iniciando Variáveis
letras = 0
palavras = 1
sentencas = 0

for caractere in texto:
#Contar letras
    if caractere.isalpha():
        letras+=1
#Contar palavras
    elif caractere == ' ':
        palavras+=1    
#Contar frases
    elif caractere == '!' or caractere == '?' or caractere == '.':
        sentencas+=1
#Printando informações no console
print('Letras:',letras,'\nPalavras:',palavras,'\nSentençass:',sentencas)
#Letras por 100 palavras
l = letras/palavras * 100
#Sentenças por 100 palavras
s = sentencas/palavras *100
#Aplicando a formula
formula = 0.0588 * l - 0.296 * s -15.8
#Printando Grade
if int(formula) < 1 :
    print('Before Grade 1')
elif int(formula) > 16:
    print('Grade 16+')
else:
    print('Grade: {:.0f}'.format(formula))
