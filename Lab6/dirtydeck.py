from playingcard import PlayingCard, CardSuit, _valid_rank_, _convert_to_rank
from collections.abc import Container
import unittest
import random


_full_deck_ = [PlayingCard(s, r) for s in CardSuit for r in range(1, 14)]


class DirtyDeck(Container):

    def __init__(self, *, hide=None):
        self.deck = _full_deck_.copy()
        self.hidden = None
        if hide is not None:
            if not _valid_rank_(hide):
                raise ValueError(f"{hide} is not a card rank")
            self.hidden = _convert_to_rank(hide)

    def __str__(self):
        retstr = ""
        for c in self.deck:
            retstr += f"{str(c)} "
        return retstr

    def __contains__(self, c):
        return c in self.deck

    def __len__(self):
        return len(self.deck)

    def __iter__(self):
        return iter(self.deck)

    def shuffle(self):
        #  copy deck over
        self.deck = _full_deck_.copy()
        #  get the total number of cards
        n = self.__len__()
        #  Fischer-Yates shuffle loop
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)

            #  swap cards to "shuffle" the deck
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

        if self.hidden is not None:
            for i in range(n - 1, -1, -1):
                #  assign the current card to check
                card = self.deck[i]
                #  check if the rank matches
                if card.rank == self.hidden:
                    card_move = self.deck.pop(i)
                    self.deck.append(card_move)
        return

    def deal(self):
        n = self.__len__()
        #  divide by 4 for only 25% of the deck
        if n <= (52 / 4):
            raise ResourceWarning("low deck")
        #  deal by popping the first card on the deck

        return self.deck.pop(0)


if __name__ == "__main__":

    d = DirtyDeck()  # rework as unittests
    print(d)
    print(f"len={len(d)}")

    for rank in [10, "Jack", "Queen", "King", "Ace", "Joker", 2]:
        _ = DirtyDeck(hide=rank)

    try:
        _ = DirtyDeck(hide=15)
    except Exception:
        print("invalid hide fails")
