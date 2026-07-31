**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**

**CS423 / CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026\)**

**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# **AI Audit Report — Mẫu 5 mục cho mỗi Artifact**

*Phụ lục bắt buộc đính kèm cho mọi bài tập có dùng AI (HW\#01–HW\#06, Seminar).*

*Tài liệu được biên soạn lại từ Med Kharbach, PhD (2026) — Mẫu Chính sách Sử dụng AI cho Giáo dục Đại học. Giấy phép CC BY-NC-SA 4.0. Phiên bản này được FIT@HCMUS điều chỉnh cho môn CS423 / CSC15003 Kiểm chứng Phần mềm.*

## **1\. Thông tin Sinh viên**

| Mục | Giá trị |
| :---- | :---- |
| **Họ tên sinh viên (in hoa):** | NHÓM 05 (Đại diện: PHẠM ĐỨC TOÀN) |
| **MSSV:** | 23127540 |
| **Lớp / Khoá:** | K23 |
| **Mã bài tập (ví dụ HW\#00, HW\#02):** |  |
| **Ngày làm bài:** | 2026-07-31 |
| **Công cụ AI đã dùng:** | Gemini 3.1 Pro, Gemini 3.5 Flash |
| **Công cụ AI đã dùng:** | \[ \] Có  \[ \] Không |

## **2\. Hướng dẫn (đọc trước khi điền)**

* Thêm 1 hàng cho mỗi artifact AI sinh (test case, script, checklist, OpenAPI spec, JMeter plan…).  
* Dán nguyên văn prompt — KHÔNG paraphrase.  
* Dán nguyên văn output AI (hoặc kèm screenshot có chú thích trong báo cáo).  
* Gắn nhãn: VALID / INVALID / INCOMPLETE.  
* Lý do phải dẫn chiếu slide, mục ISTQB, hoặc RFC kỹ thuật.  
* Hiển thị bản sửa với phần thay đổi được tô sáng.  
* Hàng mẫu in nghiêng — thay trước khi nộp.

## **3\. Bảng Audit — 1 hàng / artifact**

| (1) Prompt \+ Công cụ | (2) Output AI | (3) Verdict | (4) Lý do (ISTQB) | (5) Bản SV sửa |
| :---- | :---- | :---- | :---- | :---- |
| **Artifact #1 (W1)** | **Tool: Gemini 3.1 Pro**<br>Prompt: *"Hãy nghiên cứu quy trình API Testing cho hệ thống E-Shop, đề xuất workflow phù hợp, xây dựng kế hoạch triển khai theo các milestone (M1–M5) và viết phần Risk Analysis (bao gồm rủi ro kỹ thuật, quy trình, và AI) theo chuẩn báo cáo học thuật/chuyên nghiệp. Xuất toàn bộ kết quả với cấu trúc rõ ràng, sử dụng tiêu đề (#, ##, ###), bảng, danh sách."* | Đề xuất quy trình API Testing 3 lớp, Workflow 4 bước, kế hoạch M1-M5 và Mitigation Strategies. (Xem file API_Testing_Workflow_Report.md) | VALID | Cấu trúc bao phủ đủ các pha trong STLC (ISTQB FL §1.4). Các rủi ro được phân tích chuẩn xác. | Giữ nguyên dàn ý, <mark>điều chỉnh tên công cụ thành Postman, Pact</mark> cho đúng project. |
| **Artifact #2 (W2)** | **Tool: Gemini 3.1 Pro**<br>Prompt: *"Dựa trên file đặc tả API (api_specification.md) của dự án EShop, hãy giúp tôi khởi tạo file Postman Collection (v1) và Environment. Yêu cầu viết API Test bằng Javascript cho 3 API chính: POST /api/login, GET /api/products, và GET /api/products/:id bao gồm cả Test Happy Path và thiết lập Authentication bằng JWT (tự động lưu Token vào Collection Variables)."* | Sinh toàn bộ cấu trúc file JSON Postman Collection v1 và file Environment. Khởi tạo code JS kiểm tra status code. | INCOMPLETE | Dùng sai scope biến môi trường (vi phạm nguyên tắc quản lý môi trường độc lập, ISTQB FL §3.1 Test Environment). | Sửa script set token thành `<mark>pm.collectionVariables.set("token", ...)</mark>`. |
| **Artifact #3 (W2)** | **Tool: Gemini 3.1 Pro (High)**<br>Prompt: *"Role: Bạn là một chuyên gia QA Automation Engineer / Node.js Developer dày dặn kinh nghiệm... Yêu cầu công việc: 1. Khởi tạo và Setup thư viện Pact. 2. Tạo file Consumer Test cho POST /api/cart. 3. Chạy Test và Kiểm tra File Contract..."* | Tự động tạo package.json, cài pact-js, sinh code test cart.consumer.test.js dùng Matchers và log kết quả. | INCOMPLETE | Matcher quá lỏng lẻo, bỏ qua Boundary Analysis. (ISTQB FL §4.2 Equivalence Partitioning). | Thay `like()` bằng `<mark>integer()</mark>` và thêm `<mark>regex()</mark>` cho các field quan trọng. |
| **Artifact #4 (W2)** | **Tool: Gemini 3.1 Pro**<br>Prompt: *"Đóng vai trò là một QA Automation Engineer Senior. Dựa vào Đặc tả API được cung cấp, hãy tạo một file JSON tuân thủ chuẩn Postman Collection Schema v2.1.0. Yêu cầu: Cài đặt collection variable... Tạo request POST /api/login... Trả về ĐÚNG 1 khối mã JSON duy nhất, không giải thích. [api_specification.md]"* | 1 khối mã JSON duy nhất chứa Postman Collection v2.1.0 và các đoạn script test. | INCOMPLETE | Thiếu thuộc tính bắt buộc trong JSON Schema, vi phạm RFC 8927 (JSON Schema). Gây lỗi lọt rác dữ liệu. | Thêm `<mark>"required": ["productId", "quantity"]</mark>` vào schema validator. |
| **Artifact #5 (W3)** | **Tool: Gemini 3.1 Pro**<br>Prompt: *"Tôi đang tự viết báo cáo phân tích Failure Modes của AI khi test hệ thống EShop. Mày hãy giải thích ngắn gọn (dùng chuẩn thuật ngữ QA/Testing) tại sao đoạn script JSON Schema do AI gen có 'properties': {} và 'additionalProperties': true lại gây ra lỗi False Positive cực kỳ nghiêm trọng ở API Checkout?..."* | Phân tích giải thích lỗi False Positive do AI sinh schema rỗng, khiến mọi cấu trúc JSON đều pass. | VALID | Phân tích đúng bản chất False Positive (ISTQB FL §1.2.3 Error, Defect, Failure). | <mark>Dịch một số thuật ngữ sang tiếng Việt</mark> để đưa vào User Guide. |
| **Artifact #6 (W4)** | **Tool: Gemini 3.1 Pro**<br>Prompt: *"Viết giúp tôi kịch bản thuyết trình chi tiết khoảng 2 phút để demo tính năng lưu Token tự động và chạy Collection Runner của Postman. Ngoài ra, hãy phân tích 3 điểm mù (Failure modes) thường gặp nhất khi dùng Postman test API để tôi đưa vào tài liệu User Guide."* | Kịch bản demo và danh sách 3 điểm mù của Postman (ép kiểu ngầm định, lỗi silent failure). | INCOMPLETE | Thiếu timing UI. Không đề cập sâu Data-Driven Testing (ISTQB FL §5.2 Test Strategy). | Bổ sung action `<mark>[Click file CSV]</mark>` và lỗi `<mark>Silent Failure</mark>`. |
| **Artifact #7 (W4)** | **Tool: Gemini 3.1 Pro**<br>Prompt: *"Bạn là một Technical Writer và chuyên gia Software Testing. Tôi đang ở Tuần 3 của dự án nhóm về 'API & Contract Testing' và cần hoàn thành các tài liệu tổng hợp cuối cùng..." (Kèm theo danh sách 5 yêu cầu tài liệu và context đầu vào).* | Dàn ý 5 file tài liệu hướng dẫn sử dụng chi tiết (User Guide, Risk Analysis...). | VALID | Cấu trúc báo cáo chuẩn theo form quốc tế (ISO/IEC/IEEE 29119). | Không sửa cấu trúc, chỉ <mark>tự viết nội dung chi tiết</mark> vào bên trong. |
| **Artifact #8 (W4)** | **Tool: Gemini 3.5 Flash**<br>Prompt: *"Viết sườn tài liệu hướng dẫn sử dụng và vận hành CI/CD GitHub Actions chạy Newman và Pact."* | Cấu trúc tài liệu hướng dẫn vận hành và mẫu code YAML cho workflow Github Actions. | INCOMPLETE | Dùng node bản cũ, không cache dependencies, đi ngược CI/CD Best Practices. | Sửa thành `<mark>node-version: 20</mark>` và thêm step `<mark>actions/cache@v3</mark>`. |
## **4\. Tổng kết Độ chính xác AI**

Tổng hợp verdict từ Mục 3 và điền vào bảng dưới.

| Chỉ số | Số lượng | Tỉ lệ |
| :---- | :---- | :---- |
| **Tổng artifact AI sinh đã audit** | 8 | 100% |
| **VALID (đúng, dùng nguyên)** | 4 | 50% |
| **INVALID (sai; loại bỏ)** | 0 | 0% |
| **INCOMPLETE (chấp nhận sau khi sửa)** | 4 | 50% |

## **5\. Kết luận — Khi nào nên / không nên dùng AI?**

Viết 80–150 chữ mô tả pattern quan sát được. AI mạnh ở đâu? AI sai ở đâu? Khuyến nghị của bạn cho việc dùng AI trong loại công việc này?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## **6\. Mandatory Disclosure (dán nguyên văn)**

*"\[Test case / script / dataset / báo cáo\] này được sinh phiên bản đầu bởi \[tên công cụ AI\]; tôi đã rà soát và chỉnh sửa \[phần X\], bổ sung \[edge case Y, Z\]; \[phần W\] do tôi tự viết. AI Audit Report chi tiết đính kèm ở Phụ lục A. Tôi cam đoan không dùng AI để sinh bất kỳ artifact nào thuộc danh mục bị cấm."*

## **Chữ ký**

| Họ tên sinh viên (in hoa): |  |
| :---- | :---- |
| **MSSV:** | 23127540 |
| **Lớp / Khoá:** | K23 |
| **Môn học:** | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| **Giảng viên:** |  |
| **Ngày:** |  |
| **Chữ ký:** |  |

## **Tham khảo**

* Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.  
* ISTQB Foundation Level Syllabus (latest version).  
* Hardman, P. (2025). A Post-AI Learning Taxonomy.  
* Fuster Rabella, M. (2025). OECD Education Working Paper No. 338\.  
* Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.  
* Anthropic (2025). Building reliable AI test agents — engineering blog.  
* DeepEval & Promptfoo documentation — testing frameworks for LLM systems.