import pytest


class Test(object):

    @pytest.mark.complete("shar --")
    def test_dash(self, completion):
        assert completion.list