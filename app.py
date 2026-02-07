from dotenv import load_dotenv
import os

load_dotenv()
print("KEY:", os.getenv("OPENAI_API_KEY"))

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def ask_llm(user_input, expert_type):

    if expert_type == "旅行の専門家":
        system_message = "あなたはプロの旅行プランナーです。親切で具体的にアドバイスしてください。"

    elif expert_type == "キャリアの専門家":
        system_message = "あなたは経験豊富なキャリアコンサルタントです。現実的で前向きな助言をしてください。"

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", "{input}")
    ])

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    chain = prompt | llm

    result = chain.invoke({"input": user_input})

    return result.content

import streamlit as st

st.title("専門家AI相談アプリ")

st.write("""
このアプリでは、選択した専門家AIに相談できます。

使い方：
1. 専門家を選ぶ
2. 質問を入力
3. 送信ボタンを押す
""")

expert = st.radio(
    "専門家を選択してください",
    ["旅行の専門家", "キャリアの専門家"]
)

user_text = st.text_input("質問を入力してください")

if st.button("送信"):
    if user_text:
        answer = ask_llm(user_text, expert)
        st.write("### 回答")
        st.write(answer)
    else:
        st.warning("質問を入力してください")