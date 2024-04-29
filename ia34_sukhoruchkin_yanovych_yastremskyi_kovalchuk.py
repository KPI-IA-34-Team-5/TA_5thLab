class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_and_count_occurrences(root, key):
    count = 0
    current = root
    while current:
        if key < current.val:
            current = current.left
        elif key > current.val:
            current = current.right
        else:
            if current.left and current.left.val == key:
                count += 1
                current = current.left
            elif current.right and current.right.val == key:
                count += 1
                current = current.right
            count += 1
            current = None
    return count

root = TreeNode('m')
insert(root, 'g')
insert(root, 't')
insert(root, 'a')
insert(root, 'k')
insert(root, 'o')
insert(root, 'z')

key = input("Enter the character to find in the tree: ")
count = find_and_count_occurrences(root, key)
if count > 0:
    print(f"The character '{key}' is found in the tree and it occurs {count} times.")
else:
    print(f"The character '{key}' is not found in the tree.")