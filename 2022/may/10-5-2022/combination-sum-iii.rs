
pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
    let mut answer = vec![];
    backtracking(&mut answer, &mut vec![], 1, n, k);
    answer
}

fn backtracking(
    answers: &mut Vec<Vec<i32>>,
    buffer: &mut Vec<i32>,
    from: i32,
    sum: i32,
    rem: i32,
) {
    if rem == 0 {
        if sum == 0 {
            answers.push(buffer.clone());
            return;
        }
        return;
    }

    for idx in from..10 {
        if sum-idx < 0 {
            break;
        }

        buffer.push(idx);
        backtracking(answers, buffer, idx+1, sum-idx, rem-1);
        buffer.pop();
    }

}

fn main() {
    println!("{:?}", combination_sum3(3, 7));
}