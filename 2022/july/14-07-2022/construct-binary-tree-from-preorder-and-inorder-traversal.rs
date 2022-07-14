use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    fn build(preorder: &mut Vec<i32>, inorder: &mut Vec<i32>, bound: Option<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if inorder.is_empty() || (bound.is_some() && *inorder.last().unwrap() == bound.unwrap()) {
            return None;
        }
        let mut root = TreeNode::new(preorder.pop().unwrap());
        root.left = Self::build(preorder, inorder, Some(root.val));
        inorder.pop();
        root.right = Self::build(preorder, inorder, bound);
        Some(Rc::new(RefCell::new(root)))
    }


    pub fn build_tree(mut preorder: Vec<i32>, mut inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        preorder.reverse();
        inorder.reverse();
        Self::build(&mut preorder, &mut inorder, None)
    }
}