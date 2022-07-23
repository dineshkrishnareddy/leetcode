struct CountSegmentTree {
    start: usize, // the index in tree which is the leftmost leaf node
    tree: Vec<usize>, // index 0 not used
}

impl CountSegmentTree {
    fn new(size: usize) -> Self {
        let start = 1 << ((size as f32).log2().ceil() as usize);
        let mut tree = vec![1; 2 * size];
        for i in (1..size).rev() {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
        Self {
            start,
            tree,
        }
    }

    fn ith_leaf(&self, i: usize) -> usize {
        let mut j = i + self.start;
        if j >= self.tree.len() {
            j -= self.tree.len() / 2;
        }
        j
    }

    fn remove(&mut self, i: usize) {
        let mut j = self.ith_leaf(i);
        while j > 0 {
            self.tree[j] -= 1;
            j >>= 1;
        }
    }

    fn count_right(&self, i: usize) -> i32 {
        let mut j = self.ith_leaf(i);
        let mut count = 0;
        while j > 1 {
            if j & 1 == 0 {
                count += self.tree[j >> 1] - self.tree[j];
            }
            j >>= 1;
        }
        count as i32
    }
}

impl Solution {
    pub fn count_smaller(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![0; nums.len()];
        let mut indices: Vec<usize> = (0..nums.len()).collect();
        indices.sort_unstable_by_key(|&i| (-nums[i], -(i as i32)));
        let mut seg_tree = CountSegmentTree::new(nums.len());
        for &i in indices.iter() {
            ans[i] = seg_tree.count_right(i);
            seg_tree.remove(i);
        }
        ans
    }
}