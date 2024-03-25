cards = list(sorted(map(int, input().split())))
unique_cards = {crd: cards.count(crd) for crd in cards}
if len(unique_cards) == 1:
    print('Шулер')
else:
    count = sorted(list(unique_cards.values()))
    if count == [1, 4]:
        print('Каре')
    elif count == [2, 3]:
        print('Фулл Хаус')
    elif cards == list(range(cards[0], cards[0] + 5)):
        print('Стрит')
    elif count == [1, 1, 3]:
        print('Сет')
    elif count == [1, 2, 2]:
        print('Две пары')
    elif count == [1, 1, 1, 2]:
        print('Пара')
    else:
        print('Старшая карта')