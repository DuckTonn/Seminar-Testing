# Hướng dẫn sinh kịch bản Test bằng AI

Mục này cung cấp hướng dẫn chuyên sâu về việc tích hợp các mô hình AI (ChatGPT, Gemini, Claude) vào quy trình kiểm thử API tự động. Mục tiêu không phải là để AI thay thế QA, mà sử dụng AI như một công cụ tối ưu hóa tốc độ khởi tạo (Boilerplate Generator), kết hợp với quy trình kiểm duyệt chặt chẽ nhằm tối đa hóa hiệu suất CI/CD.

## 1. Quy trình sinh kịch bản tiêu chuẩn (Human-in-the-loop)
Để AI có thể sinh ra các script Postman chất lượng cao, đúng định dạng và có tính liên kết, kỹ sư kiểm thử cần tuân thủ 4 bước sau:

**Bước 1: Chuẩn bị Ngữ cảnh**
- Tuyệt đối không yêu cầu AI viết test bằng các câu lệnh chung chung.
- Cần cung cấp toàn bộ nội dung của **Tài liệu Đặc tả API (API Specification)** cho AI. Điều này giúp AI hiểu rõ các Endpoint, cấu trúc Body (JSON), Header yêu cầu (ví dụ: `Authorization: Bearer <token>`) và các mã lỗi HTTP dự kiến.

**Bước 2: Sử dụng Prompt Engineering**
- Sử dụng các mẫu câu lệnh đã được chuẩn hóa trong file thư viện `prompt_library.md`.
- Phân chia nhỏ yêu cầu: Thay vì bắt AI viết toàn bộ hệ thống cùng lúc, hãy yêu cầu theo từng cụm nghiệp vụ. Ví dụ: Cụm Authentication (`/api/login`, `/api/register`), cụm Order Lifecycle (`/api/cart` -> `/api/checkout` -> `/api/orders/:id`).

**Bước 3: Trích xuất và Tích hợp**
- Yêu cầu AI xuất kết quả dưới dạng chuỗi JSON tuân thủ chuẩn `Postman Collection Schema v2.1.0`.
- Sao chép khối JSON, lưu thành file `.json` và sử dụng tính năng **Import** của Postman để đưa vào Workspace mà không cần thiết lập thủ công.

**Bước 4: Review & Refactor**
- Kỹ sư QA trực tiếp kiểm tra lại các kịch bản. AI thường làm tốt phần thiết lập API skeleton (URL, Headers, Payload), nhưng phần Script Validation (`pm.test`) và các rủi ro bảo mật cần được kỹ sư trực tiếp bổ sung và tinh chỉnh lại.

## 2. Nhận diện và Khắc phục các "Điểm mù" của AI (AI Failure Modes)
Trong quá trình sinh code, AI thường mắc phải các lỗi luận lý ngầm. Việc không nhận diện được các "điểm mù" này sẽ dẫn đến hiện tượng **False Positive** (kiểm thử báo Pass nhưng thực tế hệ thống có lỗi). Khi sử dụng AI, QA Engineer đặc biệt phải rà soát các trường hợp sau:

**1. Lỗi Schema Validation rỗng (False Positives)**
- **Hiện tượng:** AI thường sinh các đoạn code kiểm tra cấu trúc JSON (Schema) rất hời hợt. Nó thường khởi tạo mảng `"properties": {}` và đặt `"additionalProperties": true`.
- **Hậu quả:** Postman sẽ chấp nhận mọi dữ liệu trả về từ Server. Dù API trả về object rỗng `{}` hay chuỗi HTML chứa lỗi nội bộ (Internal Server Error), Test Case vẫn hiện màu xanh (Pass).
- **Biện pháp:** Qua prompt, ép AI phải khai báo chi tiết các trường bắt buộc (`required`), định nghĩa rõ ràng Data Type (String, Integer) và thiết lập `"additionalProperties": false` để chặn lỗi Data Leakage.

**2. Bỏ qua Ràng buộc Nghiệp vụ (Data Hallucination)**
- **Hiện tượng:** AI sinh ra payload đúng cú pháp JSON chuẩn nhưng bỏ qua hoàn toàn các ràng buộc logic kinh doanh (Business Rules).
- **Ví dụ thực tế:** Đối với API áp dụng mã giảm giá (`POST /api/apply-coupon`), AI có thể tạo request gửi mã thành công nhưng hoàn toàn bỏ qua việc viết test case kiểm tra điều kiện `min_order_amount` (giá trị đơn hàng tối thiểu) hoặc `max_uses_per_user` (số lần dùng tối đa).
- **Biện pháp:** Kỹ sư QA phải tự thiết kế và bổ sung các "Manual Edge Cases" để kiểm thử Boundary values và các luồng thất bại.

**3. Lỗ hổng Tư duy Phân quyền (RBAC Failure)**
- **Hiện tượng:** AI mặc định sử dụng chung một biến `{{token}}` cho mọi request và ngầm định rằng mọi API đều được gọi ở trạng thái ủy quyền cao nhất (Happy-path).
- **Ví dụ thực tế:** AI gần như sẽ bỏ sót việc thiết kế test case dùng tài khoản User thông thường để gọi thử API dành riêng cho Admin, chẳng hạn như API xóa người dùng (`DELETE /api/admin/users/:id`) hoặc lấy danh sách toàn bộ đơn hàng (`GET /api/admin/orders`).
- **Biện pháp:** Yêu cầu AI tạo riêng một Folder "Security Tests", chỉ định viết các kịch bản: Broken Access Control, Privilege Escalation (Leo thang đặc quyền), và IDOR.

**4. Thiên kiến Happy-path và Dữ liệu tĩnh (Static Data)**
- **Hiện tượng:** AI thích viết các Test Case thành công và thường hardcode (gắn cứng) dữ liệu tĩnh (Ví dụ: `email: "test@domain.com"`).
- **Hậu quả:** Khi đưa Collection vào chạy tự động trên CI/CD Pipeline (như GitHub Actions), lần chạy thứ 2 sẽ lập tức báo lỗi Conflict (HTTP 409) do trùng lặp dữ liệu trong Database.
- **Biện pháp:** Bắt buộc AI sử dụng các biến động (Dynamic Data) của Postman như `{{$randomEmail}}`, `{{$randomUUID}}` trong tab Pre-request Script.