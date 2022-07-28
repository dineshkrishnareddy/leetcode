impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut map = std::collections::HashMap::new();
        s.chars().for_each(|c| *map.entry(c).or_insert(0) += 1);
        t.chars().for_each(|c| *map.entry(c).or_insert(0) -= 1);
        map.into_values().all(|v| v == 0)
    }
}