def fresh_deck():
    import random
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    # 중첩 for 문으로 52장의 카드를 만들어 리스트 deck을 만든다.
    for i in suits:
        for j in ranks:
            card = {"suit": i, "rank": j}
            deck.append(card)
    random.shuffle(deck)
    # deck을 무작위로 섞는다.
    return deck


def store_members(members):
    file = open("members.txt", "w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips, debt, debtchips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + ',' + str(debt) + "," + str(debtchips) + '\n'
        file.write(line)
    file.close()


def more(message):d
    answer = input(message)
    while not answer == 'y' and answer != 'n':  # (반복 조건):
        answer = input(message)
    return answer == 'y'  # 조건식


def show_cards(cards, message):
    print(message)
    for card in cards:
        print(" ", card["suit"], card["rank"])
        # card를 보기 좋게 한줄에 프린트
def show_cards_listed(cards, message):
    while True:
        try:
            for i in range(0, 5):
                if cards[i][1] == 11:
                    cards[i][1] = "J"
                if cards[i][1] == 12:
                    cards[i][1] = "Q"
                if cards[i][1] == 13:
                    cards[i][1] = "K"
                if cards[i][1] == 14:
                    cards[i][1] = "A"
            break
        except:
            break
    print(message)
    for card in cards:
        print(" ", card[0], card[1])
        # 카드 리스트를 보기 좋게 한줄에 프린트


def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n = n - 1
