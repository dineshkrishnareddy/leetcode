impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let (mut res, mut prev, mut curr) = (0, 0, 0);
        for i in s.chars().rev() {
            match i {
                'I' => curr = 1,
                'V' => curr = 5,
                'X' => curr = 10,
                'L' => curr = 50,
                'C' => curr = 100,
                'D' => curr = 500,
                'M' => curr = 1000,
                _ => return -1,
            };
            if curr < prev { res = res - curr } else { res = res + curr };
            prev = curr;
        }
        res
    }
}