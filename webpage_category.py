def category():
    ans = 'y'
    url = 'http://www.amazon.in/'
    while ans[0].lower() == 'y':
        cat = int(input('''which category you want to try?
        1. Mobile and Computers
        2. Electronics
        3. Men Fashion
        4. Women Fashion
        5. Books\n'''))
        # Mobile and Computers
        if cat == 1:
            cat = int(input('''Choose one :
        1. Mobile Phones
        2. Tablets
        3. Laptops
        'Any Other Number for Other Electronics'\n'''))
            if cat == 1:
                url = 'http://www.amazon.in/mobile-phones/b/ref=sd_allcat_sbc_mobcomp_all_mobiles?ie=UTF8&node=1389401031'
            elif cat == 2:
                url = 'http://www.amazon.in/Tablets/b/ref=sd_allcat_sbc_mobcomp_tablets?ie=UTF8&node=1375458031'
            elif cat == 3:
                url = 'http://www.amazon.in/Laptops/b/ref=sd_allcat_sbc_mobcomp_laptops?ie=UTF8&node=1375424031'
            else:
                url = 'http://www.amazon.in/electronics/b/ref=sd_allcat_sbc_mobcomp_elec_all?ie=UTF8&node=976419031'

        # Electronics
        elif cat == 2:
            cat = int(input('''Choose one :
        1. Headphones
        2. Speakers
        'Any Number for Other Category'\n'''))
            if cat == 1:
                url = 'http://www.amazon.in/headphones/b/ref=sd_allcat_sbc_tvelec_headphones?ie=UTF8&node=1388921031"'
            elif cat == 2:
                url = 'http://www.amazon.in/Speakers/b/ref=sd_allcat_sbc_tvelec_speakers?ie=UTF8&node=1389365031'
            else:
                url = 'http://www.amazon.in/electronics/b/ref=sd_allcat_sbc_tvelec_all_elec?ie=UTF8&node=976419031'

        # Men Fashion
        elif cat == 3:
            cat = int(input('''Choose one :
        1. Clothing
        2. Sunglasses
        3. Watches
        'Any Number for Other Category'\n'''))
            if cat == 1:
                url = 'http://www.amazon.in/Mens-Clothing/b/ref=sd_allcat_sbc_mfashion_clothing?ie=UTF8&node=1968024031'
            elif cat == 2:
                url = 'http://www.amazon.in/Sunglasses/b/ref=sd_allcat_sbc_mfashion_sunglasses?ie=UTF8&node=1968036031'
            elif cat == 3:
                url = 'http://www.amazon.in/Men-Watches/b/ref=sd_allcat_sbc_mfashion_watches?ie=UTF8&node=2563504031'
            else:
                url = 'http://www.amazon.in/b/ref=sd_allcat_sbc_mfashion_all?ie=UTF8&node=7459781031'

        # Women Fashion
        elif cat == 4:
            cat = int(input('''Choose one :
            1. Clothing
            2. Sunglasses
            3. Watches
            'Any Number for Other Electronics'\n'''))
            if cat == 1:
                url = 'http://www.amazon.in/Womens-clothing/b/ref=sd_allcat_sbc_wfashion_clothing?ie=UTF8&node=1953602031'
            elif cat == 2:
                url = 'http://www.amazon.in/Sunglasses/b/ref=sd_allcat_sbc_wfashion_sunglasses?ie=UTF8&node=1968401031'
            elif cat == 3:
                url = 'http://www.amazon.in/Women-Watches/b/ref=sd_allcat_sbc_wfashion_watches?ie=UTF8&node=2563505031'
            else:
                url = 'http://www.amazon.in/b/ref=sd_allcat_sbc_wfashion_all?ie=UTF8&node=7459780031'

        # Books
        elif cat == 5:
            cat = input('''Choose one :
        1. Fiction Book
        2. School Textbook
        'Any Number for Other Category'\n''')
            if cat == 1:
                url = '/literature-fiction-books/b/ref=sd_allcat_sbc_books_fiction?ie=UTF8&node=1318157031'
            elif cat == 2:
                url = 'http://www.amazon.in/School-Books/b/ref=sd_allcat_sbc_books_schooltexts?ie=UTF8&node=4149807031'
            else:
                url = 'http://www.amazon.in/Books/b/ref=sd_allcat_sbc_books_all?ie=UTF8&node=976389031'

        # choose no category
        else:
            print("You haven't choose any category hence search without category\n")
        # url for search
        return url
