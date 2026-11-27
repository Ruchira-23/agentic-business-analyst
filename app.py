import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from google import genai
from google.genai import types
from datatools import get_revenue
from analytics import percent_change
import os

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="InsightAI | Business Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY is missing")
    st.stop()

# -----------------------------------
# GEMINI INITIALIZATION
# -----------------------------------

if "client" not in st.session_state:
    st.session_state.client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            timeout=30000,
            retry_options=types.HttpRetryOptions(
                attempts=1
            )
        )
    )

config = types.GenerateContentConfig(
    tools=[get_revenue, percent_change]
)

if "chat" not in st.session_state:
    st.session_state.chat = (
        st.session_state.client.chats.create(
            model="gemini-3.5-flash-lite",
            config=config
        )
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# LOAD BUSINESS DATA
# -----------------------------------

df = pd.read_csv("business_data.csv")

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.title("📊 InsightAI")
    st.caption("Healthcare Intelligence Copilot")

    st.divider()

    if st.button(
        "＋ New Conversation",
        use_container_width=True,
        type="primary"
    ):
        st.session_state.messages = []

        st.session_state.chat = (
            st.session_state.client.chats.create(
                model="gemini-3.5-flash-lite",
                config=config
            )
        )

        st.rerun()

    st.subheader("🏥 Departments")

    for department in df["department"].unique():
        st.write(f"• {department}")

    st.divider()

    st.subheader("💡 Try asking")

    st.info("What was Home Care revenue in July?")
    st.info("Compare Home Care revenue in June and July.")
    st.info("What was Rehab revenue in June?")

    st.divider()

    st.subheader("⚙️ About this application")

    st.caption("""
    **AI Engine:** Google Gemini

    **Analytics:** Python

    **Interface:** Streamlit

    **Data Source:** Synthetic business dataset

    **Version:** 0.1 — Prototype
    """)

    st.warning(
        "Demo only. Do not enter patient "
        "or confidential business information."
    )

# -----------------------------------
# HEADER
# -----------------------------------

st.title("InsightAI")
st.markdown(
    "### Healthcare Business Intelligence Copilot"
)

st.caption(
    "Transform business data into conversational insights."
)

st.divider()

# -----------------------------------
# KPI DASHBOARD
# -----------------------------------

st.subheader("📈 Business Performance Overview")

june = df[df["month"] == "June"]
july = df[df["month"] == "July"]

june_revenue = june["revenue"].sum()
july_revenue = july["revenue"].sum()

june_visits = june["visits"].sum()
july_visits = july["visits"].sum()

june_fte = june["fte"].sum()
july_fte = july["fte"].sum()

revenue_change = percent_change(
    june_revenue, july_revenue
)

visits_change = percent_change(
    june_visits, july_visits
)

fte_change = percent_change(
    june_fte, july_fte
)

st.caption("July performance compared to June")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Revenue",
        f"${july_revenue:,.0f}",
        f"{revenue_change:.2f}%",
        border=True
    )

with col2:
    st.metric(
        "Total Visits",
        f"{july_visits:,}",
        f"{visits_change:.2f}%",
        delta_color="off",
        border=True
    )

with col3:
    st.metric(
        "Total FTEs",
        f"{july_fte:,}",
        f"{fte_change:.2f}%",
        delta_color="off",
        border=True
    )

# -----------------------------------
# REVENUE VISUALIZATION
# -----------------------------------

with st.expander(
    "📊 Department Revenue Analysis",
    expanded=True
):

    revenue_chart = df.pivot_table(
        index="department",
        columns="month",
        values="revenue",
        aggfunc="sum"
    )

    revenue_chart = revenue_chart[["June", "July"]]

    st.bar_chart(
        revenue_chart,
        stack=False,
        color=["#A4BBD1", "#2463A0"]
    )

# -----------------------------------
# SOURCE DATA
# -----------------------------------

with st.expander("🗂️ View Business Dataset"):
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# -----------------------------------
# CHAT INTERFACE
# -----------------------------------

st.subheader("🤖 Ask InsightAI")

if not st.session_state.messages:
    st.info(
        "Hello! I'm your AI Business Analyst. "
        "Ask me about departmental revenue "
        "and month-over-month performance."
    )

for message in st.session_state.messages:
    st.chat_message(
        message["role"]
    ).write(message["content"])

user_input = st.chat_input(
    "Ask me about your business data..."
)

if user_input and user_input.strip():

    st.chat_message("user").write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant"):

        with st.spinner(
            "Analyzing your business data..."
        ):
            try:
                response = (
                    st.session_state.chat.send_message(
                        user_input
                    )
                )

                answer = response.text

                st.write(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(
                    f"Agent request failed: {e}"
                )

st.divider()

st.caption(
    "InsightAI | Agentic Analytics Portfolio Project "
    "| Powered by Gemini, Python and Streamlit"
)