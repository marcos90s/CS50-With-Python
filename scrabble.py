POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
def compute_score(word):
#    score = 0
#    lenword = len(word)
#    for char in range (lenword):
#        if not word[char].isalpha():
#            score +=0
#        else:
#            score += POINTS[index]
#    return score
    # Iniciando o score com o valor 0
    score = 0
    # Armazenando o tamnho de POINTS
    lenpoints = len(POINTS)
    # Passando por cada caractere de word
    for char in word:
        # Transformando caractere minusculo em ASCII e subtraindo pelo ASCII de 'a'
        index = ord(char.lower()) - ord('a')
        # Se 0 for menor/igual a index e index for menor que o tamanho de POINTS, itera os pontos armazenados em POINTS[index] na variavel score
        if 0 <= index < lenpoints:
            score+= POINTS[index]
    return score
def main():
    word1 = input('Player 1: ')
    word2 = input('Player 2: ')

    score1 = compute_score(word1)
    score2 = compute_score(word2)

    print('Score Player 1: ', score1)
    print('Score Player 2: ', score2)

    if score1 > score2: print('And the Winner is... Player 1!')
    elif score1 < score2: print('And the Winner is...: Player 2!')
    else: print('Empate!')

if __name__ == '__main__':
    main()