import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import mysql.connector
from mysql.connector import Error
from io import BytesIO
from tkcalendar import DateEntry
from tkinter import ttk
from datetime import date, datetime
from datetime import date
from tkinter import messagebox  
from datetime import datetime
import pandas as pd
from tkinter import filedialog


#====Kết nối database=====
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bungbung102@",
        database="quanly_xe"
    )
    cursor = conn.cursor()
    print("✅ Kết nối MySQL thành công!")
except Error as e:
    print("❌ Kết nối thất bại:", e)
    conn = None
    cursor = None

# ==========================
# WINDOW CENTER
# ==========================
def center_window(window, width, height):
    sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
    x, y = (sw - width)//2, (sh - height)//2
    window.geometry(f"{width}x{height}+{x}+{y}")

# ==========================
# TẠO CỬA SỔ CHÍNH TRƯỚC
# ==========================
root = tk.Tk()
root.withdraw()  # Ẩn cửa sổ chính khi chưa đăng nhập

root.title("HỆ THỐNG QUẢN LÝ VẬN TẢI")
center_window(root,1000,650)
root.configure(bg="#e0e0e0")

# ==========================
# LOAD ẢNH (đã tắt vì gây lỗi — bạn đã tải banner online bên dưới rồi)
# ==========================
# banner_img = tk.PhotoImage(file="banner.png")   # ❌ Gây lỗi vì không có file này

# ==========================
# FORM ĐĂNG NHẬP
# ==========================
def open_main_app():
    login_window.destroy()
    root.deiconify()  # Hiện cửa sổ chính

def check_login():
    user = username_entry.get()
    pw = password_entry.get()

    if user == "admin" and pw == "123":
        messagebox.showinfo
        open_main_app()
    else:
        messagebox.showerror("Sai thông tin", "Tên đăng nhập hoặc mật khẩu không đúng!")

login_window = tk.Toplevel()
login_window.title("Đăng nhập hệ thống")
login_window.geometry("350x220")
login_window.resizable(False, False)

# 👉 Canh giữa form đăng nhập
sw = login_window.winfo_screenwidth()
sh = login_window.winfo_screenheight()
x = (sw - 350) // 2
y = (sh - 220) // 2
login_window.geometry(f"350x220+{x}+{y}")

tk.Label(login_window, text="ĐĂNG NHẬP HỆ THỐNG", font=("Arial", 14, "bold")).pack(pady=10)

frame_login = tk.Frame(login_window)
frame_login.pack(pady=10)

tk.Label(frame_login, text="Tên đăng nhập:").grid(row=0, column=0)
username_entry = tk.Entry(frame_login, width=25)
username_entry.grid(row=0, column=1, pady=5)

tk.Label(frame_login, text="Mật khẩu:").grid(row=1, column=0)
password_entry = tk.Entry(frame_login, show="*", width=25)
password_entry.grid(row=1, column=1, pady=5)

tk.Button(login_window, text="Đăng nhập", width=12, bg="#3498db", fg="white",
          command=check_login).pack(pady=10)

# ==========================
# BODY (Sidebar + Content)
# ==========================
body = tk.Frame(root, bg="#e0e0e0")
body.pack(fill="both", expand=True)

# Sidebar
sidebar = tk.Frame(body, bg="#34495e", width=200)
sidebar.pack(side="left", fill="y")

# Content
content_frame = tk.Frame(body, bg="#ecf0f1")
content_frame.pack(side="left", fill="both", expand=True)

# ==========================
# FOOTER
# ==========================
footer = tk.Frame(root, bg="#f8f9fa", height=30, bd=1, relief="solid")
footer.pack(fill="x", side="bottom")
tk.Label(footer, text="© 2025 Công ty TNHH Vận Tải An Toàn • Liên hệ: 0900 123 456",
         bg="#f8f9fa", fg="#2c3e50", font=("Arial", 10)).pack(expand=True)

# ==========================
# PAGES
# ==========================
pages = {}

def show_page(name):
    for p in pages.values():
        p.pack_forget()
    pages[name].pack(fill="both", expand=True)

# ===== Tạo từng tab =====
tab_home = tk.Frame(content_frame, bg="#ecf0f1")
pages["Home"] = tab_home

tab_nv = tk.Frame(content_frame, bg="#ecf0f1")
pages["NhanVien"] = tab_nv

tab_pb = tk.Frame(content_frame, bg="#ecf0f1")
pages["PhongBan"] = tab_pb

tab_xe = tk.Frame(content_frame, bg="#ecf0f1")
pages["Xe"] = tab_xe

tab_cd = tk.Frame(content_frame, bg="#ecf0f1")
pages["ChuyenDi"] = tab_cd

tab_tk = tk.Frame(content_frame, bg="#ecf0f1")
pages["ThongKe"] = tab_tk

# ==========================
# HOME PAGE
# ==========================
tk.Label(tab_home, text="HỆ THỐNG QUẢN LÝ VẬN TẢI",
         font=("Arial", 24, "bold"), bg="#ecf0f1").pack(pady=(20,5))

tk.Label(tab_home, text="Chào mừng đến với hệ thống quản lý vận tải",
         font=("Arial", 12), bg="#ecf0f1").pack(pady=(0,15))

# ===== Banner từ URL =====
url = "https://hocvientaichinh.com.vn/wp-content/uploads/2023/03/kinh-nghiem-quan-ly-van-tai-cho-cac-doanh-nghiep-dat-hieu-qua-2-696x398.jpg"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    pil_img = Image.open(BytesIO(response.content))

    width = 700
    ow, oh = pil_img.size
    height = int(oh * (width / ow))
    pil_img = pil_img.resize((width, height), Image.LANCZOS)

    banner_img = ImageTk.PhotoImage(pil_img)
    banner = tk.Label(tab_home, image=banner_img, bg="#ecf0f1")
    banner.image = banner_img
    banner.pack(pady=10)
else:
    tk.Label(tab_home, text="Không tải được banner",
             font=("Arial", 14), bg="#ecf0f1").pack(pady=10)

# Hiện trang chủ
show_page("Home")


# ==============================
# TAB NHÂN VIÊN / LÁI XE
# ==============================
tab_nv = tk.Frame(content_frame, bg="#ecf0f1")
pages["NhanVien"] = tab_nv

tk.Label(tab_nv, text="QUẢN LÝ NHÂN VIÊN / LÁI XE",
         font=("Arial", 18, "bold"), bg="#ecf0f1").pack(pady=10)

# ------------------------------
# Notebook bên trong tab NV
# ------------------------------
nv_notebook = ttk.Notebook(tab_nv)
nv_notebook.pack(fill="both", expand=True, padx=20, pady=5)

# -----------------------------
# TAB 1: Danh sách nhân viên
# -----------------------------
tab_list = tk.Frame(nv_notebook, bg="#f7f9fc")
nv_notebook.add(tab_list, text="📋 NV/LX")

columns = ("id","name","gender","dob","phongban","chucvu","phone","license")
tree_list = ttk.Treeview(tab_list, columns=columns, show="headings", height=20)

col_text = ["Mã NV/LX","Họ và tên","Giới tính","Ngày sinh","Phòng ban","Chức vụ","SĐT","Bằng lái"]
col_width = [80,120,80,80,100,80,80,80]

