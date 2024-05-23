import threading
import msvcrt

done = False
def get_input():
    while not done:
        io = input("Type something")
    return io

threading.Thread(target=get_input).start()

if msvcrt.kbhit():
    key = msvcrt.getch()
    if key == b'\x1b':
        done = True