impl Solution {
  pub fn num_submatrix_sum_target(matrix: Vec<Vec<i32>>, target: i32) -> i32 {
    let n = matrix.len();
    let m = matrix[0].len();

    let mut memo = vec![vec![0;m+1];n+1];
    for i in 0..n {
      for j in 0..m {
        memo[i+1][j+1] = memo[i+1][j] + memo[i][j+1] - memo[i][j] + matrix[i][j];
      }
    }

    let mut result = 0;
    for i in 0..n {
      for j in 0..m {
        for k in 1..=n {
          let ni = i + k;
          if n < ni { break }
          for l in 1..=m {
            let nj = j + l;
            if m < nj { break }

            let v = memo[ni][nj] - memo[ni][j] - memo[i][nj] + memo[i][j];
            if v == target {
              result += 1;
            }
          }
        }
      }
    }
    result
  }
}