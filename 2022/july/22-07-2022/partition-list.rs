// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn partition(mut head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        let (mut h1, mut h2) = (ListNode::new(0), ListNode::new(0));
        let (mut p1, mut p2) = (&mut h1, &mut h2);

        while let Some(mut node) = head  {
            head = node.next.take();
            if node.val < x {
                p1.next = Some(node);
                p1 = p1.next.as_mut().unwrap();
            } else {
                p2.next = Some(node);
                p2 = p2.next.as_mut().unwrap()
            }
        }
        p1.next = h2.next;
        h1.next
    }
}