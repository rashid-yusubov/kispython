def remove_duplicate_columns(table):
    seen = {}
    unique_cols = []
    for j in range(len(table[0])):
        col = tuple(table[i][j] for i in range(len(table)))
        if col not in seen:
            seen[col] = j
            unique_cols.append(j)
    return [[table[i][j] for j in unique_cols] for i in range(len(table))]


def remove_empty_columns(table):
    non_empty_cols = [
        j for j in range(len(table[0]))
        if any(table[i][j] is not None for i in range(len(table)))
    ]
    return [[table[i][j] for j in non_empty_cols] for i in range(len(table))]


def remove_duplicate_rows(table):
    seen = set()
    unique_rows = []
    for i in range(len(table)):
        row = tuple(table[i])
        if row not in seen:
            seen.add(row)
            unique_rows.append(i)
    return [table[i] for i in unique_rows]


def remove_empty_rows(table):
    """Удаляет строки, содержащие только None."""
    return [row for row in table if any(cell is not None for cell in row)]


def split_first_column(table):
    new_table = []
    for row in table:
        if row[0] is not None:
            parts = row[0].split(';', 1)
            email = parts[0]
            status = parts[1] if len(parts) > 1 else 'Не выполнено'
            new_row = [email, status] + row[1:]
            new_table.append(new_row)
        else:
            new_row = [None, None] + row[1:]
            new_table.append(new_row)
    return new_table


def transform_email(cell):
    """Преобразует email, заменяя '@' на '[at]'."""
    if cell is not None:
        return cell.replace('@', '[at]')
    return cell


def transform_status(cell):
    if cell is not None:
        return 'true' if cell == 'Выполнено' else 'false'
    return cell


def transform_name(cell):
    if cell is not None:
        name_parts = cell.split()
        surname = name_parts[2]
        first_name = name_parts[0]
        patronymic = name_parts[1]
        return f"{surname}, {first_name[0]}.{patronymic[0]}."
    return cell


def transform_cells(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if j == 0:
                table[i][j] = transform_email(table[i][j])
            elif j == 1:
                table[i][j] = transform_status(table[i][j])
            elif j == 2:
                table[i][j] = transform_name(table[i][j])
    return table


def reorder_columns(table):
    return [[row[0], row[2], row[1]] for row in table]


def transpose_table(table):
    return [
        [table[i][j] for i in range(len(table))]
        for j in range(len(table[0]))
    ]


def main(table):
    table = remove_duplicate_columns(table)
    table = remove_empty_columns(table)
    table = remove_duplicate_rows(table)
    table = remove_empty_rows(table)
    table = split_first_column(table)
    table = transform_cells(table)
    table = reorder_columns(table)
    table = transpose_table(table)
    return table
