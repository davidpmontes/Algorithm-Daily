class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        
        def helper(combo, openLeft, closedLeft):
            if openLeft == 0 and closedLeft == 0:
                answer.append(combo)
                return
            
            if openLeft == closedLeft:
                helper(combo + "(", openLeft - 1, closedLeft)
                return
            
            if openLeft < closedLeft: #have used an "("
                if openLeft > 0:
                    helper(combo + "(", openLeft - 1, closedLeft)
                if closedLeft > 0:
                    helper(combo + ")", openLeft, closedLeft - 1)
                return
        
        helper("", n, n)
        return answer
