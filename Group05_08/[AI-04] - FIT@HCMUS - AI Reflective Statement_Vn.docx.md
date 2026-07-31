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
| **Thành viên nhóm (nếu là nhóm):** | PHẠM ĐỨC TOÀN, NGUYỄN NHẬT NAM, NGUYỄN QUANG ĐĂNG KHOA, HUỲNH SĨ LUÂN |
| **Họ tên sinh viên:** | NHÓM 05 (Đại diện: Phạm Đức Toàn) |
| **MSSV:** | 23127540 |
| **Ngày nộp:** | 2026-08-01 |

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


### **4\. Bạn xác minh thông tin / nguồn / claim của AI như thế nào?**

- Sinh viên xác minh bằng cách chạy test thực tế (run Postman Collection, run npm test cho file Pact, trigger GitHub Actions workflow).
- Đối chiếu cấu trúc JSON được sinh ra với tiêu chuẩn của RFC 8927.
- Đánh giá chất lượng và phạm vi bao phủ test dựa trên các nguyên lý trong tài liệu ISTQB Foundation Level.


### **5\. Bạn học được điều gì qua project này mà nếu chỉ chấp nhận đầu ra AI thì sẽ không học được?**

- Nhóm nhận ra rằng nếu chỉ "nhắm mắt" chấp nhận đầu ra của AI, chúng tôi sẽ không bao giờ phát hiện được lỗi "False Positive" cực kỳ nguy hiểm trong JSON Schema.
- Việc tự rà soát giúp sinh viên nhận thức được giới hạn của AI (thiên kiến Happy-path) và thực sự thấm nhuần tầm quan trọng của tư duy kiểm thử ở góc cạnh và ranh giới (Edge/Boundary Analysis) mà con người mang lại.


## **3\. Các Cấp độ AI đã dùng**

Đánh dấu mọi cấp độ đã áp dụng ở bất kỳ giai đoạn nào:

* \[ \] Cấp 1 – Không AI  
* \[ \] Cấp 2 – AI cho chuẩn bị  
* \[ \] Cấp 3 – AI cho phản hồi / chỉnh sửa  
* \[ \] Cấp 4 – AI hỗ trợ sản xuất  
* \[ \] Cấp 5 – AI là phương pháp cốt lõi

## **4\. Chữ ký Tác giả**

*Bằng việc ký dưới đây, tôi cam đoan bài suy ngẫm này trung thực và phản ánh chính xác cách AI được dùng trong project. Tôi chịu hoàn toàn trách nhiệm trí tuệ cho sản phẩm cuối.*

## **Chữ ký**

| Họ tên sinh viên (in hoa): | PHẠM ĐỨC TOÀN |
| :---- | :---- |
| **MSSV:** | 23127540 |
| **Lớp / Khoá:** | 23CQ |
| **Môn học:** | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| **Giảng viên:** | (Giảng viên phụ trách) |
| **Ngày:** | 2026-08-01 |
| **Chữ ký:** | PDT (Đã ký) |

## **Tham khảo**

* Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.  
* ISTQB Foundation Level Syllabus (latest version).  
* Hardman, P. (2025). A Post-AI Learning Taxonomy.  
* Fuster Rabella, M. (2025). OECD Education Working Paper No. 338\.  
* Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.  
* Anthropic (2025). Building reliable AI test agents — engineering blog.  
* DeepEval & Promptfoo documentation — testing frameworks for LLM systems.