impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let N = ratings.len();
        let mut candies = vec![ 1 as i32; N ];
        // forward pass
        for i in 1 .. N {
            if ratings[i] > ratings[i-1] {
                candies[i] = candies[i-1] + 1;
            }
        }
        // backwards pass
        for i in (0 .. N-1).rev() {
            if ratings[i] > ratings[i+1] {
                candies[i] = candies[i].max(candies[i+1] + 1);
            }
        }
        candies.iter().sum()
    }
}