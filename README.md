# Language Detection Project | مشروع كشف اللغة

---

## 🚀 Overview | نظرة عامة

**English:**
This project is a machine learning application for automatic language detection of text. It uses a trained model to predict the language of any input text, with a modern web interface built using Streamlit. The project includes data processing, model training, evaluation, and a user-friendly interface for real-time predictions.

**العربية:**
هذا المشروع عبارة عن تطبيق ذكاء اصطناعي لاكتشاف لغة النصوص تلقائيًا باستخدام خوارزميات تعلم الآلة. يوفر واجهة ويب تفاعلية مبنية بـ Streamlit، ويشمل معالجة البيانات، تدريب النموذج، التقييم، وواجهة سهلة للمستخدم لعرض النتائج مباشرة.

---


## 👤 Author | المنفذ
- **Suhaib Abdullah Ahmed Almalhani | صهيب عبد الله أحمد الملحاني**
- **Mechatronics Student, Sana'a University | طالب ميكاترونكس،مستوى خامس، جامعة صنعاء**
- **Academic Number | الرقم الأكاديمي:** 202174006

---

## ⚙️ Installation & Setup | التثبيت والتشغيل

**English:**
1. Make sure you have Python 3.12+ and [uv](https://github.com/astral-sh/uv) or pip installed.
2. Clone the repository and navigate to the project folder:
   ```bash
   git clone <repo-url>
   cd project
   ```
3. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   # أو
   pip install -r requirements.txt
   ```
4. To run the web app:
   ```bash
   uv run streamlit run main.py
   # أو
   streamlit run main.py
   ```

**العربية:**
1. تأكد من وجود Python 3.12+ ووجود أداة uv أو pip.
2. استنسخ المستودع وادخل مجلد المشروع:
   ```bash
   git clone <repo-url>
   cd project
   ```
3. ثبّت المتطلبات:
   ```bash
   uv pip install -r requirements.txt
   # أو
   pip install -r requirements.txt
   ```
4. لتشغيل التطبيق:
   ```bash
   uv run streamlit run main.py
   # أو
   streamlit run main.py
   ```

---

## 🗂️ Project Structure | هيكلية المشروع

```
project/
├── app.py                # (اختياري) تطبيق إضافي أو تجارب
├── build.py              # سكريبتات بناء أو تحزيم
├── main.py               # التطبيق الرئيسي (واجهة Streamlit)
├── requirements.txt      # متطلبات المشروع
├── models/               # النماذج والمتجهات المدربة
│   ├── language_model.pkl
│   └── vectorizer.pkl
├── data/                 # بيانات التدريب والاختبار
│   ├── cleaned_language_data.csv
│   └── Language Detection.csv
├── src/
│   └── predict_language.py # كود التنبؤ بالنصوص
├── notebooks/            # دفاتر Jupyter للاستكشاف والتدريب
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
├── docs/                 # وثائق وصور
│   └── confusion_matrix.png
└── ...
```

---

## 🖥️ Usage | طريقة الاستخدام

**English:**
- Open the app in your browser after running the above command.
- Enter or paste any text in the input box and click "Detect Language".
- The app will display the predicted language and confidence score.
- This is the link in the browser:
 Local URL: http://localhost:8501
  Network URL: http://192.168.43.38:8501

**العربية:**
- افتح التطبيق في المتصفح بعد تشغيل الأمر أعلاه.
- أدخل أو الصق أي نص في مربع الإدخال واضغط "اكتشاف اللغة".
- سيعرض التطبيق اللغة المتوقعة ونسبة الثقة.
- وهذا هو الرابط في المتصفح:
 Local URL: http://localhost:8501
  Network URL: http://192.168.43.38:8501
---

## 🤖 Model Details | تفاصيل النموذج

- **Algorithm:** Machine Learning (e.g., Random Forest, Logistic Regression)
- **Vectorizer:** TF-IDF or CountVectorizer
- **Training Data:** `data/cleaned_language_data.csv`
- **Model File:** `models/language_model.pkl`
- **Vectorizer File:** `models/vectorizer.pkl`
- **Evaluation:** See `notebooks/04_model_evaluation.ipynb` and `docs/confusion_matrix.png`

---

## 📦 Packaging as EXE | تحويل التطبيق إلى ملف تنفيذي

**English:**
To create a standalone executable (Windows):
```bash
pyinstaller main.py --onefile --hidden-import=streamlit
```
The EXE will be in the `dist/` folder.

**العربية:**
لتحويل التطبيق إلى ملف تنفيذي مستقل (ويندوز):
```bash
pyinstaller main.py --onefile --hidden-import=streamlit
```
ستجد الملف التنفيذي في مجلد `dist/`.
---

## 📋 Requirements | المتطلبات

- Python 3.12+
- Libraries: pandas, numpy, scikit-learn, matplotlib, jupyter, streamlit, PyQt5
- See `requirements.txt`

---

## 📓 Notebooks | دفاتر Jupyter
- Data exploration, cleaning, training, and evaluation are documented in the `notebooks/` folder.

---

## 📝 License | الرخصة
This project is for educational and research purposes.

---

## ⚠️ Issues Faced During Development | المشاكل التي واجهتها أثناء التطوير
**English:**
- Faced an issue running the EXE file generated by PyInstaller; the executable did not work as expected and needs further investigation.

**العربية:**
- واجهت مشكلة في تشغيل الملف التنفيذي (EXE) الناتج من PyInstaller، حيث لم يعمل بالشكل المطلوب ويحتاج إلى مزيد من البحث لاحقًا.

---

## 💻 CMD Commands Used | أوامر CMD المستخدمة

**English:**
Here are all the CMD commands I used and needed during the project:

```cmd
python app1.py
python project/app1.py
pyinstaller app.py --onefile
pyinstaller main.py --onefile --hidden-import=streamlit
pip install pyinstaller
pip install PyQt5
pip install streamlit
uv pip install -r requirements.txt
uv run streamlit run main.py
streamlit run main.py
```

**العربية:**
جميع أوامر CMD التي استخدمتها واحتجتها أثناء المشروع:

```cmd
python app1.py
python project/app1.py
pyinstaller app.py --onefile
pyinstaller main.py --onefile --hidden-import=streamlit
pip install pyinstaller
pip install PyQt5
pip install streamlit
uv pip install -r requirements.txt
uv run streamlit run main.py
streamlit run main.py
```

---


## ⭐ Extra Notes | ملاحظات إضافية

**English:**
- The project is fully bilingual (Arabic/English) for maximum accessibility.
- All code, data, and results are organized for easy navigation.
- The Streamlit app provides a modern, interactive user experience.
- The project is ready for further improvements and deployment.

**العربية:**
- المشروع ثنائي اللغة بالكامل (عربي/إنجليزي) لسهولة الوصول لجميع المستخدمين.
- جميع الأكواد والبيانات والنتائج منظمة لسهولة التصفح.
- تطبيق Streamlit يوفر تجربة مستخدم حديثة وتفاعلية.
- المشروع جاهز لمزيد من التحسينات أو النشر مستقبلاً.

---

<p align="center">
   <b>Developed with ❤️ by Suhaib Abdullah Ahmed Almalhani</b>
</p>
---


## Contact | التواصل
- WhatsApp: [+967771120691](https://wa.me/967771120691)
- Email: <shyba103@gmail.com>

---

> **Developed by Suhaib Abdullah Ahmed Almalhani | تم التطوير بواسطة صهيب عبد الله أحمد الملحاني**
"# -language-detector" 
"# -language-detector" 
"# -language-detector" 
"# language-detector" 
"# language-detector" 
"# language-detector" 
