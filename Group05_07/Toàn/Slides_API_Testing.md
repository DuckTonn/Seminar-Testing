# Nội dung Seminar Slides (Phần API Testing bằng Postman)
**Người trình bày:** Phạm Đức Toàn
**Dự án:** EShop — API & Contract Testing

Đây là kịch bản và nội dung tóm tắt để đưa vào bản slide thuyết trình chung (Seminar Slides) của nhóm ở Tuần 3, tập trung vào công cụ Postman.

---

## Slide 1: Khái quát về API Testing & Postman

**Tiêu đề:** Tại sao lại chọn Postman cho API Testing?
**Nội dung chính:**
- Postman là công cụ phổ biến nhất hiện nay cho việc phát triển và kiểm thử API.
- Cung cấp giao diện trực quan (UI) dễ sử dụng cho cả Developer và QA.
- **Tính năng nổi bật áp dụng cho EShop:**
  - Hỗ trợ Import từ OpenAPI/Swagger Specification.
  - Quản lý biến môi trường linh hoạt (Environment Variables & Auth).
  - Viết kịch bản kiểm thử (Test Scripts) bằng JavaScript trực tiếp trong ứng dụng.
  - Chạy tự động hàng loạt API thông qua Collection Runner hoặc tích hợp Newman (CI/CD).

**Hình ảnh đi kèm (Gợi ý):** Logo Postman và màn hình UI tổng quan của Collection EShop.

---

## Slide 2: Cấu trúc bộ Test & Phạm vi bao phủ (Coverage)

**Tiêu đề:** Chiến lược kiểm thử API dự án EShop
**Nội dung chính:**
- **Quy mô:** Đã hoàn thiện kịch bản kiểm thử cho 5 luồng API cốt lõi:
  1. Authentication (`POST /api/login`)
  2. Product Listing (`GET /api/products`)
  3. Product Details (`GET /api/products/:id`)
  4. Cart Management (`POST /api/cart`)
  5. Order Checkout (`POST /api/checkout`)
- **Độ bao phủ Test Cases (Coverage):**
  - **Happy Path:** Đảm bảo luồng xử lý thành công đúng nghiệp vụ (Status 200, schema chuẩn).
  - **Negative Path:** Bắt lỗi các trường hợp token hết hạn, sai mật khẩu, tài khoản bị khóa.
  - **Edge Cases:** Xử lý các tình huống dị biệt (Body rỗng, quantity âm, ID không hợp lệ).

**Hình ảnh đi kèm (Gợi ý):** Bảng so sánh 3 loại Test Path hoặc hình ảnh thư mục Collection bên trái của Postman.

---

## Slide 3: Postman Failure Modes (Các lỗi thường gặp do Tool)

**Tiêu đề:** Điểm mù khi dùng Postman (Failure Modes)
**Nội dung chính:**
- Trong quá trình triển khai, nhóm nhận thấy Postman cũng có các "điểm mù" dễ gây hiểu lầm cho người test:
  1. **Lỗi báo sai kiểu dữ liệu:** API trả về String, nhưng logic test yêu cầu Number. Báo lỗi mơ hồ khiến QA lầm tưởng API sai nghiệp vụ.
  2. **Quên chọn Environment:** Gửi URL hoặc Token chứa chuỗi chưa được parse (VD: `{{baseUrl}}`), dẫn đến API sập nhưng mất thời gian debug sai hướng.
  3. **Silent Failure trong Test Script:** Viết sai cú pháp JavaScript, Postman bỏ qua toàn bộ script bên dưới nhưng UI không báo đỏ, vẫn hiện "Pass" cho các test trước đó (Ảo giác Pass).

**Take-away (Bài học):** 
Luôn kiểm tra kỹ biến môi trường và sử dụng công cụ linter/console.log trong Postman để debug script.

---

## Slide 4: Demo thực tế (Live Demo)

**Tiêu đề:** Demo Thực thi API Test (Postman)
**Kịch bản Demo (3 phút):**
- Trình diễn chạy `POST /api/login`, chỉ ra cách hệ thống tự động lưu Bearer Token vào Environment.
- Chạy nhanh Collection Runner toàn bộ 5 endpoints, hiển thị màn hình Pass/Fail hàng loạt.
- Minh họa một Bug thực tế bắt được bằng script (Ví dụ: ID chẵn trả về giá tiền kiểu chuỗi thay vì số nguyên).

*(Slide này chỉ mang tính chất chuyển cảnh sang Demo, sẽ để trống hình ảnh để tập trung chiếu màn hình ứng dụng).*
