use std::collections::BinaryHeap;

impl Solution {
    pub fn furthest_building(heights: Vec<i32>, mut bricks: i32, mut ladders: i32) -> i32 {
        let mut last_bldg = i32::MAX;
        let mut count = -1;
        let mut pq = BinaryHeap::new();
        for bldg in heights {
            let diff = bldg - last_bldg;
            if diff < 0 {
                last_bldg = bldg;
                count += 1;
                continue
            }
            if diff <= bricks {
                pq.push(diff);
                bricks -= diff;
                count += 1;
                last_bldg = bldg;
                continue
            }
            if ladders > 0 {
                if !pq.is_empty() {
                    let reclaimed_bricks = pq.pop().unwrap(); // already checked that okay to unwrap b/c not empty
                    if reclaimed_bricks > diff {
                        pq.push(diff);
                        bricks = bricks + reclaimed_bricks - diff;
                    } else {
                        pq.push(reclaimed_bricks);
                        // I don't know if more efficient to pop() then push() if not useable or to peek() then pop() if useable
                    }
                }
                ladders -= 1;
                count += 1;
                last_bldg = bldg;
                continue
            }
            return count
        }
        count
    }
}
