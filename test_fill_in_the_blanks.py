import unittest
import mock
import fill_in_the_blanks
''' Test cases for fill_in_the_blanks.py. In order for these to run, the main() at the bottom of fill_in_the_blanks.py must be 
commented out '''

def mock_get_level_from_user():
	return "EASY"

class TestCheckGuess(unittest.TestCase):
	'''Tests that guesses are checked correctly '''

	def test_correct_guess_returns_true(self):
		self.assertTrue(fill_in_the_blanks.check_guess("bat", "bat"))

	def test_incorrect_guess_returns_false(self):
		self.assertFalse(fill_in_the_blanks.check_guess("frog", "bat"))

	def test_extra_char_returns_true(self):
		self.assertTrue(fill_in_the_blanks.check_guess("bat!", "bat"))

	def test_different_case_accepted(self):
		self.assertTrue(fill_in_the_blanks.check_guess("BAT", "bat"))

	def test_capitalized_accepted(self):
		self.assertTrue(fill_in_the_blanks.check_guess("None", "None"))

class TestUpdateParagraph(unittest.TestCase):
	''' Tests that paragraphs are updated correctly when blanks found '''

	def test_paragraph_updated_successfully(self):
		self.assertEqual(fill_in_the_blanks.update_paragraph("This returns ___3___.", "None",
		 ["function", "parameters", "None", "list"], ["___1___", "___2___", "___3___", "___4___"]), "This returns None.")

	def test_answer_capitalzed_if_after_period(self):
		self.assertEqual(fill_in_the_blanks.update_paragraph(" ___2___ can be standard data types", "parameters",
		 ["function", "parameters", "None", "list"], ["___1___", "___2___", "___3___", "___4___"]), "Parameters can be standard data types" )

class TestGetLevelIndex(unittest.TestCase):
	''' The get_level_index method actually calls a helper method that gets raw user input. This has been mocked to allow to test that the 
	correct index is returned '''

	def test_EASY_has_index_0(self):
		output = fill_in_the_blanks.set_level_index(lambda: "EASY")
		self.assertEqual(output, 0)

	def test_MEDIUM_has_index_1(self):
		output = fill_in_the_blanks.set_level_index(lambda: "MEDIUM")
		self.assertEqual(output, 1)

	def test_HARD_has_index_2(self):
		output = fill_in_the_blanks.set_level_index(lambda: "HARD")
		self.assertEqual(output, 2)

class TestIsValidLevel(unittest.TestCase):
	''' Tests that unexpected input to level selection is handled correctly'''

	def test_EASY_is_valid_level(self):
		self.assertTrue(fill_in_the_blanks.is_valid_level("EASY"))

	def test_easy_is_valid_level(self):
		self.assertTrue(fill_in_the_blanks.is_valid_level("easy"))

	def test_number_is_not_is_valid_level(self):
		self.assertFalse(fill_in_the_blanks.is_valid_level(1))

	def test_jim_is_not_is_valid_level(self):
		self.assertFalse(fill_in_the_blanks.is_valid_level("Jim"))

class TestIsValidLevel(unittest.TestCase):
	''' Tests that unexpected input to level selection is handled correctly'''

	def test_EASY_is_valid_level(self):
		self.assertTrue(fill_in_the_blanks.is_valid_level("EASY"))

	def test_easy_is_valid_level(self):
		self.assertTrue(fill_in_the_blanks.is_valid_level("easy"))

class TestIsValidTotalGuesses(unittest.TestCase):
	''' Tests that unexpected input to level selection is handled correctly'''

	def test_int_between_0_and_20_valid(self):
		self.assertTrue(fill_in_the_blanks.is_valid_total_guesses(5))

	def test_float_in_range_valid(self):
		self.assertTrue(fill_in_the_blanks.is_valid_total_guesses(15.0))

	def test_lower_bound_valid(self):
		self.assertTrue(fill_in_the_blanks.is_valid_total_guesses(1))

	def test_past_lower_bound_invalid(self):
		self.assertFalse(fill_in_the_blanks.is_valid_total_guesses(0))

	def test_higher_bound_valid(self):
		self.assertTrue(fill_in_the_blanks.is_valid_total_guesses(20))

	def test_past_higher_bound_invalid(self):
		self.assertFalse(fill_in_the_blanks.is_valid_total_guesses(21))

	def test_string_invalid(self):
		self.assertFalse(fill_in_the_blanks.is_valid_total_guesses("John"))

if __name__ == '__main__':
	unittest.main()