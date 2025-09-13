# إنشاء ملف جديد باسم app.py في المجلد الرئيسي
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import re

# تحميل النموذج والمتجهات
try:
    model = joblib.load('models/language_model.pkl')
    vectorizer = joblib.load('models/vectorizer.pkl')
except:
    st.error("⚠️ لم يتم العثور على النموذج أو المتجهات. تأكد من تشغيل notebooks التدريب أولاً.")
    st.stop()

st.set_page_config(page_title="كاشف اللغة", page_icon="🌍")
st.title('🌍 كاشف اللغة - Language Detection')
st.write('أدخل النص لاكتشاف لغته تلقائياً')

# معلومات إضافية
with st.sidebar:
    st.header("معلومات عن التطبيق")
    st.write("""
    هذا التطبيق يستخدم خوارزميات تعلم الآلة للكشف عن لغة النص المدخل.
    يدعم حالياً {} لغة مختلفة.
    """.format(len(model.classes_)))
    st.write("**اللغات المدعومة:**")
    st.write(", ".join(sorted(model.classes_)))

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
            
            # عرض احتمالات جميع اللغات
            with st.expander("عرض الاحتمالات لكل اللغات"):
                probs = model.predict_proba(text_vec)[0]
                languages = model.classes_
                
                prob_df = pd.DataFrame({
                    'اللغة': languages,
                    'الاحتمال': probs
                }).sort_values('الاحتمال', ascending=False)
                
                st.dataframe(prob_df, hide_index=True, use_container_width=True)
                
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
    else:
        st.warning('⛔ يرجى إدخال نص أولاً')

