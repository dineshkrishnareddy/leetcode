struct NumArray {
 nums: Vec<i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {
 fn new(nums: Vec<i32>) -> Self {
  return NumArray { nums };
 }

 fn update(&mut self, index: i32, val: i32) {
  let mut cloned_nums = self.nums.to_vec();
  cloned_nums[index as usize] = val;
  self.nums = cloned_nums.to_vec();
 }

 fn sum_range(&mut self, left: usize, right: usize) -> i32 {
  let mut ans = 0;
  for num in self.nums[left..right].to_vec() {
   ans += num;
  }

  ans
 }
}