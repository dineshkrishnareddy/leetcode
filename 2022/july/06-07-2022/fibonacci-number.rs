use std::collections::HashMap;

impl Solution {
    pub fn fib(n: i32) -> i32 {
        fn fibr(n: i32, m: &mut HashMap<i32, i32>) -> i32 {
            if !m.contains_key(&(n - 1)) {
                let temp = fibr(n - 1, m);
                m.insert(n - 1, temp);
            }
            if !m.contains_key(&(n - 2)) {
                let temp = fibr(n - 2, m);
                m.insert(n - 1, temp);
            }

            *m.get(&(n - 1)).unwrap() + *m.get(&(n - 2)).unwrap()
        }
        if n <= 1 {
            return n;
        }
        let mut m: HashMap<i32, i32> = HashMap::new();
        m.insert(0, 0 as i32);
        m.insert(1, 1 as i32);
        fibr(n, &mut m)
    }
}