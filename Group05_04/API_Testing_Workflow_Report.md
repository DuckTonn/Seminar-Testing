# Báo Cáo Quy Trình và Kế Hoạch Triển Khai Kiểm Thử API & Contract - Hệ Thống E-Shop

## 1. Nghiên Cứu Quy Trình API Testing Cho E-Shop

Hệ thống **E-Shop** là một ứng dụng thương mại điện tử giao tiếp thông qua RESTful API và được tài liệu hóa bằng chuẩn **OpenAPI**. Dựa trên kiến trúc này, quy trình API Testing cần đảm bảo ba yếu tố: tính chính xác của chức năng, độ tin cậy của luồng dữ liệu, và tính nhất quán giữa các dịch vụ (provider và consumer).

Quy trình API Testing cho E-Shop bao gồm 3 lớp chính:
1. **Kiểm thử chức năng cơ bản (Functional API Testing):** Đảm bảo các endpoint như `/auth`, `/products`, `/cart`, và `/orders` hoạt động đúng logic nghiệp vụ.
2. **Kiểm thử tăng cường bằng AI (AI-Augmented Testing):** Sử dụng LLMs để đọc OpenAPI spec, tự động sinh ra các test coverage bao gồm happy path, negative test, và phát hiện các edge case ẩn.
3. **Kiểm thử hợp đồng (Contract Testing):** Đảm bảo API provider (backend Node.js) luôn tuân thủ hợp đồng giao tiếp đã thỏa thuận với consumer (Mobile/Web frontend).

---

## 2. Đề Xuất Workflow Kiểm Thử

Dựa trên yêu cầu và tài nguyên, workflow kết hợp **Postman**, **AI (Claude/ChatGPT)**, và **Pact** được đề xuất để tối ưu hiệu suất và độ tin cậy.

### **Workflow 4 Bước Triển Khai**

1. **Khởi tạo bằng AI (AI Scaffolding):**
   - Đưa file `api_specification.md` vào AI (Claude/ChatGPT).
   - Yêu cầu AI sinh một file Postman Collection dạng JSON bao gồm: test scripts (JavaScript/Chai), cấu hình header, biến môi trường, và dữ liệu mock.
2. **Thiết kế kiểm thử thủ công (Manual Test Design):**
   - Team QA độc lập xây dựng một Postman Collection thủ công để bao phủ các business logic cốt lõi.
   - Thiết lập cấu hình **Chained-Token Authentication** (Ví dụ: gọi `/api/login`, trích xuất `Bearer Token`, lưu vào Collection Variable để tự động inject vào `/cart`, `/orders`).
3. **Phân tích và Tinh chỉnh (Diff & Refine):**
   - So sánh bộ test thủ công và bộ test do AI sinh.
   - **Xác định điểm mù:** AI thường giỏi phát hiện lỗi định dạng dữ liệu (schema testing) nhưng kém về quy tắc nghiệp vụ (business rules). Con người tập trung bổ sung các lỗ hổng về luồng logic.
   - Hợp nhất thành một **Postman Collection hoàn chỉnh**.
4. **Kiểm thử hợp đồng bảo vệ (Contract Verification với Pact):**
   - Định nghĩa consumer contracts (pact files) trên giao diện Frontend/Mobile.
   - Viết **Provider Verification tests** trên Node backend để xác nhận các API response tuân thủ đúng định dạng mà consumer đang mong đợi. Đẩy pact lên Pact Broker (nếu có) để tích hợp CI/CD.

---

## 3. Kế Hoạch Triển Khai Theo Milestone (M1–M5)

Kế hoạch triển khai bám sát các yêu cầu từ Stage S3, phân bổ cụ thể theo 5 milestone:

| Milestone | Tên Công Việc | Chi Tiết Thực Hiện | Công Cụ | Output / Deliverable |
|:---:|---|---|---|---|
| **M1** | **Xây dựng API Collection cơ bản** | Viết Postman collection bao phủ 4 endpoints cốt lõi: `POST /api/login`, `GET /products`, `POST /cart`, `POST /orders`. | Postman | File JSON Postman Collection v1.0 |
| **M2** | **Tự động hóa luồng xác thực** | Cấu hình **chained-token auth** trên Postman. Tự động lưu Bearer token vào Collection Variables khi login và truyền vào các requests sau. | Postman | Bộ test chạy tự động không cần copy/paste token. |
| **M3** | **AI Augmented Test Generation** | Đưa `api_specification.md` cho AI sinh test scaffold. Thực hiện **Diff** giữa AI collection và Manual collection. | Claude, Postman | Bảng so sánh (Diff Analysis) & Collection v2.0 hợp nhất. |
| **M4** | **Pact Provider Verification** | Thiết lập Pact trên Node backend. Viết test script verify provider chống lại một mock consumer contract. | Pact (pact-js) | Script test passing provider verification. |
| **M5** | **Document Contract Violations** | Xác định và tài liệu hóa 5 loại contract violations có thể làm gãy hệ thống (VD: đổi type của ID, xoá mandatory field, đổi endpoint path). | Markdown | Danh sách 5 Contract Violations. |

