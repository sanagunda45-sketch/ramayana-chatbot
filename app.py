import streamlit as st
from openai import OpenAI

st.title("🪷 Ramayana Live Chatbot")
st.write("Talk with Lord Rama, Sita, or Hanuman — guided by Ramayana wisdom.")

# Use your OpenRouter key from Streamlit secrets
client = OpenAI(api_key=st.secrets['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'])

user_input = st.text_input("You:", "")

if st.button("Ask"):
    if user_input:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Lord Rama, speaking kindly and wisely from the Ramayana."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = completion.choices[0].message.content
        st.markdown(f"**Lord Rama:** {reply}")
