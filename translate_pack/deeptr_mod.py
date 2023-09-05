from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs


from langdetect import detect

def CodeLang(lang: str) -> str:
    try:
        detected_lang = detect(lang)
        return detected_lang
    except:
        return "Мова не знайдена"


def TransLate(text: str, src: str, dest: str = 'en') -> str:
    try:
        return GoogleTranslator(source=src, target=dest).translate(text)
    except Exception as e:
        return str(e)


def LangDetect(text: str, set: str = "all") -> str:
    detected_langs = detect_langs(text)
    primary_detection = detected_langs[0]
    detected_lang = primary_detection.lang
    confidence = primary_detection.prob

    if set == "lang":
        return detected_lang
    elif set == "confidence":
        return str(confidence)
    elif set == "all":
        return f"Detected(lang={detected_lang}, confidence={confidence})"
    else:
        return "Неправильний параметр set"


def LanguageList(out: str = "screen", text: str = None) -> str:
    header = "N Language      ISO-639 code Text"
    separator = "-" * 56
    translator = GoogleTranslator(source='auto', target='en')  # create an instance of GoogleTranslator
    supported = translator.get_supported_languages(as_dict=True)

    translations = []

    for index, (code, lang) in enumerate(supported.items(), 1):
        translated_text = TransLate(text, src='uk', dest=code) if text else ""
        translations.append(f"{index:<2} {lang:<12} {code:<12} {translated_text}")

    output = "\n".join([header, separator] + translations + ["Ok"])

    if out == "screen":
        return output
    elif out == "file":
        with open("lang_list.txt", "w", encoding="utf-8") as file:
            file.write(output)
        return "Ok"
    else:
        return "Неправильний параметр out"
