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
        n = self.__len__()  #  get the total number of cards
        #  Fischer-Yates shuffle loop 
        for i in range(n -1, 0, -1):
            j = random.randint(0, i)
            
            #  swap cards to "shuffle" the deck
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
            
        return

    def deal(self):
        n = self.__len__()
        if n <= (52/4):
            raise ResourceWarning("low deck")
        return

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
