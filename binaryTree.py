"""
Binary tree is a tree in which each node has maximum of 2 children.

Strict/Proper binary Tree: each node has either 0 or 2 children

complete binary tree: all level are completly filled except possibly the last one and the nodes should be as on the left side as possible

perfect binary tree: all the levels are completely filled, it will have 2^{h+1}-1 nodes

max height of complete binary tree = ceil(log2(n+1)-1) = floor(log2(n))

balanced binary tree: difference between height of left and right subtree for every node is not more than k (mostly 1)
diff = | h_left - h_right |

complete binary tree can be implemented using an array
even otherwise, a binary tree can still be represented by an array,except, we will have to keep None wherever the node isn't there
"""

