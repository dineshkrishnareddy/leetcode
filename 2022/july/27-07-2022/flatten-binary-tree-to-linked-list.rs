use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
	pub fn flatten(root: &mut Option<Rc<RefCell<TreeNode>>>) {
		let mut root = root.clone();
		while let Some(r) = root {
			let mut r = r.borrow_mut();
			if let Some(mut prec) = r.left.clone() {
				loop {
					let right = prec.borrow().right.clone();
					if let Some(ri) = right {prec = ri;}
					else {break;}
				}
				let mut b = prec.borrow_mut();
				b.right = r.right.take();
				r.right = r.left.take()
			}
			root = r.right.clone();
		}
	}
}