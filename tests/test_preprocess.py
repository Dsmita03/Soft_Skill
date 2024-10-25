import unittest
from src.preprocess import clean_text, remove_fillers, preprocess_text

class TestPreprocess(unittest.TestCase):

    def test_clean_text(self):
        text = "Hello there! This is a test text, with numbers 1234."
        cleaned_text = clean_text(text)
        self.assertTrue("hello" in cleaned_text)
        self.assertFalse("1234" in cleaned_text)

    def test_remove_fillers(self):
        text = "I like, um, really don't know what to say, you know?"
        no_fillers_text = remove_fillers(text)
        self.assertFalse("um" in no_fillers_text)
        self.assertFalse("you know" in no_fillers_text)

    def test_preprocess_text(self):
        text = "This is, like, a sample sentence."
        processed_text = preprocess_text(text)
        self.assertTrue("sample" in processed_text)
        self.assertFalse("like" in processed_text)

if __name__ == '__main__':
    unittest.main()
