from collections import defaultdict
from itertools import groupby
from pprint import pprint
from trueskill import Rating, rate_1vs1
import trueskill

initialElo = 1000.0
trueskill.setup(initialElo,initialElo/3,initialElo/6,initialElo/300,0.25,None)
alice = Rating()
bob = Rating()



print(alice)
print(bob)

alice, bob = rate_1vs1(alice, bob,drawn=False)
alice, bob = rate_1vs1(alice, bob,drawn=False)
alice, bob = rate_1vs1(alice, bob,drawn=False)
alice, bob = rate_1vs1(alice, bob,drawn=False)
alice, bob = rate_1vs1(alice, bob,drawn=False)
alice, bob = rate_1vs1(alice, bob,drawn=True)
#alice, bob = rate_1vs1(alice, bob, drawn=True)

print(alice)
print(bob)
print(alice.mu)