"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


def solution(A):
    length = len(A)
    if length < 5:
        return -1
    result = float('inf')
    link1 = 1
    while link1<length-2:
        # looking for non alternative links
        link2 = link1+2
        while link2<length-1:
            result = min(result, A[link1]+A[link2])
            link2 += 1
        link1 += 1
    return result

print(solution([5,2,4,6,3,1]))
