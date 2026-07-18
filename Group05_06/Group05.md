# Weekly Report

## General Information

- **Group ID:** Group 05
- **Project Name:** API & Contract Testing
- **Date Range:** 2026-07-12 – 2026-07-18

---

# Tasks Completed This Week

## Phạm Đức Toàn – 23127540

**Prompt đã sử dụng**

> "Dựa vào Endpoint_Agreement.md, hãy giúp tôi viết thêm các kịch bản test (Negative và Edge case) cho tất cả các Endpoints: `POST /api/login`, `GET /api/products`, `GET /api/products/:id`, `POST /api/cart`, `POST /api/checkout`. Vui lòng nâng cấp `EShop_Collection_v1.json` thành `EShop_Collection_v2.json` bao gồm toàn bộ test cases đã thống nhất (cả Happy, Negative, Edge)."

**AI đã thực hiện**

- Đọc hiểu `Endpoint_Agreement.md` và ánh xạ các test case vào Postman schema.
- Sinh toàn bộ cấu trúc file `EShop_Collection_v2.json` mở rộng từ version 1.
- Viết các Javascript test script (Assertions) cho Postman tương ứng với từng test case (ví dụ assert status code 401, 403, 200, thông báo lỗi cụ thể...).
- Tự động hóa xử lý cấu hình Auth (Bearer Token/No Auth) cho các requests hợp lệ/không hợp lệ.

**Sinh viên đã thực hiện**

- Thiết kế và chuẩn hóa các kịch bản test (Negative & Edge case) trong `Endpoint_Agreement.md` cùng đồng đội.
- Viết prompt yêu cầu AI tạo cấu trúc Postman Collection v2 dựa trên document đã chốt.
- Import `EShop_Collection_v2.json` vào Postman.
- Chạy thử toàn bộ các test cases, đối chiếu với code của backend (phát hiện một số bug như ID chẵn trả về string, endpoint checkout không validate dữ liệu).
- **Ghi chú lại các "failure mode" của Postman** :
  - _Lỗi so sánh kiểu dữ liệu ngầm định:_ Khi API trả về string nhưng assert yêu cầu number, test báo fail mà không có hint cụ thể, dễ gây nhầm lẫn là do logic API sai thay vì do kiểu dữ liệu.
  - _Quên cấu hình Environment/Token:_ Nếu biến `{{baseUrl}}` hay `{{token}}` chưa có giá trị, Postman gửi đi raw string khiến API báo lỗi (như 401 Unauthorized), làm mất thời gian debug trước khi nhận ra lỗi do biến rỗng.
  - _Silent Failure trong Test script:_ Viết sai syntax JavaScript ở tab Tests có thể khiến test không chạy hết các lệnh phía dưới nhưng Postman không báo lỗi cú pháp rõ ràng ra UI (chỉ bị skip ngầm).
- Lưu kết quả minh chứng (minh chứng bao gồm collection v2, environment file).

**Minh chứng**

- `EShop_Collection_v2.json`
- `EShop_Environment.json`
- Hình ảnh API Test:
  ![Run All](./Toàn/PostMan_RunAll.png)
  ![Negative Case](./Toàn/PostMan_Negative_Cart.png)
  ![Bug Evidence](./Toàn/PostMan_Bug_String.png)

---

## Nguyễn Nhật Nam – 23127092

**Prompt đã sử dụng**

> "Tôi đang làm dự án nhóm môn Software Testing tại HCMUS. Nhóm T06 thực hiện đề tài **API & Contract Testing** cho ứng dụng EShop. Tôi (Nam) phụ trách phần **Contract Testing bằng Pact** và **Documentation**. [...] Theo phân chia công việc, tuần 2 của tôi gồm 4 nhiệm vụ chính: Nhiệm vụ 1: Hoàn thiện Provider Verification. Nhiệm vụ 2: Ghi nhận tối thiểu 5 Contract Violations. Nhiệm vụ 3: Chuẩn bị demo Contract Testing. Nhiệm vụ 4: Ghi chú Failure Modes của Pact."

**AI đã thực hiện**

- Phân tích code `backend/server.js`, `cart.consumer.test.js` và file Pact contract JSON hiện tại.
- Viết file `provider.test.js` cấu hình Pact Verifier, xử lý xác thực (Auth) để lấy token thực tế bằng `beforeAll` và truyền vào `requestFilter`.
- Bổ sung script `"test:provider"` vào `package.json`.
- Soạn thảo `contract_violations_report.md` ghi nhận 5 vi phạm hợp đồng, trong đó bao gồm một vi phạm thực tế đang có giữa Consumer (đòi 201) và Provider (đang trả về 200).
- Viết kịch bản `demo_script.md` chi tiết từ bước khởi chạy đến khi mô phỏng lỗi.
- Soạn `failure_modes_pact.md` tổng hợp các hạn chế của Pact như Silent Schema Change, không test được performance...

