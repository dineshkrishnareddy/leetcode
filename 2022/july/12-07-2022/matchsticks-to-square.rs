impl Solution {
    pub fn makesquare(matchsticks: Vec<i32>) -> bool {
        let mut matchsticks = matchsticks;
        matchsticks.sort();
        matchsticks.reverse();
        let sum = matchsticks.iter().sum::<i32>();
        let mut matches = vec![sum / 4; 4];

        sum % 4 == 0 && Self::eval(&matchsticks, &mut matches, 0)
    }

    fn eval(matchsticks: &Vec<i32>, matches: &mut Vec<i32>, i: usize) -> bool {
        if (i == matchsticks.len()) {
            for a in matches { if *a != 0 { return false } }
            return true
        }

        for j in 0..4 {
            if matchsticks[i] > matches[j] { continue; }
            matches[j] -= matchsticks[i];
            if Self::eval(matchsticks, matches, i + 1) { return true }
            matches[j] += matchsticks[i];
        }

        false
    }

}
