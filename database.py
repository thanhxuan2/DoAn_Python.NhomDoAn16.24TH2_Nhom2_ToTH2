import mysql.connector

# 1. Kết nối database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bungbung102@",   # đổi mật khẩu của bạn
        database="ql_vantai" # chắc chắn đã có database này
    )
    print("✅ Kết nối MySQL thành công!")
except mysql.connector.Error as err:
    print(f"❌ Kết nối thất bại: {err}")
    exit()

# 2. Tạo cursor
cursor = conn.cursor()

# 3. Thực hiện truy vấn
cursor.execute("SELECT ho_ten FROM laixe")
rows = cursor.fetchall()
for row in rows:
    print(row)
