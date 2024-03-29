impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let (mut i, mut j) = (0, matrix[0].len() - 1);
        while i < matrix.len() {
            match matrix[i][j].cmp(&target) {
                std::cmp::Ordering::Less => i += 1,
                std::cmp::Ordering::Equal => return true,
                std::cmp::Ordering::Greater if j > 0 => j -= 1,
                std::cmp::Ordering::Greater => break,
            }
        }
        false
    }
}