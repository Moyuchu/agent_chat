from typing import List
from .index import RAGIndex

class RAGRetriever:
    def __init__(self, index: RAGIndex):
        self.index = index

    def retrieve(self, query: str, top_k: int = 3) -> List[str]:
        query_words = query.split()
        relevant_docs = set()
        for word in query_words:
            if word in self.index.index:
                relevant_docs.update(self.index.index[word])
        relevant_docs = list(relevant_docs)
        relevant_docs.sort(key=lambda x: len(self.index.documents[x]), reverse=True)
        return [self.index.documents[i] for i in relevant_docs[:top_k]]