from googletrans import Translator, LANGUAGES

# Ініціалізуємо глобальний об'єкт перекладача
trans_instance = Translator()


def CodeLang(lang: str) -> str:
    """
    Повертає код мови або її назву на основі введеного ідентифікатора.
    """
    reverse_LANGUAGES = {value.lower(): key for key, value in LANGUAGES.items()}
    lang_identifier_lower = lang.lower()

    if lang_identifier_lower in reverse_LANGUAGES:
        return reverse_LANGUAGES[lang_identifier_lower]

    if lang_identifier_lower in LANGUAGES:
        return LANGUAGES[lang_identifier_lower].capitalize()

    return "Мова не знайдена"


def TransLate(text: str, src: str, dest: str) -> str:
    """
    Функція повертає текст перекладений на задану мову або повідомлення про помилку.
    """
    translation_result = trans_instance.translate(text, src=src, dest=dest)
    if translation_result:
        return translation_result.text
    else:
        return "Помилка перекладу"


def LangDetect(text: str, set: str = "all") -> str:
    """
    Функція визначає мову та коефіцієнт довіри для заданого тексту.
    """
    detection_result = trans_instance.detect(text)

    if set == "lang":
        return detection_result.lang
    elif set == "confidence":
        return str(detection_result.confidence)
    elif set == "all":
        return f"Detected(lang={detection_result.lang}, confidence={detection_result.confidence})"
    else:
        return "Неправильний параметр set"


def LanguageList(out: str = "screen", text: str = None) -> str:
    """
    Виводить в файл або на екран таблицю всіх мов, що підтримуються, та їх кодів.
    """
    header = "N Language      ISO-639 code Text"
    separator = "-" * 56

    translations = []

    for index, (code, lang) in enumerate(LANGUAGES.items(), 1):
        translated_text = TransLate(text, src='uk', dest=code) if text else ""
        translations.append(f"{index:<2} {lang:<12} {code:<12} {translated_text}")

    output = "\n".join([header, separator] + translations + ["Ok"])

    if out == "screen":
        print(output)
        return "Ok"
    elif out == "file":
        with open("lang_list_g.txt", "w", encoding="utf-8") as file:
            file.write(output)
        return "Ok"
    else:
        return "Неправильний параметр out"

