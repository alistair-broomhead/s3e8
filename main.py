__author__ = 'al'

def display(text):
    from data import data

    s = data['santa']
    print s, text


def main():
    """
    Our Main function
    """
    import data as d

    data = d.data
    if data['sublime'] == d.__file__:
        display('I see what you did there...')
    else:
        display(data['sublime'].read())
    for s in data['emacs']:
        display(s)
        l = len(s)

        if l%2 == data['vi']:
            for k, v in data['pony'].items():
                display('\t%s %d' % (k, v(l)))



if __name__ == "__main__":
    main()