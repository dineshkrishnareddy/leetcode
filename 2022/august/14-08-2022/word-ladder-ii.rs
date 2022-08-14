impl Solution {
    pub fn find_ladders(begin_word: String, end_word: String, mut word_list: Vec<String>) -> Vec<Vec<String>> {
        let end = match word_list.iter().position(|s| s == &end_word) {
            None => return Vec::new(),
            Some(i) => i,
        };
        word_list.push(begin_word);
		// (list of previous words, depth of BFS)
        let mut helper: Vec<(Vec<usize>, i32)> = vec![(Vec::new(), -1); word_list.len()];
        helper[word_list.len() - 1].1 = 0;
        for depth in 0.. {
            let mut no_route = true;
            for i in 0..word_list.len() {
                if helper[i].1 == depth {
                    for j in 0..word_list.len() - 1 {
                        if (helper[j].1 == -1 || helper[j].1 == depth + 1)
                        && Self::is_adj(&word_list[i], &word_list[j]) {
                            no_route = false;
                            helper[j].0.push(i);
                            helper[j].1 = depth + 1;
                        }
                    }
                }
            }
            if no_route {
                return Vec::new();
            }
            if helper[end].1 != -1 {
                break;
            }
        }
        let mut ans = Vec::new();
        Self::backtrack(&mut vec![end], &mut ans, &helper, &word_list);
        ans
    }

    fn backtrack(route: &mut Vec<usize>,
                ans: &mut Vec<Vec<String>>,
                helper: &Vec<(Vec<usize>, i32)>,
                word_list: &Vec<String>) {
        let curr = *route.last().unwrap();
        if curr == word_list.len() - 1 {
            let ans2 = route.iter().rev()
                .map(|&i| word_list[i].to_owned())
                .collect();
            ans.push(ans2);
        }
        else {
            for &p in helper[curr].0.iter() {
                route.push(p);
                Self::backtrack(route, ans, helper, word_list);
                route.pop();
            }
        }
    }

    fn is_adj(word1: &str, word2: &str) -> bool {
        word1.chars().zip(word2.chars())
            .filter(|(ch1, ch2)| ch1 != ch2)
            .count() == 1
    }
}
