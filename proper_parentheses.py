def _proper_parent():
	matching_parentheses = {'{':'}', '[':']', '(':')'}
	all_parentheses = ['{', '}', '[', ']', '(', ')']

	collection = {}
	open_parentheses = []
	closed_parentheses = []

	_stop = False

	with open('test.txt', 'r') as test_file:
		while not _stop:
			file = list(test_file.read())

			if not file:
				_stop = True

			for letter in file:
				if letter in all_parentheses:
					collection.append(letter)

			for i in collection:
				if i in matching_parentheses.keys():
					open_parentheses.append(i)
				else:
					closed_parentheses.append(i)

			if len(open_parentheses) == len(closed_parentheses):
				result = 0
				_stop = True

				


