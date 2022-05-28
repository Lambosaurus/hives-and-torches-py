from pygame.math import Vector2 as v2
import roll


STATS_MAX = ["fatigue", "wounds"]
STATS_COMMON = ["strength", "finesse", "intellect", "willpower", "speed"]


class Creature:
    def __init__(self, name, pos: v2, stat_block: dict = {}):
        self.pos = pos
        self.name = name
        self.stats = self._create_base_stats(stat_block)

        self.set_level(stat_block.get("level", 1))

        self["fatigue"] = self["fatigue.max"]
        self["wounds"] = 0

    def set_level(self, level):
        # Sets a creature's level to a given value.
        while self["level"] < level:
            self._level_up()
        self._derive_stats()

    def _derive_stats(self):
        # strength = strength.base
        for key in STATS_COMMON:
            self[key] = self[key + ".base"]
        # fatigue.max = fatigue.base
        for key in STATS_MAX:
            self[key + ".max"] = self[key + ".base"]
        # apply strength bonus to fatigue
        self["fatigue.max"] += (self["level"] * self["strength"])

        if self["fatigue"] > self["fatigue.max"]:
            self["fatigue"] = self["fatigue.max"]

    def _create_base_stats(self, base_stats: dict = {}):
        stats = {
            "level": 0,
            "fatigue.base": roll.d(4) + 4,
            "fatigue": 0,
            "wounds": 0,
            "speed": 30,
        }
        for key in STATS_COMMON:
            stats[key + ".base"] = base_stats.get(key, 0)
        for key in STATS_MAX:
            stats[key + ".base"] = base_stats.get(key, 0)

        return stats

    def _level_up(self):
        # Handles a single level up.
        # This does not update derived stats
        self["level"] += 1
        self["fatigue.base"] += roll.d(4)

    def __getitem__(self, key):
        return self.stats[key]

    def __setitem__(self, key, value):
        self.stats[key] = value
        
    def get_sprite(self):
        return None
