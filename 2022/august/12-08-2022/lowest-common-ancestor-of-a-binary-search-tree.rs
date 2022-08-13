use std::rc::Rc;
use std::cell::RefCell;
type Node = Option<Rc<RefCell<TreeNode>>>;
impl Solution {
    pub fn lowest_common_ancestor(root: Node, p: Node, q: Node) -> Node {
        let (mut vp, mut vq) = (p.as_ref().unwrap().borrow().val, q.as_ref().unwrap().borrow().val);
        if vp>vq { vp+=vq; vq=vp-vq; vp-=vq; }
        match root {
            x if x==p => { p },
            x if x==q => { q },
            Some(node) => {
                let v = node.borrow().val;
                if vp<v && v<vq { return Some(node); }
                if vq<v { Solution::lowest_common_ancestor(node.borrow().left.clone(), p, q) }
                else { Solution::lowest_common_ancestor(node.borrow().right.clone(), p, q) }
            },
            None => None
        }
    }
}
