use std::collections::HashMap;

impl Solution {
    pub fn find_substring(s: String, words: Vec<String>) -> Vec<i32> {
        let width = words[0].len();
        if width > s.len() {
            return Vec::new();
        }
        let mut hash: HashMap<&str, i32> = HashMap::new();
        for word in words.iter() {
            *hash.entry(word.as_str()).or_insert(0) += 1;
        }

        let mut ans = Vec::new();
        for start in 0..width {
            let mut count = 0;
            let mut seq: HashMap<&str, i32> = HashMap::new();
            for i in (start..=s.len() - width).step_by(width) {
                if i >= width * words.len() {
                    let j = i - width * words.len();
                    let slice = &s[j..j + width];
                    if let Some(max) = hash.get(&slice) {
                        let entry = seq.entry(slice).or_insert(0);
                        *entry -= 1;
                        if *entry < *max {
                            count -= 1;
                        }
                    }
                }

                let slice = &s[i..i + width];
                if let Some(max) = hash.get(&slice) {
                    let entry = seq.entry(slice).or_insert(0);
                    *entry += 1;
                    if *entry <= *max {
                        count += 1;
                        if count == words.len() {
                            ans.push((i - width * (words.len() - 1)) as i32);
                        }
                    }
                }
            }
        }
        ans
    }
}
