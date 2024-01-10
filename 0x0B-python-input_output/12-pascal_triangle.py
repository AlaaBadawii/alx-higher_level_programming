def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    - n (int): The number of rows to generate.

    Returns:
    - A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row

    for i in range(1, n):
        # Calculate the next row based on the previous row
        row = [1] + [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)] + [1]
        triangle.append(row)

    return triangle
