import time
import streamlit as st

st.html(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #B4C6ED;
    }
    </style>
    """
)

splash_placeholder = st.empty()

with splash_placeholder.container():
    st.markdown(
        """
        <style>
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(15px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        /* הפעלת האנימציה על כל מה שנמצא בתוך קונטיינר הספלאש */
        [data-testid="stVerticalBlock"] > div {
            animation: fadeIn 1.8s ease-out forwards;
        }
        h2 {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", use_container_width=True)

    st.markdown("<h2 style='color: #333333;'>Loading Your Workspace...</h2>", unsafe_allow_html=True)

    time.sleep(3.0)

splash_placeholder.empty()

st.title("Main Application")
st.write("The splash screen faded in and cleared successfully.")
