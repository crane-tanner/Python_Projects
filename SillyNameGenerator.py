import random

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
            "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
            'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
            'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
            'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
            'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
            'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
            'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
            'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
            'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
            'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
            "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
            'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
            'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
            "Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
           'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
           'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
           'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
           'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
           'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
           'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
           'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
           'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
           'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
           'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
           'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
           'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
           'Woolysocks')

print("Welcome to the silly name generator!")
while True:
    first_name = random.choice(first)
    last_name = random.choice(last)
    print("\n" + "{} {}".format(first_name, last_name))
    try_again = input("\nPress enter to generate another or q to quit: ")
    if try_again == 'q':
        break

#input("Press enter to exit program")


