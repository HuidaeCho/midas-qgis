#!/bin/sh
rm -rf midas midas.zip
mkdir midas
cp -a LICENSE *.* midas
rm midas/package.sh
zip -r midas.zip midas
