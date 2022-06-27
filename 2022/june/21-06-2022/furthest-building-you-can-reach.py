class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        heights_count = len(heights)

        def abc(current_position, curr_bricks, curr_ladders):
            if current_position > heights_count:
                return current_position

            if bricks <= curr_bricks and ladders <= curr_ladders:
                return current_position
            
            if heights[current_position] > heights[current_position+1]:
                return abc(current_position+1, curr_bricks, curr_ladders)

            if bricks > curr_bricks:
                with_bricks = abc(
                    current_position+1, 
                    curr_bricks + (heights[current_position+1]-heights[current_position]), 
                    curr_ladders
                )
            else:
                with_bricks = 0

            if ladders > curr_ladders:
                with_ladders = abc(
                    current_position+1, 
                    curr_bricks, 
                    curr_ladders+1
                )
            else:
                with_ladders = 0

            return max(with_bricks, with_ladders)

        return abc(0, 0, 0)


print(Solution().furthestBuilding([4,2,7,6,9,14,12], 5, 1))
