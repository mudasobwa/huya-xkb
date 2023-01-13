# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>


# Keys that are mapped to various special actions, i.e. they do not produce
# a printable character when typed.
#
# The idea is that these keys probably should be mapped on all levels.
#
# * The ones mapped not to None come from the default Ukelele layout.
#   I am not sure what is the meaning of those mysterious code points that
#   Ukelele maps them to, so we just do the same.
# * The ones mapped to None are not form Ukelele, but rather were added
#   by myself for completeness. We don’t map them because I have no idea
#   how to determine the correct code point.
id_char = {
  36: '\x0D',  # enter
  48: '\x09',  # tab
  51: '\x08',  # delete
  53: '\x1B',  # esc
  54: None,  # right command
  55: None,  # command
  56: None,  # shift
  57: None,  # caps lock
  58: None,  # option
  59: None,  # control
  60: None,  # right shift
  61: None,  # right option
  62: None,  # right control
  63: None,  # bottom-left fn

  72: '\x1F',  # volume up
  73: None,  # volume down
  74: None,  # mute

  # Arrows and block above them
  114: '\x05',  # help (or top-right fn?)
  115: '\x01',  # home
  116: '\x0B',  # page up
  117: '\x7F',  # delete forward
  119: '\x04',  # end
  121: '\x0C',  # page down
  123: '\x1C',  # Left
  124: '\x1D',  # Right
  125: '\x1F',  # Down
  126: '\x1E',  # Up

  # F keys
  122: '\x10',  # f1
  120: '\x10',  # f2
  99:  '\x10',  # f3
  118: '\x10',  # f4
  96:  '\x10',  # f5
  97:  '\x10',  # f6
  98:  '\x10',  # f7
  100: '\x10',  # f8
  101: '\x10',  # f9
  109: '\x10',  # f10
  103: '\x10',  # f11
  111: '\x10',  # f12
  105: '\x10',  # f13
  107: '\x10',  # f14
  113: '\x10',  # f15
  106: '\x10',  # f16
  64:  '\x10',  # f17
  79:  '\x10',  # f18
  80:  '\x10',  # f19
  90:  '\x10',  # f20

  # Numpad keyboard on the right
  71: '\x1B',  # Clear
  76: '\x03',  # Enter

  # Unknown (??)
  52:  '\x03',
  66:  '\x1D',
  68:  None,
  70:  '\x1C',
  77:  '\x1E',
  108: None,
  110: None,
  112: None,
  127: None,
}

