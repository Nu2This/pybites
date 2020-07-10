import re
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    print(cars['Jeep'])
    out = ''
    for model in cars['Jeep']:
        out = out + model + ', '
        print(model)
    print(out.rstrip(', '))
    return out.rstrip(', ')

    pass


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    out = []
    for k, v in cars.items():
        print(v[0])
        out.append(v[0])
    print(out)
    return out


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    prog = re.compile('('+grep+')', flags=re.IGNORECASE)
    out = []

    for k, v in cars.items():
        for model in v:
            result = prog.search(model)
            print('result: ' + str(result))
            if result != None:
                out.append(model)

    print(sorted(out))
    return sorted(out)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""

    out_cars = {}
    for k, v in cars.items():
        print(f'Key: {k}\n Value: {v}')
        out_cars.update({k: sorted(v)})
    print(out_cars)
    return out_cars

if __name__ == '__main__':
#    get_all_jeeps(cars)
#    get_first_model_each_manufacturer(cars)
#    get_all_matching_models(cars)
    sort_car_models(cars)
