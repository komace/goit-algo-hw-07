class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1

# Функція вставки вузла в дерево
def insert(root, key):
    if not root:
        return TreeNode(key)
    elif key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    # Ліве піддерево
    if balance > 1 and key < root.left.val:
        return right_rotate(root)
    
    # Праве піддерево
    if balance < -1 and key > root.right.val:
        return left_rotate(root)

    # Ліве праве піддерево
    if balance > 1 and key > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    #   Праве ліве піддерево
    if balance < -1 and key < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root        

# Функція для отримання висоти вузла
def get_height(root):
    if not root:
        return 0
    return root.height

#  Функція для отримання балансу вузла
def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)

#   Функція для правого повороту
def right_rotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

#   Функція для лівого повороту
def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y    

# Функція для обчислення суми всіх значень у дереві
def sum_tree(root):
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)
# Створення дерева
root = None
values = [50, 30, 20, 40, 70, 60, 80]
for value in values:
    root = insert(root, value)

print("Сума всіх значень у дереві:", sum_tree(root))    