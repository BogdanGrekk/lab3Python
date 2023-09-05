from translate_pack import googletr_mod
from translate_pack.deeptr_mod import LangDetect, TransLate, CodeLang, LanguageList
if __name__ == "__main__":
    # Демонстрація роботи функцій
    print("1. Визначення мови тексту:")
    text = "Привіт, світе!"
    print(f"Текст: {text}")
    print(LangDetect(text))

    print("\n2. Переклад тексту:")
    dest_lang = "en"
    print(f"Текст для перекладу на {dest_lang}: {TransLate(text, src='auto', dest=dest_lang)}")

    print("\n3. Визначення коду мови:")
    lang_name = "English"
    print(f"Код мови для {lang_name}: {CodeLang(lang_name)}")

    print("\n4. Виведення таблиці мов:")
    print(LanguageList(out="file", text="Добрий день"))