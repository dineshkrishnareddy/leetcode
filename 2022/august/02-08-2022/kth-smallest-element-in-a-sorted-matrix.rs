use std::collections::BinaryHeap;
impl Solution {
	pub fn kth_smallest(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
		let mut pq = BinaryHeap::<i32>::new();
		for v in matrix.iter(){
			for x in v.iter() {pq.push(-x.clone());}
		}
		for i in (0..k-1) {pq.pop();}
		-pq.peek().cloned().unwrap()
	}
}
