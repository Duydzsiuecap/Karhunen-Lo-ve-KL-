import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from sklearn.decomposition import PCA

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng Dụng Phép Biến Đổi KL (PCA)")
root.geometry("1000x800")
root.resizable(False, False)

# Căn giữa cửa sổ
window_width = 1000
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Frame chứa các điều khiển
control_frame = tk.Frame(root)
control_frame.pack(pady=20)

# Label hiển thị tọa độ
coord_label = tk.Label(root, text="Tọa độ: (x, y)", font=("Arial", 12))
coord_label.pack(pady=5)

# Chức năng chọn ảnh từ máy tính
def load_image():
    global original_image, processed_image
    filepath = filedialog.askopenfilename()
    if filepath:
        image = cv2.imread(filepath)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        original_image = image_rgb.copy()
        update_button.config(state=tk.NORMAL)
        process_image()

# Chức năng xử lý ảnh với PCA
def process_image():
    global processed_image, pca_model
    k = int(entry_k.get())
    processed_image = np.zeros_like(original_image, dtype=np.uint8)
    pca_model = []
    
    for i in range(3):
        channel = original_image[:, :, i]
        pca = PCA(n_components=k)
        transformed = pca.fit_transform(channel)
        restored = pca.inverse_transform(transformed)
        processed_image[:, :, i] = np.clip(restored, 0, 255)
        pca_model.append(pca)
    
    show_image(original_image, "Ảnh Gốc", 0)
    show_image(processed_image, f"Ảnh Tái Tạo ({k} Thành Phần Chính)", 1)
    save_button.config(state=tk.NORMAL)
    restore_button.config(state=tk.NORMAL)

# Chức năng lưu ảnh
def save_image():
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")])
    if filepath:
        image = Image.fromarray(processed_image)
        image.save(filepath)

# Chức năng khôi phục ảnh
def restore_image():
    global restored_image
    restored_image = np.zeros_like(processed_image, dtype=np.uint8)
    
    for i in range(3):
        transformed = pca_model[i].transform(processed_image[:, :, i])
        restored = pca_model[i].inverse_transform(transformed)
        restored_image[:, :, i] = np.clip(restored, 0, 255)
    
    show_image(restored_image, "Ảnh Phục Hồi", 2)

# Chức năng hiển thị ảnh trên giao diện
def show_image(image, title, column):
    image = Image.fromarray(image)
    
    # Lấy kích thước của label để điều chỉnh kích thước ảnh
    label_width = 200
    label_height = 300
    image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  # Resize ảnh theo kích thước của label
    
    image_tk = ImageTk.PhotoImage(image)
    
    # Tạo label hiển thị ảnh
    label = tk.Label(image_frame, image=image_tk)
    label.image = image_tk  # Lưu tham chiếu để tránh ảnh bị xóa
    label.grid(row=0, column=column, padx=20)
    
    # Tạo label tiêu đề cho ảnh
    label_title = tk.Label(image_frame, text=title, font=("Arial", 12, "bold"))
    label_title.grid(row=1, column=column, pady=10)

# Tạo các widget trên giao diện
load_button = tk.Button(control_frame, text="Chọn Ảnh", command=load_image, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
load_button.grid(row=0, column=0, padx=10)

entry_k_label = tk.Label(control_frame, text="Số thành phần chính (k):", font=("Arial", 12))
entry_k_label.grid(row=0, column=1, padx=10)

entry_k = tk.Entry(control_frame, font=("Arial", 12), width=5)
entry_k.insert(tk.END, "50")
entry_k.grid(row=0, column=2, padx=10)

update_button = tk.Button(control_frame, text="Cập Nhật", command=process_image, font=("Arial", 12), bg="#FFA500", fg="white", padx=10, pady=5, state=tk.DISABLED)
update_button.grid(row=0, column=3, padx=10)

save_button = tk.Button(control_frame, text="Lưu Ảnh", command=save_image, font=("Arial", 12), bg="#008CBA", fg="white", padx=10, pady=5, state=tk.DISABLED)
save_button.grid(row=0, column=4, padx=10)

restore_button = tk.Button(control_frame, text="Phục Hồi", command=restore_image, font=("Arial", 12), bg="#FF5733", fg="white", padx=10, pady=5, state=tk.DISABLED)
restore_button.grid(row=0, column=5, padx=10)

# Frame chứa hình ảnh
image_frame = tk.Frame(root)
image_frame.pack(pady=20)

# Chạy giao diện
root.mainloop()
