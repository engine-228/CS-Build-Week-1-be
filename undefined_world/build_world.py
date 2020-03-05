from .player_models import Player
from .room_models import Room
from .room_setups import rooms
# room_title, room_descriptions


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    # fills up the grid zig zagged top to bottom
    def build_rooms(self, size_x, size_y, num_rooms):
        # init grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x
        # setting params for start point (lower left)
        x = -1  # <--- 0 on first step
        y = 0
        room_count = 0
        room_title_description = 0

        # build rooms moving east
        # note: 1 is east; -1 is west
        direction = 1

        # in the meantime...rooms to be created
        previous_room = None
        while room_count < num_rooms:

            # this determines the direction of the next room created
            if direction > 0 and x < size_x - 1:
                room_direction = 'e'
                x += 1
            elif direction < 0 and x > 0:
                room_direction = 'w'
                x -= 1

            else:
                # if dead-end can turn and reverse direction via north
                room_direction = 'n'
                y += 1
                direction *= -1

            # build a room in the direction moving
            room = Room(room_count, room_title[room_title_description],
                        room_descriptions[room_title_description], x, y)

            # save that new room in the grid
            self.grid[x][y] = room

            # link up prev room to new room
            if previous_room is not None:
                previous_room.connect(room, room_direction)

            # now update variables as they iterate
            previous_room = room
            room_count += 1
            room_title_description += 1
