import json
from typing import List, Dict

class RAGIndex:
    def __init__(self):
        self.index = {}
        self.documents = []

    def add_document(self, document: str):
        self.documents.append(document)
        words = document.split()
        for word in words:
            if word not in self.index:
                self.index[word] = []
            self.index[word].append(len(self.documents) - 1)

    def save(self, path: str):
        with open(path, "w") as f:
            json.dump({"index": self.index, "documents": self.documents}, f)

    @classmethod
    def load(cls, path: str):
        with open(path, "r") as f:
            data = json.load(f)
        instance = cls()
        instance.index = data["index"]
        instance.documents = data["documents"]
        return instance