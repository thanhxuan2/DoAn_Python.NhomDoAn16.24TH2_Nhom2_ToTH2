import mysql.connector

# ================== KẾT NỐI MYSQL ==================
def get_connection_no_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bungbung102@"  # <-- đổi mật khẩu root của bạn
    )

def get_connection_with_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bungbung102@",
        database="quanlyxe"
    )

# ================== TẠO DATABASE ==================
def create_database():
    try:
        conn = get_connection_no_db()
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS quanlyxe")
        print("Database 'quanlyxe' đã sẵn sàng!")
    except mysql.connector.Error as e:
        print("Lỗi tạo database:", e)
    finally:
        conn.close()

# ================== TẠO BẢNG ==================
def create_tables():
    try:
        conn = get_connection_with_db()
        cursor = conn.cursor()
        
        # Bảng Phòng Ban
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS PhongBan (
            IdPB INT AUTO_INCREMENT PRIMARY KEY,
            TenPB VARCHAR(100) NOT NULL
        )
        """)

        # Bảng Xe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Xe (
            IdXe INT AUTO_INCREMENT PRIMARY KEY,
            BienSo VARCHAR(20) NOT NULL,
            LoaiXe VARCHAR(50) NOT NULL,
            SoCho INT NOT NULL,
            TinhTrang VARCHAR(50),
            IdPB INT,
            FOREIGN KEY (IdPB) REFERENCES PhongBan(IdPB)
        )
        """)

        # Bảng Lái Xe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS LaiXe (
            IdLaiXe INT AUTO_INCREMENT PRIMARY KEY,
            HoTen VARCHAR(100) NOT NULL,
            Tuoi INT,
            BangLai VARCHAR(50),
            IdPB INT,
            FOREIGN KEY (IdPB) REFERENCES PhongBan(IdPB)
        )
        """)

        # Bảng Phân Công
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS PhanCong (
            IdPC INT AUTO_INCREMENT PRIMARY KEY,
            IdXe INT,
            IdLaiXe INT,
            NgayPhanCong DATE,
            FOREIGN KEY (IdXe) REFERENCES Xe(IdXe),
            FOREIGN KEY (IdLaiXe) REFERENCES LaiXe(IdLaiXe)
        )
        """)

        # Bảng Người Dùng
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS NguoiDung (
            IdUser INT AUTO_INCREMENT PRIMARY KEY,
            Username VARCHAR(50),
            Password VARCHAR(50),
            Role VARCHAR(20)
        )
        """)

        conn.commit()
        print("Tất cả bảng đã được tạo!")
    except mysql.connector.Error as e:
        print("Lỗi tạo bảng:", e)
    finally:
        conn.close()

# ================== CHÈN DỮ LIỆU MẪU ==================
def insert_sample_data():
    try:
        conn = get_connection_with_db()
        cursor = conn.cursor()

        # Chèn Phòng Ban
        cursor.execute("SELECT COUNT(*) FROM PhongBan")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO PhongBan (TenPB) VALUES (%s)",
                [("Phòng Kỹ Thuật",), ("Phòng Hành Chính",), ("Phòng Vận Tải",)]
            )

        # Chèn Xe
        cursor.execute("SELECT COUNT(*) FROM Xe")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO Xe (BienSo, LoaiXe, SoCho, TinhTrang, IdPB) VALUES (%s,%s,%s,%s,%s)",
                [("67A-12345", "Xe 4 chỗ", 4, "Tốt", 1),
                 ("67B-56789", "Xe 16 chỗ", 16, "Bảo dưỡng", 2)]
            )

        # Chèn Lái Xe
        cursor.execute("SELECT COUNT(*) FROM LaiXe")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO LaiXe (HoTen, Tuoi, BangLai, IdPB) VALUES (%s,%s,%s,%s)",
                [("Nguyễn Văn A", 35, "B2", 1),
                 ("Trần Văn B", 40, "D", 2)]
            )

        # Chèn Phân Công
        cursor.execute("SELECT COUNT(*) FROM PhanCong")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO PhanCong (IdXe, IdLaiXe, NgayPhanCong) VALUES (%s,%s,%s)",
                [(1, 1, "2024-11-06"), (2, 2, "2024-11-07")]
            )

        conn.commit()
        print("Dữ liệu mẫu đã được chèn!")
    except mysql.connector.Error as e:
        print("Lỗi chèn dữ liệu mẫu:", e)
    finally:
        conn.close()
    

# ================== CHẠY ==================
if __name__ == "__main__":
    create_database()
    create_tables()
    insert_sample_data()
    input("Nhấn Enter để thoát...")
