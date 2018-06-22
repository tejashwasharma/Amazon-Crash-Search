def pro_detail():
    lrange, rrange = None, None
    sort = None
    print('''enter "NA/na" for the below options, if you don't want to enter anything.\n''')
    brand = input('Any Brand You Want To Prefer? ').strip()
    item = input('Enter Product Name You Want To Search : ').strip()
    rng = input('Any Range You Want To Prefer in Rupees? (ex : 1000-1500) ').strip()
    brand += ' '
    if rng[0].lower() != 'n':
        print('Note : Range will only work if provided by Amazon ')
        lrange,  rrange = rng.split('-')
        lrange.strip()
        rrange.strip()
    if brand[0].lower() == 'n':
        brand = ''
    item = brand + item
    detail = [item, lrange, rrange]

    sort_ans = input('Want to apply any sorting? (Y/N) ')
    if sort_ans[0].lower() == 'y':
        sort = int(input('''Sorting :
                1. Relevance
                2. New and Bestselling
                3. Price: Low to High
                4. Price: High to Low
                5. Avg. Customer Review
                6. Newest Arrivals\n'''))
    star_ans = input('Want 4+ star customer review products only? (Y/N) ')
    return detail, sort, star_ans


def pin_detail():
    pin_ans = input('want to see availablity at any pin? (Y/N) ')
    if pin_ans[0].lower() == 'y':
        pin = int(input('enter your postal code : '))
    else:
        pin = None
    return pin
