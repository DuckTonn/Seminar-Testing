# Thư Viện Prompt Chuẩn Hóa (Prompt Library) — AI API Testing

> **Nguyên tắc sử dụng:**
> 1. **Đính kèm ngữ cảnh:** Luôn đính kèm toàn bộ nội dung **Tài liệu Đặc tả API (API Specification)** vào cuối mỗi prompt. Không có ngữ cảnh, AI sẽ bịa đặt dữ liệu.
> 2. **Sử dụng tuần tự:** Các prompt dưới đây được thiết kế theo luồng **chuỗi mắt xích** (prompt chain). Đầu ra của prompt trước là đầu vào chỉnh sửa của prompt sau.
> 3. **AI là điểm khởi đầu, không phải điểm cuối:** Mọi output từ AI đều phải qua bước review thủ công bởi QA Engineer trước khi đưa vào Pipeline.

---

## Prompt 1 — Khởi tạo Bộ Test Toàn diện (Boilerplate & Coverage)

**Mục đích:** Sinh ra khung sườn Postman Collection chuẩn từ API Specification. Đây là bước đầu tiên, đặt nền móng cho toàn bộ quy trình kiểm thử.

**Khi nào dùng:** Khi bắt đầu một dự án mới và cần tạo nhanh bộ test skeleton bao phủ toàn bộ API.

**Đầu ra kỳ vọng:** Một file Postman Collection JSON v2.1.0 hợp lệ, sẵn sàng import.

---

```
Đóng vai trò Senior QA Automation Engineer.

Dựa trên Tài liệu Đặc tả API được đính kèm bên dưới, hãy tạo một file JSON tuân thủ chuẩn Postman Collection Schema v2.1.0 bao phủ toàn bộ hệ thống.

Yêu cầu bắt buộc:
- Cài đặt collection variable: `baseUrl` (URL gốc của hệ thống) và `token` (để trống, sẽ được điền tự động).
- Tạo request đầy đủ cho TẤT CẢ nhóm nghiệp vụ được mô tả trong đặc tả: mỗi nhóm chức năng phải có ít nhất một request đại diện.
- Với request đăng nhập: viết script trong tab Tests để trích xuất JWT token từ response và lưu vào biến môi trường `token`.
- Với mọi request yêu cầu xác thực: gắn `Authorization: Bearer {{token}}` vào header tự động.
- Mỗi request phải có test script kiểm tra HTTP Status Code phù hợp bằng cú pháp `pm.test`.
- Nếu collection quá dài, chia thành các folder theo nhóm nghiệp vụ nhưng TUYỆT ĐỐI không được lược bỏ endpoint.
- Trả về DUY NHẤT một khối JSON hợp lệ, không giải thích, không văn bản thừa.

[Dán toàn bộ nội dung api_specification.md tại đây]
```

---

## Prompt 2 — Chặt chẽ Schema Validation (Chống False Positive)

**Mục đích:** Khắc phục điểm mù nghiêm trọng nhất của AI: sinh ra JSON Schema rỗng hoặc lỏng lẻo. Prompt này ép AI phải định nghĩa cấu trúc dữ liệu trả về một cách chặt chẽ, ngăn chặn hiện tượng False Positive.

**Khi nào dùng:** Sau Prompt 1, áp dụng cho tất cả các endpoint có response body quan trọng (đặc biệt là các luồng liên quan đến tiền tệ, dữ liệu người dùng, hoặc vòng đời đơn hàng).

**Đầu ra kỳ vọng:** Đoạn JavaScript test script chuẩn để paste vào tab Tests của Postman.

---

