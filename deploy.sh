#!/bin/sh
rm -rf midas midas.zip
mkdir midas
cp -a LICENSE *.* midas
rm midas/deploy.sh
zip -r midas.zip midas
