import language

while True:
    text = input('basic > ')
    result, error = language.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
