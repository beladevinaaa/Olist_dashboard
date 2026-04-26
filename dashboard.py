import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style seaborn
sns.set(style='dark')

# 1. Menyiapkan Helper Functions (untuk memproses data)
def create_bystate_df(df):
    bystate_df = df.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={
        "customer_id": "customer_count"
    }, inplace=True)
    return bystate_df

def create_top_products_df(df):
    top_products_df = df.groupby(by="product_category_name").order_id.nunique().reset_index()
    top_products_df.rename(columns={
        "order_id": "product_count"
    }, inplace=True)
    top_products_df = top_products_df.sort_values(by="product_count", ascending=False).head(10)
    return top_products_df

# 2. Load Data
all_df = pd.read_csv("all_data.csv")

# 3. Header
st.header('Olist E-Commerce Dashboard 🛍️')

# 4. Sidebar (Opsional: Tambahan info diri)
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png") # Bisa diganti logo lain
    st.markdown("## Proyek Analisis Data")
    st.markdown("**Bela Devina Ainiyah Widodo**")
    st.markdown("Sistem Informasi - UNESA")

# 5. Menyiapkan DataFrame Agregasi
bystate_df = create_bystate_df(all_df)
top_products_df = create_top_products_df(all_df)

# --- VISUALISASI PERTANYAAN 1 ---
st.subheader("Customer Demographics")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(
    x="customer_count", 
    y="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False).head(10),
    palette="viridis",
    ax=ax
)
ax.set_title("Number of Customers by State (Top 10)", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=12)
st.pyplot(fig)

with st.expander("Lihat Insight Demografi"):
    st.write(
        """Berdasarkan grafik di atas, Sao Paulo (SP) merupakan negara bagian dengan jumlah pelanggan terbanyak. 
        Hal ini menunjukkan konsentrasi pasar yang sangat kuat di wilayah pusat ekonomi tersebut."""
    )

# --- VISUALISASI PERTANYAAN 2 ---
st.subheader("Best Performing Product")

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))

sns.barplot(
    x="product_count", 
    y="product_category_name", 
    data=top_products_df, 
    palette="magma", 
    ax=ax
)
ax.set_title("Top 10 Best Selling Product Categories", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=12)

st.pyplot(fig)

with st.expander("Lihat Insight Performa Produk"):
    st.write(
        """Kategori produk seperti kebutuhan rumah tangga (bed_bath_table) dan kesehatan/kecantikan 
        mendominasi penjualan, yang mencerminkan pola konsumsi harian pelanggan di platform Olist."""
    )

st.caption('Copyright (c) Bela Devina 2026')