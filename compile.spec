import sys

a = Analysis(['src/BloonsFarmUI.py'],
             hiddenimports=['keyboard', 'pyautogui', 'pyqt5', 'pynput'],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          # Static link the Visual C++ Redistributable DLLs if on Windows
          a.binaries + [('msvcp100.dll', 'C:\\Windows\\System32\\msvcp100.dll', 'BINARY'),
                        ('msvcr100.dll', 'C:\\Windows\\System32\\msvcr100.dll', 'BINARY')]
          if sys.platform == 'win32' else a.binaries,
          a.zipfiles,
          a.datas + [('Resources/LuckiestGuy-Regular.ttf','src/Resources/LuckiestGuy-Regular.ttf', "DATA"),('Resources/btdfarmicon.ico', 'src/Resources/btdfarmicon.ico', "DATA")],
          name=os.path.join('dist', 'BloonsFarmUI' + ('.exe' if sys.platform == 'win32' else '')),
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='src/Resources/btdfarmicon.ico')

# Build a .app if on OS X
if sys.platform == 'darwin':
   app = BUNDLE(exe,
                name='BloonsFarmUI.app',
                icon='src/Resources/btdfarmicon.ico')
