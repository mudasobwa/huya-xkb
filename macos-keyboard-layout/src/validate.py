# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

from maps import main
from maps import other
from maps import special


def check_data():
  """Assert that our own internal data makes sense."""

  # Special and other are disjoint
  assert(not(other.id_char.keys() & special.id_char.keys()))


  # Main map is an injection
  assert(len(set(main.key_id.values())) == len(main.key_id))

  # Main does not map to special ids
  assert(not(main.key_id.values() & special.id_char.keys()))
  # Main does not map to other ids
  assert(not(main.key_id.values() & other.id_char.keys()))

  # There are no unmappable ids
  fixed = set(other.id_char.keys()) | set(special.id_char.keys())
  mappable = set(main.key_id.values())
  unmappable = set(range(0, 128)) - fixed - mappable
  assert(not(unmappable))

