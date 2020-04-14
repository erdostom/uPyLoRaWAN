# import machine
# import time


# state = 0

# led_pin = machine.Pin(16, machine.Pin.OUT)
# button_pin = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
# led_pin.value(0)

# def interrupt_fun(pin):
#     global state
#     state = not(state)
#     led_pin.value(state)
#     print(state)
#     time.sleep(1)

# button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=interrupt_fun)

# while True:
#     print('state')
#     time.sleep(1)