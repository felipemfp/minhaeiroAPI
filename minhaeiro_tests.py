import os
import minhaeiro
from models import db
import helpers
import unittest
import tempfile


class HelpersTestCase(unittest.TestCase):
    def test_length_of_auth_key(self):
        key = helpers.Auth.get_new_key()
        assert len(key) == 10


    def test_hash_sha256(self):
        # salt = development_salt
        expected = '5ae0f2b68de761322adfc0fb86956c90a7a468048595d887aeec020eb44901b4'
        sha = helpers.Crypt.hash_sha256('senha')
        assert sha == expected


if __name__ == '__main__':
    unittest.main()
