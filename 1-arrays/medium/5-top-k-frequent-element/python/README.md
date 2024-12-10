# Top K Frequent Elements - Leetcode 342

---

## Problem Statement

We are given:

1. **An array of integers (`nums`)**: This contains numbers, which may repeat.
2. **An integer (`k`)**: How many of the most frequent numbers to return.

Our task is to:

- Find the `k` most frequent numbers in the array.
- Return them in any order.

---

### **Examples**

**Example 1:**  

```markdown
Input: nums = [1, 1, 1, 2, 2, 3], k = 2  
Output: [1, 2]  

**Explanation:**  
- Number `1` appears **3 times**.  
- Number `2` appears **2 times**.  
- Number `3` appears **1 time**.  
The top 2 frequent numbers are `1` and `2`.
```

**Example 2:**  

```markdown
Input: nums = [1], k = 1  
Output: [1]  

**Explanation:**  
- The only number in the array is `1`, so it is the most frequent.
```

---

### **Constraints**  

1. `1 <= nums.length <= 10^5` (the array can have up to 100,000 elements).
2. `-10^4 <= nums[i] <= 10^4` (the numbers in the array can be negative or positive).
3. `k` is guaranteed to be valid:
   - `1 <= k <= number of unique elements in nums`.
4. **The output is guaranteed to be unique**, so there's no ambiguity in the result.

---

### **Visualizing the Problem**  

Here’s an example input and how we determine the output:

**Input:**  
`nums = [1, 1, 1, 2, 2, 3], k = 2`

---

### Step-by-step Frequency Count

```markdown
| Element | Frequency |
|---------|-----------|
| 1       | 3         |
| 2       | 2         |
| 3       | 1         |
```

**Top `k = 2` frequent elements:**  
From the table, the two most frequent elements are `1` and `2`.

---

### **Diagram of Input and Output:**

```markdown
Input Array: [1, 1, 1, 2, 2, 3]
K: 2
------------------------------------
Step 1: Count Frequencies
------------------------------------
Element Frequencies: {1: 3, 2: 2, 3: 1}

------------------------------------
Step 2: Select Top 2 Frequent Elements
------------------------------------
Result: [1, 2]
```

---

## Pseudocode - Brute Force

```plaintext
1. Create a frequency map (dictionary):
   - Loop through the array `nums` and count the occurrences of each number.

2. Sort the elements of the frequency map by their frequency:
   - Extract all the elements and their counts from the frequency map.
   - Sort the elements in descending order based on their frequency.

3. Pick the top `k` elements:
   - From the sorted list, select the first `k` elements and return them as the result.
```

---

### **Pseudo Code**

```plaintext
FUNCTION topKFrequent(nums, k):
    # Step 1: Count frequencies of each element
    CREATE an empty dictionary called frequency_map
    FOR each number num in nums:
        IF num is in frequency_map:
            Increment its count
        ELSE:
            Add num to frequency_map with count 1

    # Step 2: Sort elements by frequency
    CREATE a list called sorted_elements
    SORT frequency_map by values (frequency) in descending order
    STORE the sorted keys in sorted_elements

    # Step 3: Select top k elements
    RETURN the first k elements from sorted_elements
```

---

## Code - Brute Force Approach

```py
def top_k_frequent(nums, k):
    """
    Returns the k most frequent elements from the list 'nums'.

    Args:
    nums (list): List of integers.
    k (int): Number of most frequent elements to return.

    Returns:
    list: List of k most frequent elements.
    """
    # Step 1: Create a frequency map
    frequency_map = {}  # Dictionary to store frequency of each element
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1  # Increment count if element exists
        else:
            frequency_map[num] = 1  # Initialize count if element doesn't exist

    # Step 2: Sort elements by frequency in descending order
    # Convert dictionary items to a list of tuples and sort by frequency
    sorted_elements = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Extract the top 'k' elements
    # Take the first 'k' elements from the sorted list
    result = [element[0] for element in sorted_elements[:k]]

    return result  # Return the top 'k' frequent elements
```

---

## Time and Space Complexity - Brute Force Approach

### **Time Complexity Analysis**

#### Step 1: **Building the Frequency Map**

- We iterate through the array `nums` of size `n`.  
- Each insertion or update in the dictionary is an `O(1)` operation.  
- **Time Complexity:** `O(n)`

#### Step 2: **Sorting**

- Sorting the dictionary entries by their values involves `O(n log n)` time because there are `n` unique elements in the worst case.  

#### Step 3: **Selecting Top K Elements**

- Selecting the first `k` elements from a sorted list takes `O(k)` time.  
- However, since `k` is generally much smaller than `n`, this step is effectively constant compared to the sorting step.

