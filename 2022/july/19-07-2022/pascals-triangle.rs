impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        if num_rows == 1 {
            return vec![ vec![ 1 ] ];
        }
        let mut prev = Self::generate(num_rows - 1);
        let last_row = prev.last().unwrap();
        let mut new_row = Vec::with_capacity(last_row.len() + 1);
        new_row.push(1);
        last_row.windows(2)
            .map( |pair| pair[0] + pair[1] )
            .for_each( |c| new_row.push(c) );
        new_row.push(1);
        prev.push( new_row );
        prev
    }
}