```
Tôi vừa nhận được một Postman Collection do AI sinh ra. Trong tab Tests của các request quan trọng, AI đã tạo ra JSON Schema quá sơ sài — schema chỉ kiểm tra type là object mà không định nghĩa bất kỳ trường dữ liệu cụ thể nào, dẫn đến tình trạng False Positive nguy hiểm.

Đóng vai trò Senior QA Engineer, hãy viết lại đoạn JavaScript test script (dùng trong tab Tests của Postman) cho một API có response body phức tạp.

Yêu cầu bắt buộc về JSON Schema Validation:
- Phân tích response body dựa trên mô tả trong đặc tả API để xác định các trường dữ liệu thực sự được trả về.
- Phải định nghĩa ít nhất 3 thuộc tính (`properties`) với đúng kiểu dữ liệu (string, number, boolean, array, object).
- Phải có mảng `required` liệt kê tất cả các trường bắt buộc.
- Phải thiết lập `"additionalProperties": false` để bắt lỗi nếu server trả về dữ liệu dư thừa (Data Leakage).
- Ngoài schema validation, bổ sung thêm assertion kiểm tra kiểu dữ liệu của từng trường bằng `pm.expect(...).to.be.a(...)`.
- Chỉ trả về đoạn code JavaScript, không cần giải thích.

[Dán mô tả endpoint và cấu trúc response mong đợi từ api_specification.md tại đây]
```

**Ví dụ request đặt hàng:**

```
Tôi vừa nhận được một Postman Collection do AI sinh ra. Trong tab Tests của các request quan trọng, AI đã tạo ra JSON Schema quá sơ sài — schema chỉ kiểm tra type là object mà không định nghĩa bất kỳ trường dữ liệu cụ thể nào, dẫn đến tình trạng False Positive nguy hiểm.

Đóng vai trò Senior QA Engineer, hãy viết lại đoạn JavaScript test script (dùng trong tab Tests của Postman) cho `/api/checkout`:

Yêu cầu bắt buộc về JSON Schema Validation:
- Phân tích và định nghĩa chính xác ít nhất 3 thuộc tính phản hồi dự kiến của đơn hàng (Ví dụ: order_id, total_amount, status, message).
- Thiết lập mảng `required` chứa các trường bắt buộc và cấu hình `"additionalProperties": false` để chặn dữ liệu rác.
- Thêm assertion kiểm tra kiểu dữ liệu cho từng trường bằng `pm.expect(...).to.be.a(...)`.
- Chỉ trả về đoạn code JavaScript, không cần giải thích.

[Dán mô tả endpoint và cấu trúc response mong đợi từ api_specification.md tại đây]
```

---

## Prompt 3 — Bổ sung Kịch bản Ngoại lệ & Bảo mật (Negative & Security Tests)

**Mục đích:** AI có thiên kiến Happy-path và bỏ sót hoàn toàn các kịch bản phân quyền (RBAC). Prompt này ép AI thoát khỏi tư duy luồng chuẩn để sinh test case kiểm tra các tình huống dị biệt và lỗ hổng bảo mật.

**Khi nào dùng:** Sau khi đã có bộ Happy-path tests từ Prompt 1. Áp dụng cho các nhóm endpoint có liên quan đến dữ liệu nhạy cảm, phân quyền người dùng, hoặc nghiệp vụ có điều kiện ràng buộc.

**Đầu ra kỳ vọng:** Các request Postman mới (dạng JSON) cho một folder "Negative & Security Tests".

---

```
Đóng vai trò Penetration Tester kiêm QA Automation Engineer.

Tôi cần bổ sung các kịch bản kiểm thử ngoại lệ và bảo mật cho hệ thống mà tôi đang test. Dựa trên Đặc tả API được đính kèm, hãy tạo Postman JSON cho một folder tên là "Negative & Security Tests" bao gồm các nhóm kịch bản sau:

Nhóm 1 — Xác thực & Phân quyền (Authentication & RBAC):
- Gọi API yêu cầu xác thực mà không gửi header Authorization (Kỳ vọng: 401 Unauthorized).
- Gọi API với Token sai chữ ký hoặc đã hết hạn (Kỳ vọng: 401 hoặc 403).
- Sử dụng token của tài khoản có quyền thấp để gọi các API dành riêng cho tài khoản quản trị viên (Kỳ vọng: 403 Forbidden).

Nhóm 2 — Kiểm thử Dữ liệu Đầu vào (Input Validation):
- Gửi request với body hoàn toàn trống rỗng cho các API POST/PUT (Kỳ vọng: 400 Bad Request).
- Gửi request với các trường có kiểu dữ liệu sai (ví dụ: truyền chuỗi ký tự vào trường yêu cầu số nguyên) (Kỳ vọng: 400 Bad Request).
- Kiểm thử các giá trị biên: số âm, số 0, chuỗi rỗng cho các trường số lượng hay giá trị tiền tệ (Kỳ vọng: 400 Bad Request).

Nhóm 3 — Kiểm thử Ràng buộc Nghiệp vụ (Business Rule Validation):
- Thiết kế kịch bản vi phạm các quy tắc kinh doanh được mô tả rõ trong đặc tả (ví dụ: thực hiện hành động khi chưa đủ điều kiện theo quy định).

Yêu cầu kỹ thuật trong tab Tests của MỖI request:
- Viết pm.test kiểm tra HTTP Status Code chính xác theo kỳ vọng.
- Viết thêm pm.test kiểm tra response body chứa thông báo lỗi hợp lý (không được trả về 200 OK giả).

Trả về DUY NHẤT một khối JSON chuẩn Postman Collection, không giải thích.

[Dán toàn bộ nội dung api_specification.md tại đây]
```

