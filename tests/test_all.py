import logging
import mock


logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)


class TestPython4DepositSolutions():
    def test_hasVersion(self):
        from python_for_deposit_solutions.__version__ import version
        versionLen = len(version.split('.'))
        assert(3 == versionLen)