**Sinh viên đã thực hiện**

- Lên ý tưởng và xác định các công việc cần thực hiện, chuẩn bị prompt chi tiết bao gồm context dự án, tech stack và output mong đợi.
- Chạy thử nghiệm file `provider.test.js` bằng lệnh `npm run test:provider`, kiểm chứng việc Pact bắt lỗi không khớp status code giữa backend và consumer.
- Đọc, rà soát và tinh chỉnh lại các tài liệu báo cáo violations, kịch bản demo và failure modes do AI tạo ra để đảm bảo khớp với ngữ cảnh thực tế của đồ án.
- Thực hành kịch bản demo mô phỏng lỗi phá vỡ hợp đồng trên máy tính cá nhân để chuẩn bị cho buổi báo cáo.

**Minh chứng**

- `contract_violations_report.md`
- `demo_script.md`
- `failure_modes_pact.md`

---

## Nguyễn Quang Đăng Khoa – 23127212

**Prompt đã sử dụng**

> "Tôi đang tự viết báo cáo phân tích Failure Modes của AI khi test hệ thống EShop. Mày hãy giải thích ngắn gọn (dùng chuẩn thuật ngữ QA/Testing) tại sao đoạn script JSON Schema do AI gen có "properties": {} và "additionalProperties": true lại gây ra lỗi False Positive cực kỳ nghiêm trọng ở API Checkout? Ngoài ra, tôi cần update thư viện Prompt của nhóm. Hãy đề xuất cho tôi 1 mẫu prompt ngắn gọn để ép AI viết test Postman có tính liên kết (Request Chaining) - cụ thể là tự động trích xuất order_id từ API Checkout truyền sang API Get Order."

**AI đã thực hiện**

- Cung cấp lời giải thích kỹ thuật chi tiết về hiện tượng False Positive, chỉ ra rằng việc để trống object sẽ khiến Postman chấp nhận mọi dữ liệu trả về (kể cả lỗi nội bộ).
- Đề xuất một đoạn mẫu prompt tập trung vào kỹ thuật "Request Chaining" và lưu biến môi trường để tái sử dụng giữa 2 API liền kề.

**Sinh viên đã thực hiện**

- Tự lên dàn ý và trực tiếp soạn thảo toàn bộ nội dung đánh giá so sánh trong file `AI_Comparison_Report.md`, dựa trên quan sát thực tế khi đối chiếu giữa AI và con người.
- Chủ động phát hiện và tổng hợp các "điểm mù" của AI (ảo giác dữ liệu, bỏ qua ràng buộc phân quyền RBAC, thiên kiến Happy-path) để đưa vào file `AI_Failure_Modes.md`.
- Tự thiết kế toàn bộ "Manual Edge Cases" nhắm vào Security, Coupon logic và Order Lifecycle để bù đắp giới hạn của AI.
- Trực tiếp refactor `prompt_library.md`, tinh chỉnh lại câu lệnh "Request Chaining" do AI gợi ý cho sát với Đặc tả hệ thống EShop và tổ chức lại thư viện cho đồng đội dễ dùng.  

**Minh chứng**

- `AI_Comparison_Report.md`
- `AI_Failure_Modes.md`
- `prompt_library_ver_13-7-2026.md`

## Huỳnh Sĩ Luân – 23127086

**Prompt đã sử dụng**

**AI đã thực hiện**

**Sinh viên đã thực hiện**

---

# AI Usage Declaration

## Phạm Đức Toàn

- **Tool name, version, and platform**: Gemini (Gemini 3.1 Pro), Antigravity IDE.
- **Access time**: 21:50 on July 16, 2026.
- **Prompts used**: "Dựa vào Endpoint_Agreement.md, hãy giúp tôi viết thêm các kịch bản test (Negative và Edge case) cho tất cả các Endpoints: `POST /api/login`, `GET /api/products`, `GET /api/products/:id`, `POST /api/cart`, `POST /api/checkout`. Vui lòng nâng cấp `EShop_Collection_v1.json` thành `EShop_Collection_v2.json` bao gồm toàn bộ test cases đã thống nhất (cả Happy, Negative, Edge)."
- **Purpose of use**: Hỗ trợ tự động hóa việc ánh xạ (mapping) các kịch bản test từ tài liệu đặc tả sang cấu trúc JSON của Postman Collection, đồng thời sinh ra các đoạn mã kiểm thử (Javascript assertions) cho các kịch bản Negative và Edge case.
- **Which content was generated by AI**: Cấu trúc JSON mở rộng của `EShop_Collection_v2.json` (bao gồm requests cho cart, checkout, và các test scripts bắt lỗi 401, 403, kiểm tra kiểu dữ liệu, v.v...).
- **Which content was done independently and how the student edited or validated it**: Sinh viên độc lập thảo luận với team để chốt `Endpoint_Agreement.md`. Sinh viên tự import collection do AI sinh ra vào Postman, chạy test thực tế trên Backend đang bật ở localhost. Sinh viên tự phân tích log để bắt bug Backend và tự rà soát các "failure mode" của Postman để đưa vào báo cáo.

