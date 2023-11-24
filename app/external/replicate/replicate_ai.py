import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = "r8_fG5laWlXKezHHs4KCekQm2tasBesc7S1S4MrX"

class ReplicateAPI:
    def __init__(self):
        pass

    def generate_description(self, prompt_input):
        output = replicate.run(
            "meta/llama-2-7a0b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
            input={
                "debug": False,
                "top_k": 50,
                "top_p": 1,
                "prompt": prompt_input,
                "temperature": 0.5,
                "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
                "max_new_tokens": 500,
                "min_new_tokens": -1
            }
        )
        output_list = list(output)
        description_string = ''.join(output_list)

        return description_string
