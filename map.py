from locations import game_map, location_descriptions
from typing import Tuple, List

GRID_SIZE = 5
SCREEN_WIDTH = 80


def _format_cell_lines(text_top: str, text_bottom: str, width: int) -> Tuple[str, str]:
    # width includes the two padding spaces we add around centered content
    content_width = max(1, width - 2)
    top = text_top[:content_width].center(content_width)
    bottom = text_bottom[:content_width].center(content_width)
    return f" {top} ", f" {bottom} "


def build_map_display() -> str:
    # Compute equal per-cell widths and center the whole map so total line length == SCREEN_WIDTH
    separators = GRID_SIZE + 1
    total_content = SCREEN_WIDTH - separators
    base = total_content // GRID_SIZE
    remainder = total_content - (base * GRID_SIZE)

    # We'll center the map horizontally by padding left/right with spaces allocated from remainder
    pad_left = remainder // 2
    pad_right = remainder - pad_left

    # All cells use the same width `base`
    widths: List[int] = [base for _ in range(GRID_SIZE)]

    inner = "+" + "+".join(["-" * w for w in widths]) + "+"
    horizontal = (" " * pad_left) + inner + (" " * pad_right)

    # Create a top header that embeds the word MAP centered inside the horizontal line
    header = list(horizontal)
    label = "MAP"
    start = (SCREEN_WIDTH - len(label)) // 2
    for i, ch in enumerate(label):
        if start + i < len(header):
            header[start + i] = ch
    header_line = "".join(header)

    lines = [header_line, horizontal]

    for y in range(GRID_SIZE):
        top_cells = []
        bottom_cells = []
        for x in range(GRID_SIZE):
            w = widths[x]
            name = game_map.get((x, y), "Unknown")
            # split name into first and second word
            parts = name.split()
            top_word = parts[0] if parts else ""
            bottom_word = parts[1] if len(parts) > 1 else ""
            top_cell, bottom_cell = _format_cell_lines(top_word, bottom_word, w)
            top_cells.append(top_cell)
            bottom_cells.append(bottom_cell)

        # add left/right padding to each printed row so the overall width is SCREEN_WIDTH
        left_pad = " " * pad_left
        right_pad = " " * pad_right
        lines.append(left_pad + "|" + "|".join(top_cells) + "|" + right_pad)
        lines.append(left_pad + "|" + "|".join(bottom_cells) + "|" + right_pad)
        lines.append(horizontal)

    return "\n".join(lines)


def describe_location(coords: Tuple[int, int]) -> str:
    if coords not in game_map:
        return "There is no location at those coordinates."
    location_name = game_map[coords]
    description = location_descriptions.get(location_name, "No description is available for this location.")
    return f"{location_name} ({coords[0]},{coords[1]}): {description}"