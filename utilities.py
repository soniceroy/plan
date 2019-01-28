import os

def is_entry(dir_item):
	return len(dir_item) == 10 and \
		   dir_item[-4:] == '.txt' and \
		   can_be_int(dir_item[:6])

def can_be_int(a_string):
	if a_string[:1] == '-': # I know I really mean natural number, not int
		return False
	try:
		int(a_string)
	except ValueError:
		return False
	return True

def generate_entries(dir, entry_confirmed=is_entry):
	possible_entries = os.listdir(dir)
	for e in possible_entries:
		if entry_confirmed(e):
			yield Entry(os.path.join(dir, e))


class Entry:
	def __init__(path):
		self.path = path
		date = (path[-10:])[:6]
		if len(date) < 6 or  not can_be_int(date):
			raise Exception("Invalid Entry: Cannot Convert To Date")

		# todo: replace with datetime module use?
		if int(date[:2]) > 31:
			raise Exception("Invalid Entry: invalid date day (greater than 31)")
		elif int(date[2:4]) > 12:
			raise Exception("Invalid Entry: invalid date month (greater than 12)")
		elif int(date[4:6]) < 19:
			raise Exception("Invalid Entry: invalid date year (less than 19)")

		self.day, self.month, self.year = date[:2], date[2:4], date[4:6]
