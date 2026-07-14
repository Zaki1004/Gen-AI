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

    box-shadow:0 2px 8px rgba(0,0,0,.04);

}


/* =========================================
Chat Input
========================================= */

[data-testid="stChatInput"]{

    border-radius:16px;

    border:1px solid #DDD4CB;

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

    transition:0.2s ease;

}

.stButton>button:hover{

    background:#5A3E2B;

    transform:translateY(-1px);

}


/* =========================================
Popover
========================================= */

[data-testid="stPopover"] button{

    border-radius:12px;

}

/* =========================================
Chat Bubble
========================================= */

[data-testid="stChatMessage"]{

    margin-bottom:18px;

}

[data-testid="stChatMessageContent"]{

    padding:14px 18px;

}


/* =========================================
Markdown
========================================= */

[data-testid="stMarkdownContainer"] p{

    line-height:1.8;

}


/* =========================================
Divider
========================================= */

hr{

    border-color:#DDD4CB;

    margin-top:16px;

    margin-bottom:20px;

}


/* =========================================
Caption
========================================= */

[data-testid="stCaptionContainer"]{

    color:#8B7D70;

    margin-top:-6px;

    margin-bottom:18px;

}


/* =========================================
Table
========================================= */

table{

    border-radius:10px;

}


/* =========================================
Code Block
========================================= */

pre{

    border-radius:12px;

}


/* =========================================
Scrollbar
========================================= */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#C8A27C;

    border-radius:10px;

}

</style>
""",
        unsafe_allow_html=True
    )