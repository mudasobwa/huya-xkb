#!/bin/sh

TARGET_DIR="/usr/share/huya/xkb"
XKB_DIR="/usr/share/X11/xkb/symbols"
if [ ! -d $TARGET_DIR ]; then
  echo "Installing HUYA/XKB for the first time"
else
  echo "HUYA/XKB is already installed, reinstalling"
  cp $TARGET_DIR/*.bup /tmp
  rm -rf $TARGET_DIR
fi

echo "Cloning the repository..."
[ -d $XKB_DIR ] || exit 1

git clone https://github.com/mudasobwa/huya-xkb.git $TARGET_DIR
[ -f $XKB_DIR/ru_es ] && rm -rf $XKB_DIR/ru_es
ln -s $TARGET_DIR/ru_es.layout $XKB_DIR/ru_es

CURR_DIR=$(pwd)
cd $TARGET_DIR || exit 1

for i in ru es ; do
  cp -f $XKB_DIR/$i $TARGET_DIR/$i.bup
  patch -p0 -N --dry-run --silent $XKB_DIR/$i < $TARGET_DIR/$i.patch 2>/dev/null
  if [ $? -eq 0 ]; then
    patch -b $XKB_DIR/$i < $TARGET_DIR/$i.patch
  fi
done
cd "$CURR_DIR" || exit 2

echo "Removing xkb cache..."
rm /var/lib/xkb/*xkm 2>/dev/null

echo "Executing setxkbmap..."
setxkbmap

echo "Done."
