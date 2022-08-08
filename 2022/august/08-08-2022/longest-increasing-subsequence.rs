impl Solution {
    pub fn length_of_lis(mut nums: Vec<i32>) -> i32 {
        let mut ans = 1;
        for i in 1..nums.len() {
            let j = nums[..ans].partition_point(|&x| x < nums[i]);
            nums[j] = nums[i];
            ans = ans.max(j + 1);
        }
        ans as i32
    }
}
