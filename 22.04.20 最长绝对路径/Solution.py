class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res =[]
        arr=input.split('\n')
        cur=[]
        #cur[i] 记录每一层
        for i in arr:
            num = i.count('\t')
            item = i.replace('\t','')
            if len(cur)>num:
                cur[num]=item
            else:
                cur.append(item)
            if item.count('.')>0:
                res.append('/'.join(cur[0:num+1]))
        return max([len(x) for x in res])if len(res)>0 else 0

input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
solution = Solution()
print(solution.lengthLongestPath(input))