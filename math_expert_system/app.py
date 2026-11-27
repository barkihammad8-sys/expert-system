"""Optional Streamlit user interface.

Run from the repository root with: streamlit run math_expert_system/app.py
"""

import streamlit as st

from math_expert_system.core import MathematicsExpertSystem
from math_expert_system.cli import EXAMPLES

st.set_page_config(page_title="Mathematics Expert System", page_icon="🧮", layout="centered")
st.title("🧮 Mathematics Expert System")
st.write("Ask a supported algebra, calculus, geometry, or trigonometry question.")
st.caption("Educational project: answers are limited to the operations listed in the examples.")

if "expert_system" not in st.session_state:
    st.session_state.expert_system = MathematicsExpertSystem()

with st.expander("Example questions"):
    for example in EXAMPLES:
        st.code(example)

question = st.text_input("Your mathematics question", placeholder="e.g. solve 2*x + 3 = 7")
if st.button("Solve", type="primary") and question.strip():
    response = st.session_state.expert_system.ask(question)
    if response["success"]:
        st.success(f"Answer: {response['answer']}")
        if response.get("formula"):
            st.write(f"**Formula:** {response['formula']}")
        st.write(f"**Explanation:** {response['explanation']}")
        verification = response["verification"]
        st.write(f"**Verification:** {verification['details']}")
        with st.expander("View reasoning trace"):
            for step in response["reasoning_trace"]:
                st.write(f"- {step}")
    else:
        st.error(response["error"])
