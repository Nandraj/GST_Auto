# -*- mode: python -*-

block_cipher = None


a = Analysis(['GST_Auto_Main.py'],
             pathex=['C:\\Users\\Admin\\Desktop\\GST_Auto_1dot5'],
             binaries=[],
             datas=[('N.ico', '.')],
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='NR GST Auto',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='N.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='NR GST Auto')
