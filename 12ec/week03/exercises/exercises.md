# Exercises Week 3

## 1. Working with CSV files

1. Take a dataset of your choice - something from your own work maybe. If it is not a CSV file (but, for instance, an Excel sheet or an SPSS file), export it as CSV. Inspect the file in a text editor of your choice (such as the ones available at https://www.sublimetext.com/, https://notepad-plus-plus.org, or https://atom.io) and check:
- the encoding
- the line ending style
- the delimiter
- whether it has a header row or not
- take a quick look and check whether the file looks "ok", i.e. all rows have equal number of fields etc.


2. Open your file in Python and write it back (with a different file name). Do so both with the low-level (basic Python) and the high-level (pandas) approach. Inspect the result again in the editor and compare. (NB: Depending on the dialect, there may be small differences. If you observe some, which are they?)


## 2. Working with JSON files and APIs

1. Reproduce examples 12.1 (page 315), 12.2 (page 316) and 12.3 (page 334) from the book. Explain the code to a classmate.

2. Think of different ways of storing the data you collected. What would be the pros and cons? Discuss with a classmate.

3. What do you think of example 12.2 (or line 12 in example 12.3, for that matter)? Would you rather store your data *before* or *after* the `json_normalize()` function? Discuss with a classmate. (NB: there are arguments to be made for both)

4. What would happen if you would directly create a dataframe (e.g., via `pd.Dataframe(allitems)`, `pd.Dataframe(data['items'])`, or similar)? Based on this observation, can you describe what `json_normalize()` does?
