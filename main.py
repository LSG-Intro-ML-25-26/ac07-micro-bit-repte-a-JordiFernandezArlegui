def on_button_pressed_a():
    global player, cpu
    player = piedra
    cpu = randint(1, 3)
    if piedra == cpu:
        basic.show_string("Empate!")
    else:
        if papel == cpu:
            basic.show_string("Perdiste!")
        else:
            basic.show_string("Ganaste!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global player, cpu
    player = tijeras
    cpu = randint(1, 3)
    if piedra == cpu:
        basic.show_string("Perdiste!")
    else:
        if papel == cpu:
            basic.show_string("Ganaste!")
        else:
            basic.show_string("Empate!")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global player, cpu
    player = papel
    cpu = randint(1, 3)
    if piedra == cpu:
        basic.show_string("Ganaste!")
    else:
        if papel == cpu:
            basic.show_string("Empate!")
        else:
            basic.show_string("Perdiste!")
input.on_button_pressed(Button.B, on_button_pressed_b)

cpu = 0
player = 0
tijeras = 0
papel = 0
piedra = 0
piedra = 1
papel = 2
tijeras = 3