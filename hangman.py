from ast import Assign


class Hangman:
    def __init__(self) -> None:
        self.word = list()
        self.tries = list()
        self.interface = list()
        self.vida = 5

    def setWord(self, word) -> None:
        for letter in word:
            self.word.append(letter)
        self.interface = ['_'] * len(self.word)
    
    def show(self):
        if len(self.interface) == 0:
            for letter in self.word:
                unknow = ' '.join(self.interface)
        else: 
            unknow = ' '.join(self.interface)

        return f'Lifes: {self.vida} - Word: {unknow} '

    def assign(self, letter): 
        position = 0
        for unknown in self.word:
            if unknown == letter:
                self.interface[position] = letter
            position += 1


    def play(self):
        self.show()
        word = self.setWord(input('Ingrese palabra: '))
        letter = input('Ingrese una letra: ')
        if letter not in self.intentos:
            self.riesgo += 1
        self.tries.append(letter)

if __name__=='__main__':
    hangman = Hangman()
    hangman.setWord('ahorcado')
    
    print(hangman.assign('a'))
    print(hangman.show())

    print(hangman.assign('o'))
    print(hangman.show())

    print(hangman.assign('l'))
    print(hangman.show())

    print(hangman.assign('d'))
    print(hangman.show())
