
pub fn count_vowel_strings(n: i32) -> i32 {
    
    let vowels = vec!['a', 'e', 'i', 'o', 'u'];
    let mut result = vec![];
    dfs(&mut result, &mut vec![], vowels, 0, n);
    result.len()
}

fn dfs(result: &mut Vec<str>, buffer: &mut Vec<str>, vowels: Vec<str>, index: i32, count: i32) {
    if buffer.len() > count {
        return;
    }
    if buffer.len() == count {
        result.push(buffer.join());
    }

    for i in index..vowels.len() {
        buffer.push(vowels[i]);
        dfs(result, buffer, vowels, i, count);
        buffer.pop();
    }
}


fn main() {
    println!("{:?}", count_vowel_strings(2));
}
