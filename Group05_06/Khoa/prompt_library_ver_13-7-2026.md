# Thư Viện Prompt (Prompt Library) - Phục vụ AI API Testing

Tài liệu này lưu trữ các câu lệnh (prompts) được thiết kế đặc biệt để tối ưu hóa khả năng sinh test case của AI (ChatGPT/Gemini/Claude). Các prompt được chia theo từng chiến lược nhằm khắc phục những điểm yếu cố hữu của AI (thiếu Edge Cases, Schema Validation hời hợt, không biết nối chuỗi request, v.v.).

> **Lưu ý chung:** Trong tất cả các prompt dưới đây, luôn đính kèm **[Đặc tả API - api_specification.md]** ở cuối câu lệnh để AI có ngữ cảnh.

---

## 1. Prompt Khởi tạo Bộ Test Cơ Bản (Boilerplate & Happy-Path)
**Mục đích:** Dùng để sinh nhanh khung sườn Collection v2.1.0 và các luồng thành công (Happy-path) cơ bản nhất. Tiết kiệm thời gian setup URL, Headers, Body.

> "Đóng vai trò là một QA Automation Engineer Senior. Dựa vào Đặc tả API được cung cấp, hãy tạo một file JSON tuân thủ chuẩn Postman Collection Schema v2.1.0. 
> Yêu cầu:
> - Cài đặt collection variable: `baseUrl` (http://localhost:3000) và `token` (rỗng).
> - Tạo request `POST /api/login`: Test status 200, response time < 500ms, trích xuất và lưu `token` vào biến môi trường.
> - Tạo request `POST /api/cart`: Test status 200. Gắn Bearer Token tự động từ biến.
> - Trả về ĐÚNG 1 khối mã JSON duy nhất, không giải thích."

---

## 2. Prompt Ép AI viết Schema Validation chặt chẽ 
**Mục đích:** Khắc phục tình trạng AI viết JSON Schema rỗng (`"properties": {}`). Ép AI phải định nghĩa rõ kiểu dữ liệu, bắt lỗi rò rỉ dữ liệu và cấu hình các trường bắt buộc.

> "Tôi đang kiểm thử API `POST /api/checkout`. AI trước đó đã tạo ra JSON Schema quá hời hợt (chỉ check type: object).
> Đóng vai trò là Senior QA, hãy viết lại đoạn script Javascript trong thẻ `event` của Postman (phần Tests) cho API này. 
> Yêu cầu bắt buộc đối với JSON Schema Validation:
> - Phải định nghĩa ít nhất 3 thuộc tính (properties) dự kiến trả về khi checkout thành công (ví dụ: `order_id` (number), `message` (string)).
> - Phải có mảng `required` chứa các trường bắt buộc.
> - Phải thiết lập `"additionalProperties": false` để bắt lỗi nếu API trả về data rác (data leakage).
> Chỉ trả về đoạn code Javascript, không cần giải thích."

---

## 3. Prompt Bổ sung Kịch bản Ngoại lệ (Edge Cases & Negative Tests)
**Mục đích:** Ép AI thoát khỏi tư duy Happy-path để sinh ra các test case "phá" hệ thống.

> "Hệ thống EShop cần kiểm thử các luồng ngoại lệ (Negative Tests). Đóng vai trò là Automation Tester, hãy thiết kế các request Postman cho API `POST /api/cart` để xử lý các Edge Cases sau:
> 1. Thêm sản phẩm với `quantity` là số âm (VD: -2) hoặc bằng 0.
> 2. Thêm sản phẩm với `id` không tồn tại hoặc sai kiểu dữ liệu (String thay vì Integer).
> 3. Bỏ trống body request.
> 
> Trong tab Tests của mỗi request, hãy viết script (pm.test) để:
> - Đảm bảo HTTP Status Code trả về là 400 (Bad Request) hoặc 404 (Not Found), tuyệt đối không được là 200 hay 201.
> - Kiểm tra xem response body có chứa chuỗi thông báo lỗi hợp lý không.
> Trả về định dạng JSON Postman Collection chứa các request trên."

---

## 4. Prompt Kiểm thử Bảo mật & Phân quyền (Security & RBAC)
**Mục đích:** Yêu cầu AI kiểm tra các lỗ hổng về phân quyền (Auth) và thao tác chéo tài khoản.

> "Dựa vào API Specification, hệ thống phân tách rõ API User và API Admin. Hãy tạo một Folder 'Security Tests' (chuẩn Postman JSON). Trong thư mục này, tạo các request:
> 1. **No Token:** Gọi `GET /api/orders/my-orders` không có header Authorization (Kỳ vọng: 401).
> 2. **Invalid Token:** Gọi `GET /api/orders/my-orders` với Token hết hạn/sai định dạng (Kỳ vọng: 401 hoặc 403).
> 3. **Privilege Escalation:** Dùng biến `{{user_token}}` (của khách hàng thường) để gọi API Admin `DELETE /api/admin/users/2` (Kỳ vọng: 403 Forbidden).
> Sinh mã JSON chuẩn chứa các request và test script tương ứng."

---

## 5. Prompt Test Liên Kết Chuỗi (Request Chaining & Statefulness)
**Mục đích:** Giúp AI sinh code test có tính liên kết, kiểm tra vòng đời của dữ liệu thay vì test rời rạc từng request. Rất quan trọng khi chạy CI/CD.

> "Đóng vai trò là QA Automation Engineer. Tôi cần test luồng nghiệp vụ tạo đơn hàng liên hoàn. Hãy tạo Postman JSON cho 3 API liên tiếp: 
> 1. `POST /api/cart` (Thêm sản phẩm) 
> 2. `POST /api/checkout` (Đặt hàng) 
> 3. `GET /api/orders/:id` (Kiểm tra lại đơn hàng). 
> Yêu cầu trong tab Tests: Bắt buộc trích xuất `order_id` từ Response của API số 2, lưu vào biến Collection, và truyền tự động vào URL của API số 3. Ở API số 3, viết script assert rằng `status` của đơn hàng vừa tạo là 'pending'. Trả về JSON."

---

## 6. Prompt Sinh Dữ Liệu Động (Dynamic Data Generation)
**Mục đích:** Xử lý lỗi trùng lặp dữ liệu khi chạy test nhiều lần trên Pipeline.

> "Khi test API `POST /api/register`, việc dùng email tĩnh sẽ làm test bị fail (HTTP 409 Conflict) ở các lần chạy sau. Hãy tạo request đăng ký chuẩn Postman JSON, trong đó:
> - Tab Pre-request Script: Sử dụng `pm.variables.replaceIn('{{$randomEmail}}')` hoặc viết script JS thuần để sinh chuỗi random cho Email và Username.
> - Lưu các giá trị này vào biến và truyền vào Body Request dưới dạng `{{randomEmail}}`.
> - Tab Tests: Assert status 200 hoặc 201."
