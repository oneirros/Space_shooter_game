"""Testy dla modułu spaceship."""
import unittest

import spaceship
import game


class SpaceShipTest(unittest.TestCase):
    """Klasa testująca moduł spaceship"""

    def setUp(self) -> None:
        """Obiekty potrzebe w testach."""
        self.player = spaceship.MotherShip(game, [100, 100], 75, 75)
        self.alien = spaceship.AlienShip(game, [100, 0], 75, 75)

    def test_create_player(self) -> None:
        """Test konstruktora dla klasy MotherShip"""
        self.assertEqual(self.player.game, game)
        self.assertEqual(self.player.position, [100, 100])
        self.assertEqual(self.player.width, 75)
        self.assertEqual(self.player.height, 75)

    def test_create_alien(self) -> None:
        """Test konstruktora dla klasy AlienShip"""
        self.assertEqual(self.alien.game, game)
        self.assertEqual(self.alien.position, [100, 0])
        self.assertEqual(self.alien.width, 75)
        self.assertEqual(self.alien.height, 75)

    def test_ship_colision(self) -> None:
        """Test kolizji gracza i AlineShip"""
        self.assertIsNone(self.alien.collision(self.player.position, self.player.mask))

        for i in range(100):
            self.alien.control()

        self.assertIsNotNone(self.alien.collision(self.player.position, self.player.mask))


if __name__ == "__main__":
    unittest.main()
