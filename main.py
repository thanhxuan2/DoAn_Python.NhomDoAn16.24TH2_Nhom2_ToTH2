import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkcalendar import DateEntry
from tkinter import ttk
from datetime import date, datetime
from datetime import date
from tkinter import messagebox  

# ==========================
# WINDOW
# ==========================
def center_window(window, width, height):
    sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
    x, y = (sw - width)//2, (sh - height)//2
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("HỆ THỐNG QUẢN LÝ VẬN TẢI")
center_window(root,1000,650)
root.configure(bg="#e0e0e0")

# ==========================
# BODY + SIDEBAR + CONTENT + FOOTER
# ==========================
body = tk.Frame(root, bg="#e0e0e0")
body.pack(fill="both", expand=True)

# Sidebar
sidebar = tk.Frame(body, bg="#34495e", width=200)
sidebar.pack(side="left", fill="y")

# Content
content_frame = tk.Frame(body, bg="#ecf0f1")
content_frame.pack(side="left", fill="both", expand=True)

# Footer nằm **ngoài body**, luôn sát đáy
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
# ===== Home Page =====

# 1 - Trang Home
tab_home = tk.Frame(content_frame, bg="#ecf0f1")
pages["Home"] = tab_home
# 2 - Trang Nhân viên
tab_nv = tk.Frame(content_frame, bg="#ecf0f1")
pages["NhanVien"] = tab_nv

# 3 - Trang Phòng ban
tab_pb = tk.Frame(content_frame, bg="#ecf0f1")
pages["PhongBan"] = tab_pb

# 4 - Trang Xe
tab_xe = tk.Frame(content_frame, bg="#ecf0f1")
pages["Xe"] = tab_xe

# 5 - Trang Chuyến đi
tab_cd = tk.Frame(content_frame, bg="#ecf0f1")
pages["ChuyenDi"] = tab_cd

# 6 - Trang Thống kê
tab_tk = tk.Frame(content_frame, bg="#ecf0f1")
pages["ThongKe"] = tab_tk

# Tiêu đề nằm trên cùng
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

    # Resize giữ tỉ lệ, không bị méo
    width = 700
    orig_w, orig_h = pil_img.size
    height = int(orig_h * (width / orig_w))

    pil_img = pil_img.resize((width, height), Image.LANCZOS)

    banner_img = ImageTk.PhotoImage(pil_img)
    banner_label = tk.Label(tab_home, image=banner_img, bg="#ecf0f1")
    banner_label.image = banner_img
    banner_label.pack(pady=10)

else:
    banner_label = tk.Label(
        tab_home,
        text="Không tải được banner",
        font=("Arial", 14),
        bg="#ecf0f1"
    )
    banner_label.pack(pady=10)

# GẮN banner_label vào Frame để show_page dùng được
tab_home.banner_label = banner_label

from tkcalendar import DateEntry
from tkinter import ttk

# ========================
# Tab Nhân viên / Lái xe
# ========================
tab_nv = tk.Frame(content_frame, bg="#ecf0f1")
pages["NhanVien"] = tab_nv

# Tiêu đề
tk.Label(tab_nv, text="QUẢN LÝ NHÂN VIÊN / LÁI XE",
         font=("Arial", 18, "bold"), bg="#ecf0f1").pack(pady=10)

# =======================
# Form nhập liệu – Có khung
# =======================
form_frame = tk.LabelFrame(tab_nv, text="Thông tin nhân viên / lái xe",
                           bg="#ecf0f1", font=("Arial", 12, "bold"))
form_frame.pack(fill="x", padx=20, pady=10)

# Hàng 1
tk.Label(form_frame, text="Mã NV/LX:", bg="#ecf0f1").grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_id = tk.Entry(form_frame, width=25)
entry_id.grid(row=0, column=1, padx=10, pady=8)

tk.Label(form_frame, text="Họ tên:", bg="#ecf0f1").grid(row=0, column=2, padx=10, pady=8, sticky="e")
entry_name = tk.Entry(form_frame, width=25)
entry_name.grid(row=0, column=3, padx=10, pady=8)

# Hàng 2 - Giới tính
tk.Label(form_frame, text="Giới tính:", bg="#ecf0f1").grid(row=1, column=0, padx=10, pady=8, sticky="e")

gender_var = tk.StringVar(value="Nam")
gender_frame = tk.Frame(form_frame, bg="#ecf0f1")  # frame gom 2 radio
gender_frame.grid(row=1, column=1, padx=10, pady=8, sticky="w")

tk.Radiobutton(gender_frame, text="Nam", variable=gender_var, value="Nam", bg="#ecf0f1").pack(side="left")
tk.Radiobutton(gender_frame, text="Nữ", variable=gender_var, value="Nữ", bg="#ecf0f1").pack(side="left")

