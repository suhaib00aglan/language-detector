# -*- mode: python ; coding: utf-8 -*-


from PyInstaller.utils.hooks import collect_all
streamlit_datas, streamlit_binaries, streamlit_hiddenimports = collect_all('streamlit')
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=streamlit_binaries,
    datas=[
        ('models/language_model.pkl', 'models'),
        ('models/vectorizer.pkl', 'models'),
        ('data/cleaned_language_data.csv', 'data')
    ] + streamlit_datas,
    hiddenimports=[
        'pandas', 'sklearn', 'scipy', 'numpy',
        'sklearn.utils._weight_vector',
        'sklearn.neighbors._typedefs',
        'sklearn.neighbors._quad_tree'
    ] + streamlit_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='LanguageDetector',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # تغيير إلى True إذا كنت تريد نافذة console
    # icon='icon.ico',  # أضف أيقونة إذا كنت تريد
)