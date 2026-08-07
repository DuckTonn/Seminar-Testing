# Kịch Bản Quay Video Demo (Phần Postman - API Testing)
**Người thực hiện:** Phạm Đức Toàn
**Thời lượng dự kiến:** 2 - 3 phút
**Mục tiêu:** Show được tính năng cốt lõi của Postman, tự động hóa Authentication, bắt các Bug thực tế của hệ thống bằng bộ test v3, và trình diễn một "Failure Mode" (Điểm mù của Postman)

---

## Chuẩn bị trước khi quay
1. Mở sẵn terminal chạy `node server.js` ở background.
2. Mở sẵn ứng dụng Postman, chọn đúng Workspace và mở **EShop_Collection_v3**. (Lưu ý: Bắt buộc dùng v3).
3. Nhớ clear (xóa) biến `token` trong Environment/Collection Variables đi để demo việc tự động lấy token trông cho "thật".
4. Mở sẵn phần mềm quay màn hình (OBS, Bandicam, hoặc tính năng Record của Win/Mac). Khuyên dùng thu âm giọng nói trực tiếp để video sinh động hơn.

---

## Kịch Bản Chi Tiết (Từng bước)

### Bước 1: Mở đầu và Giới thiệu (Khoảng 15s)
- **Hành động:** Trỏ chuột vào thanh Sidebar (chứa các thư mục API).
- **Thoại:** *"Chào cô và các bạn, mình là Toàn, phụ trách phần API Testing bằng Postman. Sau đây mình xin demo cách nhóm áp dụng Postman để kiểm thử tự động luồng nghiệp vụ cốt lõi của EShop, đồng thời dùng bộ test chặt chẽ để phát hiện các lỗ hổng của Backend."*

### Bước 2: Demo tính năng Tự động hóa Authentication (Khoảng 30s)
- **Hành động:** 
  1. Click vào tên Collection **EShop Collection v3**, chọn tab **Variables**, chỉ cho người xem thấy biến `token` ở mục Current Value đang để trống.
  2. Mở request `1.1 Happy Path — Đăng nhập thành công` trong thư mục Authentication.
  3. Bấm sang tab **Tests** và bôi đen dòng lệnh `pm.collectionVariables.set("token", ...)`.
  4. Bấm **Send**, sau đó chỉ vào tab **Test Results** (xanh rực). Quay lại tab **Variables** của Collection để thấy token đã tự động được điền vào.
- **Thoại:** *"Điểm mạnh đầu tiên của Postman là khả năng viết script JavaScript. Ở API Login này, nhóm đã cài đặt để ngay khi login thành công, Postman sẽ tự động trích xuất Bearer Token và lưu vào Collection Variables. Nhờ đó, tất cả các API phía sau như Giỏ hàng hay Thanh toán sẽ tự động được cấp quyền mà không cần copy/paste token thủ công."*

### Bước 3: Chạy Collection Runner & Bắt Bug Hệ Thống (Khoảng 1 phút)
- **Hành động:**
  1. Click dấu `...` ở tên Collection, chọn **Run Collection**.
  2. Bấm nút **Run EShop Collection v3**.
  3. Màn hình Summary chạy ra. Dừng lại ở các test case bị **ĐỎ (FAIL)** (ví dụ trong thư mục Cart và Checkout như thêm số lượng âm, thiếu field).
  4. Click mở rộng một báo cáo lỗi màu đỏ để người xem thấy dòng chữ `AssertionError: expected response to have status code 400 but got 200`.
- **Thoại:** *"Bây giờ mình sử dụng Collection Runner để chạy hàng loạt toàn bộ 28 kịch bản. Như các bạn thấy, bên cạnh các case màu xanh, có khá nhiều case bị báo ĐỎ (FAIL). Đừng hoảng sợ, đây là chủ đích của nhóm! Nhóm đã viết các test case Edge cases rất chặt chẽ, yêu cầu Backend phải trả về lỗi 400 Bad Request khi truyền vào số lượng âm hoặc giỏ hàng rỗng. Tuy nhiên Backend lại đang bị lỗi thiếu Data Validation nên vẫn trả về 200 OK. Bộ test Postman v3 đã phát huy tác dụng và tóm gọn được các lỗ hổng này!"*

### Bước 4: Demo một "Điểm mù" (Failure Mode) của Postman (Khoảng 45s)
- **Hành động:** 
  1. Đóng Runner, mở request `3.1 Happy Path — Xem Chi Tiết Sản Phẩm (ID lẻ)`.
  2. Ở ô URL, đổi giá trị `id` từ `1` thành số `2` (số chẵn sẽ kích hoạt Bug Backend trả về giá tiền dạng chuỗi).
  3. Bật sang tab **Tests**, tạm thời comment dòng check ID để tránh nhiễu. Sửa dòng check price thành: `pm.expect(jsonData.price).to.eql(28000000);` (kiểu số).
  4. Bấm **Send**. Bật sang tab **Test Results**, sẽ thấy báo lỗi Fail ở test price: `AssertionError: expected '28000000' to deeply equal 28000000`. Bôi đen 2 số này cho khán giả thấy sự khác biệt nhỏ (dấu nháy đơn).
- **Thoại:** *"Cuối cùng, chiếu theo yêu cầu của đề tài, mình xin demo một Điểm Mù (Failure mode) rất điển hình của Postman: Lỗi hiển thị ép kiểu. Khi Backend trả về giá tiền kiểu Chuỗi thay vì kiểu Số, lệnh so sánh .eql() báo lỗi rất mơ hồ là 'expected 28 triệu bằng 28 triệu'. Nhìn thoáng qua Tester rất dễ ảo giác tưởng hệ thống tính toán sai logic, nhưng thực chất là sai kiểu dữ liệu do khác biệt ở dấu nháy đơn. Điều này đòi hỏi Tester phải dùng strict equality hoặc hàm kiểm tra type rõ ràng (.to.be.a('number')) mới bắt lỗi minh bạch được."*

### Bước 5: Kết thúc (Khoảng 10s)
- **Hành động:** Trở lại màn hình chính của Postman.
- **Thoại:** *"Đó là phần trình diễn API Testing bằng Postman. Tiếp theo, xin nhường lời cho Khoa để demo phần tự động sinh kịch bản test bằng AI."*


