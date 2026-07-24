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
- **Hành động:** Mở API `POST /api/checkout` mà AI vừa sinh. Bấm Send. API trả về Pass. Sau đó, mở tab Tests, bôi đen đoạn `"properties": {}`.
- **Thoại:** "Tuy nhiên, AI không hoàn hảo. Nhìn qua thì request này Pass, nhưng đây là lỗi False Positive cực kỳ nghiêm trọng. AI gen JSON schema với `properties` rỗng, nghĩa là Postman sẽ chấp nhận mọi dữ liệu trả về kể cả khi Backend văng ra lỗi nội bộ. Nó tạo cho QA cảm giác ảo rằng hệ thống đang an toàn."

### Bước 4: Khắc phục bằng Prompt Request Chaining (45s)
- **Hành động:** Copy mẫu prompt "Request Chaining" thả vào AI để ép nó sửa lại API Checkout và Get Order. Import code mới vào Postman, chạy thử để thấy `order_id` được tự động gán qua API sau.
- **Thoại:** "Để khắc phục, nhóm áp dụng chiến lược 'Human-in-the-loop'. Mình dùng một câu prompt đặc trị từ thư viện, ép AI phải viết script trích xuất `order_id` lưu vào biến môi trường, tự động truyền sang API Get Order. Như các bạn thấy, giờ các API đã liên kết logic với nhau."

### Bước 5: Kết thúc (10s)
- **Thoại:** "Tổng kết lại, AI là công cụ sinh code xuất sắc, nhưng không thay thế được tư duy của QA. Tiếp theo, xin mời Nam trình bày về Contract Testing với Pact."