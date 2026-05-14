import ollama

def ask_llm(question: str) -> str:

    response = ollama.chat(

        model="llama3",

        messages=[

            {

                "role": "system",

                "content": "You are a helpful AI assistant."

            },

            {

                "role": "user",

                "content": question

            }

        ],

        options={

            "temperature": 0.3

        }

    )

    answer = response["message"]["content"]

    return answer