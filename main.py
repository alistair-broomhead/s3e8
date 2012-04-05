
import time
time.sleep = lambda *x:None
def display(text):
    from data import data
    from render import render

    s = data['santa']
    render(text, s)


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
                for x in v:
                    display('\t%s %d' % (k, x(l)))
            if data['santa'] == 10e100j: return



if __name__ == "__main__":
    main()