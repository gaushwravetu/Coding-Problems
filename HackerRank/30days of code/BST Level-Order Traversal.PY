

    def levelOrder(self,root):
        nodes_to_search = list()
        nodes_to_search.append(root)
        nodes_searched = ''
        while len(nodes_to_search) > 0:
            node = nodes_to_search.pop(0)
            if node.left:
                nodes_to_search.append(node.left)
            if node.right:
                nodes_to_search.append(node.right)
            nodes_searched += str(node.data) + ' '
        print(nodes_searched)

