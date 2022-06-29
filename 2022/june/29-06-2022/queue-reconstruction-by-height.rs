const Height: usize = 0;
const Rank: usize = 1;

impl Solution {
    pub fn reconstruct_queue(mut people: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        // Sort people by decreasing height, and increasing rank:
        people.sort_by_key(|p| (-p[Height], p[Rank]));
        // Reconstruct the queue:
        let mut queue = Vec::with_capacity(people.len());
        for person in people.iter() {
            queue.insert(person[Rank] as usize, person.to_vec());
        }
        queue
    }
}
