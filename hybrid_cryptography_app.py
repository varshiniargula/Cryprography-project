from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            char = char.upper()
            key_char = key[key_index % len(key)].upper()
            key_index += 1
            char_num = ord(char) - 65
            key_num = ord(key_char) - 65
            encrypted_num = (char_num + key_num) % 26
            encrypted_char = chr(encrypted_num + 65)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            char = char.upper()
            key_char = key[key_index % len(key)].upper()
            key_index += 1
            char_num = ord(char) - 65
            key_num = ord(key_char) - 65
            decrypted_num = (char_num - key_num) % 26
            decrypted_char = chr(decrypted_num + 65)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

@app.route('/', methods=['GET', 'POST'])
def index():
    ciphertext = None
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        key = request.form['key']
        ciphertext = vigenere_encrypt(plaintext, key)
    return render_template('index.html', ciphertext=ciphertext)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    plaintext = None
    if request.method == 'POST':
        ciphertext = request.form['ciphertext']
        key = request.form['key']
        plaintext = vigenere_decrypt(ciphertext, key)
    return render_template('index.html', plaintext=plaintext)

if __name__ == '__main__':
    app.run(debug=True,port=8000)
