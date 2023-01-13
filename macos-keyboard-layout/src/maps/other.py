# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>


# Keys that produce a printable symbol but we do not allow
# overriding them.
# The idea is that these get mapped only on the first two layers.
id_char = {
  # Numpad keyboard on the right
  65: '.',  # Weird key to the right of zero
  67: '*',
  69: '+',
  75: '/',
  78: '-',
  81: '=',
  82: '0',
  83: '1',
  84: '2',
  85: '3',
  86: '4',
  87: '5',
  88: '6',
  89: '7',
  91: '8',
  92: '9',

  # JIS
  93:  None,  # JIS yen
  94:  None,  # JIS underscore
  95:  None,  # JIS keypad comma
  102: None,  # JIS eisu
  104: None,  # JIS kana
}

