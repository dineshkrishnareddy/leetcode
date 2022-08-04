impl Solution {
	pub fn mirror_reflection(mut p: i32, mut q: i32) -> i32 {
		while p%2==0 && q%2==0 {p>>=1;q>>=1;}
		1-p%2+q%2
	}
}
