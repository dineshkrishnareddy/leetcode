impl Solution {
    pub fn poor_pigs(buckets: i32, minutes_to_die: i32, minutes_to_test: i32) -> i32 {
        if buckets == 1 { return 0; }
        let rounds = minutes_to_test / minutes_to_die;
        let base = rounds + 1;
        let mut pigs = 1;
        let mut acc = base.clone();
        while acc < buckets {
            pigs += 1;
            acc *= base;  // or call .pow() each time
        }
        pigs
    }
}
