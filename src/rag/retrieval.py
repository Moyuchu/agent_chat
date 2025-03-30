# import numpy as np
# import faiss
# import logging
# from sentence_transformers import SentenceTransformer

# class KnowledgeRetriever:
#     def __init__(self, knowledge_base_path="knowledge.txt"):
#         """
#         初始化检索系统：
#         - 加载 SentenceTransformer 作为嵌入模型
#         - 读取本地知识库，并创建索引
#         - 设置日志记录
#         """
#         self.model = SentenceTransformer("all-MiniLM-L6-v2")  
#         self.database, self.index = self.load_knowledge_base(knowledge_base_path)
#         self.query_count = 0  # 记录查询次数

#         logging.basicConfig(level=logging.INFO, format="%(asctime)s - [RAG] %(message)s")

#     def load_knowledge_base(self, filepath):
#         """
#         读取知识库文件，并构建 FAISS 索引
#         :param filepath: 知识库文件路径
#         :return: (知识库列表, FAISS 索引)
#         """
#         try:
#             with open(filepath, "r", encoding="utf-8") as f:
#                 knowledge = [line.strip() for line in f.readlines() if line.strip()]
#         except FileNotFoundError:
#             logging.error("知识库文件未找到！")
#             return [], None

#         if not knowledge:
#             logging.warning("知识库为空！")
#             return [], None

#         # 计算嵌入向量
#         embeddings = np.array([self.model.encode(text) for text in knowledge])
        
#         # 构建 FAISS 索引
#         index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 距离索引
#         index.add(embeddings)

#         logging.info(f"知识库加载完成，共 {len(knowledge)} 条知识")
#         return knowledge, index

#     def query(self, text, top_k=1):
#         """
#         查询最相关的知识
#         :param text: 用户输入
#         :param top_k: 返回最相关的 k 条知识
#         :return: 最相关的知识文本
#         """
#         if self.index is None or not self.database:
#             return "知识库不可用"

#         self.query_count += 1  # 更新查询计数
#         logging.info(f"查询次数: {self.query_count} - 用户输入: {text}")

#         # 计算查询的嵌入向量
#         query_embedding = np.array([self.model.encode(text)])
#         distances, indices = self.index.search(query_embedding, k=top_k)

#         # 过滤无效结果
#         results = []
#         for i in range(top_k):
#             if indices[0][i] >= 0:
#                 results.append(self.database[indices[0][i]])

#         if results:
#             logging.info(f"检索结果: {results[0]}")
#             return results[0]
#         else:
#             logging.info("未找到相关知识")
#             return "未找到相关知识"

# # 运行测试
# if __name__ == "__main__":
#     retriever = KnowledgeRetriever("knowledge.txt")
#     while True:
#         user_input = input("\n用户输入: ")
#         if user_input.lower() in ["exit", "quit"]:
#             break
#         print("RAG Result:", retriever.query(user_input))
