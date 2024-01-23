from solution import Solution

def testA():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    res = Solution().minimumTotal(triangle)
    ans = 11
    assert res==ans

def testB():
    triangle = [[-10]]
    res = Solution().minimumTotal(triangle)
    ans = -10
    assert res==ans

def testC():
    triangle = [[-1],[-2,-3]]
    res = Solution().minimumTotal(triangle)
    ans = -4
    assert res==ans