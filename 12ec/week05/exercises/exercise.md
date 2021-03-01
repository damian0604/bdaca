# Working with textual data

### 0. Get the data.

- Download `articles.tar.gz` from 
https://dx.doi.org/10.7910/DVN/ULHLCB

- Unpack it. On Linux and MacOS, you can do this with `tar -xzf mydata.tar.gz` on the command line. On Windows, you may need an additional tool such as `7zip` for that (note that technically speaking, there is a `tar` archive within a `gz` archive, so unpacking may take *two* steps depending on your tool).


### 1. Inspect the structure of the dataset. 
What information do the following elements give you?

- Folder (directory) names
- Folder structure/hierachy
- File names
- File contents

### 2. Discuss strategies for working with this dataset!

- Which questions could you answer?
- How could you deal with it, given the size and the structure?
- How much memory[^1] (RAM) does your computer have? How large is the complete dataset? What does that mean?
- Make a sketch (e.g., with pen&paper), how you could handle your workflow and your data to answer your question.

[^1] *memory* (RAM), not *storage* (harddisk)!

### 3. Read some (or all?) data

Here is some example code that you can modify. Assuming that he folder `articles` is in the same folder as the notebook you are currently working on, you could, for instance, do the following to read a *part* of your dataset.

```python3
from glob import glob
infowarsfiles = glob('articles/*/Infowars/*')
infowarsarticles = []
for filename in infowarsfiles:
    with open(filename) as f:
	    infowarsarticles.append(f.read())
```

- Can you explain what the `glob` function does? 
- What does `infowarsfiles` contain, and what doets `infowarsarticles` contain? First make an educated guess based on the code snippet, then check it! Do *not* print the whole thing, but use `len`, `type` en slicing `[:10]` to get the info you need.

### 4. Perform some analyses!

- Perform some first analyses on the data using string methods and regular expressions!

