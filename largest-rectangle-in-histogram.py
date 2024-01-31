class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = [-1]
        for i, height in enumerate(heights):
            while stack[-1] != -1 and height <= heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                result = max(result, cur_height * cur_width)
            stack.append(i)
        while stack[-1] != -1:
            cur_height = heights[stack.pop()]
            cur_width = len(heights) - stack[-1] - 1
            result = max(result, cur_height * cur_width)
        return result


