import logging
import mock
import python_for_deposit_solutions


class TestCli():

    def test_noOptions(self):
        python_for_deposit_solutions.cli.main([])

    def test_hasVerboseShort(self):
        python_for_deposit_solutions.cli.main(["-v"])

    def test_hasVerboseLong(self):
        python_for_deposit_solutions.cli.main(["--verbose"])

    def test_hasQuietShort(self):
        python_for_deposit_solutions.cli.main(["-q"])

    def test_hasQuietLong(self):
        python_for_deposit_solutions.cli.main(["--quiet"])
