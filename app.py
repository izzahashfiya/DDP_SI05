import streamlit as st

dashboard = st.Page("./fitur/dashboard.py", title="dashboard")
nabung = st.Page("./fitur/nabung.py", title="nabung")

pg = st.navigation(
    {
     "Menu Utama" : [dashboard],
     "Transaksi" : [nabung],
    }
)

if "Total_Semua" not in st.session_state:
    st.session_state["Total_Semua"] = []

pg.run()