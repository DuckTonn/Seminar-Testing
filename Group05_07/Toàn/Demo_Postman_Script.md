# Kịch Bản Quay Video Demo (Phần Postman - API Testing)
**Người thực hiện:** Phạm Đức Toàn
**Thời lượng dự kiến:** 2 - 3 phút
**Mục tiêu:** Show được tính năng cốt lõi của Postman, tự động hóa Authentication, bắt một Bug thực tế của hệ thống, và trình diễn một "Failure Mode" (Điểm mù của Postman)

---

## Chuẩn bị trước khi quay
1. Mở sẵn terminal chạy `node server.js` ở background.
2. Mở sẵn ứng dụng Postman, chọn đúng Workspace và mở `EShop_Collection_v2`.
3. Nhớ clear (xóa) biến `token` trong Environment đi để demo việc tự động lấy token trông cho "thật".
4. Mở sẵn phần mềm quay màn hình (OBS, Bandicam, hoặc tính năng Record của Win/Mac). Khuyên dùng thu âm giọng nói trực tiếp để video sinh động hơn.

---

## Kịch Bản Chi Tiết (Từng bước)

### Bước 1: Mở đầu và Giới thiệu (Khoảng 15s)
- **Hành động:** Trỏ chuột vào thanh Sidebar (chứa các thư mục API).
- **Thoại:** *"Chào cô và các bạn, mình là Toàn, phụ trách phần API Testing bằng Postman. Sau đây mình xin demo cách nhóm áp dụng Postman để kiểm thử tự động luồng nghiệp vụ cốt lõi của EShop, đồng thời phát hiện một số bug của hệ thống."*

### Bước 2: Demo tính năng Tự động hóa Authentication (Khoảng 30s)
- **Hành động:** 
  1. Click vào tên Collection **EShop Collection v2**, chọn tab **Variables**, chỉ cho người xem thấy biến `token` ở mục Current Value đang để trống.
  2. Mở request `1.1 Happy Path — Đăng nhập thành công` trong thư mục Authentication.
  3. Bấm sang tab **Tests** và bôi đen dòng lệnh `pm.collectionVariables.set("token", ...)`.
  4. Bấm **Send**, sau đó chỉ vào tab **Test Results** (xanh rực). Quay lại tab **Variables** của Collection để thấy token đã tự động được điền vào.
- **Thoại:** *"Điểm mạnh đầu tiên của Postman là khả năng viết script JavaScript. Ở API Login này, nhóm đã cài đặt để ngay khi login thành công, Postman sẽ tự động trích xuất Bearer Token và lưu vào Collection Variables (biến cấp Collection). Nhờ đó, tất cả các API phía sau như Giỏ hàng hay Thanh toán sẽ tự động được cấp quyền mà không cần copy/paste thủ công."*

### Bước 3: Chạy Collection Runner & Demo Bắt Bug Backend (Khoảng 1 phút)
- **Hành động:**
  1. Click dấu `...` ở tên Collection, chọn **Run Collection**.
  2. Bấm nút **Run EShop Collection v2**.
  3. Màn hình Summary chạy ra. Rất nhiều Pass (Màu xanh), nhưng lướt xuống dưới sẽ có một cái Fail (Màu đỏ) ở mục `POST /api/checkout`.
  4. Click thẳng vào cái dòng màu đỏ đó để mở chi tiết lỗi.
- **Thoại:** *"Tiếp theo, thay vì chạy tay từng cái, mình sử dụng Collection Runner để chạy hàng loạt toàn bộ kịch bản test. Như các bạn thấy, đa số là Pass. Tuy nhiên, ở API Checkout có một kịch bản bị Fail. Đây là kịch bản Negative - cố tình gửi `total_amount` rỗng. Kịch bản kỳ vọng Backend phải chặn lại và trả về lỗi 400 Bad Request, nhưng thực tế Backend lại trả về 200 OK và vẫn lưu vào database. Nhờ Postman, nhóm đã bắt được Bug thiếu Validate Data này của hệ thống (được đánh mã là Bug B4 trong báo cáo)."*

### Bước 4: Demo một "Điểm mù" (Failure Mode) của Postman (Khoảng 45s)
- **Hành động:** 
  1. Đóng Runner, mở request `GET /api/products/:id`.
  2. Ở ô URL, đổi giá trị `id` thành số `2` (số chẵn sẽ kích hoạt Bug B1 trả về giá tiền dạng chuỗi).
  3. Bấm **Send**. Bật sang tab **Test Results**, sẽ thấy báo lỗi Fail: `AssertionError: expected '28000000' to deeply equal 28000000`.
- **Thoại:** *"Cuối cùng, mình xin demo một Điểm Mù (Failure mode) rất điển hình khi dùng công cụ này: Lỗi ép kiểu ngầm định. Ở API lấy chi tiết sản phẩm, Backend có một bug là ID chẵn sẽ trả về giá tiền kiểu Chuỗi (String) thay vì Số (Number). Khi Postman so sánh, nó báo lỗi rất mơ hồ là 'expected 28 triệu bằng 28 triệu'. Tester mới rất dễ bị ảo giác tưởng logic hệ thống sai, nhưng thực chất là sai kiểu dữ liệu. Điều này đòi hỏi Tester phải dùng strict equality (so sánh chặt) để Postman bắt lỗi chính xác hơn."*

### Bước 5: Kết thúc (Khoảng 10s)
- **Hành động:** Trở lại màn hình chính của Postman.
- **Thoại:** *"Đó là phần trình diễn tính năng của Postman. Tiếp theo, xin nhường lời cho phần demo sinh kịch bản test tự động bằng trí tuệ nhân tạo AI của Khoa."*