**Ví dụ về các API quản lý người dùng (`GET /api/admin/users` và `DELETE /api/admin/users/:id`):**

```
Đóng vai trò Penetration Tester kiêm QA Automation Engineer. Hãy tạo Postman JSON cho folder "Negative & Security Tests" tập trung DUY NHẤT vào các API Dành cho Admin (cụ thể: GET /api/admin/users và DELETE /api/admin/users/:id):

Nhóm 1 — Xác thực (Authentication):
- Gọi API danh sách người dùng mà không gửi header Authorization (Kỳ vọng: 401 Unauthorized).

Nhóm 2 — Phân quyền (RBAC):
- Sử dụng token của một tài khoản User bình thường (không có quyền Admin) để gọi API lấy danh sách người dùng hoặc xóa người dùng (Kỳ vọng: 403 Forbidden).

Nhóm 3 — Input Validation:
- Gửi request Xóa người dùng (DELETE /api/admin/users/:id) với ID không hợp lệ (ví dụ: truyền chuỗi ký tự "abc" thay vì ID số) (Kỳ vọng: 400 Bad Request).

Yêu cầu kỹ thuật:
- Mọi request phải có `pm.test` kiểm tra HTTP Status Code chính xác theo kỳ vọng.
- Trả về DUY NHẤT một khối JSON chuẩn Postman Collection v2.1.0, không giải thích.

Trả về DUY NHẤT một khối JSON chuẩn Postman Collection, không giải thích.

[Dán toàn bộ nội dung api_specification.md tại đây]
```

---

## Prompt 4 — Kiểm thử Chuỗi Liên kết & Dữ liệu Động (Request Chaining & Dynamic Data)

**Mục đích:** Sinh test case kiểm tra **vòng đời dữ liệu** (data lifecycle) xuyên suốt nhiều API liên tiếp, thay vì kiểm tra từng request rời rạc. Đồng thời khắc phục lỗi dữ liệu tĩnh (hardcoded data) gây Conflict 409 khi chạy CI/CD lặp lại nhiều lần.

**Khi nào dùng:** Khi cần kiểm thử một luồng nghiệp vụ đầu-cuối (end-to-end flow) có nhiều bước phụ thuộc nhau (ví dụ: đăng ký → đăng nhập → thực hiện giao dịch → kiểm tra kết quả).

**Đầu ra kỳ vọng:** Một folder Postman chứa chuỗi request liên kết với nhau qua biến môi trường và pre-request script sinh dữ liệu động.

---

