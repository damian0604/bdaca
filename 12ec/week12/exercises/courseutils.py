
from pathlib import Path
import tarfile
import bz2
import urllib.request
import re
import pickle
import requests

def get_review_data(filename = "reviewdata.pickle.bz2", url = "http://cssbook.net/d/aclImdb_v1.tar.gz"):
    '''
    Checks whether review dataset has already been downloaded.
    If not, downloads it.
    
    Parameters
    ----------
    filename : string
        name of cached file
    url : string
        url of IMDB dataset
    
    Returns
    -------
    tuple of lists of strings
        reviews_train, reviews_test, label_train, label_test
    '''

    if Path(filename).exists():
        print(f"Using cached file {filename}")
        with bz2.BZ2File(filename, 'r') as f:
            reviews_train, reviews_test, label_train, label_test = pickle.load(f)
    else:
        print(f"Downloading from {url}")
        fn, _headers = urllib.request.urlretrieve(url, filename=None)
        t = tarfile.open(fn, mode="r:gz")
        reviews_train, reviews_test, label_train, label_test = [], [], [], []
        for file in t.getmembers():
            try:
                _imdb, dataset, label, _fn = Path(file.name).parts
            except ValueError:
                # if the Path cannot be parsed, e.g. because it does not consist of exactly four parts, then it is not a part of the dataset but for instance a folder name. Let's skip it then
                continue
            if dataset == "train" and (label=='pos' or label=='neg'):
                reviews_train.append(t.extractfile(file).read().decode("utf-8"))
                label_train.append(label)
            elif dataset == "test" and (label=='pos' or label=='neg'):
                reviews_test.append(t.extractfile(file).read().decode("utf-8"))
                label_test.append(label)
        print(f"Saving {len(label_train)} training and {len(label_test)} test cases to {filename}")
        with bz2.BZ2File(filename, 'w') as f:
            pickle.dump((reviews_train, reviews_test, label_train, label_test), f)
    return reviews_train, reviews_test, label_train, label_test

