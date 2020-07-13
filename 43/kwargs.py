def get_profile(name = 'julian', profession = 'programmer'):
    while True:
        try:
            out = str(name + ' is a ' + profession)

        except TypeError:
            print('bleh')
    return out
