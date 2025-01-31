# Реализуйте итератор колоды карт (52 штуки) CardDeck:
# Каждая карта представлена в виде строки типа "2 Пик".
# При вызове функции next() будет представлена следующая карта.
# По окончании перебора всех элементов возникнет ошибка StopIteration

def cards():
    card_deck = iter(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'K', 'T'])
    card_deck_copy = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'K', 'T']

    cart_suit = ['пик', 'бубей', 'кресте', 'червей']

    card = input('Enter your card: ').split(' ')

    if card[1].lower() not in cart_suit:
        print('Invalid card')
    else:
        if card[0] not in card_deck_copy:
            print('Invalid card')
        elif card[0] == 'T':
            print('Your card is highest')
        else:
            try:
                while True:
                    i = next(card_deck)

                    if i == card[0]:
                        print(f'Next card is {next(card_deck)} {card[1]}')
                        break
            except StopIteration:
                print('The end')

cards()
