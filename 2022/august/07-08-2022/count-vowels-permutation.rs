impl Solution {
    pub fn count_vowel_permutation(n: i32) -> i32 {
        const C: i64 = 10_i64.pow(9) + 7;
        let mut old = [1_i64; 5];
        let mut new = [1_i64; 5];
        for _ in 1..n {
            new[0] = (old[1] + old[2] + old[4]) % C; //a
            new[1] = (old[0] + old[2]) % C; //e
            new[2] = (old[1] + old[3]) % C; //i
            new[3] = old[2] % C; //o
            new[4] = (old[2] + old[3]) % C; //u
            old = new;
        }
        ((old[0] + old[1] + old[2] + old[3] + old[4]) % C) as i32
    }
}
