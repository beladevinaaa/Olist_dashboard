import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style seaborn agar grafik terlihat profesional
sns.set(style='dark')

# 1. Load Data
# Pastikan file all_data.csv berada di folder yang sama dengan file dashboard.py ini
all_df = pd.read_csv("all_data.csv")

# Pastikan kolom tanggal benar-benar tipe datetime agar filter tanggal berfungsi
all_df["order_purchase_timestamp"] = pd.to_datetime(all_df["order_purchase_timestamp"])

# 2. Sidebar - Fitur Interaktif (Filtering)
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.header("⚙️ Filter Eksplorasi")
    
    # FILTER 1: Rentang Waktu (Date Range) - Memenuhi kriteria SMART (Time-bound)
    min_date = all_df["order_purchase_timestamp"].min()
    max_date = all_df["order_purchase_timestamp"].max()
    
    try:
        start_date, end_date = st.date_input(
            label='Rentang Waktu Analisis',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
    except ValueError:
        st.error("Silakan pilih rentang tanggal yang valid.")
        st.stop()

    # FILTER 2: Negara Bagian (State) - Memungkinkan user manipulasi data langsung
    states = sorted(all_df["customer_state"].dropna().astype(str).unique())
    selected_states = st.multiselect(
        label="Pilih Negara Bagian (State):",
        options=states,
        default=states
    )

# 3. Menghubungkan Filter ke Data Utama (Data Manipulation)
# main_df akan berubah secara dinamis setiap kali filter di sidebar diubah
main_df = all_df[
    (all_df["order_purchase_timestamp"] >= pd.to_datetime(start_date)) & 
    (all_df["order_purchase_timestamp"] <= pd.to_datetime(end_date)) &
    (all_df["customer_state"].isin(selected_states))
]

# 4. Header Utama
st.header('Olist E-Commerce Analysis Dashboard 🛍️')
st.markdown(f"**Menampilkan Data Periode:** {start_date} s/d {end_date}")

# --- VISUALISASI 1: Demografi Pelanggan ---
st.subheader("📍 Customer Demographics (2016-2018)")
bystate_df = main_df.groupby("customer_state").customer_id.nunique().reset_index().sort_values(by="customer_id", ascending=False).head(10)

if not bystate_df.empty:
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="customer_id", y="customer_state", data=bystate_df, palette="viridis", ax=ax)
    ax.set_title(f"10 Negara Bagian dengan Pelanggan Terbanyak", fontsize=15)
    ax.set_xlabel("Jumlah Pelanggan")
    ax.set_ylabel(None)
    st.pyplot(fig)

    # REVISI INSIGHT DINAMIS 1
    with st.expander("Lihat Insight Demografi Pelanggan"):
        top_state = bystate_df.iloc[0]['customer_state']
        st.write(f"""
        **Analisis Geografis (2016-2018):**
        * Berdasarkan filter yang Anda pilih, **{top_state}** (Sao Paulo) muncul sebagai kontributor pelanggan terbesar. Hal ini mengonfirmasi sentralisasi ekonomi e-commerce Brazil masih berada di wilayah Tenggara.
        * Dominasi ini menunjukkan infrastruktur logistik di wilayah tersebut sudah matang, sehingga penetrasi pasar digital jauh lebih cepat dibandingkan wilayah lainnya.
        * **Saran Strategis:** Olist disarankan melakukan subsidi ongkos kirim ke wilayah di luar {top_state} untuk mendorong pemerataan pasar dan mengurangi ketergantungan pada satu wilayah saja.
        """)
else:
    st.warning("Data tidak tersedia untuk filter wilayah ini.")

# --- VISUALISASI 2: Performa Produk ---
st.subheader("📦 Best Performing Product (2016-2018)")
top_products_df = main_df.groupby("product_category_name").order_id.nunique().reset_index().sort_values(by="order_id", ascending=False).head(10)

if not top_products_df.empty:
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="order_id", y="product_category_name", data=top_products_df, palette="magma", ax=ax)
    ax.set_title("10 Kategori Produk dengan Penjualan Tertinggi", fontsize=15)
    ax.set_xlabel("Jumlah Pesanan")
    ax.set_ylabel(None)
    st.pyplot(fig)

    # REVISI INSIGHT DINAMIS 2
    with st.expander("Lihat Insight Performa Produk"):
        top_cat = top_products_df.iloc[0]['product_category_name']
        st.write(f"""
        **Analisis Performa Produk (2016-2018):**
        * Kategori **{top_cat}** (Bed, Bath, Table) menjadi tulang punggung transaksi dalam rentang waktu terpilih.
        * Keberhasilan kategori ini menunjukkan bahwa konsumen memercayai Olist untuk produk kebutuhan rumah tangga esensial yang memiliki risiko pengiriman rendah (tidak mudah pecah dan ukuran standar).
        * **Saran Strategis:** Pastikan ketersediaan stok (*safety stock*) pada kategori {top_cat} tetap terjaga. Selain itu, perusahaan bisa melakukan *cross-selling* dengan kategori Health & Beauty untuk meningkatkan nilai belanja per transaksi.
        """)
else:
    st.info("Data produk tidak tersedia untuk rentang waktu ini.")

# 7. Footer & Identity
st.markdown("---")
st.sidebar.markdown("---")
st.sidebar.markdown("### Profile")
st.sidebar.markdown("**Bela Devina Ainiyah Widodo**")
st.sidebar.caption("Sistem Informasi - UNESA")
st.caption('Copyright (c) Bela Devina 2026')
