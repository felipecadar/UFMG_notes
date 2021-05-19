# Author: Felipe Cadar Chamone
# run: python3 thread.txt


import threading

N_INT = 10

# Bool mostrando se o numero deve ser printado
shoud_print = [False] * N_INT

# Lista que guarda os numeros
to_print = [None] * N_INT

#thread que le N_INT numeros
def read():
    global to_print
    for i in range(N_INT):
        to_print[i] = input()
        shoud_print[i] = True

#thread que printa os N_INT numeros
def write():
    global shoud_print
    j = 0
    while j < N_INT:
        for i, el in enumerate(shoud_print):
            if el:
                j += 1
                print(to_print[i])
                shoud_print[i] = False

if __name__ == "__main__":
    write_t = threading.Thread(target=write)
    read_t  = threading.Thread(target=read)

    write_t.start()
    read_t.start()

    read_t.join()
    write_t.join()