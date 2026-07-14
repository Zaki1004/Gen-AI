import streamlit as st


def apply_theme():

    st.markdown(
        """
<style>

/* ==========================================================
GLOBAL
========================================================== */

html,
body,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppScrollToBottomContainer"],
[data-testid="stMainBlockContainer"],

/* ==========================================================
HEADER
========================================================== */

header,
[data-testid="stHeader"]{

    background: transparent !important;
    backdrop-filter: blur(8px);

    border-bottom: 1px solid rgba(150,150,150,.15);

}

/* ==========================================================
TEXT
========================================================== */

h1,
h2,
h3,
h4,
h5,
h6{

    color: inherit !important;

}

p,
span,
label,
small,
strong,
li,
div{

    color: inherit !important;

}

[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] *{

    color: inherit !important;

}

[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] *{

    color: inherit !important;
    opacity:.85;

}

/* ==========================================================
CHAT
========================================================== */

[data-testid="stChatMessage"]{

    margin-bottom:18px;

}

[data-testid="stChatMessageContent"]{

    background: var(--secondary-background-color,#FFFFFF) !important;

    border-radius:18px;

    border:1px solid rgba(160,160,160,.18);

    padding:16px;

    color:inherit !important;

}

/* ==========================================================
CHAT INPUT
========================================================== */

[data-testid="stChatInput"]{

    background:transparent !important;

    border:none !important;

    box-shadow:none !important;

}

[data-baseweb="textarea"]{

    border-radius:18px !important;

    border:1px solid rgba(150,150,150,.25) !important;

    overflow:hidden !important;

    background:var(--secondary-background-color,#FFFFFF) !important;

}

[data-baseweb="base-input"]{

    background:transparent !important;

    border-radius:18px !important;

}

textarea{

    background:transparent !important;

    color:inherit !important;

    border:none !important;

}

textarea::placeholder{

    color:gray !important;

}

/* ==========================================================
BUTTON
========================================================== */

.stButton>button{

    background:#6F4E37 !important;

    color:white !important;

    border:none !important;

    border-radius:12px !important;

    transition:.2s;

    font-weight:600;

}

.stButton>button:hover{

    background:#5A3E2B !important;

}

/* ==========================================================
POPOVER
========================================================== */

[data-testid="stPopover"] button{

    border-radius:12px !important;

}

/* ==========================================================
METRIC
========================================================== */

[data-testid="stMetric"]{

    background:var(--secondary-background-color,#FFFFFF) !important;

    border-radius:14px;

    padding:12px;

    border:1px solid rgba(150,150,150,.18);

    box-shadow:0 3px 8px rgba(0,0,0,.05);

}

/* ==========================================================
TABLE
========================================================== */

table{

    border-radius:12px;

}

/* ==========================================================
CODE
========================================================== */

pre{

    border-radius:12px;

}

/* ==========================================================
DIVIDER
========================================================== */

hr{

    border-color:rgba(150,150,150,.18);

}

/* ==========================================================
LINK ICON (Anchor Heading)
========================================================== */

[data-testid="stHeaderActionElements"]{

    display:none;

}

/* ==========================================================
SCROLLBAR
========================================================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#C8A27C;

    border-radius:10px;

}

/* ==========================================================
DARK MODE
========================================================== */

@media (prefers-color-scheme: dark){

html,
body,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppScrollToBottomContainer"],
[data-testid="stMainBlockContainer"],
.stMain{

    background:#121212 !important;

    color:#F2F2F2 !important;

}

[data-testid="stChatMessageContent"]{

    background:#1E1E1E !important;

    border:1px solid #343434 !important;

}

[data-testid="stMetric"]{

    background:#1E1E1E !important;

    border:1px solid #343434 !important;

}

[data-baseweb="textarea"]{

    background:#1E1E1E !important;

    border:1px solid #444 !important;

}

textarea{

    color:white !important;

}

textarea::placeholder{

    color:#A0A0A0 !important;

}

header,
[data-testid="stHeader"]{

    background:#121212 !important;

}

}

</style>
""",
        unsafe_allow_html=True,
    )