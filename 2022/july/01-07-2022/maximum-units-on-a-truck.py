class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result = 0

        for boxes, units in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            boxesToAdd = boxes if boxes <= truckSize else truckSize
            result += boxesToAdd * units
            truckSize -= boxesToAdd

        return result
