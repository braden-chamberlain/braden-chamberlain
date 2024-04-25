from llama_cpp import Llama


model_path = "./models/openorca-platypus2-13b.Q4_K_M.gguf"

def generate_story(user_prompt: str):
    system_prompt = """You are a storyteller, specializing in dramatic,
                       often dark stories about the old west.
                       You grew up in the badlands and hideouts of Arizona,
                       and have devoted your time to telling grand, 
                       realistic stories about outlaws and saddletramps.
                       Write a short story of 1750 words based
                       on the following prompt."""
    prompt = f"### Instruction: {system_prompt}\n\n" \
             f"{user_prompt}\n\n" \
             f"### Response:\n"
    try:
        llm = Llama(
            model_path=model_path,
            n_ctx=4096,
        )
        raw_output = llm(
            prompt,
            stop=["###"],
            max_tokens=-1,
            temperature=0.25,
        )
        reply = raw_output.get("choices")[0].get("text").strip()

        with open('story.txt', 'w') as file:
            file.write(reply)

        return reply
    
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    print(generate_story("""Tell me a story about the notorious outlaw,
                         known as 'the hootsman', due to his nocturnal nature,
                         and his encounter with the eagle-eyed sheriff
                         in southern utah"""))
