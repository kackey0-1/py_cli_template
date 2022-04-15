from click.testing import CliRunner
from main.cli import hello1, hello2
import unittest
"""
To test the entire project and print output, run this from the root directory:
python -m pytest -s
"""


class TestUser(unittest.TestCase):

    runner = CliRunner()

    def setup(self):
        """
        # This should execute at the start of each test.
        :return: None
        """
        print("Executing Setup")

    def teardown(self):
        """
        This should execute at the end of each test.
        :return: None
        """
        print("Executing Teardown")

    def test_hello1(self):
        """
        To test hello1 without greeting option
        :return: None
        """
        result = self.runner.invoke(hello1, ['world'])
        assert not result.exception
        assert result.output == 'Hello1, world\n'

    def test_hello1_with_greeting(self):
        """
        To test hello1 with greeting option
        :return: None
        """
        result = self.runner.invoke(hello1, ['world', '--greeting', 'Hello'])
        assert not result.exception
        assert result.output == 'Hello, world\n'

    def test_hello2(self):
        """
        To test hello2 without greeting option
        :return: None
        """
        result = self.runner.invoke(hello2, ['world'])
        assert not result.exception
        assert result.output == 'Hello2, world\n'

    def test_hello2_with_greeting(self):
        """
        To test hello2 with greeting option
        :return: None
        """
        result = self.runner.invoke(hello1, ['world', '--greeting', 'Hello'])
        assert not result.exception
        assert result.output == 'Hello, world\n'
