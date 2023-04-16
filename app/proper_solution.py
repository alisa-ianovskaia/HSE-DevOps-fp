# Leetcode problem №42: Trapping Rain Water

# Given n non-negative integers representing an elevation map
# where the width of each bar is 1,
# compute how much water it can trap after raining.

# Example
# Input: heights = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The elevation map is
# represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.


def calc_rain_water(heights):
    '''
    Takes list of integers (heights in "elevation map") as a parameter.
    Returns integer: number of water blocks from given list.
    '''

    water_blocks = 0
    blocks = len(heights)
    left_max = [heights[0]] + [0] * (blocks - 1)
    right_max = [0] * (blocks - 1) + [heights[blocks - 1]]

    for i in range(1, blocks):
        left_max[i] = max(left_max[i - 1], heights[i])

    for i in range(blocks - 2, -1, -1):
        right_max[i] = max(heights[i], right_max[i + 1])

    for i in range(blocks):
        water_blocks += min(left_max[i], right_max[i]) - heights[i]

    return water_blocks
