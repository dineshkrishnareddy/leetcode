use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut ans = vec![];
        let mut bfs = vec![];
        match root {
            Some(x) => bfs.push(x),
            None => ()
        }
        while bfs.len() != 0 {
            ans.push(bfs[bfs.len()-1].borrow().val);
            let mut row = vec![];
            for node in bfs.iter() {
                match node.borrow().left.as_ref() {
                    // only push onto row if the node actually contains something.
                    Some(x) => row.push(Rc::clone(x)),
                    None => (),
                };
                match node.borrow().right.as_ref() {
                    Some(x) => row.push(Rc::clone(x)),
                    None => (),
                };
            };
            bfs = row;
        }
        ans
    }
}
