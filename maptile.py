import enemy, items, world, actions

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
 
        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You awake in a room all too familiar, yet unlike anything you’ve ever seen.
        Fighting through your splitting headache, you take a few dizzying moments to look around,
        until there’s no longer any doubt in your mind: you’re in the Diplomatic Reception Room of the white house.
        However, the panoramic painting you remember being full of trees and sweeping landscapes has been replaced
        with nightmarish vignettes, with colossal creatures destroying countless civilizations.
        Impossibly large tentacles flutter down from the clouds,
        snatching people and buildings alike and crushing them, before launching them into an ocean of blood and gore.
        In your terror you try to escape, running out the door leading outside… but the door is gone,
        replaced with a solid wall of pulsating flesh. Ravenous, fist-sized creatures scuttle around,
        gnawing at the meat, as blood squirts from the wounds and dribbles to the floor.
        You return to the center of the room, adequately mortified,
        and can only wonder at what has happened to the white house you once knew.
        Still, escape is a more pertinent endeavor at the moment.

        You notice a door to your north, seemingly functional.
        A small, wooden chest lies next to the wall by the door. What do you do?
        """
 
    def modify_player(self, player):
        # Room has no action on player
        pass

class EmptyRoom(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the White House. You must forge onwards.
        """

    def modify_player(self, the_player):
        # Room has no action on player
        pass

class LootRoom(MapTile):
    """A room that adds something to the player's inventory"""
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()