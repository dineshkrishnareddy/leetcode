use std::collections::HashMap;

impl Solution {
    pub fn find_and_replace_pattern(words: Vec<String>, pattern: String) -> Vec<String> {
        let p = compile(pattern.as_bytes());
        words.into_iter()
            .filter( |w| compile(w.as_bytes()) == p )
            .collect()
    }
}

fn compile(word: &[u8]) -> Vec<i32> {
    let N = word.len();
    let mut out = vec![ 0 as i32; N ];
    let mut perm: HashMap<u8, i32> = HashMap::new();
    let mut uniqueness: i32 = 0;
    for i in 0 .. N {
        let c = word[i];
        out[i] = *perm.entry(c)
            .or_insert_with( || {
                uniqueness += 1;
                uniqueness
            });
    }
    out
}