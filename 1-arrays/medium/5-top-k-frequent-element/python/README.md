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

## Pseudocode - Optimized Approach

### **Step-by-Step Pseudo Code**

Here’s the high-level idea of our optimized approach:

1. **Frequency Counting**:
   - Use a dictionary to count how many times each number appears in the array. This gives us the frequency of each element.

2. **Bucket Sort**:
   - Use an array of lists (buckets), where the index represents the frequency of elements.
   - For example, numbers that appear 3 times are placed in the bucket at index 3.

3. **Reverse Traversal**:
   - Iterate through the buckets from the highest frequency to the lowest.
   - Gather elements until we have exactly `k` most frequent elements.

---

### **Detailed Pseudo Code**

#### **Input**

- `nums`: List of integers.
- `k`: Number of most frequent elements to find.

#### **Output**

- List of `k` most frequent elements.

#### **Steps**

1. **Initialize a Frequency Dictionary**:
   - Create a dictionary `frequency_count` to store the frequency of each element in `nums`.

2. **Count Frequencies**:
   - For each number in `nums`:
     - Update its count in `frequency_count`.

3. **Create Frequency Buckets**:
   - Initialize an array of empty lists, `frequency_buckets`, where the size of the array is `len(nums) + 1`.

4. **Populate Frequency Buckets**:
   - For each element and its count in `frequency_count`:
     - Add the element to the list at index `count` in `frequency_buckets`.

5. **Collect Top K Elements**:
   - Initialize an empty list `top_k_frequent_elements`.
   - Iterate through `frequency_buckets` in reverse (from highest frequency to lowest).
   - For each non-empty bucket:
     - Add the elements to `top_k_frequent_elements`.
     - Stop once the size of `top_k_frequent_elements` equals `k`.

6. **Return Result**:
   - Return `top_k_frequent_elements`.

---

## Code - Optimized Approach

```python
def top_k_frequent(nums, k):
    # Dictionary to count the frequency of each number
    frequency_count = {}
    
    # List of lists (buckets) to group numbers by their frequency
    frequency_buckets = [[] for index in range(len(nums) + 1)]

    # Populate the frequency count dictionary
    for number in nums:
        frequency_count[number] = 1 + frequency_count.get(number, 0)

    # Populate the frequency buckets based on the count
    for number, count in frequency_count.items():
        frequency_buckets[count].append(number)

    # List to store the result
    top_k_frequent_elements = []

    # Iterate over the buckets in reverse order (starting from the highest frequency)
    for frequency in range(len(frequency_buckets) - 1, 0, -1):
        top_k_frequent_elements += frequency_buckets[frequency]
        
        # Stop when the result contains exactly 'k' elements
        if len(top_k_frequent_elements) == k:
            return top_k_frequent_elements
```

---

## Time and Space Complexity - Optimized Approach

### **Why This Approach is Better**

1. **Time Complexity**:
   - **Frequency Counting**: Takes \(O(n)\), where \(n\) is the length of `nums`.
   - **Bucket Creation and Traversal**: Both take \(O(n)\), since we are just organizing elements by frequency and iterating through the buckets.
   - **Overall**: \(O(n)\), which is much faster than the brute-force \(O(n \log n)\).

2. **Space Complexity**:
   - We use a dictionary to store frequencies and a bucket array of size \(n + 1\).
   - Space complexity is \(O(n)\), which is efficient for large inputs.

---

### **Real-World Scenarios Where This Optimization Matters**

Imagine you’re analyzing website traffic data to determine the top 5 most visited pages. Instead of sorting all pages by their frequency (which could be time-consuming for millions of pages), you can use this optimized approach to find the top pages more efficiently.

---
