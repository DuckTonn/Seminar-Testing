# Hướng Dẫn Sử Dụng Postman (Postman User Guide)
**Tác giả:** Phạm Đức Toàn
**Dự án:** EShop — API & Contract Testing

Tài liệu này hướng dẫn các thành viên trong nhóm và người đánh giá cách thiết lập và thực thi tự động các kịch bản kiểm thử API (API Testing) sử dụng công cụ Postman.

---

## 1. Cài đặt và Thiết lập cơ bản

### 1.1. Cài đặt Postman
- Truy cập [trang chủ Postman](https://www.postman.com/downloads/) và tải phiên bản phù hợp với hệ điều hành của bạn.
- Cài đặt và đăng nhập vào tài khoản Postman (hoặc sử dụng không cần tài khoản bằng cách click "Skip and go to the app").

### 1.2. Import Collection và Environment
- Mở Postman, chọn **Import** ở góc trái phía trên.
- Chọn file `EShop_Collection_v2.json` và `EShop_Environment.json` từ thư mục `Group05_06/Toàn/`.
- Sau khi import thành công, ở thanh bên trái (Sidebar) sẽ xuất hiện collection **EShop Collection v2**.
- Ở góc phải phía trên, click vào dropdown chọn Environment và đổi thành **EShop_Environment** (môi trường này chứa biến `{{baseUrl}}` trỏ đến `http://localhost:3000`).

---

## 2. Cấu trúc của Collection

Collection **EShop Collection v2** được tổ chức thành 4 thư mục chính, phản ánh các chức năng cốt lõi của EShop:
- **Authentication:** Chứa các API liên quan đến đăng nhập.
- **Products:** Chứa API lấy danh sách và chi tiết sản phẩm.
- **Cart:** Chứa API thêm sản phẩm vào giỏ hàng.
- **Checkout:** Chứa API đặt hàng và thanh toán.

Mỗi request bên trong đã được lập trình sẵn kịch bản kiểm thử (test scripts) trong tab **Tests** để tự động kiểm tra Status Code, Schema, và Logic dữ liệu trả về (cả trường hợp đúng - Happy Path, và trường hợp sai/cố tình bắt lỗi - Negative/Edge Path).

---

## 3. Cách chạy kiểm thử (Thực thi Test)

### 3.1. Chạy một Request đơn lẻ
1. Mở thư mục chứa API bạn muốn test (VD: `Authentication`).
2. Click chọn request `1.1 Happy Path — Đăng nhập thành công`.
3. Nhấn nút **Send** màu xanh ở góc phải.
4. Xem kết quả ở phía dưới màn hình:
   - Tab **Body:** Hiển thị dữ liệu API trả về (JSON).
   - Tab **Test Results:** Hiển thị kết quả tự động kiểm tra (VD: `PASS: Status code is 200`).

*Lưu ý: Script trong API Đăng nhập thành công đã được cài đặt để tự động lấy `token` từ response và lưu vào Environment variables, giúp các API cần xác thực (Cart, Checkout) phía sau có thể sử dụng ngay lập tức.*

### 3.2. Chạy tự động toàn bộ Collection (Collection Runner)
Thay vì chạy từng API thủ công, bạn có thể chạy toàn bộ kịch bản kiểm thử bằng một click:
1. Click vào biểu tượng dấu 3 chấm `...` bên cạnh tên collection **EShop Collection v2**.
2. Chọn **Run collection**.
3. Màn hình Runner sẽ hiện ra, liệt kê toàn bộ các requests. Bạn có thể giữ nguyên cài đặt mặc định (Iterations: 1, Delay: 0).
4. Nhấn nút **Run EShop Collection v2**.
5. Đọc bảng tóm tắt kết quả (Run Summary): Postman sẽ báo có bao nhiêu test passed (xanh) và bao nhiêu test failed (đỏ). 
   - Những test failed có thể là do API backend có lỗi (đã được ghi chú là "Bug" trong tên request).

---

## 4. Ghi chú các lỗi thường gặp (Postman Failure Modes)

> [!WARNING]
> Trong quá trình sử dụng Postman để kiểm thử API, người dùng dễ gặp phải các "ảo giác" (ảo giác test pass/fail) do chính hạn chế của công cụ này chứ không hẳn do lỗi của hệ thống API. Dưới đây là các "failure mode" đã được nhóm đúc kết:

### 4.1. Lỗi so sánh kiểu dữ liệu ngầm định (Type Mismatch)
Khi API backend trả về dữ liệu bị sai kiểu (ví dụ trả về `price` dạng chuỗi `"28000000"` thay vì số nguyên `28000000`), nếu trong tab Tests bạn dùng `pm.expect(price).to.eql(28000000);`, test sẽ báo fail với thông báo mơ hồ như *AssertionError: expected '28000000' to deeply equal 28000000*. Người mới dùng rất dễ nhầm lẫn rằng logic API tính toán sai giá tiền, chứ không nhận ra đó là lỗi ép kiểu dữ liệu.

### 4.2. Quên cấu hình Environment/Token (Unresolved Variables)
Nếu bạn quên chọn Environment (đang ở trạng thái "No Environment"), các biến như `{{baseUrl}}` hay `{{token}}` sẽ không có giá trị. Tuy nhiên, Postman **không báo lỗi ngay** mà gửi nguyên cái chuỗi chữ `{{baseUrl}}` đi làm URL. Kết quả là hệ thống trả về lỗi `404 Not Found` hoặc `401 Unauthorized`. Người test sẽ mất nhiều thời gian debug API trong khi nguyên nhân chỉ là quên chọn cấu hình môi trường.

### 4.3. Lỗi "Silent Failure" trong JavaScript (Bỏ qua lỗi ngầm)
Tab **Tests** trong Postman sử dụng mã JavaScript. Nếu bạn lỡ tay viết sai cú pháp (syntax error) hoặc gọi một hàm không tồn tại ở nửa đầu đoạn script, đoạn script đó sẽ bị crash. Tuy nhiên, **Postman không báo lỗi cú pháp đỏ rực lên màn hình UI**, mà nó chỉ âm thầm skip (bỏ qua) các câu lệnh `pm.test` bên dưới. Hệ quả là số lượng Test Cases trong tab "Test Results" bị giảm đi (ví dụ thay vì 5 thì chỉ hiện 2), và nếu 2 cái đó đều Pass, UI vẫn hiện màu xanh "Pass" đánh lừa người dùng rằng mọi thứ đều ổn định.

---
*Tài liệu này được soạn thảo vào Tuần 3, nằm trong phạm vi đồ án KTPM - Seminar API & Contract Testing.*
