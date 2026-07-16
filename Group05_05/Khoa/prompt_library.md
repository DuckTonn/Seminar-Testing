# Thư Viện Prompt (Prompt Library) - Phục vụ AI API Testing

Tài liệu này lưu trữ các câu lệnh (prompts) được thiết kế đặc biệt để tối ưu hóa khả năng sinh test case của AI (ChatGPT/Claude). Các prompt được chia theo từng chiến lược nhằm khắc phục những điểm yếu cố hữu của AI (thiếu Edge Cases, Schema Validation hời hợt, v.v.).

> **Lưu ý chung:** Trong tất cả các prompt dưới đây, luôn đính kèm **[Đặc tả API - api_specification.md]** ở cuối câu lệnh để AI có ngữ cảnh.

---

## 1. Prompt Khởi tạo Bộ Test Cơ Bản (Boilerplate & Happy-Path)
**Mục đích:** Dùng để sinh nhanh khung sườn Collection v2.1.0 và các luồng thành công (Happy-path) cơ bản nhất.

> "Đóng vai trò là một QA Automation Engineer Senior. Dựa vào Đặc tả API được cung cấp, hãy tạo một file JSON tuân thủ chuẩn Postman Collection Schema v2.1.0. 
> Yêu cầu:
> - Cài đặt collection variable: `baseUrl` (http://localhost:3000) và `token` (rỗng).
> - Tạo request `POST /api/login`: Test status 200, response time < 500ms, trích xuất và lưu `token` vào biến.
> - Tạo request `POST /api/cart`: Test status 200. Gắn Bearer Token.
> - Trả về ĐÚNG 1 khối mã JSON duy nhất, không giải thích."

---

## 2. Prompt Ép AI viết Schema Validation chặt chẽ 
**Mục đích:** Khắc phục tình trạng AI viết JSON Schema rỗng (`"properties": {}`). Ép AI phải định nghĩa rõ kiểu dữ liệu và các trường bắt buộc, giống như cách Manual QA soi tài liệu.

> "Tôi đang kiểm thử API `POST /api/checkout`. AI trước đó đã tạo ra JSON Schema quá hời hợt (chỉ check type: object).
> Đóng vai trò là Senior QA, hãy viết lại đoạn script Javascript trong thẻ `event` của Postman (phần Tests) cho API này. 
> Yêu cầu bắt buộc đối với JSON Schema Validation:
> - Phải định nghĩa ít nhất 3 thuộc tính (properties) dự kiến trả về khi checkout thành công (ví dụ: `order_id` (number), `status` (string), `total_amount` (number)).
> - Phải mảng `required` chứa các trường bắt buộc.
> - Phải thiết lập `"additionalProperties": false` để bắt lỗi nếu API trả về data rác.
> Chỉ trả về đoạn code Javascript, không cần giải thích."

---

## 3. Prompt Bổ sung Kịch bản Ngoại lệ (Edge Cases & Negative Tests)
**Mục đích:** Khắc phục điểm yếu lớn nhất của AI là chỉ tập trung vào luồng thành công. Prompt này ép AI phải sinh ra các test case "phá" hệ thống.

> "Hệ thống EShop cần kiểm thử các luồng ngoại lệ (Negative Tests). Đóng vai trò là Automation Tester, hãy thiết kế các request Postman Collection cho API `POST /api/cart` để xử lý các Edge Cases sau:
> 1. Thêm sản phẩm với `quantity` là số âm (VD: -2).
> 2. Thêm sản phẩm với `id` không tồn tại hoặc để trống.
> 3. Bỏ trống body request.
> 
> Trong tab Tests của mỗi request, hãy viết script (pm.test) để:
> - Đảm bảo HTTP Status Code trả về là 400 (Bad Request) hoặc 404 (Not Found), tuyệt đối không được là 200.
> - Kiểm tra xem response body có chứa chuỗi thông báo lỗi hợp lý không.
> Trả về định dạng JSON Postman Collection chứa 3 request trên."

---

## 4. Prompt Kiểm thử Bảo mật & Ủy quyền (Security & Authorization)
**Mục đích:** Yêu cầu AI kiểm tra các lỗ hổng về phân quyền (Auth) thay vì chỉ test logic tính toán bình thường.

> "Dựa vào API Specification, các API thuộc nhóm Giỏ hàng và Đơn hàng đều yêu cầu xác thực bằng Bearer Token.
> Hãy tạo một thư mục (Folder) trong Postman Collection tên là 'Security Tests' dưới dạng JSON. Trong thư mục này, tạo các request cho API `GET /api/orders/my-orders` để kiểm tra các trường hợp bảo mật sau:
> 1. **No Token:** Gửi request hoàn toàn không có header Authorization. (Kỳ vọng: Status 401 Unauthorized).
> 2. **Invalid Token:** Gửi request với Bearer Token sai định dạng hoặc đã bị chỉnh sửa. (Kỳ vọng: Status 401 hoặc 403).
> Sinh mã JSON Postman chuẩn, bao gồm cả request và code test cho các kịch bản này."
