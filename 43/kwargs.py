def get_profile(*, name = 'julian', profession = 'programmer'):
    try:
        out = str(name + ' is a ' + profession)

    except TypeError:
        print('bleh')
    print(out)
    return out

if __name__ == '__main__':
    get_profile('julian')
