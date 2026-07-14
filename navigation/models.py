from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Encounter:
	"""A possible fight in a room. Kept identical to the grid semantics for the
	prototype: a battle triggers only when randint(1, battle_chance) == battle_chance."""
	enemies: list
	battle_chance: int


@dataclass
class Gate:
	"""Swaps a room for an alternate variant once `needs` has been unlocked
	(via player key items or the phase's unlocked-token list). Replaces the old
	block_value + alt_pathway pair."""
	needs: str
	opens_to: Room


@dataclass
class Room:
	id: str
	description: list = field(default_factory=list)
	exits: dict = field(default_factory=dict)          # "north" -> room id
	encounter: Encounter | None = None
	gate: Gate | None = None
	dispenser: str | None = None                        # item_type for handle_dispenser
	unlock: dict | None = None                          # {'value': ..., 'display': ...} for handle_unlock
	transition: str | None = None                       # e.g. 'VICTORY'
	on_first_enter: list | None = None                  # one-time text (was alt_description)
	first_token: str | None = None                      # token appended once on_first_enter shows


@dataclass
class Phase:
	entry: str
	rooms: dict                                         # room id -> Room
