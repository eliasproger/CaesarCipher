let ua_letters = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
function coder(text = '', offset = 1) {
    let coded_text = ''
    for (let v of Array.from(text.toLowerCase())) {
        if (v == ' ') coded_text += v
        if (v == 'я') coded_text += ua_letters[0]
        else coded_text += ua_letters[ua_letters.indexOf(v) + offset]
    }
    return coded_text.replaceAll('undefined', '');
}
function decoder(text = '', offset = 1) {
    let decoded_text = ''

    for (let v of Array.from(text.toLowerCase())) {
        if (v == ' ') decoded_text += v
        if (v == 'а') decoded_text += ua_letters.slice(-1).toString()
        else decoded_text += ua_letters[ua_letters.indexOf(v) - offset]
    }
    return decoded_text.replaceAll('undefined', '');
}

// Control Page

var reverse = document.getElementById('reverse_svg'),
    txt_coder = document.getElementById('code'),
    txt_decoder = document.getElementById('decode'),
    block = document.getElementById('block');

function reverse_fn() {
    block.classList.toggle('active')
    if (block.classList.contains('active')) {
        txt_coder.setAttribute('readonly', 'readonly')
        txt_decoder.removeAttribute('readonly', 'readonly')
    } else {
        txt_coder.removeAttribute('readonly', 'readonly')
        txt_decoder.setAttribute('readonly', 'readonly')
    }

}
function update() {
    if (block.classList.contains('active')) {
        txt_coder.innerText = decoder(txt_decoder.value)
    } else {
        txt_decoder.innerText = coder(txt_coder.value)
    }
}