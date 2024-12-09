import pytest
from brute_force import groupAnagrams  # Import the function to be tested


# Test cases
def test_group_anagrams():
    # Test case 1: Normal case with multiple anagrams
    input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert sorted(groupAnagrams(input_data)) == sorted(expected_output)

    # Test case 2: Empty list
    input_data = []
    expected_output = []
    assert groupAnagrams(input_data) == expected_output

    # Test case 3: Single word (no anagrams)
    input_data = ["apple"]
    expected_output = [["apple"]]
    assert groupAnagrams(input_data) == expected_output

    # Test case 4: All strings are anagrams
    input_data = ["listen", "silent", "enlist", "inlets"]
    expected_output = [["listen", "silent", "enlist", "inlets"]]
    assert sorted(groupAnagrams(input_data)) == sorted(expected_output)

    # Test case 5: Strings with no anagrams
    input_data = ["abc", "def", "ghi"]
    expected_output = [["abc"], ["def"], ["ghi"]]
    assert sorted(groupAnagrams(input_data)) == sorted(expected_output)

    # Test case 6: Edge case with an empty string
    input_data = ["", "b", "a", ""]
    expected_output = [["", ""], ["b"], ["a"]]
    assert sorted(groupAnagrams(input_data)) == sorted(expected_output)

    # Test case 8: All characters the same
    input_data = ["aaaa", "aaaa", "aaaaa"]
    expected_output = [["aaaa", "aaaa"], ["aaaaa"]]
    assert sorted(groupAnagrams(input_data)) == sorted(expected_output)

    # Test case 9: Single character strings
    input_data = ["a", "b", "a", "b", "c"]
    expected_output = [["a", "a"], ["b", "b"], ["c"]]
    assert sorted(groupAnagrams(input_data)) == sorted(expected_output)
