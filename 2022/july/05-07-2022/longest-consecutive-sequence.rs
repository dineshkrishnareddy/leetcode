use std::collections::HashSet;
use std::cmp::max;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut s: HashSet<i32> = HashSet::new();
        for v in nums.iter() {
            s.insert(*v);
        }
        let mut ans = 0;
        for &v in nums.iter() {
            let mut i = v;
            let mut curr = 1;
            s.remove(&i);
            while s.contains(&(i+1)) {
                curr += 1;
                i += 1;
                s.remove(&i);
            }
            let mut i = v;
            while s.contains(&(i-1)) {
                curr += 1;
                i -= 1;
                s.remove(&i);
            }
            ans = max(ans, curr);
        }
        ans
    }
}