# Open file
file = open('example.in')
first_line = file.readline()

# Save all magic numbers in a tuple by cutting the first line as soon as a whitespace is found
row_count, column_count, min_ingredient, max_area = tuple(map(int, first_line.split(' ')))

grid = []

for i in range(row_count):
    grid.append(file.readline().rstrip())  # rstrip() removes the whitespace at EOL

file.close()

results = []

for r in range(row_count):
    beg = 0
    end = 0
    mushroom_count = 0
    tomato_count = 0

    while end < column_count:
        if grid[r][end] == 'M':
            mushroom_count += 1
        elif grid[r][end] == 'T':
            tomato_count += 1

        end += 1

        if end - beg > max_area:
            if grid[r][beg] == 'M':
                mushroom_count -= 1
            elif grid[r][beg] == 'T':
                tomato_count -= 1

            beg += 1

        if (end - beg <= max_area
                and mushroom_count >= min_ingredient
                and tomato_count >= min_ingredient):

            results.append((r, beg, r, end - 1))
            beg = end
            tomato_count = 0
            mushroom_count = 0

print(grid, results, sep="\n")