**Overall Time Complexity:**  
\[ O(n) + O(n \log n) + O(k) \approx O(n \log n) \]

---

### **Space Complexity Analysis**

#### Frequency Map

- We use a dictionary to store the frequency of each element.  
- In the worst case, all elements in `nums` are unique, so the dictionary size is `O(n)`.

#### Sorted List

- We store the keys of the dictionary in a separate list.  
- This requires an additional `O(n)` space.

**Overall Space Complexity:**  
\[ O(n) \]  

---

### **Why Brute Force is Inefficient**

1. **Sorting is Expensive:**  
   Sorting the elements by frequency takes \( O(n \log n) \), which becomes slow for large inputs.

2. **Additional Memory Usage:**
   The approach requires storing both the frequency map and a sorted list of elements.

---

## Pseudocode - Optimized Approach

### **Step-by-Step Pseudo Code**

Here’s the high-level idea of our optimized approach:

1. **Count the Frequencies:**
   - Use a **hash map (dictionary)** to count the frequency of each element in the array.

2. **Store Frequencies in a Heap:**
   - Insert each unique element into a **min-heap**, where the heap is limited to a size of `k`.
   - The heap ensures the `k` most frequent elements remain at the top.

3. **Extract the Top K Elements:**
   - Convert the elements in the heap into a list for the final output.

---

### **Detailed Pseudo Code**

```plaintext
Input: nums (list of integers), k (integer)
Output: List of k most frequent elements

1. Create a hash map (frequency_map) to store the frequency of each number:
    For each number in nums:
        If number exists in frequency_map:
            Increment its count
        Else:
            Add it to frequency_map with count 1

2. Initialize an empty min-heap (min_heap).

3. Iterate over the frequency_map:
    For each (number, frequency) pair:
        Add the pair to the min-heap (frequency as the key for comparison).
        If the size of min-heap exceeds k:
            Remove the smallest element (heap property ensures smallest is removed).

4. Extract the elements from the min-heap:
    Initialize an empty list (result).
    While min-heap is not empty:
        Pop the smallest element and append it to the result list.

5. Return the result list.
```

---

## Code - Optimized Approach

```py
# Function to find the top K frequent elements
def topKFrequent(nums, k):
    """
    Finds the k most frequent elements in the list nums.
    Args:
    - nums (List[int]): Input list of integers
    - k (int): Number of top frequent elements to find

    Returns:
    - List[int]: List of the k most frequent elements
    """
    # Step 1: Create a frequency map using a dictionary
    # This will store each unique number and its frequency
    frequency_map = {}
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1  # Increment count if the number exists
        else:
            frequency_map[num] = 1  # Initialize count if the number is new

    # Step 2: Use a min-heap to keep track of the top k elements
    # Importing the heapq module for heap operations
    import heapq
    min_heap = []  # Min-heap to store (frequency, number) pairs

    # Iterate over the frequency map
    for num, freq in frequency_map.items():
        # Add the current frequency and number as a tuple into the heap
        heapq.heappush(min_heap, (freq, num))
        # If the heap exceeds size k, remove the smallest frequency
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 3: Extract the numbers from the heap to form the result
    result = []
    while min_heap:
        freq, num = heapq.heappop(min_heap)
        result.append(num)

    # Step 4: Return the result
    return result
```

---

## Time and Space Complexity - Optimized Approach

### **Why This Approach is Better**

1. **Efficiency in Finding Top K Elements:**
   - Instead of sorting all elements (O(n log n)), we maintain only the top `k` elements in the heap, which reduces the overhead.

2. **Improved Time Complexity:**
   - Building the frequency map: O(n), where `n` is the size of the array.
   - Adding elements to the heap: O(n log k), since the heap has a maximum size of `k`.
   - Total Time Complexity: **O(n log k)**, significantly faster than the brute force approach for large `n`.

3. **Real-World Analogy:**
   - Imagine you're hosting a popularity contest where only the top `k` contestants win. Instead of ranking every single participant, you maintain a leaderboard of the top `k` as contestants register. This way, you only focus on the winners and save time by ignoring the rest.

---

### **Space Complexity**

1. **Hash Map:**
   - Stores the frequency of all unique elements, requiring O(n) space.

2. **Heap:**
   - Maintains the top `k` elements, requiring O(k) space.

**Overall Space Complexity: O(n + k)**.

---

### **Real-World Scenarios Where This Optimization Matters**

1. **Data Stream Analysis:**
   - When processing continuous streams of data (e.g., website hits or user activity logs), maintaining a top `k` leaderboard ensures efficiency.

2. **Recommendation Systems:**
   - Applications like Netflix or Amazon use similar approaches to identify the top `k` trending movies or products based on user interactions.

---
