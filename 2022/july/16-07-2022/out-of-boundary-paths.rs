use std::collections::HashMap;

impl Solution {
    pub fn find_paths(m: i32, n: i32, max_move: i32, start_row: i32, start_column: i32) -> i32 {
        let max_move = max_move as usize;
        let bound = (m as usize, n as usize);
        let pos = (start_row as usize, start_column as usize);

        let mut cache = HashMap::new();
        Self::dfs(bound, pos, max_move, &mut cache) as i32
    }

    fn dfs(
        bound: (usize, usize),
        pos: (usize, usize),
        max_move: usize,
        cache: &mut HashMap<(usize, usize, usize), usize>
    ) -> usize {
        if max_move == 0 { return 0; }
        let (m, n) = bound;
        let (x, y) = pos;
        if let Some(cached) = cache.get(&(x, y, max_move)) {
            return *cached;
        }
        let mut res = 0;
        if x > 0 {
            res += Self::dfs(bound, (x - 1, y), max_move - 1, cache);
        } else {
            res += 1;
        }
        if x + 1 < m {
            res += Self::dfs(bound, (x + 1, y), max_move - 1, cache);
        } else {
            res += 1;
        }
        if y > 0 {
            res += Self::dfs(bound, (x, y - 1), max_move - 1, cache);
        } else {
            res += 1;
        }
        if y + 1 < n {
            res += Self::dfs(bound, (x, y + 1), max_move - 1, cache);
        } else {
            res += 1;
        }
        res %= 1_000_000_007;
        cache.insert((x, y, max_move), res);
        res
    }
}