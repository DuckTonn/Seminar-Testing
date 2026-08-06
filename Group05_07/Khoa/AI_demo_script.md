# Kịch Bản Quay Video Demo (Phần AI Test Generation)
**Thời lượng dự kiến:** 2 - 3 phút
**Mục tiêu:** Thực hiện cách kết hợp AI tạo Boilerplate nhanh, tìm lỗi False Positive của AI và cách dùng Prompt đặc trị (Request Chaining).

---
## Chuẩn bị trước khi quay
1. Mở sẵn AI có nạp sẵn file Đặc tả API hệ thống EShop.
2. Mở Postman, chuẩn bị sẵn một Workspace trống.
3. Copy sẵn các đoạn prompt chuẩn bị dùng.

---
## Kịch Bản Chi Tiết

### Bước 1: Mở đầu & Giới thiệu (15s)
- **Thoại:** "Tiếp nối phần API Testing của Toàn, mình là Khoa sẽ demo cách nhóm áp dụng AI để tăng tốc độ viết script, đồng thời chỉ ra những điểm mù nguy hiểm khi dùng AI sinh test tự động."

### Bước 2: Khởi tạo cực nhanh bằng AI (45s)
- **Hành động:** Paste prompt Boilerplate vào AI. Lấy file JSON kết quả import vào Postman. 
- **Thoại:** "Thay vì tốn hàng giờ setup thủ công, mình chỉ mất chưa tới 1 phút dùng AI để sinh toàn bộ khung Postman Collection chuẩn v2.1.0 từ API Spec."

### Bước 3: Chỉ ra Failure Mode - False Positive (45s)
- **Hành động:** Mở API `POST /api/checkout` mà AI vừa sinh. Bấm tab Scripts cho thấy màn hình trống rỗng khi AI không gen ra script cho API này. Thêm  Bấm Send. Chỉ vào tab Test Results 1/1 (màu xanh PASS) -> Bôi đen đoạn "properties": {} trên dòng 3.
- **Thoại:** "Tuy nhiên, đây chính là điểm hạn chế cố hữu khi để AI sinh test tự động. Các bạn có thể thấy ở API Checkout này, AI chỉ tạo ra phần Body request chứ tab Scripts hoàn toàn trống rỗng. Nếu QA thiếu kinh nghiệm chỉ bấm Send, thấy Backend trả về HTTP 200 OK rồi vội kết luận API đã chạy đúng, thì hệ thống rất dễ rơi vào tình trạng False Positive. Bởi vì nếu Backend bị lỗi logic trả về data rỗng hay thiếu trường quan trọng, Postman vẫn sẽ nhận về Status 200 và báo Pass. Việc thiếu đi các bước validate Schema và dữ liệu chi tiết trong tab Scripts sẽ tạo ra cảm giác an toàn giả cực kỳ nguy hiểm cho cả đội ngũ."

### Bước 4: Khắc phục bằng Prompt Request Chaining (45s)
- **Hành động:** Copy mẫu prompt "Request Chaining" thả vào AI để ép nó sửa lại API Checkout và Get Order. Import code mới vào Postman, chạy thử để thấy `order_id` được tự động gán qua API sau.
- **Thoại:** "Để khắc phục, nhóm áp dụng chiến lược 'Human-in-the-loop'. Mình dùng một câu prompt đặc trị từ thư viện, ép AI phải viết script trích xuất `order_id` lưu vào biến môi trường, tự động truyền sang API Get Order. Như các bạn thấy, giờ các API đã liên kết logic với nhau."

### Bước 5: Kết thúc (10s)
- **Thoại:** "Tổng kết lại, AI là công cụ sinh code xuất sắc, nhưng không thay thế được tư duy của QA. Tiếp theo, xin mời Nam trình bày về Contract Testing với Pact."