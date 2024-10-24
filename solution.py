class Solution(object):
    def minimumTotal(self, triangle):
        """
        Calculate the minimum path sum from top to bottom in a triangle.
        
        :param triangle: List[List[int]] - A list of lists of integers representing the triangle.
        :return: int - The minimum path sum.
        """
        # If the triangle is empty, return 0
        if not triangle:
            return 0
        
        # If the triangle has only one row, return the single element
        if len(triangle) == 1:
            return triangle[0][0]
        
        # Initialize the 'prev' list with the last row of the triangle
        prev = triangle[-1]
        
        # Iterate from the second last row to the top row
        for i in range(len(triangle) - 2, -1, -1):
            # Update each element in the current row
            for j in range(len(triangle[i])):
                # Update the element to be the sum of itself and the minimum of the two elements directly below it
                prev[j] = triangle[i][j] + min(prev[j], prev[j + 1])
        
        # The top element of 'prev' now contains the minimum path sum
        return prev[0]
