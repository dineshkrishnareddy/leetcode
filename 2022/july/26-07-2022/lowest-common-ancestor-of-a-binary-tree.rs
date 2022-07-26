use std::rc::Rc;
use std::cell::RefCell;
type OptNode = Option<Rc<RefCell<TreeNode>>>;
impl Solution {
    pub fn lowest_common_ancestor(root: OptNode, p: OptNode, q: OptNode) -> OptNode {
        Self::count_matches(&root, p.as_ref()?.borrow().val, q.as_ref()?.borrow().val).0
    }

    fn count_matches(node: &OptNode, p: i32, q: i32) -> (OptNode, i32) {
        if node.is_none() {
            return (None, 0);
        }
        let n = node.as_ref().unwrap();
        let b = n.borrow();
        let left_ans = Self::count_matches(&b.left, p, q);
        if left_ans.0.is_some() {
            return left_ans;
        }
        let right_ans = Self::count_matches(&b.right, p, q);
        if right_ans.0.is_some() {
            return right_ans;
        }
        let count = left_ans.1 + right_ans.1
            + if b.val == p || b.val == q { 1 } else { 0 };
        let found = if count == 2 { Some(Rc::clone(n)) } else { None };
        (found, count)
    }
}