class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = 0
        tmp = []
        nEle = len(triangle)
        if nEle <= 0:
            return 0
        if nEle == 1:
            return triangle[0][0]
        prev = triangle[nEle-1]
        for i in range(nEle-1, 0, -1):
            above = triangle[i-1]
            row = prev
            tmp = []
            for j in range(0, i):
                if row[j] < row[j+1]:
                    t = above[j] + row[j]
                else:
                    t = above[j] + row[j+1]
                tmp.append(t)
            prev = tmp
            print(prev)
        res = prev[0]
        return res
