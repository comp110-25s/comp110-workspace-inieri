"""Practicing with Dictionaries"""

__author__: str = "730543747"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary of strings, raising a KeyError if duplicate values exist."""
    inverted = {}
    for key in original:
        value = original[key]
        if value in inverted:
            raise KeyError(f"Duplicate key found for value: {value}")
        inverted[value] = key
    return inverted


def count(original_list: list[str]) -> dict[str, int]:
    """Count occurences of each string in a list"""
    new_dictionary: dict[str, int] = {}
    for i in original_list:
        if i in new_dictionary:
            new_dictionary[i] += 1
        else:
            new_dictionary[i] = 1
    return new_dictionary


def favorite_color(fav_colors: dict[str, str]) -> str:
    """Determine most popular color"""
    color_list: list[str] = []
    for key in fav_colors:
        color_list.append(fav_colors[key])
    color_dict: dict[str, int] = count(color_list)
    most_popular: str = ""
    max_count: int = 0
    for key in color_dict:
        if color_dict[key] > max_count:
            most_popular = key
            max_count = color_dict[key]
    return most_popular


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings into a dictionary based on string length."""
    length_bins: dict[int, set[str]] = {}

    for word in words:
        length = len(word)
        if length not in length_bins:
            length_bins[length] = set()
        length_bins[length].add(word)
    return length_bins
