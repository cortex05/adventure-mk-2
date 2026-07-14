# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running

```
python main_menu.py
```

Pure Python standard library — no dependencies, no build step, no test suite, no linter config. The game is an interactive terminal app driven entirely by `input()` prompts.

**Windows-only as written:** screen clearing uses `os.system('cls')` throughout. It will not clear the screen on macOS/Linux (would need `clear`). The intended deployment target is a Replit instance (see README).

## Architecture

### Flow

`main_menu.py` → `main_functions.launcher()` (menu loop) → `game.main()`.

`game.main()` runs the phases **sequentially**, threading the same `player` object through each:

```
start (name + class select + intro)
  → swamp_loop → moat_loop → castle_loop (level_one → level_two) → final_battle
```

Each phase loop returns a bool: `False` means the player died and `main()` prints "game over" and returns. `final_battle` returns win/lose. Phase entry points live in `phases/<name>/<name>.py`.

### Grid-based navigation (the core pattern)

Every phase is a 2D grid of "location" dicts in `phases/<name>/<name>_coordinates.py`. The player's position is a mutable `location_coords = [row, col]` list passed by reference and mutated in place.

Movement uses a compass where the input digit maps to a direction (`directions/nav_options.py`, applied in `utility/nav_functions.navigation_options`):

- `1` West → `col - 1`
- `2` North → `row - 1`
- `3` South → `row + 1`
- `4` East → `col + 1`

Note the off-by-one convention: a location's `options` list holds **0-indexed** direction values (`0,1,2,3`), while the player types the **1-indexed** digit (`1,2,3,4`). `navigation_options` reconciles these. `reverse_step` undoes the last move (used on retreat / after a blocked victory step).

### Location dict schema

The grid dicts are the game's data model. Common keys (see `phases/swamp/swamp_coordinates.py` for the fullest example):

- `description` — list of strings printed line-by-line (`"HOLDER"` marks an unused/unreachable cell).
- `options` — 0-indexed directions available from this cell.
- `random_battle` / `battle_chance` / `enemy_options` — if `random_battle`, roll `randint(1, battle_chance)`; a battle triggers only when the roll **equals** `battle_chance` (so higher `battle_chance` = rarer). `enemy_options` is a list of enemy IDs.
- `unlock_value` — `'VICTORY'` ends the phase successfully; otherwise a dict `{value, display}` routed through `handle_unlock` to grant keys/weapons/armor.
- `block_value` + `alt_pathway` — a gated cell. If the player holds the matching key item (or the value is already in `unlocked_values`), the location is swapped for its `alt_pathway` variant. `first_unlock` + `alt_description` show one-time flavor text the first time a cell is entered.
- `dispenser` — refills consumables via `utility/dispenser_functions.handle_dispenser`.

`unlocked_values` (a per-phase list of unlocked string tokens) and the player's `inventory["key_items"]` both act as unlock state; `utilities.check_key_items_unlock` checks membership in either.

### Characters

- `characters/Player.py` — base `Player` with stats as **class attributes**. Concrete classes `Elf`/`Dwarf`/`Swordsman` in `characters/player_options/` subclass it, override stats, and in `__init__` equip a starting weapon and seed potions. Class selection happens in `phases/start.initialiationLoop`.
- `characters/Enemy.py` — near-empty base; each enemy in `characters/enemy_options/` is a subclass with combat stats as class attributes. `utility/battle_functions.random_enemy` maps integer IDs (the `enemy_options` in grid cells) to enemy classes — **this switch is the source of truth for enemy IDs** (1=Wharg, 2=Goblin, 3=Duke, 4=Guard, 5=Sorcerer, 6=Warlock, 7=Dragon, 11=GiantWharg).

Note: because `Player.inventory` / `Player.gear` are mutable class attributes, they are shared across instances. This is fine only because exactly one player exists per run.

### Combat & leveling (`utility/battle_functions.py`)

`battle_launch` → `battle_loop` is a turn-based menu (attack / stats / retreat / item / quit). Damage blends `player.strength`, weapon `attack_boost`, `agility` (crit chance + dodge), `defense`, and summed armor `defense_bonus`. Returns `WIN` / `LOSE` / `RETREAT`.

`level_up` is recursive with experience spillover; `class_level_up` applies per-class stat growth. Max level is 15.

### Items

Three different representations coexist — match the existing one when editing:

- **Weapons** are plain dicts (`items/weapons/*.py`): `name`, `attack_boost`, `id`, `critical_chance`, `level`.
- **Armor** are `ArmorItem` instances (`items/armor/ArmorItem.py`): `name`, `id`, `defense_bonus`, `part`, `level`.
- **Consumables** are class instances (`items/health/potion.py`, `super_potion.py`, subclassing `Consumable`).

`handle_unlock` in `battle_functions.py` is the dispatcher that swaps in upgraded weapons/armor and key items when a location's `unlock_value` fires.

## Conventions & gotchas

- **Indentation is tabs** project-wide (one tab per level). Do not introduce space-based indentation — mixing the two triggers `TabError`.
- `handle_unlock` compares strings with
 `is` (e.g. `unlock_dict['value'] is 'CASTLE_KEY'`). This currently works via CPython literal interning but is fragile; prefer `==` for any new comparisons.
- Pacing relies on `time.sleep(...)` and `input(press_any_to_continue)` (`utility/texts.py`) between screens — expect these when reading flow.
