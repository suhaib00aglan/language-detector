import joblib

# تحميل النموذج وأداة التحويل
model = joblib.load('../models/language_model.pkl')
vectorizer = joblib.load('../models/vectorizer.pkl')

def predict_language(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    confidence = model.predict_proba(text_vec).max()
    return prediction, confidence

if __name__ == "__main__":
    print("أدخل النص المراد التعرف على لغته (أو اكتب 'خروج' للخروج):")
    while True:
        text = input('> ')
        if text.strip().lower() in ['خروج', 'exit', 'quit']:
            break
        prediction, confidence = predict_language(text)
        print(f"اللغة المتوقعة: {prediction} (ثقة: {confidence:.2%})\n")