## Nguyễn Nhật Nam

- **Tool name, version, and platform**: Gemini 3.1 Pro, Antigravity IDE.
- **Access time**: 15:35 on July 16, 2026.
- **Prompts used**: "Tôi đang làm dự án nhóm môn Software Testing tại HCMUS. Nhóm T06 thực hiện đề tài **API & Contract Testing** cho ứng dụng EShop. Tôi (Nam) phụ trách phần **Contract Testing bằng Pact** và **Documentation**. [...] Theo phân chia công việc, tuần 2 của tôi gồm 4 nhiệm vụ chính: Nhiệm vụ 1: Hoàn thiện Provider Verification. Nhiệm vụ 2: Ghi nhận tối thiểu 5 Contract Violations. Nhiệm vụ 3: Chuẩn bị demo Contract Testing. Nhiệm vụ 4: Ghi chú Failure Modes của Pact."
- **Purpose of use**: Hỗ trợ setup code cho Provider Verification bằng Pact, sinh các báo cáo phân tích lỗi vi phạm hợp đồng (Contract Violations) và kịch bản thuyết trình demo, cũng như giúp tìm hiểu/đúc kết các hạn chế (failure modes) của công cụ Pact.
- **Which content was generated by AI**: File test `provider.test.js`, và các tài liệu markdown: `contract_violations_report.md`, `demo_script.md`, `failure_modes_pact.md`.
- **Which content was done independently and how the student edited or validated it**: Sinh viên tự thiết kế kịch bản test, chuẩn bị tài liệu input (context, tech stack) chi tiết để prompt AI. Sinh viên chạy thực tế đoạn code verify trên máy để xác nhận Pact bắt đúng lỗi mismatch. Sinh viên tự đọc, rà soát và điều chỉnh các báo cáo tài liệu do AI tạo ra để phù hợp với ngữ cảnh nhóm.

## Nguyễn Quang Đăng Khoa

- **Tool name, version, and platform**: Gemini 3.1 Pro, Antigravity IDE.
- **Access time**: 10:37 on July 13, 2026.
- **Prompts used**: "Tôi đang tự viết báo cáo phân tích Failure Modes của AI khi test hệ thống EShop. Mày hãy giải thích ngắn gọn (dùng chuẩn thuật ngữ QA/Testing) tại sao đoạn script JSON Schema do AI gen có "properties": {} và "additionalProperties": true lại gây ra lỗi False Positive cực kỳ nghiêm trọng ở API Checkout? Ngoài ra, tôi cần update thư viện Prompt của nhóm. Hãy đề xuất cho tôi 1 mẫu prompt ngắn gọn để ép AI viết test Postman có tính liên kết (Request Chaining) - cụ thể là tự động trích xuất order_id từ API Checkout truyền sang API Get Order."
- **Purpose of use**: Tìm cách diễn đạt chuẩn xác thuật ngữ kiểm thử cho lỗi Schema và tham khảo một chiến lược thiết kế prompt mới (Request Chaining) để bổ sung vào thư viện nhóm.
- **Which content was generated by AI**: Lời giải thích cơ chế gây ra lỗi False Positive của JSON Schema và một đoạn câu prompt mẫu phục vụ việc trích xuất biến.
- **Which content was done independently and how the student edited or validated it**: Sinh viên tự phát hiện các lỗi sai của API Test, tự tay soạn thảo >90% nội dung các file báo cáo (`AI_Comparison_Report.md`, `AI_Failure_Modes.md`). Các Edge Cases về IDOR, phân quyền, logic giỏ hàng hoàn toàn do tư duy của sinh viên rà soát từ API Spec. Đoạn prompt mẫu do AI gen ra cũng được sinh viên sửa lại context cho khớp với dự án trước khi đưa vào `prompt_library.md`.

# Tasks Planned for Next Week

---

# Issues
