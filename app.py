# 以下を「app.py」に書き込み
import streamlit as st
import google.generativeai as genai
import secret_keys  # 外部ファイルにAPI keyを保存

# GOOGLE_API_KEY の設定
# genai.configure(api_key=secret_keys.google_api_key)
genai.configure(api_key=se.secrets.GoogleAPI.oogle_api_key)

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = ["hoge"]

# 生きる意味を聞いてみる
model = genai.GenerativeModel("gemini-pro")

if "chat" not in st.session_state:
    st.session_state["chat"] = model.start_chat(history=[])

def communicate():
  messages = st.session_state["messages"]
  chat = st.session_state["chat"]
  response = chat.send_message(st.session_state["user_input"])
  st.session_state["chat"] = chat
  messages.append(response.text)
  st.session_state["user_input"] = "" # 入力欄を消去

# ユーザーインターフェイスの構築
st.title("My First AI Chatbot")
st.write("Gemini APIを使ったチャットボットです。")

if st.session_state["chat"]:
    chat = st.session_state["chat"]

    for message in chat.history:  # 直近のメッセージを上に
        if message.role == "user":
          speaker = "🙂"
        if message.role == "model":
          speaker="🤖"
        st.write(speaker + ": " + message.parts[0].text)

st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)