for col, txt, w in zip(columns, col_text, col_width):
    tree_list.heading(col, text=txt)
    tree_list.column(col, width=w, anchor="center")

sb = ttk.Scrollbar(tab_list, orient="vertical", command=tree_list.yview)
tree_list.configure(yscrollcommand=sb.set)
tree_list.pack(side="left", fill="both", expand=True)
sb.pack(side="right", fill="y")


# -------- Style Treeview đẹp --------
style = ttk.Style()
style.configure("Treeview", rowheight=22, font=("Arial", 10))
style.map('Treeview', background=[('selected', '#2980b9')], foreground=[('selected', 'white')])
tree_list.tag_configure('oddrow', background="#f0f3f7")
tree_list.tag_configure('evenrow', background="#ffffff")


# ==============================
# TAB 2: Thêm/Sửa/Xóa
# ==============================
tab_form = tk.Frame(nv_notebook, bg="#ecf0f1")
nv_notebook.add(tab_form, text="Nhập / Sửa / Xóa")

# -------- Form nhập liệu --------
form_frame = tk.LabelFrame(tab_form, text="Thông tin nhân viên / lái xe",
                           bg="#ecf0f1", font=("Arial", 12, "bold"))
form_frame.pack(fill="x", pady=10, padx=10)

tk.Label(form_frame, text="Mã NV/LX:", bg="#ecf0f1").grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_id = tk.Entry(form_frame, width=25)
entry_id.grid(row=0, column=1, padx=10, pady=8)

tk.Label(form_frame, text="Họ tên:", bg="#ecf0f1").grid(row=0, column=2, padx=10, pady=8, sticky="e")
entry_name = tk.Entry(form_frame, width=25)
entry_name.grid(row=0, column=3, padx=10, pady=8)

gender_var = tk.StringVar(value="Nam")
tk.Label(form_frame, text="Giới tính:", bg="#ecf0f1").grid(row=1, column=0, padx=10, pady=8, sticky="e")
gender_frame = tk.Frame(form_frame, bg="#ecf0f1")
gender_frame.grid(row=1, column=1, padx=10, pady=8, sticky="w")
tk.Radiobutton(gender_frame, text="Nam", variable=gender_var, value="Nam", bg="#ecf0f1").pack(side="left")
tk.Radiobutton(gender_frame, text="Nữ", variable=gender_var, value="Nữ", bg="#ecf0f1").pack(side="left")

tk.Label(form_frame, text="Ngày sinh:", bg="#ecf0f1").grid(row=1, column=2, padx=10, pady=8, sticky="e")
entry_dob = DateEntry(form_frame, width=23, background='darkblue', foreground='white', borderwidth=2, date_pattern="yyyy-mm-dd")
entry_dob.grid(row=1, column=3, padx=10, pady=8)

tk.Label(form_frame, text="Phòng ban:", bg="#ecf0f1").grid(row=2, column=0, padx=10, pady=8, sticky="e")
cb_phongban = ttk.Combobox(form_frame, width=22, state="readonly")
cb_phongban.grid(row=2, column=1, padx=10, pady=8)

tk.Label(form_frame, text="Chức vụ:", bg="#ecf0f1").grid(row=2, column=2, padx=10, pady=8, sticky="e")
cb_chucvu = ttk.Combobox(form_frame, width=22, state="readonly")
cb_chucvu.grid(row=2, column=3, padx=10, pady=8)

tk.Label(form_frame, text="SĐT:", bg="#ecf0f1").grid(row=3, column=0, padx=10, pady=8, sticky="e")
entry_phone = tk.Entry(form_frame, width=25)
entry_phone.grid(row=3, column=1, padx=10, pady=8)

tk.Label(form_frame, text="Bằng lái:", bg="#ecf0f1").grid(row=3, column=2, padx=10, pady=8, sticky="e")
cb_license = ttk.Combobox(form_frame, values=["A1","A2","B1","B2","C","D","E","FC","FE"], width=25, state="readonly")
cb_license.grid(row=3, column=3, padx=10, pady=8)
# ==============================
# HÀM CRUD
# ==============================
def clear_form():
    entry_id.config(state="normal")
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    gender_var.set("Nam")
    entry_dob.set_date(date.today())
    cb_phongban.set("")
    cb_chucvu.set("")
    entry_phone.delete(0, tk.END)
    cb_license.set("")
    global selected_id
    selected_id = None


def load_nhanvien():
    tree_nv.delete(*tree_nv.get_children())
    cur = conn.cursor()
    cur.execute("""
        SELECT nv.id, nv.ho_ten, nv.gioi_tinh, nv.ngay_sinh,
               pb.ten_phongban, cv.ten_chucvu,
               nv.sdt, nv.bang_lai
        FROM laixe nv
        LEFT JOIN phongban pb ON nv.id_phongban = pb.id
        LEFT JOIN chucvu cv ON nv.id_chucvu = cv.id
    """)
    for row in cur.fetchall():
        tree_nv.insert("", "end", values=row)
    cur.close()


def add_nv():
    name = entry_name.get().strip()
    phongban = cb_phongban.get()
    chucvu = cb_chucvu.get()
    if not name or not phongban or not chucvu:
        return messagebox.showwarning("Chú ý", "Không để trống Tên / Phòng ban / Chức vụ")

    nv_id = entry_id.get().strip() or None
    gender = gender_var.get()
    dob = entry_dob.get_date().strftime("%Y-%m-%d")
    phone = entry_phone.get().strip()
    license_val = cb_license.get()

    cur = conn.cursor()
    cur.execute("SELECT id FROM phongban WHERE ten_phongban=%s", (phongban,))
    pb_id = cur.fetchone()[0]

    cur.execute("SELECT id FROM chucvu WHERE ten_chucvu=%s", (chucvu,))
    cv_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO laixe (id, ho_ten, gioi_tinh, ngay_sinh, id_phongban, id_chucvu, sdt, bang_lai)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (nv_id, name, gender, dob, pb_id, cv_id, phone, license_val))
    conn.commit()
    cur.close()

    load_nhanvien()
    clear_form()

def edit_nv():
    global selected_id
    sel = tree_nv.selection()
    if not sel:
        return messagebox.showwarning("Chú ý", "Chọn nhân viên để sửa!")

    values = tree_nv.item(sel)["values"]
    selected_id = values[0]

    entry_id.config(state="disabled")
    entry_id.delete(0, tk.END)
    entry_id.insert(0, values[0])
    entry_name.delete(0, tk.END)
    entry_name.insert(0, values[1])
    gender_var.set(values[2])
    entry_dob.set_date(values[3])
    cb_phongban.set(values[4])
    cb_chucvu.set(values[5])
    entry_phone.delete(0, tk.END)
    entry_phone.insert(0, values[6])
    cb_license.set(values[7])


