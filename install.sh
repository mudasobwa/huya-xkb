#!/bin/sh

TARGET_DIR="/usr/share/huya/xkb"
if [ ! -d $TARGET_DIR ]; then
    echo "Installing HUYA/XKB for the first time"
else
    echo "HUYA/XKB is already installed, reinstalling"
    cp $TARGET_DIR/*.bup /tmp
    rm -rf $TARGET_DIR
fi

echo "Cloning the repository..."
git clone https://github.com/mudasobwa/huya-xkb.git $TARGET_DIR
cd $TARGET_DIR
[ "$1" = "ask" ] && export ASK="true"
cd /usr/share/X11/xkb/symbols || exit 1
ln -s $TARGET_DIR/ru_es.layout ru_es
for i in ru es ; do
  cp $i $TARGET_DIR/$i.bup
  patch $i < $TARGET_DIR/$i.patch
done

echo "Removing xkb cache..."
rm /var/lib/xkb/*xkm 2>/dev/null

echo "Done."
