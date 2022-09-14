import string



def coder(txt, offset=1):
    coded_text = ''
    for i in txt:
        if i in 'я' and i.islower():
            coded_text = chr(ord(i)-31)
        elif i in 'Я' and i.isupper():
            coded_text = chr(ord(i)-63+32)
        elif i in string.punctuation+string.digits+' ':
            coded_text += i
        else:
            coded_text += chr(ord(i) + offset) if i != ' ' else i
    return coded_text

def decoder(txt, offset=1):
    decoded_text = ''
    for i in txt:
        if i == 'а' and i.islower():
            decoded_text += chr(ord(i)+31)
        elif i == 'А' and i.isupper():
            decoded_text += chr(ord(i)+31)
        elif i in string.punctuation+string.digits+' ':
            decoded_text += i
        else:
            decoded_text += chr(ord(i) - offset) if i != ' ' else i
    return decoded_text

if __name__ == '__main__':
    print("Ти можеш Вибрати: \n\"К\" якщо Кодувати чи \"Д\" якщо Декодувати")
    whats = input("Що ти хочеш робити: ")
    text = input("Введи текст: ")
    # print decoder or coder
    print(coder(text))