def save_nv():
    global selected_id
    if not selected_id:
        return messagebox.showwarning("Chú ý", "Bạn chưa chọn nhân viên để lưu!")

    name = entry_name.get().strip()
    phongban = cb_phongban.get()
    chucvu = cb_chucvu.get()
    gender = gender_var.get()
    dob = entry_dob.get_date().strftime("%Y-%m-%d")
    phone = entry_phone.get().strip()
    license_val = cb_license.get()

    cur = conn.cursor()
    cur.execute("SELECT id FROM phongban WHERE ten_phongban=%s", (phongban,))
    pb_id = cur.fetchone()[0]

    cur.execute("SELECT id FROM chucvu WHERE ten_chucvu=%s", (chucvu,))
    cv_id = cur.fetchone()[0]

    cur.execute("""
        UPDATE laixe
        SET ho_ten=%s, gioi_tinh=%s, ngay_sinh=%s, id_phongban=%s, id_chucvu=%s, sdt=%s, bang_lai=%s
        WHERE id=%s
    """, (name, gender, dob, pb_id, cv_id, phone, license_val, selected_id))
    conn.commit()
    cur.close()

    load_nhanvien()
    clear_form()

def delete_nv():
    sel = tree_nv.selection()
    if not sel:
        return messagebox.showwarning("Chú ý", "Chọn nhân viên để xóa!")

    nv_id = tree_nv.item(sel)["values"][0]

    if not messagebox.askyesno("Xác nhận", f"Bạn chắc chắn xóa {nv_id}?"):
        return

    cur = conn.cursor()
    cur.execute("DELETE FROM laixe WHERE id=%s", (nv_id,))
    conn.commit()
    cur.close()

    load_nhanvien()
    clear_form()
# Frame chứa nút, full chiều ngang
btn_frame = tk.Frame(tab_form, bg="#ecf0f1")
btn_frame.pack(fill="x", pady=10, padx=10)

# Frame con để căn giữa các nút
center_frame = tk.Frame(btn_frame, bg="#ecf0f1")
center_frame.pack(anchor="center")  # anchor center

# Tạo các nút trong frame con
buttons = [
    ("Thêm", "#1abc9c", add_nv),
    ("Sửa", "#3498db", edit_nv),
    ("Xóa", "#e74c3c", delete_nv),
    ("Lưu", "#f39c12", save_nv),
    ("Hủy", "#95a5a6", clear_form),
    ("Thoát", "#7f8c8d", lambda: show_page("Home"))
]

for text, color, cmd in buttons:
    tk.Button(center_frame, text=text, bg=color, fg="white", width=12, command=cmd).pack(side="left", padx=5)

  
def load_pb_to_combobox():
    """Cập nhật danh sách Phòng ban và Chức vụ cho combobox của tab NV"""
    try:
        cur = conn.cursor()
        # Phòng ban
        cur.execute("SELECT ten_phongban FROM phongban ORDER BY ten_phongban")
        pb_list = [r[0] for r in cur.fetchall()]
        cb_phongban['values'] = pb_list

        # Chức vụ
        cur.execute("SELECT ten_chucvu FROM chucvu ORDER BY ten_chucvu")
        cv_list = [r[0] for r in cur.fetchall()]
        cb_chucvu['values'] = cv_list

        cur.close()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không tải được danh sách PB/CV: {e}")

def refresh_cb_nv():
    cur = conn.cursor()
    cur.execute("SELECT ten_phongban FROM phongban ORDER BY ten_phongban")
    cb_phongban['values'] = [r[0] for r in cur.fetchall()]

    cur.execute("SELECT ten_chucvu FROM chucvu ORDER BY ten_chucvu")
    cb_chucvu['values'] = [r[0] for r in cur.fetchall()]
    cur.close()
load_pb_to_combobox()

# -------- Treeview Frame --------
tree_frame = tk.Frame(tab_form, bg="#ecf0f1")
tree_frame.pack(fill="both", expand=True, pady=10, padx=10)

columns = ("id","name","gender","dob","phongban","chucvu","phone","license")
tree_nv = ttk.Treeview(tree_frame, columns=columns, show="headings", height=12)

col_text = ["Mã NV/LX","Họ và tên","Giới tính","Ngày sinh","Phòng ban","Chức vụ","SĐT","Bằng lái"]
col_width = [80,120,80,80,100,80,80,80]

for col, txt, w in zip(columns, col_text, col_width):
    tree_nv.heading(col, text=txt)
    tree_nv.column(col, width=w, anchor="center")

# Scrollbars
scroll_y = ttk.Scrollbar(tree_frame, orient="vertical", command=tree_nv.yview)
scroll_x = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree_nv.xview)
tree_nv.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

tree_nv.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")

# ==============================
# BIẾN TRẠNG THÁI
# ==============================
selected_id = None

# ==============================
# KHỞI TẠO TAB NV
# ==============================
refresh_cb_nv()   # load PB/CV cho combobox
load_nhanvien()  # load dữ liệu Treeview
clear_form()      # reset form


# ================================
# TAB CHÍNH: PHÒNG BAN
# ================================
tab_pb = tk.Frame(content_frame, bg="#ecf0f1")
pages["PhongBan"] = tab_pb


# -------------------------------
# Sub-Notebook trong tab PB
# -------------------------------
sub_tab_control = ttk.Notebook(tab_pb)
sub_tab_control.pack(fill="both", expand=True, padx=10, pady=10)

# ================================
# Sub-tab 1: Danh sách PB + CV
# ================================
tab_pb_list = tk.Frame(sub_tab_control, bg="#ecf0f1")
sub_tab_control.add(tab_pb_list, text="Danh sách PB + CV")

tree1_frame = tk.Frame(tab_pb_list)
tree1_frame.pack(fill="both", expand=True, padx=20, pady=20)

columns1 = ("stt", "id", "ten_pb", "mota_pb", "ten_cv", "mota_cv")
tree_pb_all = ttk.Treeview(tree1_frame, columns=columns1, show="headings", height=20)

headers = ["STT", "Mã PB", "Tên PB", "Mô tả PB", "Tên CV", "Mô tả CV"]
widths = [50, 60, 150, 200, 150, 200]

for col, head, w in zip(columns1, headers, widths):
    tree_pb_all.heading(col, text=head)
    tree_pb_all.column(col, width=w, anchor="center")

tree_pb_all.pack(fill="both", expand=True)
scroll_y1 = ttk.Scrollbar(tree1_frame, orient="vertical", command=tree_pb_all.yview)
tree_pb_all.configure(yscrollcommand=scroll_y1.set)
scroll_y1.pack(side="right", fill="y")

# ================================
# Sub-tab 2: Quản lý PB (CRUD)
# ================================
tab_pb_crud = tk.Frame(sub_tab_control, bg="#ecf0f1")
sub_tab_control.add(tab_pb_crud, text="Quản lý PB")

# --- Form nhập liệu
form_frame = tk.LabelFrame(tab_pb_crud, text="Thông tin PB", bg="#ecf0f1", font=("Arial", 12, "bold"))
form_frame.pack(fill="x", padx=20, pady=10)

tk.Label(form_frame, text="Tên PB:", bg="#ecf0f1").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_pb_name = tk.Entry(form_frame, width=30)
entry_pb_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Mô tả PB:", bg="#ecf0f1").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_pb_desc = tk.Entry(form_frame, width=50)
entry_pb_desc.grid(row=1, column=1, columnspan=2, sticky="w", padx=10, pady=5)

