rm -rf dist
cxfreeze main.py -c --target-dir dist --target-name=PyBlock.exe  --icon=gui/skin/images/logo.ico --base-name=win32gui
mkdir -p dist/log
mkdir -p dist/gui/skin
cp -rf gui/skin/* dist/gui/skin
cp -rf web dist
