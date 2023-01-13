<!-- SPDX-License-Identifier: MPL-2.0 -->
<!-- © 2019 Kirill Elagin <kirelagin@gmail.com> -->

macOS keyboard layout generator
================================

This small tool simplifies creating custom keyboard layouts for macOS.


Typography layouts
-------------------

_`misc:typo` for your MacBook._

This repository also contains everything needed to build a typography layout. The
typography layer is based on the [`typo` modifier from `xkeyboard-config`][typo-xkbd],
which in turn is based on the [Typography Layout by Ilya Birman][typo-birman].

[typo-xkbd]: https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/blob/master/symbols/typo
[typo-birman]: https://ilyabirman.net/projects/typography-layout/

You can build an English Typography layout by running:

* `PYTHONPATH=src python3 src/layouts/typo/english.py > english_typo.keylayout`

Then install it with:

* `cp english_typo.keylayout ~/Library/"Keyboard Layouts"/`

Bundles
--------

In addition to simple `.keylayout` files, macOS supports layout bundles.
The most important reason to distribute your layouts as bundles is that, apparently,
only in a bundle you can specify the language category for a layout; all
`.keylayout` layouts seem to always end in the “Others” group.

See the `bin/bundle` script that builds a bundle containing all typography layouts
defined in this project.
