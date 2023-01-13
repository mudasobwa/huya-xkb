# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

# When the “control” key is down we need to send a control character.
# These come from standard layouts. Almost all of them turn out to be
# the standard terminal control characters.

chars = {
  # '\x00' (^@) is missing
  'a': '\x01',
  'b': '\x02',
  'c': '\x03',
  'd': '\x04',
  'e': '\x05',
  'f': '\x06',
  'g': '\x07',
  'h': '\x08',
  'i': '\x09',
  'j': '\x0a',
  'k': '\x0b',
  'l': '\x0c',
  'm': '\x0d',
  'n': '\x0e',
  'o': '\x0f',
  'p': '\x10',
  'q': '\x11',
  'r': '\x12',
  's': '\x13',
  't': '\x14',
  'u': '\x15',
  'v': '\x16',
  'w': '\x17',
  'x': '\x18',
  'y': '\x19',
  'z': '\x1a',
  '[': '\x1b',
 '\\': '\x1c',
  ']': '\x1d',
  # '\x1e' (^^) is missing
  '-': '\x1f',

  # Not sure if it makes any sense to map the following keys,
  # but we do this just in case, because other layouts do.

  '1': '1',
  '2': '2',
  '3': '3',
  '4': '4',
  '5': '5',
  '6': '6',
  '7': '7',
  '8': '8',
  '9': '9',
  '0': '0',
  '=': '=',

  ';': ';',
  "'": "'",
  ',': '/',
  '.': '.',
  ' ': ' ',
  '`': '`',

  '§': '0',
}
