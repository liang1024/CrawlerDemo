#coding=utf-8
'''
15求最大树深

'''
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1