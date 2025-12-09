input.onButtonPressed(Button.A, function () {
    player = piedra
    cpu = randint(1, 3)
    if (piedra == cpu) {
        basic.showString("Empate!")
    } else if (papel == cpu) {
        basic.showString("Perdiste!")
    } else {
        basic.showString("Ganaste!")
    }
})
input.onButtonPressed(Button.AB, function () {
    player = tijeras
    cpu = randint(1, 3)
    if (piedra == cpu) {
        basic.showString("Perdiste!")
    } else if (papel == cpu) {
        basic.showString("Ganaste!")
    } else {
        basic.showString("Empate!")
    }
})
input.onButtonPressed(Button.B, function () {
    player = papel
    cpu = randint(1, 3)
    if (piedra == cpu) {
        basic.showString("Ganaste!")
    } else if (papel == cpu) {
        basic.showString("Empate!")
    } else {
        basic.showString("Perdiste!")
    }
})
let cpu = 0
let player = 0
let tijeras = 0
let papel = 0
let piedra = 0
piedra = 1
papel = 2
tijeras = 3
