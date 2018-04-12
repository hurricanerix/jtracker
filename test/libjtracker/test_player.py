import unittest

from libjtracker.player import Player


class TestPlayer(unittest.TestCase):

    def test_foo(self):
        self.assertEqual('foo'.upper(), 'FOO')
        p = Player('foo')
        p.play()


if __name__ == '__main__':
    unittest.main()
