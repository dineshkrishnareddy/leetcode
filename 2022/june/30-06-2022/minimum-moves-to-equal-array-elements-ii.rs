impl Solution {
    pub fn min_moves2(nums: Vec<i32>) -> i32 {
        let mut nums_mutable = nums;
        nums_mutable.sort();

        let mut median_value: i32 = 0;
        let mut output:i32 = 0;

        let l = nums_mutable.len();
        let rc = (l/2) as usize;

        if ((l % 2) == 0) {
            let lc:usize = rc - 1;
            median_value = ((nums_mutable[rc] + nums_mutable[lc])/2) as i32;

        } else {
            median_value = nums_mutable[rc] as i32;
        }

        for n in &nums_mutable {
            let mut diff = (*n as i32 - median_value);
            if (diff < 0) {
                diff = 0 - diff
            }

            output += (diff as i32);
        }

        return output as i32;
    }
}
