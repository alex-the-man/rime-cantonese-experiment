#!/bin/bash

echo "Backup original librime... It requires sudo. Please eneter your account password if prompted."
sudo cp /Library/Input\ Methods/Squirrel.app/Contents/Frameworks/librime.1.dylib /Library/Input\ Methods/Squirrel.app/Contents/Frameworks/librime.1.dylib.org-`date +"%s"`

echo "Install patched librime..."
sudo cp mac-lib/librime.1.dylib /Library/Input\ Methods/Squirrel.app/Contents/Frameworks/librime.1.dylib

echo "Install new schema"
cp -r schema/* $HOME/Library/Rime

echo "Please edit $HOME/Library/Rime/default.custom.yaml to enable new schema: jyut6ping3neo"
open $HOME/Library/Rime/default.custom.yaml

echo "Please logoff to restart Squirrel. Then redeploy Squirrel to build the new schema."
