#!/usr/bin/python3
"""
Lockbox Module
"""


def canUnlockAll(boxes):
    """
    Method to determine if all boxes can be opened
    """
    # If list is empty
    if not boxes:
        return False

    # Total number of boxes
    n = len(boxes)

    # If only one box exists
    if n == 1:
        return True

    # Declare set to track opened boxes
    visited_boxes = set()

    # Stack to store keys from the boxes
    # Start with first box [0] which is already open
    stack = [0]

    while stack:
        box_number = stack.pop()

        # Check if we have visited the box before
        if box_number not in visited_boxes:
            visited_boxes.add(box_number)
            keys_inside_box = boxes[box_number]

            # Add all keys inside current box to the stack
            for key in keys_inside_box:
                stack.append(key)

    # Check if we have visited all boxes
    if len(visited_boxes) == n:
        return True
    return False
