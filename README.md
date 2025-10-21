# capstone-project-1
# 🏪 TOKO SUKSES SELALU BERJAYA  
### A Python-based Point of Sale (POS) System with Multi-User Access and Daily Sales Report  

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

---

## 📖 Introduction  

**TOKO SUKSES SELALU BERJAYA** is a **Python-based Point of Sale (POS)** and **inventory management system** built for small retail businesses.  
The system automates product management, sales transactions, and daily revenue reporting — all through a simple and user-friendly terminal interface.  

This project demonstrates practical applications of:
- **File handling (CSV-based storage)**
- **Role-based authentication**
- **Modular and maintainable Python functions**

It’s perfect for learning how Python can be applied to real-world business cases such as cashier systems and inventory control.

---

## 🎯 Main Features  

### 👥 Multi-User Login System  
- **Admin**
  - Add, edit, or delete products  
  - Adjust stock and pricing  
  - View daily revenue reports  
- **Cashier**
  - Perform customer transactions  
  - Calculate discounts automatically  
  - Generate purchase receipts  

---

### 📦 Inventory Management (CRUD)  
- Supports Create, Read, Update, and Delete operations for products  
- Automatically stores inventory data in `barang.csv`  
- Instant stock updates after transactions  

---

### 💸 Sales Transaction System  
- Automatic subtotal, total, discount, and change calculation  
- Discount tiers:  
  - 🟡 **5%** for total ≥ Rp30,000  
  - 🟢 **10%** for total ≥ Rp50,000  
- Stock decreases automatically with each purchase  

---

### 🧾 Automatic Transaction Recording  
Every transaction is logged in `penjualan.csv` including:  
- Date and time  
- Cashier name  
- Product details  
- Quantity, total, and change  

---

### 📊 Daily Revenue (Omzet) Report  
- Admin can view daily revenue summaries  
- Option to show detailed transaction history  

---

## ⚙️ Technologies Used  
- **Language:** Python 3.10.5 
- **Libraries:**  
  - `csv` — Data management  
  - `datetime` — Transaction timestamping  
  - `os` — File verification  

> ✅ *No external libraries required — fully standalone.*

---

## 💻 How to Run  

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/toko-sukses-selalu-berjaya.git
   cd toko-sukses-selalu-berjaya
