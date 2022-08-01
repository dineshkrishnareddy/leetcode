impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        if m == 1 || n == 1 { return 1; }
        let width = n as usize;
        let height = m as usize;
        let mut grid = vec![ vec![ 0 as i32; width]; height];
        grid.last_mut().unwrap().fill(1);
        grid.iter_mut().for_each( |r| *r.last_mut().unwrap() = 1 );
        // like PNG pixel scanlines but backwards
        for row in (0 .. height-1).rev() {
            for cell in (0 .. width-1).rev() {
                grid[row][cell] = grid[row+1][cell] + grid[row][cell+1];
            }
        }
        grid[0][0]
    }
}
