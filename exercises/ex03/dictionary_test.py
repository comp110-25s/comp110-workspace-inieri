"""Test Functions in EX03"""

__author__: str = "730543747"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

import pytest


def test_invert_basic() -> None:
    """Test basic inversion of a dictionary."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single_pair() -> None:
    """Test inversion of a single key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_duplicate_values() -> None:
    """Test that KeyError is raised when duplicate values exist."""
    with pytest.raises(KeyError):
        my_dictionary = {"orange": "purple", "blue": "purple"}
        invert(my_dictionary)


def test_count_multiple() -> None:
    """Test counting occurrences of multiple elements."""
    assert count(["agh", "agh", "boo", "foo"]) == {"agh": 2, "boo": 1, "foo": 1}


def test_count_unique() -> None:
    """Test counting when all elements are unique."""
    assert count(["stink", "blink"]) == {"stink": 1, "blink": 1}


def test_count_empty() -> None:
    """Test counting with an empty list."""
    assert count([]) == {}


def test_favorite_color_tie() -> None:
    """Test favorite color when there's a tie."""
    assert (
        favorite_color(
            {"bella": "purple", "olivia": "blue", "mike": "blue", "jen": "purple"}
        )
        == "purple"
    )


def test_favorite_color_winner() -> None:
    """Test favorite color when there is a clear winner."""
    assert (
        favorite_color({"julia": "green", "caroline": "green", "kate": "blue"})
        == "green"
    )


def test_favorite_color_empty() -> None:
    """Test favorite color when input is empty."""
    assert favorite_color({}) == ""


def test_bin_len_varied_lengths() -> None:
    """Test bin_len with words of different lengths."""
    assert bin_len(["agh", "blo", "haha"]) == {3: {"agh", "blo"}, 4: {"haha"}}


def test_bin_len_single_character() -> None:
    """Test bin_len with a mix of short and long words."""
    assert bin_len(["peek", "a", "boo"]) == {4: {"peek"}, 1: {"a"}, 3: {"boo"}}


def test_bin_len_empty() -> None:
    """Test bin_len with an empty list."""
    assert bin_len([]) == {}
