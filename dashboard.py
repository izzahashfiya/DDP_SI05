import streamlit as st

st.title("Halaman Dashboard")
st.image("profil3.jpg", caption="This me!")

#fungsi menghitung dan menyimpan total
def total():
    total_nabung = sum(i["Jumlah"]
                       for i in st.session_state["Total_Semua"]
                       if i ["Tipe"] == "Menabung")
    
    return total_nabung

Total_Semua = st.session_state["Total_Semua"]
total_nabung = total()

st.metric("Total Menabung", f"Rp {total_nabung}")