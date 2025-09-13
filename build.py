import os
import subprocess
import shutil

def build_app():
    print("🚀 بدء بناء التطبيق...")
    
    # تنظيف المجلدات القديمة
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    
    # بناء التطبيق مباشرة من app.py
    result = subprocess.run([
        'pyinstaller',
        '--name', 'LanguageDetector',
        '--onefile',
        '--collect-all', 'streamlit',
        'app.py'
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ تم بناء التطبيق بنجاح!")
        print("📁 التطبيق موجود في مجلد: dist/LanguageDetector")
    else:
        print("❌ فشل بناء التطبيق:")
        print(result.stderr)

if __name__ == "__main__":
    build_app()