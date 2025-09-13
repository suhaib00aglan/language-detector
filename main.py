import streamlit as st
import pandas as pd
import joblib
import numpy as np
import sys
import os

# إعداد المسارات بشكل صحيح للتطبيق المحزم
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# تحميل النموذج والمتجهات
try:
    model_path = resource_path('models/language_model.pkl')
    vectorizer_path = resource_path('models/vectorizer.pkl')
    
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
except Exception as e:
    st.error(f"⚠️ خطأ في تحميل النماذج: {e}")
    st.stop()

# واجهة التطبيق
st.set_page_config(page_title="كاشف اللغة", page_icon="🌍", layout="wide")
st.title('🌍 كاشف اللغة - Language Detection')
st.write('أدخل النص لاكتشاف لغته تلقائياً')

# واجهة الإدخال
user_input = st.text_area("النص:", height=100, placeholder="اكتب أو الصق النص هنا...")

if st.button('اكتشاف اللغة', type="primary"):
    if user_input.strip():
        try:
            # تحويل النص
            text_vec = vectorizer.transform([user_input])
            
            # التنبؤ
            prediction = model.predict(text_vec)[0]
            confidence = model.predict_proba(text_vec).max()
            
            # عرض النتيجة
            st.success(f'**اللغة: {prediction}**')
            st.info(f'**مستوى الثقة: {confidence:.2%}**')
            
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
    else:
        st.warning('⛔ يرجى إدخال نص أولاً')

# معلومات إضافية في الشريط الجانبي
if 'model' in globals():
    with st.sidebar:
        st.header("معلومات عن التطبيق")
        st.write("""
        هذا التطبيق يستخدم خوارزميات تعلم الآلة للكشف عن لغة النص المدخل.
        يدعم حالياً {} لغة مختلفة.
        """.format(len(model.classes_)))