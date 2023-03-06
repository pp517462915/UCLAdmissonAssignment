def mat_to_list(adj_mat):
    if not adj_mat or len(adj_mat) < 0:
        return []

    result = []
    for i in range(len(adj_mat)):
        cur_link = []
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] != 0:
                cur_link.append(j)
        result.append(cur_link)

    return result

def create_data():
    data_list = []
    mat = [[0, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0]]
    mat2 = [[0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]]

    mat3 = [[0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0]]
    mat4 = [[0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]]

    data_list.append(mat)
    data_list.append(mat2)
    data_list.append(mat3)
    data_list.append(mat4)

    return data_list

def test_method():
    data = create_data()

    for mat in data:
        result = mat_to_list(mat)
        print(result)


if __name__ == '__main__':
    test_method()