---

## 4. Phân Tích Rủi Ro (Risk Analysis)

Phân tích các rủi ro có thể xảy ra trong quá trình triển khai, kèm phương án giảm thiểu (Mitigation Strategies).

### 4.1 Rủi Ro Kỹ Thuật (Technical Risks)
- **Cấu hình Pact phức tạp:** Việc tích hợp Pact vào backend Node.js có learning curve cao và dễ lỗi cấu hình.
  - *Mitigation:* Bám sát tài liệu `pact-js` official. Dành 1-2 buổi tập trung cấu hình proof-of-concept bằng một API đơn giản (như `/products`) trước khi áp dụng toàn hệ thống.
- **Spec API bị sai lệch (Outdated Spec):** File `api_specification.md` có thể không khớp với thực tế backend đang chạy.
  - *Mitigation:* Viết test script tự động cảnh báo (schema validation) trong Postman. Thêm phần đánh giá "spec deviation" vào báo cáo M5.

### 4.2 Rủi Ro Quy Trình (Process Risks)
- **Xung đột khi hợp nhất Test (Merge Conflicts):** Khó khăn khi kết hợp bộ test thủ công và bộ test của AI.
  - *Mitigation:* Phân chia ranh giới rõ ràng: AI chuyên test validation/schema/negative, manual chuyên test business logic/integration.
- **Hạn chế thời gian:** Có quá nhiều công cụ cần nghiên cứu trong cùng một seminar.
  - *Mitigation:* Chọn Postman làm công cụ nền tảng duy nhất cho API functional, tập trung thời gian còn lại cho Pact và AI. Dùng Karate làm backup thay vì dàn trải.

### 4.3 Rủi Ro Từ AI (AI Risks)
- **AI Hallucination (Ảo giác AI):** AI sinh ra các API endpoint không tồn tại hoặc các payload không hợp lệ dựa trên dự đoán thay vì spec.
  - *Mitigation:* Tuyệt đối không chạy output của AI trực tiếp trên production. Phải có bước human-review và dry-run trên môi trường staging/mock.
- **Bỏ lỡ quy tắc nghiệp vụ (Business Rule Ignorance):** AI chỉ test cấu trúc dữ liệu, có thể cho test "Pass" dù logic sai (VD: user mua số lượng lớn hơn tồn kho).
  - *Mitigation:* Team QA tự đánh giá và chèn thủ công các "assertion" về business logic.

---

## 5. AI Disclosure (Tuyên Bố Sử Dụng AI)

Nhằm đảm bảo tính minh bạch theo tiêu chuẩn báo cáo học thuật, nhóm báo cáo chi tiết về mức độ sử dụng Trí tuệ nhân tạo (AI) trong quá trình thực hiện dự án này.

| Hạng Mục | Mô Tả Chi Tiết |
|---|---|
| **Công cụ AI đã sử dụng** | Claude (Anthropic) / ChatGPT (OpenAI) phiên bản miễn phí. |
| **Mục đích sử dụng AI** | 1. Tra cứu và tóm tắt tính năng của Postman, Karate, Pact.<br>2. Đọc file `api_specification.md` để tự động sinh test case (JSON scaffold).<br>3. Tạo dữ liệu đầu vào (adversarial payloads) cho negative test. |
| **Nội dung do AI tạo ra** | - Các đoạn mã JSON Postman Collection sơ khởi.<br>- Gợi ý về các edge cases dựa trên file OpenAPI. |
| **Kiểm chứng dữ liệu (Cross-check)** | Mọi output của AI đều được nhóm review thủ công. Kiến thức về tool licensing được đối chiếu với trang chủ chính thức (`postman.com/pricing`, `docs.pact.io`). Mã JSON sinh ra được validate trực tiếp thông qua Postman Runner. |
| **Nội dung con người (Human-authored)** | Các đánh giá về độ phù hợp công cụ, kiến trúc workflow, kế hoạch dự án, phân tích rủi ro chuyên sâu và toàn bộ mã kiểm thử hợp đồng (Pact) đều do các thành viên tự nghiên cứu và code thủ công. |
