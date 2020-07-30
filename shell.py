
import language

# Infinite loop for shell
while True:
	text = input('language > ')
	if text.strip() == "": continue 
	result, error = language.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))