tk.Label(form_frame, text="Ngày sinh:", bg="#ecf0f1").grid(row=1, column=2, padx=10, pady=8, sticky="e")
entry_dob = DateEntry(form_frame, width=23, background='darkblue', foreground='white', borderwidth=2)
entry_dob.grid(row=1, column=3, padx=10, pady=8)

# Hàng 3
tk.Label(form_frame, text="Phòng ban:", bg="#ecf0f1").grid(row=2, column=0, padx=10, pady=8, sticky="e")
cb_phongban = ttk.Combobox(form_frame, values=["Vận tải", "Hành chính", "Kỹ thuật"], width=22)
cb_phongban.grid(row=2, column=1, padx=10, pady=8)

tk.Label(form_frame, text="Chức vụ:", bg="#ecf0f1").grid(row=2, column=2, padx=10, pady=8, sticky="e")
cb_chucvu = ttk.Combobox(form_frame, values=["Tài xế chính", "Tài xế dự bị", "Phụ lái"], width=22)
cb_chucvu.grid(row=2, column=3, padx=10, pady=8)

# Hàng 4
tk.Label(form_frame, text="SĐT:", bg="#ecf0f1").grid(row=3, column=0, padx=10, pady=8, sticky="e")
entry_phone = tk.Entry(form_frame, width=25)
entry_phone.grid(row=3, column=1, padx=10, pady=8)

tk.Label(form_frame, text="Bằng lái:", bg="#ecf0f1").grid(row=3, column=2, padx=10, pady=8, sticky="e")
cb_license = ttk.Combobox(form_frame, values=["A1", "A2", "B1", "B2", "C", "D", "E", "FC", "FE"], width=25)
cb_license.grid(row=3, column=3, padx=10, pady=8)

# =======================
# Nút thao tác – căn giữa
# =======================
btn_frame = tk.Frame(tab_nv, bg="#ecf0f1")
btn_frame.pack(fill="x", padx=20, pady=5)

# Frame con để căn giữa
inner_frame = tk.Frame(btn_frame, bg="#ecf0f1")
inner_frame.pack()

btn_add = tk.Button(inner_frame, text="Thêm", bg="#1abc9c", fg="white", width=12)
btn_edit = tk.Button(inner_frame, text="Sửa", bg="#3498db", fg="white", width=12)
btn_delete = tk.Button(inner_frame, text="Xóa", bg="#e74c3c", fg="white", width=12)
btn_save = tk.Button(inner_frame, text="Lưu", bg="#f39c12", fg="white", width=12)
btn_cancel = tk.Button(inner_frame, text="Hủy", bg="#95a5a6", fg="white", width=12)
btn_exit = tk.Button(inner_frame, text="Thoát", bg="#7f8c8d", fg="white", width=12)

# Pack các nút với khoảng cách đều nhau
for btn in [btn_add, btn_edit, btn_delete, btn_save, btn_cancel, btn_exit]:
    btn.pack(side="left", padx=5)

# =======================
# Frame bao quanh Treeview 
# =======================
# Frame chứa Treeview
tree_frame = tk.LabelFrame(tab_nv, text="Danh sách lái xe / nhân sự vận tải",
                           bg="#ecf0f1", font=("Arial", 12, "bold"))
tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

style = ttk.Style()
style.configure("Custom.Treeview", 
                font=("Arial", 10), 
                rowheight=25)  # chiều cao mỗi hàng
style.configure("Custom.Treeview.Heading", 
                font=("Arial", 10))  # chữ tiêu đề bình thường
style.layout("Custom.Treeview", [('Custom.Treeview.treearea', {'sticky': 'nswe'})])

# =======================
# Treeview
# =======================
columns = ("id", "name", "gender", "dob", "phongban", "chucvu", "phone", "license")
tree_nv = ttk.Treeview(tree_frame,
                       columns=columns,
                       show="headings",
                       style="Custom.Treeview",
                       height=15)

col_text = ["Mã NV/LX", "Họ và tên", "Giới tính", "Ngày sinh", "Phòng ban", "Chức vụ", "SĐT", "Bằng lái"]
col_width = [100,80, 80, 80, 80, 80,70, 80]
col_anchor = ["center"] * len(columns)

for col, txt, w, a in zip(columns, col_text, col_width, col_anchor):
    tree_nv.heading(col, text=txt)
    tree_nv.column(col, width=w, anchor=a)

# =======================
# Scrollbar
# =======================
scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree_nv.yview)
tree_nv.configure(yscrollcommand=scrollbar.set)

# Pack Treeview và Scrollbar
tree_nv.pack(side="left", fill="both", expand=True, padx=(5,0), pady=5)
scrollbar.pack(side="right", fill="y", padx=(0,5), pady=5)

