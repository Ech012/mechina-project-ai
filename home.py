import streamlit as st

st.set_page_config(page_title="Support Teach - Materials", page_icon="📚", layout="centered")

st.html(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #B4C6ED;
    }

    [data-testid="stVerticalBlock"] {
        background-color: #F3F1FA;
        border-radius: 30px;
        padding: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.05);
        max-width: 480px;
        margin: 0 auto;
    }

    .custom-header-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        margin-bottom: 20px;
        direction: rtl;
    }
    .header-logo-text {
        text-align: center; 
        color: #3A3566; 
        margin: 0; 
        font-size: 24px;
        font-weight: bold;
        white-space: nowrap;
    }

    .custom-filter-row {
        display: flex;
        justify-content: space-between;
        gap: 8px;
        width: 100%;
        margin-bottom: 20px;
        direction: rtl;
    }
    .filter-btn {
        background-color: white;
        border: 1px solid #EAE6F8;
        border-radius: 12px;
        padding: 8px 12px;
        color: #3A3566;
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
        flex: 1;
        text-align: center;
        white-space: nowrap;
        box-shadow: 0px 2px 6px rgba(142, 126, 219, 0.04);
        transition: all 0.2s ease;
    }
    .filter-btn:hover {
        background-color: #8E7EDB;
        color: white;
    }

    input {
        direction: rtl !important;
        text-align: right !important;
    }
    ::placeholder {
        text-align: right !important;
        font-size: 13px !important;
    }

    .custom-card {
        background-color: white;
        border-radius: 20px;
        padding: 14px 16px;
        margin-bottom: 12px;
        box-shadow: 0px 4px 12px rgba(142, 126, 219, 0.06);
        direction: rtl;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .card-right-section {
        display: flex;
        align-items: center;
        gap: 14px;
        flex-grow: 1;
        overflow: hidden;
    }

    .card-icon-box {
        font-size: 24px; 
        background-color: #EAE6F8; 
        width: 48px;
        height: 48px;
        min-width: 48px;
        border-radius: 14px; 
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .card-text-box {
        text-align: right;
        overflow: hidden;
    }

    .card-title {
        margin: 0; 
        color: #3A3566; 
        font-size: 15px;
        font-weight: 600;
        white-space: nowrap;
    }

    .card-subtitle {
        margin: 4px 0 0 0; 
        color: #8A8A8A; 
        font-size: 12px;
        white-space: nowrap;
    }

    .header-card {
        background-color: white;
        border-radius: 20px;
        padding: 16px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 12px rgba(142, 126, 219, 0.06);
        text-align: center;
        direction: rtl;
    }

    h1, h2, h3, h4, h5, p, span {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .tag {
        background-color: #EAE6F8;
        color: #7B61FF;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
        white-space: nowrap;
        margin-right: 10px;
    }

    .fab-btn {
        background-color: #8E7EDB;
        color: white;
        border: none;
        border-radius: 50%;
        width: 56px;
        height: 56px;
        font-size: 28px;
        position: fixed;
        bottom: 90px;
        left: 30px;
        box-shadow: 0px 6px 16px rgba(142, 126, 219, 0.4);
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 999;
    }
    </style>
    """
)

st.markdown(
    """
    <div class="custom-header-row">
        <div style="font-size: 22px;">👤</div>
        <h3 class="header-logo-text">support <span style="color:#8E7EDB;">teach</span></h3>
        <div style="font-size: 22px;">🔔</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="header-card">
        <h4 style='margin:0 0 6px 0; color:#3A3566; font-weight:600;'>חומרי הוראה ולמידה</h4>
        <p style='margin:0; color:#8A8A8A; font-size:13px;'>חפשו מערכי שיעור, דפי עבודה ומצגות של המורים המובילים</p>
    </div>
    """,
    unsafe_allow_html=True
)

search_query = st.text_input("🔍 חפש חומר לימודי...", placeholder="למשל: אנגלית לכיתה י', מתמטיקה שאלון 581...")

st.markdown(
    "<p style='direction: rtl; text-align: right; color:#3A3566; font-weight:bold; margin-bottom:8px; font-size:14px;'>סינון לפי קטגוריה:</p>",
    unsafe_allow_html=True)

st.markdown(
    """
    <div class="custom-filter-row">
        <div class="filter-btn">הכל</div>
        <div class="filter-btn">דפי עבודה</div>
        <div class="filter-btn">מצגות</div>
        <div class="filter-btn">מבחנים</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<p style='direction: rtl; text-align: right; color:#3A3566; font-weight:bold; font-size:14px;'>חומרים מובילים בשבילך:</p>",
    unsafe_allow_html=True)

st.markdown(
    """
    <div class="custom-card">
        <div class="card-right-section">
            <div class="card-icon-box">🏙️</div>
            <div class="card-text-box">
                <h5 class="card-title">מערך שיעור אינטראקטיבי - מחוז תל אביב</h5>
                <p class="card-subtitle">נושא: הסתברות מותנית | שכבת י'</p>
            </div>
        </div>
        <span class="tag">מצגת</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="custom-card">
        <div class="card-right-section">
            <div class="card-icon-box" style="background-color: #D1F2D9;">🏡</div>
            <div class="card-text-box">
                <h5 class="card-title">דף הכנה לבגרות - מחוז מרכז</h5>
                <p class="card-subtitle">חטיבה עליונה | מתמטיקה</p>
            </div>
        </div>
        <span class="tag" style="background-color: #D1F2D9; color: #27AE60;">תרגול</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="custom-card">
        <div class="card-right-section">
            <div class="card-icon-box" style="background-color: #8E7EDB; color: white; font-weight: bold; font-size: 16px;">Aa</div>
            <div class="card-text-box">
                <h5 class="card-title">אנגלית – חטיבה עליונה</h5>
                <p class="card-subtitle">שיתוף רעיונות, חומרי למידה והתייעצויות</p>
            </div>
        </div>
        <span class="tag" style="background-color: #FCE4D6; color: #E67E22;">ספרות</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<button class="fab-btn">+</button>', unsafe_allow_html=True)

st.write("---")
nav_cols = st.columns(4)

with nav_cols[0]:
    st.markdown(
        "<p style='text-align:center; font-size:22px; margin:0;'>🏠</p><p style='text-align:center; margin:0; font-size:12px; color:#8A8A8A;'>בית</p>",
        unsafe_allow_html=True)

with nav_cols[1]:
    st.markdown(
        "<p style='text-align:center; font-size:22px; margin:0;'>💬</p><p style='text-align:center; margin:0; font-size:12px; color:#8A8A8A;'>הודעות</p>",
        unsafe_allow_html=True)

with nav_cols[2]:
    st.markdown(
        "<p style='text-align:center; font-size:24px; margin:0; color:#8E7EDB;'>📚</p><p style='text-align:center; margin:0; font-size:12px; color:#8E7EDB; font-weight:bold;'>חומרים</p>",
        unsafe_allow_html=True)

with nav_cols[3]:
    st.markdown(
        "<p style='text-align:center; font-size:22px; margin:0; color:#8A8A8A;'>...</p><p style='text-align:center; margin:0; font-size:12px; color:#8A8A8A;'>עוד</p>",
        unsafe_allow_html=True)
