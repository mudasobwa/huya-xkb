# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

from layers import english, typo
from layout import TypoLayout


layout = TypoLayout(
  0, -8324, 'en', 'English',
  alpha=english.alpha, alpha_shifted={k: v.upper() for k,v in english.alpha.items()},
  numsym=english.numsym, numsym_shifted=english.numsym_shifted,
  typo=typo.normal, typo_shifted=typo.shifted
)

if __name__ == '__main__':
  print('\n'.join(layout.yield_xml()))
