# 19. output a number, and wait for a keypress, then increment the number and print it out, then repeat

import keyboard # pip install keyboard

# The operating system sends multiple key events (known as key repeat or key auto-repeat).
# keyboard.read_key() captures all of them, even from a single long press.keyboard.read_key() captures all of them, even from a single long press.
# keyboard.read_event() to wait for both press and release, and respond only on 'down' (first press) or 'up' (after full key release).

x: int = 1
print("Press q to exit")
while True:
    event = keyboard.read_event()
    if event.event_type == "down":
        if event.name == "q":
            print("exit")
        else:
            print(x)
            x+=1