impl Solution {
    pub fn wiggle_max_length(nums: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = 0;
        let mut ans = 1;
        for k in 1..nums.len() {
            if nums[k] != nums[j] && nums[k].cmp(&nums[j]) != nums[j].cmp(&nums[i]) {
                i = j;
                ans += 1;
            }
            j = k;
        }
        ans
    }
}
