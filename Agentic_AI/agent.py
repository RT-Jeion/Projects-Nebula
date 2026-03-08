from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from llm_sertup import get_llm

store = {}

def get_chat_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()

    return store[session_id]

def create_agent():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a Helpful chatBot"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ]
    )

    chain = prompt | llm

    return RunnableWithMessageHistory(
        chain,
        get_chat_history,
        input_messages_key="input",
        history_messages_key="history"
    )

agent_executor = create_agent()