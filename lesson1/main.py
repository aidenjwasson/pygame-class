for i in range(0, 6):
    spaces = ''
    for a in range(0, 6 - i - 1):
        spaces = spaces + ' '
    stars = ''
    for j in range(0, i + 13):
        stars = stars + '*'
    print(spaces + stars)
