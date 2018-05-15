def solve_system(variables, results):
    """ Gaussian elimination with pivoting """
    n = len(variables)
    M = variables

    # TODO: Loop with index
    i = 0
    for x in M:
        x.append(results[i])
        i += 1

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        for j in range(k+1, n):
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] = float(M[n-1][n])/M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z = z + float(M[i][j])*x[j]
        x[i] = float(M[i][n] - z)/M[i][i]

    return x


def get_variables(w, x, y, z):
    """ Returns 2D list of variables """
    len_z = len(z)
    sum_w = sum(w)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_wx = multiply_lists(w, x)
    sum_wy = multiply_lists(w, y)
    sum_xy = multiply_lists(x, y)

    first_column = [len_z, sum_w, sum_x, sum_y]
    second_column = [sum_w, sum([r**2 for r in w]), sum_wx, sum_wy]
    third_column = [sum_x, sum_wx, sum([r**2 for r in x]), sum_xy]
    fourth_column = [sum_y, sum_wy, sum_xy, sum([r**2 for r in y])]

    return [first_column, second_column, third_column, fourth_column]


def get_answers(w, x, y, z):
    """ Returns list of answers """

    sum_z = sum(z)
    sum_wz = multiply_lists(w, z)
    sum_xz = multiply_lists(x, z)
    sum_yz = multiply_lists(y, z)

    return [sum_z, sum_wz, sum_xz, sum_yz]


def multiply_lists(list_a, list_b):
    """Multiplies lists and returns sum of products

    Multiplies each number in list_a with the corresponding number on the
    same index in list_b and returns the sum of all products

    If the two lists are with different lengths the result so far will be
    returned.
    """
    result = 0
    try:
        for index, value in enumerate(list_a):
            result += value * list_b[index]
    except IndexError:
        pass

    return result
