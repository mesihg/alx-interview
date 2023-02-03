#!/usr/bin/python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    """Checks if all the boxes in a list of boxes containing the keys
    to other boxes can be unlocked given that the first
    box is unlocked.
    """
    n = len(boxes)
    keys = [0]
    visited = [False] * n
    visited[0] = True

    for key in keys:
        for box in boxes[key]:
            if box < n and not visited[box]:
                visited[box] = True
                keys.append(box)
    return all(visited)
