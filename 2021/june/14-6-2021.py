"""
1710. Maximum Units on a Truck
https://leetcode.com/problems/maximum-units-on-a-truck/
"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_boxes = sorted(boxTypes, key=lambda x: -x[1])
        result = 0
        for box_count, box_units in sorted_boxes:
            count = min(truckSize, box_count)
            truckSize -= count
            result += count * box_units
        return result
