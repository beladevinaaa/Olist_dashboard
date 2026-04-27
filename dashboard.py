import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style seaborn
sns.set(style='dark')

# 1. Menyiapkan Helper Functions
def create_bystate_df(df):
    bystate_df = df.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)
    return bystate_df

def create_top_products_df(df):
    top_products_df = df.groupby(by="product_category_name").order_id.nunique().reset_index()
    top_products_df.rename(columns={"order_id": "product_count"}, inplace=True)
    top_products_df = top_products_df.sort_values(by="product_count", ascending=False).head(10)
    return top_products_df

# 2. Load Data
all_df = pd.read_csv("all_data.csv")

# 3. Inisialisasi Session State (Biar menu yang diklik tersimpan lokasinya)
if 'menu_aktif' not in st.session_state:
    st.session_state.menu_aktif = "Demografi"

# 4. Sidebar Navigation (Style List Menu)
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.markdown("## 🧭 Main Menu")
    
    # Membuat tombol yang berfungsi sebagai List Menu
    if st.button("📊 Demografi Pelanggan", use_container_width=True):
        st.session_state.menu_aktif = "Demografi"
        
    if st.button("📦 Performa Produk", use_container_width=True):
        st.session_state.menu_aktif = "Produk"
    
    st.markdown("---")
    st.markdown("### Profile")
    st.markdown("**Bela Devina Ainiyah Widodo**")
    st.caption("Sistem Informasi - UNESA")

# 5. Header Utama
st.header('Olist E-Commerce Analysis Dashboard 🛍️')

# 6. Logika Konten Berdasarkan Tombol yang Diklik
if st.session_state.menu_aktif == "Demografi":
    st.subheader("📍 Customer Distribution by State")
    
    bystate_df = create_bystate_df(all_df)
    chart_data = bystate_df.sort_values(by="customer_count", ascending=False).head(10)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        x="customer_count", 
        y="customer_state",
        data=chart_data,
        palette="viridis",
        ax=ax
    )
    ax.set_title("10 Negara Bagian dengan Pelanggan Terbanyak", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel("Jumlah Pelanggan")
    st.pyplot(fig)

    with st.expander("Lihat Insight"):
        st.write("Wilayah Sao Paulo (SP) mendominasi pasar secara signifikan.")

elif st.session_state.menu_aktif == "Produk":
    st.subheader("📦 Top Selling Product Categories")
    
    top_products_df = create_top_products_df(all_df)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        x="product_count", 
        y="product_category_name", 
        data=top_products_df, 
        palette="magma", 
        ax=ax
    )
    ax.set_title("10 Kategori Produk Paling Banyak Terjual", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel("Jumlah Pesanan")
    st.pyplot(fig)

    with st.expander("Lihat Insight"):
        top_cat = top_products_df.iloc[0]['product_category_name']
        st.write(f"Kategori **{top_cat}** menjadi pemenang di pasar Olist. Kategori Cama, Mesa e Banho mendominasi penjualan karena sifat produknya yang merupakan kebutuhan pokok rumah tangga dengan risiko pengiriman rendah. Stabilitas permintaan di kategori ini menjadikannya kontributor utama pendapatan platform Olist sepanjang periode analisis")

# Footer
st.markdown("---")
st.caption('Copyright (c) Bela Devina 2026')
