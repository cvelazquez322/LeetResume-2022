def recur(ilist, scorea, scoreb, turn):
    try:
       # print(scorea,scoreb)
        if turn % 2 == 0:
            scorea += ilist[0]
        else:
            scoreb += ilist[0]
    except:
        if scorea > scoreb:
            return True
        else:
            return False
    turn += 1
    return recur(ilist[1:], scorea, scoreb, turn) or recur(ilist[:-1], scorea, 
        scoreb, turn)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
                return True
        #return recur(piles, 0, 0, 0) or recur(piles[::-1], 0,0,0)
  #      astone = 0
  #      bstone = 0
  #      i = 0
  #      while len(piles) > 0:
  #          if piles[0] > piles[-1]:
  #              if i % 2 == 0:
  #                  astone += piles[0]
  #              else:
  #                  bstone += piles[0]
  #              piles.pop(0)
  #          else: 
  #              if i % 2 == 0:
  #                  astone += piles[-1]
  #              else:
  #                  bstone += piles[-1]
  #              piles.pop(-1)
  #          i += 1
  #      if astone > bstone:
  #          return True
  #      else:
  #          return False