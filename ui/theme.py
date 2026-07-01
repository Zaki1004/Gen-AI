import streamlit as st


def apply_theme():

    st.markdown(
        """
<style>

/* =========================================
Background
========================================= */

.stApp{

    background-color:#F8F5F2;

}


/* =========================================
Header
========================================= */

h1{

    color:#4E342E;

}

h2{

    color:#4E342E;

}

h3{

    color:#5D4037;

}


/* =========================================
Metric
========================================= */

[data-testid="stMetric"]{

    background:white;

    border-radius:14px;

    padding:10px;

    border:1px solid #E0D7CF;

}


/* =========================================
Chat Input
========================================= */

[data-testid="stChatInput"]{

    border-radius:16px;

}


/* =========================================
Button
========================================= */

.stButton>button{

    background:#6F4E37;

    color:white;

    border:none;

    border-radius:12px;

    font-weight:600;

}

.stButton>button:hover{

    background:#5A3E2B;

}


/* =========================================
Popover
========================================= */

[data-testid="stPopover"] button{

    border-radius:12px;

}


/* =========================================
Sidebar
========================================= */

section[data-testid="stSidebar"]{

    background:#EFE8E1;

}

</style>
""",
        unsafe_allow_html=True
    )