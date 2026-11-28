"""Streamlit interface for the Mathematics Expert System."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from math_expert_system.core import MathematicsExpertSystem
from math_expert_system.cli import EXAMPLES

st.set_page_config(page_title="Mathematics Expert System", page_icon="🧮", layout="centered")
st.title("🧮 Mathematics Expert System")
st.write("Enter a mathematics question and get a clear answer.")
st.caption("Supports the operations demonstrated in the examples. Use * for multiplication or write 2x; use ^ for powers.")

if "expert_system" not in st.session_state:
    st.session_state.expert_system = MathematicsExpertSystem()

with st.expander("Try an example"):
    for example in EXAMPLES:
        st.code(example)

question = st.text_input(
    "Enter your question",
    placeholder="e.g. 2x^3 + 3x^2 + 5x + 6 = 0",
)

show_steps = st.checkbox("Show explanation and verification", value=False)

if st.button("Calculate", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a mathematics question.")
    else:
        response = st.session_state.expert_system.ask(question)
        if response["success"]:
            st.success("Answer")
            if response.get("latex_answer"):
                st.latex(response["latex_answer"])
            else:
                st.markdown(f"**{response['answer']}**")

            if response.get("numeric_answer") and response["numeric_answer"] != response["answer"]:
                st.markdown("**Decimal / numerical form**")
                st.write(response["numeric_answer"])

            if response.get("formula"):
                st.caption(f"Formula: {response['formula']}")

            if show_steps:
                st.divider()
                st.subheader("Explanation")
                st.write(response.get("explanation", "No explanation is available."))
                verification = response.get("verification", {})
                st.subheader("Verification")
                st.write(verification.get("details", "No verification details are available."))
                with st.expander("Reasoning trace"):
                    for step in response.get("reasoning_trace", []):
                        st.write(f"- {step}")
        else:
            st.error(response["error"])
            st.info("Check the expression and try again. Examples are available above.")
