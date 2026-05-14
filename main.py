# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI
from routes.chat import router as chat_router
app = FastAPI(
    title="Enterprise AI Assistant",
    version="1.0.0"
)

app.include_router(chat_router)

@app.get("/")

def home():

    return {"message": "AI Assistant Running"}




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
