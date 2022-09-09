ua_letters = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
              'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']


def coder(text: str, offset=1):
    coded_text = ''

    for i, v in enumerate(text.lower().strip()):
        coded_text += v if v == ' ' or v in '1234567890' else str(ua_letters[0 if v == 'я' else ua_letters.index(v) + offset])
    return coded_text


def decoder(text: str, offset=1):
    decoded_text = ''
    for i, v in enumerate(text.lower().strip()):
        decoded_text += v if v == ' ' or v in '1234567890' else str(ua_letters[0 if v == 'я' else ua_letters.index(v) - offset])
    return decoded_text


if __name__ == '__main__':
    text = input("Enter text: ")
    # print decoder or coder
    print(decoder('а леп'))
