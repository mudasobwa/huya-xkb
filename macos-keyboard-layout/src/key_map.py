# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

from maps import main
from maps import other
from maps import special


class IdMap:
  """One level of a keyboard layout.

  This is a map from key ids.
  """

  def __init__(self, id_map):
    self._id_map = id_map

  @staticmethod
  def from_keymap(key_map):
    return IdMap(resolve_map(key_map))


  # Dict-like interface
  def keys(self):
    return self._id_map.keys()
  def items(self):
    return self._id_map.items()
  def __missing__(self, _key):
    return None

  # Set-like interface
  def __or__(self, other):
    result = self._id_map.copy()
    result.update(other._id_map)
    return IdMap(result)

  # XML
  def yield_xml(self, index):
    yield '<keyMap index="{}">'.format(index)
    for k, v in sorted(self._id_map.items()):
      if v is None: continue
      yield '  <key code="{}" output="{}"/>'.format(k, kbd_escape(v))
    yield '</keyMap>'


def kbd_escape(char):
  """Like XML escape, but escapes everything :)."""

  if len(char) == 0:
    return char
  elif len(char) == 1:
    return '&#x{:x};'.format(ord(char))
  else:
    assert(False)

def resolve_map(key_map):
  """Translate ANSI human-readable key names to ids.

  >>> resolve_map({'a': 'A', '/': '?'})
  {0: 'A', 44: '?'}
  """

  id_map = {main.key_id[k]: v for k, v in key_map.items()}

  # User is not trying to map a special key
  assert(not(special.id_char.keys() & id_map.keys()))
  # User is not trying to map an other key
  assert(not(other.id_char.keys() & id_map.keys()))

  return id_map