tk.Label(form_frame, text="Tên CV:", bg="#ecf0f1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_cv_name = tk.Entry(form_frame, width=30)
entry_cv_name.grid(row=2, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Mô tả CV:", bg="#ecf0f1").grid(row=2, column=2, padx=10, pady=5, sticky="e")
entry_cv_desc = tk.Entry(form_frame, width=30)
entry_cv_desc.grid(row=2, column=3, padx=10, pady=5)

# --- Buttons CRUD
btn_frame = tk.Frame(tab_pb_crud, bg="#ecf0f1")
btn_frame.pack(pady=10)

for text, color, cmd in [
    ("Thêm", "#1abc9c", lambda: add_pb()),
    ("Sửa", "#3498db", lambda: edit_pb()),
    ("Lưu", "#f39c12", lambda: save_pb()),
    ("Xóa", "#e74c3c", lambda: delete_pb()),
    ("Hủy", "#95a5a6", lambda: reset_form())
]:
    tk.Button(btn_frame, text=text, bg=color, fg="white", width=12, command=cmd).pack(side="left", padx=8)

# --- Treeview CRUD
tree2_frame = tk.Frame(tab_pb_crud)
tree2_frame.pack(fill="both", expand=True, padx=20, pady=10)

columns2 = ("stt", "id", "ten_pb", "mota_pb", "ten_cv", "mota_cv")
tree_pb_crud = ttk.Treeview(tree2_frame, columns=columns2, show="headings", height=15)

for col, head, w in zip(columns2, headers, widths):
    tree_pb_crud.heading(col, text=head)
    tree_pb_crud.column(col, width=w, anchor="center")

tree_pb_crud.pack(fill="both", expand=True)
scroll_y2 = ttk.Scrollbar(tree2_frame, orient="vertical", command=tree_pb_crud.yview)
tree_pb_crud.configure(yscrollcommand=scroll_y2.set)
scroll_y2.pack(side="right", fill="y")

# ================================
# Biến toàn cục
# ================================
pb_mode = ""
selected_pb_id = None

# ================================
# RESET FORM
# ================================
def reset_form():
    global pb_mode, selected_pb_id
    entry_pb_name.delete(0, tk.END)
    entry_pb_desc.delete(0, tk.END)
    entry_cv_name.delete(0, tk.END)
    entry_cv_desc.delete(0, tk.END)
    pb_mode = ""
    selected_pb_id = None

# ================================
# LOAD TREEVIEW
# ================================
def load_tree(tab="all"):
    cur = conn.cursor()
    cur.execute("""
        SELECT pb.id, pb.ten_phongban, pb.mota,
               cv.ten_chucvu, cv.mota
        FROM phongban pb
        LEFT JOIN chucvu cv ON pb.id = cv.id_phongban
        ORDER BY pb.id
    """)
    rows = cur.fetchall()
    cur.close()

    target_tree = tree_pb_all if tab == "all" else tree_pb_crud
    target_tree.delete(*target_tree.get_children())

    for stt, r in enumerate(rows, start=1):
        target_tree.insert("", "end", values=(stt, r[0], r[1], r[2], r[3], r[4]))

# ================================
# CRUD PB + CV
# ================================
def add_pb():
    tenpb = entry_pb_name.get().strip()
    mota = entry_pb_desc.get().strip()
    tencv = entry_cv_name.get().strip()
    motacv = entry_cv_desc.get().strip()
    if not tenpb:
        messagebox.showerror("Lỗi", "Tên PB không được để trống!")
        return

    cur = conn.cursor()
    cur.execute("INSERT INTO phongban (ten_phongban, mota) VALUES (%s, %s)", (tenpb, mota))
    conn.commit()
    pb_id = cur.lastrowid
    if tencv:
        cur.execute("INSERT INTO chucvu (ten_chucvu, mota, id_phongban) VALUES (%s,%s,%s)",
                    (tencv, motacv, pb_id))
        conn.commit()
    messagebox.showinfo("Thành công", "Đã thêm PB + CV!")
    reset_form()
    load_tree(tab="crud")
    load_tree(tab="all")
    load_pb_to_combobox()  # Cập nhật combobox NV/LX

def edit_pb():
    global pb_mode, selected_pb_id
    selected = tree_pb_crud.focus()
    if not selected:
        messagebox.showwarning("Chú ý", "Chọn dòng để sửa!")
        return
    values = tree_pb_crud.item(selected, "values")
    selected_pb_id = values[1]
    pb_mode = "edit"

    entry_pb_name.delete(0, tk.END)
    entry_pb_desc.delete(0, tk.END)
    entry_cv_name.delete(0, tk.END)
    entry_cv_desc.delete(0, tk.END)

    entry_pb_name.insert(0, values[2])
    entry_pb_desc.insert(0, values[3])
    entry_cv_name.insert(0, values[4])
    entry_cv_desc.insert(0, values[5])

def save_pb():
    global pb_mode, selected_pb_id
    if pb_mode != "edit" or not selected_pb_id:
        messagebox.showwarning("Chú ý", "Chọn dòng để sửa trước khi lưu!")
        return

    tenpb = entry_pb_name.get().strip()
    mota = entry_pb_desc.get().strip()
    tencv = entry_cv_name.get().strip()
    motacv = entry_cv_desc.get().strip()
    if not tenpb:
        messagebox.showerror("Lỗi", "Tên PB không được để trống!")
        return

    cur = conn.cursor()
    cur.execute("UPDATE phongban SET ten_phongban=%s, mota=%s WHERE id=%s", (tenpb, mota, selected_pb_id))
    cur.execute("SELECT id FROM chucvu WHERE id_phongban=%s", (selected_pb_id,))
    res = cur.fetchone()
    if tencv:
        if res:
            cur.execute("UPDATE chucvu SET ten_chucvu=%s, mota=%s WHERE id=%s", (tencv, motacv, res[0]))
        else:
            cur.execute("INSERT INTO chucvu (ten_chucvu, mota, id_phongban) VALUES (%s,%s,%s)",
                        (tencv, motacv, selected_pb_id))
    conn.commit()
    messagebox.showinfo("Thành công", "Đã cập nhật PB + CV!")
    reset_form()
    load_tree(tab="crud")
    load_tree(tab="all")
    load_pb_to_combobox()  # Cập nhật combobox NV/LX

def delete_pb():
    selected = tree_pb_crud.focus()
    if not selected:
        messagebox.showwarning("Chú ý", "Chọn dòng để xóa!")
        return
    values = tree_pb_crud.item(selected, "values")
    id_pb = values[1]
    if not messagebox.askyesno("Xác nhận", f"Xóa PB {id_pb}?"):
        return
    cur = conn.cursor()
    cur.execute("DELETE FROM chucvu WHERE id_phongban=%s", (id_pb,))
    cur.execute("DELETE FROM phongban WHERE id=%s", (id_pb,))
    conn.commit()
    messagebox.showinfo("Thành công", "Đã xóa PB!")
    reset_form()
    load_tree(tab="crud")
    load_tree(tab="all")
    load_pb_to_combobox()  # Cập nhật combobox NV/LX

# ================================
# Double-click chọn dòng CRUD
# ================================
def on_crud_double_click(event):
    selected = tree_pb_crud.focus()
    if not selected:
        return
    values = tree_pb_crud.item(selected, "values")
    entry_pb_name.delete(0, tk.END)
    entry_pb_desc.delete(0, tk.END)
    entry_cv_name.delete(0, tk.END)
    entry_cv_desc.delete(0, tk.END)

    entry_pb_name.insert(0, values[2])
    entry_pb_desc.insert(0, values[3])
    entry_cv_name.insert(0, values[4])
    entry_cv_desc.insert(0, values[5])

    global pb_mode, selected_pb_id
    pb_mode = "edit"
    selected_pb_id = values[1]

tree_pb_crud.bind("<Double-1>", on_crud_double_click)

# ================================
# Cập nhật PB + CV cho combobox NV/LX
# ================================
def load_pb_to_combobox():
    try:
        cur = conn.cursor()
        cur.execute("SELECT ten_phongban FROM phongban ORDER BY ten_phongban")
        pb_list = [r[0] for r in cur.fetchall()]
        try:
            cb_phongban['values'] = pb_list
        except NameError:
            pass
        cur.execute("SELECT ten_chucvu FROM chucvu ORDER BY ten_chucvu")
        cv_list = [r[0] for r in cur.fetchall()]
        try:
            cb_chucvu['values'] = cv_list
        except NameError:
            pass
        cur.close()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không tải được danh sách PB/CV: {e}")

# ================================
# Load dữ liệu ban đầu
# ================================
reset_form()
load_tree(tab="all")
load_tree(tab="crud")
load_pb_to_combobox()


# TAB QUẢN LÝ XE
# ==============================
tab_xe = tk.Frame(content_frame, bg="#ecf0f1")
pages["Xe"] = tab_xe

tk.Label(tab_xe, text="QUẢN LÝ XE", font=("Arial", 18, "bold"), bg="#ecf0f1").pack(pady=10)

# ------------------------------
# FORM NHẬP LIỆU
# ------------------------------
form_frame_xe = tk.LabelFrame(tab_xe, text="Thông tin xe", bg="#ecf0f1", font=("Arial", 12, "bold"))
form_frame_xe.pack(fill="x", padx=20, pady=5)

tk.Label(form_frame_xe, text="Biển số:", bg="#ecf0f1").grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_bienso = tk.Entry(form_frame_xe, width=25)
entry_bienso.grid(row=0, column=1, padx=10, pady=8)

tk.Label(form_frame_xe, text="Loại xe:", bg="#ecf0f1").grid(row=0, column=2, padx=10, pady=8, sticky="e")
entry_loaixe = tk.Entry(form_frame_xe, width=25)
entry_loaixe.grid(row=0, column=3, padx=10, pady=8)

tk.Label(form_frame_xe, text="Sức chứa:", bg="#ecf0f1").grid(row=1, column=0, padx=10, pady=8, sticky="e")
entry_succhua = tk.Entry(form_frame_xe, width=25)
entry_succhua.grid(row=1, column=1, padx=10, pady=8)

tk.Label(form_frame_xe, text="Năm SX:", bg="#ecf0f1").grid(row=1, column=2, padx=10, pady=8, sticky="e")
entry_namsx = tk.Entry(form_frame_xe, width=25)
entry_namsx.grid(row=1, column=3, padx=10, pady=8)

tk.Label(form_frame_xe, text="Tình trạng:", bg="#ecf0f1").grid(row=2, column=0, padx=10, pady=8, sticky="e")
entry_tinhtrang = tk.Entry(form_frame_xe, width=25)
entry_tinhtrang.grid(row=2, column=1, padx=10, pady=8)

# ------------------------------
# BUTTONS CRUD
# ------------------------------
btn_frame_xe = tk.Frame(tab_xe, bg="#ecf0f1")
btn_frame_xe.pack(pady=10)

mode = None  # 'add' hoặc 'edit'

def make_btn(text, color, cmd):
    return tk.Button(btn_frame_xe, text=text, bg=color, fg="white", width=12, command=cmd)

def clear_form_xe():
    entry_bienso.delete(0, tk.END)
    entry_loaixe.delete(0, tk.END)
    entry_succhua.delete(0, tk.END)
    entry_namsx.delete(0, tk.END)
    entry_tinhtrang.delete(0, tk.END)
    global mode
    mode = None

# ------------------------------
# TREEVIEW
# ------------------------------
tree_frame_xe = tk.Frame(tab_xe)
tree_frame_xe.pack(fill="both", expand=True, padx=20, pady=5)

columns_xe = ("stt", "bien_so", "loai_xe", "suc_chua", "nam_sx", "tinh_trang")
tree_xe = ttk.Treeview(tree_frame_xe, columns=columns_xe, show="headings", height=15)

headers = ["STT", "Biển số", "Loại xe", "Sức chứa", "Năm SX", "Tình trạng"]
widths = [50, 120, 120, 80, 80, 100]

for col, head, w in zip(columns_xe, headers, widths):
    tree_xe.heading(col, text=head)
    tree_xe.column(col, width=w, anchor="center")

tree_xe.pack(fill="both", expand=True)

scroll_y = ttk.Scrollbar(tree_frame_xe, orient="vertical", command=tree_xe.yview)
tree_xe.configure(yscrollcommand=scroll_y.set)
scroll_y.pack(side="right", fill="y")

scroll_x = ttk.Scrollbar(tree_frame_xe, orient="horizontal", command=tree_xe.xview)
tree_xe.configure(xscrollcommand=scroll_x.set)
scroll_x.pack(side="bottom", fill="x")

# ------------------------------
# CRUD FUNCTIONS
# ------------------------------
def load_xe():
    tree_xe.delete(*tree_xe.get_children())
    cursor = conn.cursor()
    cursor.execute("SELECT bien_so, loai_xe, suc_chua, nam_sx, tinh_trang FROM xe ORDER BY id ASC")
    rows = cursor.fetchall()
    for stt, row in enumerate(rows, start=1):
        tree_xe.insert("", tk.END, values=(stt, row[0], row[1], row[2], row[3], row[4]))

def add_xe():
    bien_so = entry_bienso.get()
    loai_xe = entry_loaixe.get()
    suc_chua = entry_succhua.get()
    nam_sx = entry_namsx.get()
    tinh_trang = entry_tinhtrang.get() or "Tốt"

    if not bien_so:
        messagebox.showwarning("Cảnh báo", "Biển số không được để trống!")
        return

    try:
        suc_chua_val = int(suc_chua) if suc_chua else 0
    except ValueError:
        messagebox.showerror("Lỗi", "Sức chứa phải là số nguyên!")
        return

    try:
        nam_sx_val = int(nam_sx) if nam_sx else None
    except ValueError:
        messagebox.showerror("Lỗi", "Năm SX phải là số hợp lệ!")
        return

    cursor = conn.cursor()
    sql = "INSERT INTO xe (bien_so, loai_xe, suc_chua, nam_sx, tinh_trang) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, (bien_so, loai_xe, suc_chua_val, nam_sx_val, tinh_trang))
    conn.commit()

    messagebox.showinfo("Thành công", "Thêm xe thành công!")
    clear_form_xe()
    load_xe()

def edit_xe_mode():
    global mode
    selected = tree_xe.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Chọn xe để sửa!")
        return
    mode = "edit"
    data = tree_xe.item(selected)["values"]
    entry_bienso.delete(0, tk.END)
    entry_bienso.insert(0, data[1])
    entry_loaixe.delete(0, tk.END)
    entry_loaixe.insert(0, data[2])
    entry_succhua.delete(0, tk.END)
    entry_succhua.insert(0, data[3])
    entry_namsx.delete(0, tk.END)
    entry_namsx.insert(0, data[4])
    entry_tinhtrang.delete(0, tk.END)
    entry_tinhtrang.insert(0, data[5])

def save_xe():
    global mode
    if mode != "edit":
        messagebox.showinfo("Info", "Chỉ dùng để cập nhật sửa!")
        return

    selected = tree_xe.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Chọn xe để sửa!")
        return

    bien_so = entry_bienso.get()
    loai_xe = entry_loaixe.get()
    suc_chua = entry_succhua.get()
    nam_sx = entry_namsx.get()
    tinh_trang = entry_tinhtrang.get() or "Tốt"

    try:
        suc_chua_val = int(suc_chua) if suc_chua else 0
    except ValueError:
        messagebox.showerror("Lỗi", "Sức chứa phải là số nguyên!")
        return

    try:
        nam_sx_val = int(nam_sx) if nam_sx else None
    except ValueError:
        messagebox.showerror("Lỗi", "Năm SX phải là số hợp lệ!")
        return

    stt = tree_xe.item(selected)["values"][0]
    # Lấy ID thực từ DB để UPDATE
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM xe ORDER BY id ASC LIMIT %s,1", (stt-1,))
    xe_id = cursor.fetchone()[0]

    sql = "UPDATE xe SET bien_so=%s, loai_xe=%s, suc_chua=%s, nam_sx=%s, tinh_trang=%s WHERE id=%s"
    cursor.execute(sql, (bien_so, loai_xe, suc_chua_val, nam_sx_val, tinh_trang, xe_id))
    conn.commit()
    messagebox.showinfo("Thành công", "Cập nhật xe thành công!")
    clear_form_xe()
    load_xe()
    mode = None

def delete_xe():
    selected = tree_xe.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Chọn xe để xóa!")
        return

    stt = tree_xe.item(selected)["values"][0]
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM xe ORDER BY id ASC LIMIT %s,1", (stt-1,))
    xe_id = cursor.fetchone()[0]

    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa xe này?"):
        cursor.execute("DELETE FROM xe WHERE id=%s", (xe_id,))
        conn.commit()
        messagebox.showinfo("Thành công", "Xóa xe thành công!")
        clear_form_xe()
        load_xe()
        
def exit_app():
    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn thoát chương trình?"):
        root.destroy()  # đóng hẳn cửa sổ Tkinter

def exit_tab():
    root.destroy()
# ------------------------------
# BUTTONS
# ------------------------------
btn_add = make_btn("Thêm", "#1abc9c", add_xe)
btn_edit = make_btn("Sửa", "#3498db", edit_xe_mode)
btn_save = make_btn("Lưu", "#f39c12", save_xe)
btn_delete = make_btn("Xóa", "#e74c3c", delete_xe)
btn_cancel = make_btn("Hủy", "#95a5a6", clear_form_xe)
btn_exit = make_btn("Thoát",  "#7f8c8d", exit_tab)

# list theo thứ tự mong muốn
buttons = [btn_add, btn_edit, btn_save, btn_delete, btn_cancel, btn_exit]

for b in buttons:
    b.pack(side="left", padx=8)


# ------------------------------
# LOAD DỮ LIỆU BAN ĐẦU
# ------------------------------
load_xe()


# ==============================
# TAB CHUYẾN ĐI
# ==============================
tab_trip = tk.Frame(content_frame, bg="#ecf0f1")
pages["ChuyenDi"] = tab_trip

tk.Label(tab_trip, text="QUẢN LÝ CHUYẾN ĐI", font=("Arial", 18, "bold"), bg="#ecf0f1").pack(pady=10)

# ======================================================================
# FORM NHẬP LIỆU
# ======================================================================
form_frame_trip = tk.LabelFrame(tab_trip, text="Thông tin chuyến đi",
                                bg="#ecf0f1", font=("Arial", 12, "bold"))
form_frame_trip.pack(fill="x", padx=20, pady=5)

tk.Label(form_frame_trip, text="Mã chuyến đi:", bg="#ecf0f1").grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_trip_id = tk.Entry(form_frame_trip, width=25)
entry_trip_id.grid(row=0, column=1, padx=10, pady=8)

tk.Label(form_frame_trip, text="Xe:", bg="#ecf0f1").grid(row=0, column=2, padx=10, pady=8, sticky="e")
combo_trip_xe = ttk.Combobox(form_frame_trip, width=25, state="readonly")
combo_trip_xe.grid(row=0, column=3, padx=10, pady=8)

tk.Label(form_frame_trip, text="Lái xe:", bg="#ecf0f1").grid(row=1, column=0, padx=10, pady=8, sticky="e")
combo_trip_driver = ttk.Combobox(form_frame_trip, width=25, state="readonly")
combo_trip_driver.grid(row=1, column=1, padx=10, pady=8)

tk.Label(form_frame_trip, text="Điểm xuất phát:", bg="#ecf0f1").grid(row=1, column=2, padx=10, pady=8, sticky="e")
entry_trip_from = tk.Entry(form_frame_trip, width=25)
entry_trip_from.grid(row=1, column=3, padx=10, pady=8)

tk.Label(form_frame_trip, text="Điểm đến:", bg="#ecf0f1").grid(row=2, column=0, padx=10, pady=8, sticky="e")
entry_trip_to = tk.Entry(form_frame_trip, width=25)
entry_trip_to.grid(row=2, column=1, padx=10, pady=8)

tk.Label(form_frame_trip, text="Ngày đi:", bg="#ecf0f1").grid(row=2, column=2, padx=10, pady=8, sticky="e")
entry_trip_start = DateEntry(form_frame_trip, width=23, background='darkblue',
                             foreground='white', date_pattern='yyyy-mm-dd')
entry_trip_start.grid(row=2, column=3, padx=10, pady=8)

tk.Label(form_frame_trip, text="Ngày về:", bg="#ecf0f1").grid(row=3, column=0, padx=10, pady=8, sticky="e")
entry_trip_end = DateEntry(form_frame_trip, width=23, background='darkblue',
                           foreground='white', date_pattern='yyyy-mm-dd')
entry_trip_end.grid(row=3, column=1, padx=10, pady=8)

tk.Label(form_frame_trip, text="Trạng thái:", bg="#ecf0f1").grid(row=3, column=2, padx=10, pady=8, sticky="e")
combo_trip_status = ttk.Combobox(form_frame_trip, width=25, state="readonly")
combo_trip_status['values'] = ["Chưa khởi hành", "Đang đi", "Hoàn thành", "Hủy"]
combo_trip_status.grid(row=3, column=3, padx=10, pady=8)



#--------------
# ======================================================================
# HÀM CHỨC NĂNG
# ======================================================================
def clear_form_trip():
    entry_trip_id.config(state="normal")
    entry_trip_id.delete(0, tk.END)

    combo_trip_xe.set("")
    combo_trip_driver.set("")

    entry_trip_from.delete(0, tk.END)
    entry_trip_to.delete(0, tk.END)

    # ❗ FIX LỖI: KHÔNG ĐƯỢC set_date("")
    entry_trip_start.delete(0, tk.END)
    entry_trip_end.delete(0, tk.END)

    combo_trip_status.set("")

def save_trip():
    id_trip = entry_trip_id.get()
    xe = combo_trip_xe.get()
    laixe = combo_trip_driver.get()
    noi_di = entry_trip_from.get()
    noi_den = entry_trip_to.get()
    ngay_di = entry_trip_start.get_date()
    ngay_ve = entry_trip_end.get_date()
    trang_thai = combo_trip_status.get()

    if not xe or not laixe or not noi_di or not noi_den:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        return

    if id_trip == "":
        # Tạo mã tự động
        id_trip = str(len(tree_trip.get_children()) + 1)
    else:
        # Xóa bản ghi cũ nếu sửa
        for item in tree_trip.get_children():
            if tree_trip.item(item, "values")[0] == id_trip:
                tree_trip.delete(item)
                break

    tree_trip.insert("", "end", values=(id_trip, xe, laixe, noi_di, noi_den, ngay_di, ngay_ve, trang_thai))
    clear_form_trip()
    messagebox.showinfo("Thành công", "Lưu chuyến đi thành công!")

def edit_trip_mode():
    selected = tree_trip.focus()
    if not selected:
        messagebox.showwarning("Thông báo", "Chọn 1 chuyến đi để sửa")
        return
    values = tree_trip.item(selected, "values")
    entry_trip_id.config(state="normal")
    entry_trip_id.delete(0, tk.END)
    entry_trip_id.insert(0, values[0])
    entry_trip_id.config(state="readonly")
    combo_trip_xe.set(values[1])
    combo_trip_driver.set(values[2])
    entry_trip_from.delete(0, tk.END); entry_trip_from.insert(0, values[3])
    entry_trip_to.delete(0, tk.END); entry_trip_to.insert(0, values[4])
    entry_trip_start.set_date(values[5])
    entry_trip_end.set_date(values[6])
    combo_trip_status.set(values[7])

def delete_trip():
    selected = tree_trip.focus()
    if not selected:
        messagebox.showwarning("Thông báo", "Chọn chuyến đi để xóa!")
        return
    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa chuyến đi này?"):
        tree_trip.delete(selected)
        clear_form_trip()
        messagebox.showinfo("Thành công", "Đã xóa chuyến đi!")

def finish_trip():
    selected = tree_trip.focus()
    if not selected:
        messagebox.showwarning("Thông báo", "Chọn chuyến đi!")
        return
    values = list(tree_trip.item(selected, "values"))
    values[7] = "Hoàn thành"
    tree_trip.item(selected, values=values)
    messagebox.showinfo("OK", "Đã cập nhật trạng thái!")

# ======================================================================
# BUTTONS CĂN GIỮA
# ======================================================================
button_trip_frame = tk.Frame(tab_trip, bg="#ecf0f1")
button_trip_frame.pack(fill="x", padx=20, pady=10)

button_center = tk.Frame(button_trip_frame, bg="#ecf0f1")
button_center.pack(anchor="center")

# ======================================================================
# NÚT BẤM
# ======================================================================
btn_trip_new = tk.Button(button_center, text="Thêm mới", width=12, bg="#27ae60", fg="white",
                         command=clear_form_trip)
btn_trip_new.grid(row=0, column=0, padx=6)

btn_trip_save = tk.Button(button_center, text="Lưu", width=12, bg="#2980b9", fg="white",
                          command=save_trip)
btn_trip_save.grid(row=0, column=1, padx=6)

btn_trip_edit = tk.Button(button_center, text="Sửa", width=12, bg="#f39c12", fg="white",
                          command=edit_trip_mode)
btn_trip_edit.grid(row=0, column=2, padx=6)

btn_trip_delete = tk.Button(button_center, text="Xóa", width=12, bg="#c0392b", fg="white",
                            command=delete_trip)
btn_trip_delete.grid(row=0, column=3, padx=6)

btn_trip_cancel = tk.Button(button_center, text="Hủy", width=12, bg="#d35400", fg="white",
                            command=clear_form_trip)
btn_trip_cancel.grid(row=0, column=5, padx=6)

btn_trip_exit = tk.Button(button_center, text="Thoát", width=12, bg="#2c3e50", fg="white",
                          command=root.quit)
btn_trip_exit.grid(row=0, column=6, padx=6)

# ===========================
# TREEVIEW + SCROLLBAR
# ===========================
tree_frame_trip = tk.Frame(tab_trip)
tree_frame_trip.pack(fill="both", expand=True, padx=20, pady=5)

columns_trip = ("MaChuyenDi", "Xe", "LaiXe", "DiemXuatPhat", "DiemDen", "NgayDi", "NgayVe", "TrangThai")
tree_trip = ttk.Treeview(tree_frame_trip, columns=columns_trip, show="headings", height=15)

headers = ["Mã chuyến đi", "Xe", "Lái xe", "Điểm xuất phát", "Điểm đến", "Ngày đi", "Ngày về", "Trạng thái"]
widths = [80, 100, 100, 120, 120, 100, 100, 100]

for col, head, w in zip(columns_trip, headers, widths):
    tree_trip.heading(col, text=head)
    tree_trip.column(col, width=w, anchor="center")

# Scrollbar dọc
scroll_y_trip = ttk.Scrollbar(tree_frame_trip, orient="vertical", command=tree_trip.yview)
scroll_y_trip.pack(side="right", fill="y")

# Scrollbar ngang
scroll_x_trip = ttk.Scrollbar(tree_frame_trip, orient="horizontal", command=tree_trip.xview)
scroll_x_trip.pack(side="bottom", fill="x")

# Gắn scrollbar vào treeview
tree_trip.configure(yscrollcommand=scroll_y_trip.set, xscrollcommand=scroll_x_trip.set)

tree_trip.pack(fill="both", expand=True)


# ======================================================================
# DỮ LIỆU MẪU
# ======================================================================
sample_data = [
    ("1", "101 - Xe tải A", "201 - Lái xe 1", "An Giang", "TP.HCM", "2025-12-01", "2025-12-02", "Chưa khởi hành"),
    ("2", "102 - Xe tải B", "202 - Lái xe 2", "Cần Thơ", "Hà Nội", "2025-12-03", "2025-12-05", "Đang đi"),
    ("3", "103 - Xe tải C", "203 - Lái xe 3", "Hải Phòng", "Đà Nẵng", "2025-12-06", "2025-12-07", "Hoàn thành")
]

for r in sample_data:
    tree_trip.insert("", "end", values=r)

# Combo mẫu
combo_trip_xe['values'] = ["101 - Xe tải A", "102 - Xe tải B", "103 - Xe tải C"]
combo_trip_driver['values'] = ["201 - Lái xe 1", "202 - Lái xe 2", "203 - Lái xe 3"]

# ==============================
# CHẠY APP
# ==============================

# ==============================
# TAB THỐNG KÊ
# ==============================
tab_thongke = tk.Frame(content_frame, bg="#ecf0f1")
pages["ThongKe"] = tab_thongke

tk.Label(tab_thongke, text="THỐNG KÊ CHUYẾN ĐI",
         font=("Arial", 20, "bold"), bg="#ecf0f1").pack(pady=10)

# ==============================
# FRAME LỌC THEO NGÀY
# ==============================
filter_frame = tk.LabelFrame(tab_thongke, text="Bộ lọc thống kê",
                             bg="#ecf0f1", font=("Arial", 12, "bold"))
filter_frame.pack(fill="x", padx=20, pady=5)

tk.Label(filter_frame, text="Từ ngày:", bg="#ecf0f1").grid(row=0, column=0, padx=10, pady=8)
entry_from_date = DateEntry(filter_frame, width=15, background='darkblue',
                            foreground='white', date_pattern='yyyy-mm-dd')
entry_from_date.grid(row=0, column=1, padx=10, pady=8)

tk.Label(filter_frame, text="Đến ngày:", bg="#ecf0f1").grid(row=0, column=2, padx=10, pady=8)
entry_to_date = DateEntry(filter_frame, width=15, background='darkblue',
                          foreground='white', date_pattern='yyyy-mm-dd')
entry_to_date.grid(row=0, column=3, padx=10, pady=8)

# ==============================
# TREEVIEW
# ==============================
tree_frame_tk = tk.Frame(tab_thongke)
tree_frame_tk.pack(fill="both", expand=True, padx=20, pady=10)

columns_tk = ("MaChuyen", "BienSo", "TenLaiXe", "NgayDi", "NoiDi", "NoiDen", "TinhTrang")
headers = ["Mã chuyến", "Biển số xe", "Tên lái xe", "Ngày đi", "Nơi đi", "Nơi đến", "Tình trạng"]
widths = [90, 90, 100, 100, 100, 100, 100]

tree_thongke = ttk.Treeview(tree_frame_tk, columns=columns_tk, show="headings")
for col, head, w in zip(columns_tk, headers, widths):
    tree_thongke.heading(col, text=head)
    tree_thongke.column(col, width=w, anchor="center")
tree_thongke.pack(fill="both", expand=True, side="left")

scroll_y = ttk.Scrollbar(tree_frame_tk, orient="vertical", command=tree_thongke.yview)
scroll_y.pack(side="right", fill="y")
tree_thongke.configure(yscrollcommand=scroll_y.set)

scroll_x = ttk.Scrollbar(tab_thongke, orient="horizontal", command=tree_thongke.xview)
scroll_x.pack(fill="x", padx=20)
tree_thongke.configure(xscrollcommand=scroll_x.set)

# ==============================
# HÀM LỌC DỮ LIỆU
# ==============================
def filter_data():
    from_date = entry_from_date.get()
    to_date = entry_to_date.get()

    if not from_date or not to_date:
        messagebox.showwarning("Thông báo", "Vui lòng nhập đầy đủ từ ngày và đến ngày!")
        return

    cursor = conn.cursor()
    query = """
        SELECT c.id, x.bien_so, lx.ho_ten, c.ngay_di, c.noi_di, c.noi_den, c.tinh_trang
        FROM chuyendi c
        LEFT JOIN xe x ON c.id_xe = x.id
        LEFT JOIN laixe lx ON c.id_laixe = lx.id
        WHERE c.ngay_di BETWEEN %s AND %s
        ORDER BY c.ngay_di
    """
    cursor.execute(query, (from_date, to_date))
    rows = cursor.fetchall()

    tree_thongke.delete(*tree_thongke.get_children())
    for r in rows:
        tree_thongke.insert("", tk.END, values=r)

# ==============================
# HÀM XUẤT EXCEL
# ==============================
def export_excel():
    data = [tree_thongke.item(row)['values'] for row in tree_thongke.get_children()]
    if not data:
        messagebox.showwarning("Thông báo", "Không có dữ liệu để xuất!")
        return

    df = pd.DataFrame(data, columns=headers)
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Thông báo", "Xuất file Excel thành công!")

# ==============================
# NÚT
# ==============================
btn_filter = tk.Button(filter_frame, text="Lọc dữ liệu",
                       bg="#3498db", fg="white", width=15, command=filter_data)
btn_filter.grid(row=0, column=4, padx=10, pady=8)

btn_export = tk.Button(filter_frame, text="Xuất Excel",
                       bg="#2ecc71", fg="white", width=15, command=export_excel)
btn_export.grid(row=0, column=5, padx=10, pady=8)

# ==============================
# HÀM LOAD DỮ LIỆU BAN ĐẦU
# ==============================
def load_thongke_all():
    cursor = conn.cursor()
    query = """
        SELECT c.id, x.bien_so, lx.ho_ten, c.ngay_di, c.noi_di, c.noi_den, c.tinh_trang
        FROM chuyendi c
        LEFT JOIN xe x ON c.id_xe = x.id
        LEFT JOIN laixe lx ON c.id_laixe = lx.id
        ORDER BY c.ngay_di
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    tree_thongke.delete(*tree_thongke.get_children())
    for r in rows:
        tree_thongke.insert("", tk.END, values=r)

# ==============================
# THÊM DỮ LIỆU MẪU CHỈ KHI BẢNG TRỐNG
# ==============================
def add_sample_data():
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM xe")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO xe (id, bien_so, loai_xe, suc_chua, nam_sx, tinh_trang)
            VALUES 
            (1, '51A-12345', 'Xe tải', 30, 2020, 'Tốt'),
            (2, '51B-54321', 'Xe khách', 45, 2019, 'Tốt')
        """)
        conn.commit()
def load_thongke_all():
    cursor = conn.cursor()
    query = """
        SELECT c.id, x.bien_so, lx.ho_ten, c.ngay_di, c.noi_di, c.noi_den, c.tinh_trang
        FROM chuyendi c
        LEFT JOIN xe x ON c.id_xe = x.id
        LEFT JOIN laixe lx ON c.id_laixe = lx.id
        ORDER BY c.ngay_di
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    # Xóa toàn bộ dữ liệu hiện tại trong Treeview trước khi load
    tree_thongke.delete(*tree_thongke.get_children())

    # Thêm dữ liệu mới vào Treeview
    for r in rows:
        tree_thongke.insert("", tk.END, values=r)



# ==============================
# KHỞI TẠO TAB
# ==============================
add_sample_data()
load_thongke_all()


# SIDEBAR BUTTONS
# ==========================
sidebar_buttons = []
sidebar_active = {}

# Menu đề xuất cho đồ án quản lý vận tải
menu_items = [
    ("🏠 Home", "Home"),                                # Trang chính
    ("👤 Lái xe / Nhân sự vận tải", "NhanVien"),       # Tab nhân viên / lái xe
    ("🏢 Phòng ban", "PhongBan"),                       # Quản lý phòng ban riêng
    ("🚛 Quản lý Xe", "Xe"),                            # Quản lý thông tin xe
    ("🛣️ Chuyến đi", "ChuyenDi"),                     # Quản lý chuyến đi / lịch trình
    ("📊 Thống kê", "ThongKe")                          # Thống kê, báo cáo
]

for text, page_name in menu_items:
    # Xóa ký tự lạ nếu có
    text = text.replace("️", "")
    
    btn = tk.Button(
        sidebar, 
        text=f"  {text}", 
        anchor="w",
        bg="#34495e", fg="white", font=("Arial", 12),
        relief="flat", activebackground="#1abc9c",
        command=lambda n=page_name: show_page(n)
    )
    btn.pack(fill="x", pady=5, padx=0)
    btn.configure(padx=10)  # khoảng cách text với viền

    sidebar_buttons.append(btn)
    sidebar_active[page_name] = btn

# Hiển thị Home mặc định
show_page("Home") 
root.mainloop()
