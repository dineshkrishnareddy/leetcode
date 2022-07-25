impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        fn binary_search(nums: Vec<i32>, target: i32) -> i32{
            let (mut l, mut r) = (0, nums.len());
            while l < r{
                let mid = l + (r - l) / 2;
                if nums[mid]< target{
                    l = mid + 1;
                } else {
                    r = mid
                }
            }
            return l as i32;
        }
       let l = binary_search(nums.clone(), target);
       let r = binary_search(nums.clone(), target+1)-1; // next number of target - 1
       if l <= r {vec![l, r]} else {vec![-1, -1]}
    }
}