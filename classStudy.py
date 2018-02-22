'''
class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


e = Example(8, 10)
print('The sum of two number:', e.add())
'''
'''
class Student:
    def __init__(self, Name, Age, ID, Marks):
        self.Name = Name
        self.Age = Age
        self.ID = ID
        self.Marks = Marks
Student1=Student('Abol Basher', '28', '8172615', '86' )
print('Information of Student:', Student1.Name, Student1.Age, Student1.ID, Student1.Marks)
'''
'''
from string import punctuation


class Analyzer:
    def __init__(self, s):
        for c in punctuation:
            s = s.replace(c, '')
            s = s.lower()
            self.words = s.split()

    def number_of_words(self):
        return len(self.words)

    def starts_with(self, s):
        return len(w for w in self.words if w[:len(s)] == s)

    def number_with_length(self, n):
        return len([w for w in self.words if len(w) == n])


s = 'This is a test of the class.'
analyzer = Analyzer(s)
print(analyzer.words)
print('Number of words:', analyzer.number_of_words())
print('Number of words starting with "t":', analyzer.starts_with('t'))
print('Number of 2-letter words:', analyzer.number_with_length(2))
'''
# Inheritance
'''
class Parent:
    def __init__(self, a):
        self.a = a
    def method1(self):
        print(self.a*2)
    def method2(self):
        print(self.a+'!!!')
class Child(Parent):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def method1(self):
        print(self.a*7)
    def method3(self):
        print(self.a + self.b)
p = Parent('hi')
c = Child('hi', 'bye')
print('Parent Method 1:', p.method1())
print('Parent Method 2:', p.method2())
print()
print('Child method 1:', c.method1())
print('Child method 2:', c.method2())
print('Child method 2:', c.method3())
'''
'''
class Parent:
    def __init__(self, a):
        self.a = a
    def print_var(self):
        print("The value of this class's variables are:")
        print(self.a)
class Child(Parent):
    def __init__(self, a, b):
        Parent.__init__(Self, a)
        self.b = b
    def print_var(self):
        Parent.print_var(self)
        print(self.b)
'''

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        names = ['Jack', 'Queen', 'King', 'Ace']
        if self.value <= 10:
            return '{} of {}'.format(self.value, self.suit)
        else:
            return '{} of {}'.format(names[self.value-11], self.suit)
import random
class Card_group:
    def __init__(self, cards=[]):
        self.cards = cards
    def nextCard(self):
        return self.cards.pop(0)
    def hasCard(self):
        return len(self.cards) > 0
    def size(self):
        return len(self.cards)
    def shuffle(self):
        random.shuffle(self.cards)
class Standard_deck(Card_group):
    def __init__(self):
        self.cards = []
        for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for v in range(2, 15):
                self.cards.append(Card(v, s))
class Pinochle_deck(Card_group):
    def __init__(self):
        self.cards = []
        for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']*2:
            for v in range(9, 15):
                self.cards.append(Card(v, s))
deck = Standard_deck()
deck.shuffle()
new_card = deck.nextCard()
print('\n', new_card)
choice = input("Higher (h) or lower (l):")
streak = 0
while (choice == 'h' or choice == 'l'):
    if not deck.hasCard():
        deck = Standard_deck()
        deck.shuffle()
    old_card = new_card
    new_card = deck.nextCard()
    if(choice.lower() == 'h' and new_card.value > old_card.value or \
            choice.lower() == 'l' and new_card.value < old_card.value):
        streak = streak + 1
        print("Right ! That's", streak, "in a row!")
    elif (choice.lower() == 'h' and new_card.value < old_card.value or \
            choice.lower() == 'l' and new_card.value > old_card.value):
        streak = 0
        print('Wrong.')
    else:
        print('Push:')
    print('\n', new_card)
    choice = input("Higher (h) or lower (l):")
