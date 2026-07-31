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
| **Mẫu (italic) — thay trước khi nộp:** |  |  |  |  |
| **Tool: AI Tool (e.g., ChatGPT, Claude, Gemini) Thời gian: 14:32 25/02/2026 Prompt: "Sinh test case cho hàm parsePhoneNumberVN…"** | TC01: parsePhoneNumberVN("0912345678") Kỳ vọng: {prefix:84, number:912345678, valid:true} … | INCOMPLETE | AI bỏ qua định dạng RFC 3966\. ISTQB FL §4.3 Boundary Value Analysis yêu cầu test ranh giới định dạng. | Thêm TC: parsePhoneNumberVN("+84-91-234-5678") Kỳ vọng: {prefix:84, number:912345678, valid:true} |
| **Artifact #1 (W1)** | **Tool: Gemini 3.1 Pro**<br>Prompt: "Hãy nghiên cứu quy trình API Testing cho hệ thống E-Shop, đề xuất workflow phù hợp, xây dựng kế hoạch triển khai theo các milestone..." | Workflow API Testing và Risk Analysis | VALID | Phân tích rủi ro bám sát hệ thống. | Giữ nguyên dàn ý, bổ sung chi tiết dự án. |
| **Artifact #2 (W2)** | **Tool: Gemini 3.1 Pro**<br>Prompt: "Dựa trên file đặc tả API (api_specification.md)... khởi tạo file Postman Collection (v1)..." | JSON Postman Collection v1 | INCOMPLETE | Script auth JWT chưa tối ưu. | Cấu hình lại Collection Variables cho token. |
| **Artifact #3 (W2)** | **Tool: Gemini 3.1 Pro**<br>Prompt: "Bạn là chuyên gia QA... thiết lập môi trường Contract Testing ở phía Consumer..." | Code Jest/Pact Consumer test | VALID | Sử dụng đúng Pact matchers. | Review và chỉnh sửa một số properties bắt buộc. |
| **Artifact #4 (W2)** | **Tool: Gemini 3.1 Pro**<br>Prompt: "Đóng vai trò là QA... tạo một file JSON tuân thủ chuẩn Postman Collection Schema v2.1.0..." | File JSON Postman chuẩn v2.1.0 | INCOMPLETE | Thiếu test cases cho các API phụ. | Fix các giá trị mặc định, bổ sung schema validation. |
| **Artifact #5 (W3)** | **Tool: Gemini 3.1 Pro**<br>Prompt: "Tôi đang tự viết báo cáo phân tích Failure Modes của AI... giải thích tại sao đoạn script JSON Schema do AI gen có 'properties': {} lại gây ra lỗi False Positive..." | Giải thích nguyên nhân lỗi False Positive | VALID | Logic test đúng, thuật ngữ chuẩn xác. | Diễn đạt lại cho sát với bài thuyết trình. |
| **Artifact #6 (W4)** | **Tool: Gemini 3.1 Pro**<br>Prompt: "Viết giúp tôi kịch bản thuyết trình chi tiết khoảng 2 phút để demo tính năng lưu Token tự động..." | Khung sườn kịch bản demo Postman | INCOMPLETE | Thiếu timing chi tiết cho thao tác chuột. | Thêm timing chi tiết và hành động thực tế. |
| **Artifact #7 (W4)** | **Tool: Gemini 3.1 Pro**<br>Prompt: "Bạn là một Technical Writer và chuyên gia Software Testing... hoàn thành các tài liệu tổng hợp cuối cùng..." | Dàn ý 5 file tài liệu tổng hợp | VALID | Đúng cấu trúc tài liệu yêu cầu. | Giữ nguyên cấu trúc, điền nội dung chi tiết. |
| **Artifact #8 (W4)** | **Tool: Gemini 3.5 Flash**<br>Prompt: "Viết sườn tài liệu hướng dẫn sử dụng và vận hành CI/CD GitHub Actions chạy Newman và Pact." | Các step cấu hình YAML Github Actions | INCOMPLETE | Chưa khớp với cấu trúc thư mục project. | Cấu hình lại path và branch trong YAML. |

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