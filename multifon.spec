# -*- mode: python -*-

block_cipher = None


a = Analysis(['multifon.py', 'multifon.spec'],
             pathex=['C:\\Python27\\work\\multifon'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='multifon',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='C:\\Python27\\work\\multifon\\icon.ico')
