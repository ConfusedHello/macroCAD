import board

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation


keyboard = KMKKeyboard()
keyboard.modules.append(Layers())


keyboard.row_pins = (board.D0, board.D1)
keyboard.col_pins = (board.D2, board.D3, board.D4, board.D5)

keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [
        KC.L, KC.R, KC.C, KC.ESC,
        KC.D, KC.E, KC.MO(1), KC.MO(2)
    ],

    [
        KC.F, KC.T, KC.S, KC.LCTL(KC.Z),
        KC.F6, KC.DEL, KC.TRNS, KC.TRNS
    ],

    [
        KC.M, KC.P, KC.LCTL(KC.S), KC.ENT,
        KC.H, KC.SPC, KC.TRNS, KC.TRNS
    ]
]


if __name__ == '__main__':
    keyboard.go()
