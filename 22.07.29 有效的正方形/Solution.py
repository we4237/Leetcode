import collections
import itertools
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def get_distance(a,b):
            return (a[0]-b[0])**2+(a[1]-b[1])**2
        mydict = collections.defaultdict(int)
        for i,j in itertools.combinations([p1,p2,p3,p4],2):
            mydict[get_distance(i,j)]+=1
        if len(mydict) != 2:return False
        x,y=min(mydict.keys()),max(mydict.keys())
        if mydict[y]!=2 or mydict[x]!=4:return False
        if 2*x!=y:return False
        return True