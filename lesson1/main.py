for i in range(0, 10):
    spaces = ''''''''''''
    for a in range(0, 10 - i * 1):
        spaces = spaces + ' '
    stars = ''
    for j in range(0, i + 13-3*4):
        stars = stars + '**'
    print(spaces + stars)