#======================================
# Xóa dữ liệu trên form
#======================================
def clear_form():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    gender_var.set("Nam")
    entry_dob.set_date(date.today())   # đặt ngày hiện tại
    cb_phongban.set("")
    cb_chucvu.set("")
    entry_phone.delete(0, tk.END)
    cb_license.set("")
#======================================
# Thêm nhân viên / lái xe
#======================================
def add_nv():
    id_ = entry_id.get()
    name = entry_name.get()
    gender = gender_var.get()
    dob = entry_dob.get_date()
    phongban = cb_phongban.get()
    chucvu = cb_chucvu.get()
    phone = entry_phone.get()
    license_ = cb_license.get()
    
    if id_ == "" or name == "":
        messagebox.showwarning("Lỗi", "Mã NV và Họ tên không được để trống!")
        return
    
    # Kiểm tra trùng ID
    for row_id in tree_nv.get_children():
        if tree_nv.item(row_id)["values"][0] == id_:
            messagebox.showerror("Lỗi", f"Mã NV/LX '{id_}' đã tồn tại!")
            return
    
    tree_nv.insert("", "end", values=(id_, name, gender, dob, phongban, chucvu, phone, license_))
    clear_form()  # Xóa form sau khi thêm

btn_add.config(command=add_nv)

#======================================
# Sửa nhân viên / lái xe
#======================================
def edit_nv():
    selected = tree_nv.selection()
    if not selected:
        messagebox.showwarning("Lỗi", "Chọn nhân viên để sửa!")
        return

    # Lấy dữ liệu từ form
    id_ = entry_id.get()
    name = entry_name.get()
    gender = gender_var.get()
    dob = entry_dob.get_date()
    phongban = cb_phongban.get()
    chucvu = cb_chucvu.get()
    phone = entry_phone.get()
    license_ = cb_license.get()

    # Kiểm tra trùng ID (ngoại trừ bản ghi đang sửa)
    for row_id in tree_nv.get_children():
        if row_id != selected[0] and tree_nv.item(row_id)["values"][0] == id_:
            messagebox.showerror("Lỗi", f"Mã NV/LX '{id_}' đã tồn tại!")
            return

    # Cập nhật dữ liệu cho Treeview
    tree_nv.item(selected[0], values=(id_, name, gender, dob, phongban, chucvu, phone, license_))
btn_edit.config(command=edit_nv)

#======================================
# Xóa nhân viên / lái xe
#======================================
def delete_nv():
    selected = tree_nv.selection()
    if not selected:
        messagebox.showwarning("Lỗi", "Chọn nhân viên để xóa!")
        return
    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa?"):
        tree_nv.delete(selected[0])
        clear_form()

btn_delete.config(command=delete_nv)
btn_cancel.config(command=clear_form)
btn_exit.config(command=root.destroy)
#======================================
# Khi chọn dòng trên Treeview thì hiện dữ liệu lên form
#======================================
def on_tree_select(event):
    selected = tree_nv.selection()
    if selected:
        values = tree_nv.item(selected[0], "values")
        entry_id.delete(0, tk.END)
        entry_id.insert(0, values[0])
        entry_name.delete(0, tk.END)
        entry_name.insert(0, values[1])
        gender_var.set(values[2])
        dob_date = datetime.strptime(values[3], "%Y-%m-%d").date()
        entry_dob.set_date(dob_date)
        cb_phongban.set(values[4])
        cb_chucvu.set(values[5])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, values[6])
        cb_license.set(values[7])

tree_nv.bind("<<TreeviewSelect>>", on_tree_select)

def save_nv():
    all_data = []
    for row_id in tree_nv.get_children():
        values = tree_nv.item(row_id)["values"]
        all_data.append(values)
    messagebox.showinfo("Lưu", f"Đã lưu {len(all_data)} nhân viên/lái xe!")
    # TODO: ghi all_data ra file hoặc database nếu cần

btn_save.config(command=save_nv)

# Phòng ban & Chức vụ
tab_pb = tk.Frame(content_frame, bg="#ecf0f1")
pages["PhongBan"] = tab_pb
tk.Label(tab_pb, text="QUẢN LÝ PHÒNG BAN & CHỨC VỤ", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=10)

# Xe
tab_xe = tk.Frame(content_frame, bg="#ecf0f1")
pages["Xe"] = tab_xe
tk.Label(tab_xe, text="QUẢN LÝ XE", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=10)

# Chuyến đi
tab_trip = tk.Frame(content_frame, bg="#ecf0f1")
pages["ChuyenDi"] = tab_trip
tk.Label(tab_trip, text="CHUYẾN ĐI", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

# Thống kê
tab_thongke = tk.Frame(content_frame, bg="#ecf0f1")
pages["ThongKe"] = tab_thongke
tk.Label(tab_thongke, text="THỐNG KÊ", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

# ==========================
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


# Mặc định mở Home
show_page("Home")

root.mainloop()
