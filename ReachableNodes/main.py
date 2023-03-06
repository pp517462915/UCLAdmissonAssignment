def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node
    """
    # TODO
    if not adj_list:
        return

    queue = []
    queue.append(start_node)
    visited = []
    res = []

    while queue:
        cur = queue.pop()
        visited.append(cur)
        res.append(cur)

        for next_node in adj_list[cur]:
            if next_node in visited:
                continue
            queue.append(next_node)
    res = sorted(res)
    res = {x for x in res}
    return res

def create_date():
    list = [[1, 3], [2], [0], [4], [3], []]
    list2 = [[1, 3], [0, 2], [1, 3], [0, 2]]
    list3 = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]
    list4 = [[1], [0, 2], [1]]

    data_list = []
    data_list.append(list)
    data_list.append(list2)
    data_list.append(list3)
    data_list.append(list4)

    return data_list

def test_method():
    data_list = create_date()
    for list in data_list:
        for i in range(len(list)):
            result = reachable(list, i)
            print("node:", i, ",reachable nodes:", result)

if __name__ == '__main__':
    test_method()