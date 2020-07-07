names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    i = 1

    for name in names:
        country = countries[i-1]
        print(f'{i}. {name:11}{country}')
        i += 1
    pass

if __name__ == '__main__':
    enumerate_names_countries()
