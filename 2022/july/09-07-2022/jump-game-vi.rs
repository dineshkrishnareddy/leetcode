use std::collections::BinaryHeap;

impl Solution {
    pub fn max_result(nums: Vec<i32>, k: i32) -> i32 {
		// score[i] = max { score[i-k], ..., score[i-1] } + nums[i]
        // maintain a priority queue to reduce each score calc to O(logn) time
        // time: O(nlogn)
        // space: O(n)
        let n = nums.len();
        let k = k as usize;
        let mut score = nums[0];
        let mut pq = BinaryHeap::new();
        pq.push((nums[0], 0));
        for i in 1..n {
            while let Some(&(v, idx)) = pq.peek() {
                if idx + k < i {
                    pq.pop();
                    continue;
                }
                score = v + nums[i];
                pq.push((score, i));
                break;
            }
        }
        score
    }
}
