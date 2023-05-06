def read_next(*args):

    for el in args:
        for x in el:
            yield x

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)




