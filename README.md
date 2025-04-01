# KL-Karhunen-Lo-ve-Transform-
huydietxylyanh
1. Cài đặt và Thư viện
cv2: Sử dụng thư viện OpenCV để xử lý ảnh.

numpy: Dùng để thao tác với mảng dữ liệu, rất quan trọng trong xử lý ảnh.

tkinter: Thư viện giao diện người dùng (GUI) để xây dựng cửa sổ và các điều khiển.

PIL (Pillow): Sử dụng để chuyển đổi hình ảnh giữa các định dạng và hiển thị ảnh trong giao diện Tkinter.

PCA từ sklearn: Phép biến đổi chính phương (Principal Component Analysis) để giảm chiều dữ liệu của ảnh.

2. Cấu trúc Ứng Dụng
Ứng dụng này có một giao diện người dùng (GUI) được xây dựng bằng Tkinter với các tính năng như:

Chọn ảnh từ máy tính.

Hiển thị ảnh gốc và ảnh đã xử lý bằng PCA.

Lưu ảnh đã xử lý.

Phục hồi ảnh đã xử lý từ PCA.

3. Chức Năng Chi Tiết
a. Chọn Ảnh (load_image)
Chức năng này mở một hộp thoại để người dùng chọn một hình ảnh từ máy tính.

Sau khi chọn ảnh, ảnh sẽ được đọc vào bộ nhớ dưới dạng mảng numpy và chuyển đổi sang định dạng RGB để xử lý với OpenCV.

Lưu trữ ảnh gốc và kích hoạt nút "Cập Nhật" để người dùng có thể tiến hành xử lý ảnh.

b. Xử Lý Ảnh với PCA (process_image)
Dựa trên số thành phần chính (k) mà người dùng nhập vào, ứng dụng sẽ thực hiện PCA trên từng kênh màu (Red, Green, Blue) của ảnh.

PCA giảm số lượng thành phần trong mỗi kênh màu xuống còn k (số chiều nhỏ hơn).

Sau khi thực hiện PCA, ảnh được tái tạo từ các thành phần chính và hiển thị trong giao diện.

c. Lưu Ảnh (save_image)
Người dùng có thể lưu ảnh đã được tái tạo từ PCA vào máy tính bằng cách chọn vị trí lưu file thông qua một hộp thoại.

Ảnh được lưu dưới dạng PNG hoặc JPEG.

d. Khôi Phục Ảnh (restore_image)
Ứng dụng có thể phục hồi ảnh từ các thành phần chính đã bị giảm xuống trong quá trình PCA.

Chức năng này sử dụng lại các mô hình PCA đã được huấn luyện từ trước (lưu trong pca_model), và tái tạo lại ảnh ban đầu (hoặc gần giống).

e. Hiển Thị Ảnh (show_image)
Các ảnh (gốc, tái tạo, phục hồi) sẽ được hiển thị trên giao diện người dùng.

Các ảnh được resize để phù hợp với kích thước của các label trên giao diện.

4. Cấu Trúc Giao Diện
control_frame: Một khung chứa các nút điều khiển (chọn ảnh, cập nhật ảnh, lưu ảnh, phục hồi ảnh).

image_frame: Khung chứa các hình ảnh để hiển thị ảnh gốc, ảnh đã xử lý và ảnh phục hồi.

Các nút chức năng như:

Chọn Ảnh: Cho phép người dùng chọn một ảnh từ máy tính.

Cập Nhật: Thực hiện phép biến đổi PCA trên ảnh đã chọn và hiển thị ảnh đã được tái tạo.

Lưu Ảnh: Cho phép người dùng lưu ảnh đã được tái tạo.

Phục Hồi: Khôi phục lại ảnh từ các thành phần PCA.

5. Các Biến và Mảng
original_image: Mảng chứa ảnh gốc.

processed_image: Mảng chứa ảnh đã được xử lý bằng PCA.

restored_image: Mảng chứa ảnh phục hồi từ ảnh đã được giảm chiều.

pca_model: Danh sách chứa các mô hình PCA cho từng kênh màu.

6. Khởi Tạo Giao Diện và Vị Trí Cửa Sổ
Cửa sổ chính được khởi tạo với kích thước cố định và vị trí giữa màn hình, sử dụng winfo_screenwidth() và winfo_screenheight() để căn giữa cửa sổ.

Tóm Tắt Quy Trình:
Chọn ảnh: Người dùng chọn một ảnh từ máy tính.

Cập nhật ảnh: Ảnh sẽ được xử lý PCA và ảnh tái tạo sẽ được hiển thị.

Lưu ảnh: Người dùng có thể lưu ảnh đã được xử lý.

Phục hồi ảnh: Người dùng có thể phục hồi ảnh từ các thành phần PCA đã giảm chiều.

Ứng dụng này giúp người dùng hiểu và áp dụng phép biến đổi PCA vào xử lý ảnh, làm giảm số lượng thông tin trong ảnh mà vẫn giữ lại được những đặc trưng quan trọng.
