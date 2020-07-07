NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    rlist = []
    [rlist.append(name.title()) for name in names if name.title() not in rlist]
    print(rlist)
    return rlist
    pass


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    s = sorted(names, key=lambda x: x.split(" ")[-1], reverse=True)
    print(s)
    return s
    # ...


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    s = sorted(names, key=lambda x: len(x))
    print(s[0].split(' ')[0])
    return s[0].split(' ')[0]
    # ...

if __name__ == '__main__':
    dedup_and_title_case_names(NAMES)
    sort_by_surname_desc(NAMES)
    shortest_first_name(NAMES)
