import os
from typing import Optional
import chromadb


class LongTermMemory:

    def __init__(self, name: str, system: Optional[str] = None):
        self.name = name
        memory_path = f"./memory/{name}"
        system_path = f"{memory_path}/system.txt"
        self.client = chromadb.PersistentClient(path=memory_path)
        self.collection = self.client.get_or_create_collection(name=name)
        if system:
            self.system = system
            with open(system_path, "w") as file:
                file.write(system)
        elif os.path.exists(system_path):
            with open(system_path, "r") as file:
                self.system = file.read()
        else:
            self.system = ""

    def count(self):
        return self.collection.count()
    
    def insert(self, message: str) -> int:
        count = str(self.count())
        self.collection.add(
            documents=[message],
            ids=[count]
        )
        return self.collection.count()
    
    def recent(self, n: int = 10) -> list[str]:
        return self.query(n=self.count())[-n:]
    
    def query(self, query_basis: list[str] = None, n: int = 10) -> list[str]:
        if not self.count():
            return []
        else:
            result = self.collection.query(
                query_text = query_basis or [""],
                n_results=min(n, self.count())
            )
            inverted = [
                {"id": result["ids"][0][i], "document": ["documents"][0][i]}
                for i in range(len(result["ids"][0]))
            ]
            result = [
                doc['document']
                for doc in sorted(inverted, key=lambda d: int(d["id"]))
            ]
            return result

    def __str__(self):
        return f"SYSTEM: {self.system}/n{''.join(self.query(n=self.count())).strip()}"
    