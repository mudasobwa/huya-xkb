# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

from collections import OrderedDict
import re
import xml.etree.cElementTree as ET

from key_map import IdMap
from layers import control
from maps import other, special


class Layout:
  """A keyboard layout consisting of multiple levels."""

  def __init__(self, group, id, sid, lang, name, levels):
    """Create a new keyboard layout.

    levels: ordered map from modifiers list to IdMap
    """
    self._group = group
    self._id = id
    self._sid = sid
    self._lang = lang
    self._name = name
    self._levels = levels

  @property
  def sid(self):
    return self._sid

  @property
  def lang(self):
    return self._lang

  @property
  def name(self):
    return self._name

  def __getitem__(self, index):
    return list(self._levels.values())[index]

  # XML
  def yield_xml(self):
    yield '<?xml version="1.1" encoding="UTF-8"?>'
    yield '<!DOCTYPE keyboard SYSTEM "file://localhost/System/Library/DTDs/KeyboardLayout.dtd">'
    yield '<keyboard group="{}" id="{}" name="{}" maxout="1">'.format(self._group, self._id, self._name)

    def yield_layouts():
      yield '<layouts>'
      yield '<layout first="0" last="17" mapSet="ANSI" modifiers="Mods"/>'
      yield '</layouts>'
    for line in yield_layouts():
      yield line

    def yield_modifier_map():
      yield '<modifierMap id="Mods" defaultIndex="0">'
      for index, mods in enumerate(self._levels.keys()):
        yield '  <keyMapSelect mapIndex="{}">'.format(index)
        if not isinstance(mods, tuple):
          yield '    <modifier keys="{}"/>'.format(mods)
        else:
          for mods1 in mods:
            yield '    <modifier keys="{}"/>'.format(mods1)
        yield '  </keyMapSelect>'
      yield '</modifierMap>'
    for line in yield_modifier_map():
      yield line

    def yield_key_map_sets():
      yield '<keyMapSet id="ANSI">'
      for index, id_map in enumerate(self._levels.values()):
        for line in id_map.yield_xml(index):
          yield '  ' + line
      yield '</keyMapSet>'
    for line in yield_key_map_sets():
      yield line

    yield '</keyboard>'


class TypoLayout(Layout):
  """A standard Typography Layout template.

  It automatically handles Shift vs. Caps Lock both for the standard
  and typo levels; special keys; and translates from ANSI key maps.
  """
  def __init__(
      self,
      group, id, lang, name,
      alpha, alpha_shifted,
      numsym, numsym_shifted,
      typo, typo_shifted,
      base=None,
      **kwargs):

    (id_special, id_other) = map(IdMap, [special.id_char, other.id_char])
    ( id_alpha, id_Alpha,
      id_numsym, id_Numsym,
      id_typo, id_Typo,
      id_control ) = map(IdMap.from_keymap,
    [ alpha, alpha_shifted,
      numsym, numsym_shifted,
      typo, typo_shifted,
      control.chars])

    levels = OrderedDict()

    if base is not None:
      # Index 0 (default) is the default idnex of the base keymap
      levels['command anyControl? anyShift? caps? anyOption?'] = base[0]

    levels.update([
      ('', id_special | id_other | id_alpha | id_numsym),
      ('anyShift', id_special | id_other | id_Alpha | id_Numsym),

      ('caps', id_special | id_other | id_Alpha | id_numsym),
      ('caps anyShift', id_special | id_other | id_alpha | id_Numsym),

      ('anyOption caps?', id_special | id_typo),
      ('anyOption anyShift caps?', id_special | id_Typo),

      ('command? anyControl anyShift? caps? anyOption?', id_special | id_other | id_control),
    ])

    super().__init__(group, id, 'typo.' + lang, lang, name + ' – Typography', levels)
