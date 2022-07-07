impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        let (l1, l2, l3) = (s1.len(), s2.len(), s3.len());
        if l1 + l2 != l3 {
            return false;
        }

        let (s1, s2, s3) = (s1.as_bytes(), s2.as_bytes(), s3.as_bytes());
        let mut dp: Vec<Vec<usize>> = vec![vec![0; l2 + 1]; l1 + 1];

        for i1 in 0..=l1 {
            for i2 in 0..=l2 {
                let i3 = i1 + i2;
                if i1 < l1 && s1[i1] == s3[i3] {
                    dp[i1 + 1][i2] = std::cmp::max(dp[i1 + 1][i2], dp[i1][i2] + 1);
                }
                if i2 < l2 && s2[i2] == s3[i3] {
                    dp[i1][i2 + 1] = std::cmp::max(dp[i1][i2 + 1], dp[i1][i2] + 1);
                }
            }
        }

        dp[l1][l2] == l3
    }
}