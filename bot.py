from typing import Optional
from ctransformers import AutoModelForCausalLM
from memory import LongTermMemory


class ChatBot:

    def __init__(self, name: str, system: Optional[str] = None):
        self.name = name
        self.system = system
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path_or_repo_id=".models/airoboros-l2-7b-2.2.Q4_K_M.gguf",
            model_type="llama",
            context_length=4096,
            max_new_tokens=1024,
            stop=["USER:"]
        )
        self.memory = LongTermMemory(name, system)

    def __call__(self):
        while True:
            user_input = input(">>> ")
            if not user_input:
                break
            print(self.chat(user_input))

    def chat(self, user_input: str) -> str:
        """
        insert the user's input into memory
        get recent memories
        get related memories
        combine memories -> model -> reply

        @param user_input: String
        @return: String
        """
        self.memory.insert(f"USER: {user_input}\n")
        recent_mem = self.memory.recent()
        past_mem = self.memory.query(recent_mem)
        context = [mem for mem in past_mem if mem not in recent_mem] + recent_mem
        context_str = ''.join(context).strip()
        prompt = f"{self.system}\n{context_str}\nASSISTANT: "
        reply = self.model(prompt).strip()
        self.memory.insert(f"ASSISTANT: {reply}\n")
        return reply

    def __str__(self):
        return f"{'='*32} Chat History {'='*32}\n{self.memory}"