# Example in the book p. 231

On page 231, there is an example that involves the line

```python3
cv = CountVectorizer(tokenizer=mytokenizer.tokenize)
```

This example only works if `mytokenizer` has been "instantiated" before, and that instruction is missing. 

Essentially, it assumes that this example from page 230 has been run before

```python3
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.tokenize import TreebankWordTokenizer
import regex

class MyTokenizer:
    def tokenize(self, text):
        result = []
        word = r"\p{letter}" 
        for sent in nltk.sent_tokenize(text): 
            tokens = TreebankWordTokenizer().tokenize(sent)
            tokens = [t for t in tokens if regex.search(word, t)]
            result += tokens 
        return result			
```

**and** that you create an "instantiate" of this class with the following command:
```python3
mytokenizer = MyTokenizer()
```

Then, the command ```cv = CountVectorizer(tokenizer=mytokenizer.tokenize)``` will run as expected
```
