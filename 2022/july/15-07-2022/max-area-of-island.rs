impl Solution {
    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if grid[i][j] == 1 {
                    ans = ans.max(Self::count_island(i as i32, j as i32, &mut grid));
                }
            }
        }
        ans
    }

    fn count_island(i: i32, j: i32, grid: &mut Vec<Vec<i32>>) -> i32 {
        let mut count = 1;
        grid[i as usize][j as usize] = 2;
        for dir in [0, 1, 0, -1, 0].windows(2) {
            let x = i + dir[0];
            let y = j + dir[1];
            if x >= 0 && x < grid.len() as i32
            && y >= 0 && y < grid[0].len() as i32
            && grid[x as usize][y as usize] == 1 {
                count += Self::count_island(x, y, grid);
            }
        }
        count
    }
}
