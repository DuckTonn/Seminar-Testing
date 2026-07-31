**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**

**CS423 / CSC15003 – Kiểm chứng Phần mềm (AI-augmented · 2026\)**

**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# **Bài Suy ngẫm về Sử dụng AI**

*Bắt buộc cho Project lớn, Seminar, Đồ án Tốt nghiệp. Áp dụng khi bài nộp ở Cấp độ AI 4 hoặc 5\.*

*Tài liệu được biên soạn lại từ Med Kharbach, PhD (2026) — Mẫu Chính sách Sử dụng AI cho Giáo dục Đại học. Giấy phép CC BY-NC-SA 4.0. Phiên bản này được FIT@HCMUS điều chỉnh cho môn CS423 / CSC13003 Kiểm chứng Phần mềm.*

## **1\. Thông tin Project & Tác giả**

| Mục | Giá trị |
| :---- | :---- |
| **Môn học:** | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| **Tên Project / Đồ án:** | Seminar - API & Contract Testing |
| **Thành viên nhóm (nếu là nhóm):** | Toàn, Nam, Khoa, Luân |
| **Họ tên sinh viên:** | NHÓM 05 (Đại diện: Phạm Đức Toàn) |
| **MSSV:** | 23127540 |
| **Ngày nộp:** | 2026-07-31 |

## **2\. Câu hỏi Suy ngẫm**

### **1\. AI đã hỗ trợ công việc của bạn như thế nào?**

- AI đóng vai trò như một trợ lý sinh boilerplate code (Pact JS, Postman Javascript Assertions) và hỗ trợ tạo dàn ý các báo cáo phân tích rủi ro, CI/CD pipeline (YAML).
- Nhờ AI, nhóm tiết kiệm được 40% thời gian setup ban đầu để tập trung vào việc thiết kế Test Case (Endpoint Agreement) và phân tích Failure modes thực tế.

### **2\. Bạn chấp nhận / từ chối / sửa gì từ đầu ra AI?**

- **Chấp nhận**: Các khung sườn tài liệu Markdown, cấu trúc khung JSON Collection v1/v2 cơ bản.
- **Từ chối/Sửa**: Loại bỏ các dòng code Assertions lỏng lẻo (vd: dùng `==` thay vì `===`, hàm `like()` của Pact quá lỏng). Sửa cấu hình CI/CD thiếu cache và bổ sung điều kiện upload artifact khi fail (`if: always()`). Sửa lại scope biến môi trường token từ global xuống `collectionVariables`.

### **3\. Bạn nhận ra lỗi / bias / giới hạn nào trong đầu ra AI?**

- **Thiên kiến Happy-path**: Code test do AI viết thường chỉ chạy đúng trong điều kiện hoàn hảo, bỏ qua các validation dữ liệu hẹp (Boundary Analysis).
- **Lỗi False Positive nguy hiểm**: AI sinh JSON Schema rỗng (`properties: {}`), dẫn đến Postman báo Pass cho mọi dữ liệu rác trả về từ API.
- **Dữ liệu/Syntax lỗi thời**: AI thường dùng các thư viện/cú pháp cũ (ví dụ cấu hình GitHub Actions dùng Node.js v12 thay vì v20, không tự biết cài cache dependencies).

.