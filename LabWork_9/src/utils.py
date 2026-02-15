from random import randint

def gen_matrix(rows=10, cols=10,):
    return [
        [
            randint(-1000,1000)
        for _ in range(cols)]
    for _ in range(rows)]
