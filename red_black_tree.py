# 红黑树的一个节点
class Node:
    # left和right属性分别指向左子树和右子树的根节点
    def __init__(self, color, left=None, right=None):
        self.color = color
        self.left = left
        self.right = right


# 递归地遍历树，计算红黑树的黑高度，
# 即从给定节点到其任何叶子节点的路径上的黑色节点数
def getBlackHeight(node):
    # 按照红黑树的定义，空节点被视为黑色
    if node is None:
        return 1

    left_black_height = getBlackHeight(node.left)
    right_black_height = getBlackHeight(node.right)

    # 不是有效的红黑树，返回-1
    if (
        left_black_height == -1
        or right_black_height == -1
        or left_black_height != right_black_height
    ):
        return -1

    if node.color == "black":
        return left_black_height + 1
    # 红色节点不计入黑高度
    else:
        return left_black_height
