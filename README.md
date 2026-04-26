# Olist E-Commerce Data Analysis Dashboard 🛍️

## Deskripsi
Proyek ini merupakan analisis data dari dataset E-Commerce Olist di Brazil. Dashboard ini dibuat untuk memberikan insight mengenai demografi pelanggan dan performa kategori produk yang paling banyak diminati.

## Fitur Dashboard
- **Customer Demographics:** Menampilkan 10 negara bagian (states) dengan jumlah pelanggan terbanyak.
- **Best Performing Product:** Menampilkan 10 kategori produk dengan volume penjualan tertinggi.
- **Interactive Insights:** Penjelasan singkat mengenai tren data di setiap visualisasi.

## Struktur Proyek
- `/dashboard.py`: File utama untuk menjalankan dashboard Streamlit.
- `/all_data.csv`: Dataset yang telah dibersihkan dan diproses.
- `/requirements.txt`: Daftar library Python yang dibutuhkan.
- `/Submission_Bela.ipynb`: Notebook proses EDA dan data cleaning.

## Cara Menjalankan Secara Lokal
1. Clone repository ini:
   ```bash
   git clone [https://github.com/beladevinaaa/Olist_dashboard.git](https://github.com/beladevinaaa/Olist_dashboard.git)


## Setup Environment - Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Anaconda
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
## Run Steamlit App
```bash
streamlit run dashboard.py
```
