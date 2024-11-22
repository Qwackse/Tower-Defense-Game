import pygame
import os
"""
Tower Class for Defense Tower Game

This file defines a Tower class used in a tower defense game. Each Tower object has attributes 
such as damage, attack range, and cooldown, and methods for attacking enemies, upgrading, 
and displaying itself on the screen.

Attributes:
    - name (str): Name of the tower.
    - damage (int): Damage dealt per attack.
    - shot_cooldown (int): Time (in frames) between attacks.
    - price (int): Cost to build the tower.
    - attack_range (int): Attack range for hitting enemies.
    - attack_pattern (int): Defines the tower's specific attack style.
    - position (tuple): Position of the tower on the screen.
    - upgrade_level (int): Current level of the tower.
    - enemies_defeated (int): Count of enemies defeated by this tower.
"""


class Tower:
    def __init__(self, name: str, damage: int, shot_cooldown: int, price: int, attack_range: int, attack_pattern: int):
        """Initializes the Tower with its primary attributes."""
        self._name = name
        self._damage = damage
        self._shot_cooldown = shot_cooldown * 60
        self._price = price
        self._sell_price = int(price * 0.25)
        self._attack_range = attack_range
        self._attack_pattern = attack_pattern
        self._position = None
        self._upgrade_level = 1
        self._upgrade_cost = price + (price * 0.5)
        self._enemies_defeated = 0
        self._cooldown_counter = 0
        self._image = pygame.image.load(os.path.join('game_assests', "tower.png"))
        self.size = 28

    def render(self, window):
        """Draws the tower image on the game window at its position."""
        if self._position:
            adjusted_x = self._position[0] - (self.size * 3) // 2
            adjusted_y = self._position[1] - (self.size * 3) // 2
            tower_surface = pygame.transform.scale(self._image, (self.size * 3, self.size * 3))
            window.blit(tower_surface, (adjusted_x, adjusted_y))

    def _render_range(self, window):
        """Displays a circle around the tower to indicate its attack range."""
        range_surface = pygame.Surface((self._attack_range * 2, self._attack_range * 2), pygame.SRCALPHA)
        range_surface.fill((0, 0, 0, 0))
        pygame.draw.circle(
            range_surface,
            (128, 128, 128, 100),
            (self._attack_range, self._attack_range),
            self._attack_range
        )

        adjusted_x = self._position[0] - self._attack_range
        adjusted_y = self._position[1] - self._attack_range
        window.blit(range_surface, (adjusted_x, adjusted_y))

    def place(self, position):
        """Sets the tower's position on the game map."""
        self._position = position

    def get_name(self):
        """Returns the name of the tower."""
        return self._name

    def set_name(self, name):
        """Sets the name of the tower, raising an error if the name is empty."""
        if name == "":
            raise ValueError("Not a Valid Name")
        else:
            self._name = name

    def get_damage(self):
        """Returns the current damage of the tower."""
        return self._damage

    def set_damage(self, damage):
        """Sets the tower's damage, ensuring it is positive."""
        if damage > 0:
            self._damage = damage
        else:
            raise ValueError("Damage must be greater than 0.")

    def get_range(self):
        """Returns the tower's attack range."""
        return self._attack_range

    def set_attack_range(self, attack_range):
        """Sets the tower's attack range, ensuring it is positive."""
        if attack_range > 0:
            self._attack_range = attack_range
        else:
            raise ValueError("Range must be greater than 0.")

    def get_price(self):
        """Returns the initial cost of the tower."""
        return self._price

    def get_sell_price(self):
        """Returns the sell price of the tower."""
        return self._sell_price

    def get_upgrade_cost(self):
        """Returns the cost to upgrade the tower to the next level."""
        return self._upgrade_cost

    def get_enemies_defeated(self):
        """Returns the count of enemies defeated by this tower."""
        return self._enemies_defeated

    def upgrade_tower(self):
        """Upgrades the tower's attributes, increasing damage, range, and upgrade cost."""
        self._upgrade_level += 1
        self._damage += int(self._damage * 0.5)
        self._attack_range += 1
        self._upgrade_cost = int(self._price * (1 + 0.5 * self._upgrade_level))

    def sell_tower(self):
        """Displays a message indicating the tower has been sold."""
        print(f"{self._name} tower sold for {self._sell_price} credits.")

    def attack(self, enemies):
        """Attacks the first enemy within range if the tower is not on cooldown."""
        if self._cooldown_counter > 0:
            self._cooldown_counter -= 1
            return
        for enemy in enemies:
            if self._in_range(enemy):
                enemy.take_damage(self._damage)
                self._cooldown_counter = self._shot_cooldown
                self._enemies_defeated += 1
                break

    def _in_range(self, enemy):
        """Calculates if the enemy is within the tower's attack range."""
        ex, ey = enemy._position
        tx, ty = self._position
        distance = ((tx - ex) ** 2 + (ty - ey) ** 2) ** 0.5
        return distance <= self._attack_range

    def get_stats(self):
        """Returns a dictionary of the tower's statistics."""
        return {
            "Name": self._name,
            "Damage": self._damage,
            "Range": self._attack_range,
            "Cooldown": self._shot_cooldown,
            "Enemies Defeated": self._enemies_defeated,
            "Sell Tower": self._sell_price,
            "Upgrade Cost": self._upgrade_cost
        }

# Example
tower = Tower("Archer Tower", 50, 3, 100, 5, 1)

