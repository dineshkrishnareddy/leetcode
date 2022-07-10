impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut one = 0;
        let mut two = 0;
        for i in 2..cost.len()+1{
            let tmp = one;
            one = (one + cost[i-1]).min(two + cost[i-2]);
            two = tmp;
        }
        one
    }
}
