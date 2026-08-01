**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**

**CS423 / CSC15003 – Kiểm chứng Phần mềm (AI-augmented · 2026\)**

**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# **Biểu mẫu Khai báo Sử dụng AI**

*Đính kèm cho mọi bài tập có dùng AI ở bất kỳ mức nào.*

*Tài liệu được biên soạn lại từ Med Kharbach, PhD (2026) — Mẫu Chính sách Sử dụng AI cho Giáo dục Đại học. Giấy phép CC BY-NC-SA 4.0. Phiên bản này được FIT@HCMUS điều chỉnh cho môn CS423 / CSC15003 Kiểm chứng Phần mềm.*

## **1\. Thông tin Môn học & Sinh viên**

| Mục | Giá trị |
| :---- | :---- |
| **Môn học:** | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| **Mã bài tập:** | T06_API_and_Contract_Testing |
| **Tên bài tập:** | Seminar - API & Contract Testing |
| **Cấp độ AI (1–5):** | Cấp \_\_\_\_ |
| **Ngày:** | 2026-08-01 |
| **Họ tên sinh viên:** | NHÓM 05 (Đại diện: Phạm Đức Toàn) |
|  |  |
| **MSSV:** | 23127540 - 23127212 - 23127092 - 23127086 |

## **2\. Câu hỏi Khai báo**

### **1\. Công cụ AI đã dùng:**

*Liệt kê mọi công cụ AI dùng cho bài tập này (ví dụ AI Tool (e.g., ChatGPT, Claude, Gemini), ChatGPT, GitHub Copilot, Cursor, Gemini).*

- Gemini 3.1 Pro
- Gemini 3.5 Flash

### **2\. Giai đoạn nào của bài tập có dùng AI:**

*Tick tất cả: [x] brainstorm  [x] outline  [x] viết nháp  [ ] phản hồi  [x] sửa chữa  [x] code  [ ] phân tích dữ liệu  [ ] thiết kế đồ hoạ  [ ] khác (ghi rõ).*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **3\. Prompt / nhiệm vụ chính cho AI:**

- Tổng cộng 12 prompts từ 4 thành viên (Toàn, Nam, Khoa, Luân) ở Tuần 5 và Tuần 6.
- Các tác vụ chính: setup JSON Postman v1/v2, viết Contract test bằng Pact, thiết lập CI/CD bằng GitHub Actions, sinh JSON Schema, phân tích lỗi Failure modes.
- (Xem toàn văn 12 prompt tại Bảng AI Audit [AI-02]).

### **4\. Phần cụ thể AI đóng góp:**

- AI hỗ trợ sinh các khung sườn báo cáo, sinh file collection Postman v1/v2, script test Pact (Javascript), và file YAML cấu hình CI/CD.
- AI KHÔNG tham gia vào việc phát hiện bug thực tế. Sinh viên tự rà soát Endpoint_Agreement, tự phân tích log, tự sửa các script test bị lỗi False Positive, và cấu hình lại environment variables.

### **5\. Cách tôi rà soát / chỉnh sửa / xác minh đầu ra AI:**

- Sinh viên tự cấu hình môi trường, chạy test thực tế trên Postman và chạy lệnh `npm test` cho Pact. Nếu test fail không đúng do lỗi logic của script AI, sinh viên sẽ tự debug và điều chỉnh code Assertions. Đồng thời đối chiếu các test case với chuẩn ISTQB Foundation Level.

### **6\. Trích dẫn (nếu môn yêu cầu):**

- Google. (2026). Gemini 3.1 Pro & 3.5 Flash [Large language model]. https://gemini.google.com

## **3\. Cam đoan Trung thực**

*Bằng việc ký tên dưới đây, tôi cam đoan thông tin khai báo ở trên là chính xác và đầy đủ. Tôi hiểu rằng việc không khai báo hoặc khai báo sai lệch về việc dùng AI sẽ bị coi là vi phạm liêm chính học thuật và có thể dẫn đến điểm 0 cho bài tập cùng việc bị chuyển lên hội đồng kỷ luật.*

## **Chữ ký**

| Họ tên sinh viên (in hoa): | PHẠM ĐỨC TOÀN |
| :---- | :---- |
| **MSSV:** | 23127540 |
| **Lớp / Khoá:** | 23KTPM2 |
| **Môn học:** | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| **Giảng viên:** | Mr. LÂM QUANG VŨ - Mr. HỒ TUẤN THANH |
| **Ngày:** | 2026-08-01 |
| **Chữ ký:** | PHẠM ĐỨC TOÀN |

## **Tham khảo**

* Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.  
* ISTQB Foundation Level Syllabus (latest version).  
* Hardman, P. (2025). A Post-AI Learning Taxonomy.  
* Fuster Rabella, M. (2025). OECD Education Working Paper No. 338\.  
* Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.  
* Anthropic (2025). Building reliable AI test agents — engineering blog.  
* DeepEval & Promptfoo documentation — testing frameworks for LLM systems.