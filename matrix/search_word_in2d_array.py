"""

Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "GEEKS"

Output: pattern found at 0, 0
        pattern found at 0, 8
        pattern found at 1, 0
Explanation: 'GEEKS' can be found as prefix of
1st 2 rows and suffix of first row

Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "EEE"

Output: pattern found at 0, 2
        pattern found at 0, 10
        pattern found at 2, 2
        pattern found at 2, 12
Explanation: EEE can be found in first row 
twice at index 2 and index 10
and in second row at 2 and 12 

"""

def find_word_in_grid(grid, word):
    for i, row in enumerate(grid):
        start = 0
        while start < len(row):
            start = row.find(word, start)
            if start == -1:
                break
            print(f"pattern found at {i}, {start}")
            start += 1  # Move to the next character to find overlapping patterns

# Example usage
grid = ["GEEKSFORGEEKS", "GEEKSQUIZGEEK", "IDEQAPRACTICE"]
word = "GEEKS"
find_word_in_grid(grid, word)

word = "EEE"
find_word_in_grid(grid, word)

