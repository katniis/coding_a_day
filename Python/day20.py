# 20. output fibonacci sequence (base 1) on each keypress

import keyboard

x1: int = 1
x2: int = 1

print("Press any key to show the next Fibonacci number.")
print("press q to exti")

while True:
    event = keyboard.read_event()
    if event.event_type == "down":
        if event.name == "q":
            print("exit")
            break
        else:
            print(x2)
            x1, x2 = x2, x1 + x2