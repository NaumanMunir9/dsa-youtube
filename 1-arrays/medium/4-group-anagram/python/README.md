# Group Anagram - Leetcode 49

## Pseudocode - Brute Force

- Creating an empty list to store the groups of anagrams. Each group will be a list containing strings that are anagrams of each other.
- Iterate over each string in the input list. For each string, compare it with all the previously processed strings to see if any of them are anagrams.
  - Check if two strings are anagrams by comparing their sorted versions. If the sorted strings are the same, then they are anagrams.
  - Find a group where the current string is an anagram, add it to that group. Don't process it again.
  - If no matching anagram group is found, create a new group and add the string to it.
- Finally, return the list of anagram groups.

---

### Time and Space Complexity - Brute Force Approach

#### Time Complexity

- For each string in the input list, compare it to all previously processed strings. If there are *n* strings, that gives a nested loop: the outer loop runs *n* times, and for each string, compare it with *n-1* other strings. So, the comparison process itself takes **O(n^2)** operations.

- In addition, for each comparison, we need to check if the strings are anagrams. To do that, sort the strings, and sorting a string of length *m* takes **O(m log m)** time.

- The time complexity of checking if two strings are anagrams is **O(m log m)**, where *m* is the length of the string.

- The total time complexity of the brute force approach is **O(n^2 * m log m)**, where *n* is the number of strings, and *m* is the length of the longest string in the list."

```plaintext
Time Complexity: O(n^2 * m log m)
```

#### Space Complexity

- The main space usage comes from the list that stores the anagram groups. A list is used to store each group, and since there are *n* strings, the space complexity is **O(n)** to store all the groups."

- No additional data structures like hash maps or auxiliary arrays are used, so the space complexity of this brute force approach is **O(n)**.

```plaintext
Space Complexity: O(n)
```

---

## Optimized Approach

1. **Create empty hash map**: Initializing an empty hash map. The key of the map will represent a characteristic of the anagrams, and the value will be a list of strings that are anagrams of each other.

2. **For each string in the list**: Iterate over each string in the input list, and for each string, we generate a unique key that will help us identify anagram groups."

3. **Convert the string to a key**: Create a **frequency count** of characters. The frequency of each character in an anagram is identical, so this can also serve as a unique key."

4. **Add the string to the hash map**: Once key is generated for the string, look it up in the hash map. If it exists, append the string to the existing list. If it doesn't exist, create a new list for that key and add the string.

5. **Return the values of the hash map**: Finally, return the values of the hash map, which are the lists of anagram groups.

---

```py
input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input_strings))

```

```shell
{
  'aet': ['eat', 'tea', 'ate'],
  'ant': ['tan', 'nat'],
  'abt': ['bat']
}
```

---

### Time and Space Complexity - Optimized Approach

- The main operation is generating the key for each string, for which, use a frequency count approach, the time complexity for generating the key is **O(m)**, where *m* is the length of the string (since we only need to count characters). In this case, the overall time complexity becomes **O(n * m)**, where *n* is the number of strings, and *m* is the length of the longest string in the input.

- The space complexity is **O(n)** because of storing the anagram groups in the hash map, and in the worst case, all strings might be anagrams of each other and be grouped together. So, the space needed for storing the groups is proportional to the number of strings in the input.

---
