import os
import fizzbuzz

class TestIntegration(object):
    def test_can_be_called_from_command_line(self):
        out = os.popen("python fizzbuzz.py 3").read()
        assert out == "fizz\n"

    def test_can_be_called_from_command_line_with_multiple_args(self):
        out = os.popen("python fizzbuzz.py 1 2 3 4 5").read()
        assert out == "1\n2\nfizz\n4\nbuzz\n"