```
Đóng vai trò Senior QA Automation Engineer chuyên về test automation cho CI/CD pipeline.

Tôi cần kiểm thử một luồng nghiệp vụ đầu-cuối (end-to-end flow) của hệ thống. Dựa trên Đặc tả API được đính kèm, hãy chọn một luồng quan trọng nhất (thường là luồng tạo và xác nhận dữ liệu) và tạo Postman JSON cho chuỗi request liên tiếp.

Yêu cầu kỹ thuật cực kỳ nghiêm ngặt:

Về Dữ liệu Động (Dynamic Data):
- Tab Pre-request Script của request đầu tiên: viết JavaScript để sinh dữ liệu ngẫu nhiên (email, username, mã định danh) thay thế cho mọi giá trị hardcoded. Sử dụng pm.variables.replaceIn('{{$randomEmail}}') hoặc logic tự sinh chuỗi random.
- Lưu các giá trị sinh ra vào biến môi trường để các request sau tái sử dụng.

Về Request Chaining (Liên kết Chuỗi):
- Tab Tests của mỗi request trung gian: phân tích JSON response, tìm trường định danh quan trọng (ID, token, mã xác nhận...) và lưu vào biến môi trường bằng pm.environment.set("tên_biến", giá_trị). Nếu trường không tồn tại, throw error rõ ràng.
- Tab Params / URL của request tiếp theo: sử dụng {{tên_biến}} để tự động truyền giá trị đã lưu.

Về Assertion cuối chuỗi:
- Request cuối cùng: viết script kiểm tra trạng thái của dữ liệu vừa tạo ra thông qua một API GET/READ để xác nhận backend đã ghi dữ liệu đúng vào database (không chỉ nhận 200 OK là tin ngay).

Trả về DUY NHẤT một khối JSON chuẩn Postman Collection v2.1.0, không giải thích.

[Dán toàn bộ nội dung api_specification.md tại đây]
```

**Ví dụ về luồng Đăng ký -> Đăng nhập -> Đặt hàng:**

```
Đóng vai trò Senior QA Automation Engineer chuyên về test automation cho CI/CD pipeline. Hãy tạo Postman JSON cho một chuỗi request liên tiếp xuyên suốt luồng: Đăng ký (POST /api/register) -> Đăng nhập (POST /api/login) -> Đặt hàng (POST /api/checkout).

Yêu cầu kỹ thuật nghiêm ngặt:
1. Request Đăng ký (POST /api/register):
- Tab Pre-request Script: Viết JavaScript sinh dữ liệu ngẫu nhiên cho `email` (ví dụ: dùng Date.now() hoặc $randomEmail) và lưu vào biến môi trường để tránh lỗi 409 Conflict ở các lần chạy sau.
- Dùng biến môi trường này trong Body request.

2. Request Đăng nhập (POST /api/login):
- Sử dụng email vừa được tạo từ biến môi trường.
- Tab Tests: Phân tích JSON response, trích xuất chuỗi JWT `token` và lưu vào biến môi trường bằng `pm.environment.set("token", ...)`.

3. Request Đặt hàng (POST /api/checkout):
- Header: Tự động truyền `Authorization: Bearer {{token}}`.
- Body: Truyền dữ liệu hợp lệ (total_amount, shipping_address).
- Tab Tests: Viết script kiểm tra đơn hàng tạo thành công (Status 200/201).

Trả về DUY NHẤT một khối JSON chuẩn Postman Collection v2.1.0, không giải thích.
```

---

## Tổng kết: Luồng sử dụng Prompt Chain

Thứ tự khuyến nghị:

```
Prompt 1  →  Prompt 2  →  Prompt 3  →  Prompt 4
(Khởi tạo)   (Siết Schema) (Negative/Security)  (Chaining/Dynamic)
```

| Prompt | Khắc phục điểm mù AI | Kết quả thu được |
|:---:|:---|:---|
| **P1** | Bỏ sót endpoint, không có structure | Collection skeleton đầy đủ |
| **P2** | Schema rỗng → False Positive | Test script chặt chẽ, chống data leak |
| **P3** | Happy-path bias, bỏ qua RBAC | Negative & security test cases |
| **P4** | Hardcoded data → CI/CD fail, test rời rạc | Chuỗi liên kết, chạy lặp lại an toàn |

> **Lưu ý cuối — Human-in-the-loop là bắt buộc:** Sau khi thu thập đủ output từ 4 prompt, QA Engineer phải thực hiện bước **Review thủ công** — đối chiếu với đặc tả API, bổ sung các edge case từ tư duy nghiệp vụ, rồi mới đưa collection vào Newman/CI pipeline.
