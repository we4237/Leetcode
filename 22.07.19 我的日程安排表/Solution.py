
# 直接遍历
# class MyCalendarTwo:
#
#     def __init__(self):
#         self.booked = []
#         self.overlaps = []
#
#     def book(self, start: int, end: int) -> bool:
#         if any(s < end and start < e for s,e in self.overlaps):
#             return False
#         for s,e in self.booked:
#             if s < end and start < e:
#                 self.overlaps.append((max(s,start),min(e,end)))
#         self.booked.append((start,end))
#         return True


# 线段树
# class MyCalendarTwo:
#
#     def __init__(self):
#         self.tree = {}
#
#     def update(self,start:int,end:int,val:int,l:int,r:int,idx:int) -> None:
#         if start > r or end < l :
#             return
#         if start <= l and r <= end:
#             p = self.tree.get(idx,[0,0])
#             p[0] += val
#             p[1] += val
#             self.tree[idx] = p
#             return
#         mid = (l+r)//2
#         self.update(start,end,val,l,mid,2*idx)
#         self.update(start,end,val,mid+1,r,2 * idx + 1 )
#         p = self.tree.get(idx,[0,0])
#         p[0] = p[1] + max(self.tree.get(2*idx,(0,))[0],self.tree.get(2*idx+1,(0,))[0])
#         self.tree[idx] = p
#
#     def book(self, start: int, end: int) -> bool:
#         self.update(start, end - 1, 1, 0, 10 ** 9, 1)
#         if self.tree[1][0] > 2:
#             self.update(start, end - 1, -1, 0, 10 ** 9, 1)
#             return False
#         return True

# 遍历 + 二分




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)