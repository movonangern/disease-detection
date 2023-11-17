import streamlit as st


def setPageConfig():
    st.set_page_config(
        page_title="Streamlit App",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def setSidebar():
    st.setSidebar(
        page_title="Streamlit App",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
def mainPage():
    st.write("Hello World")
    
    



def main():
    setPageConfig()
if "__main__" == main():
    main()