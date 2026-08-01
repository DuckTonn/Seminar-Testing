# MEETING REPORT - 30/07/2026

**1. Thông tin chung**
- **Dự án:** API & Contract Testing (Hệ thống EShop)
- **Thời gian:** 20:00 - 21:30, Thứ Năm (30/07/2026)
- **Hình thức:** Trực tuyến (Google Meet)
- **Thành viên tham dự:** Phạm Đức Toàn, Nguyễn Nhật Nam, Nguyễn Quang Đăng Khoa, Huỳnh Sĩ Luân (Đủ 4/4)

**2. Mục tiêu cuộc họp**
- Review chéo các đoạn script và tài liệu do AI sinh ra trong tuần.
- Thống nhất giải pháp fix các bug cấu hình (Pact, GitHub Actions, Postman Schema) đang tồn đọng.
- Đưa ra kế hoạch quay video demo và thuyết trình.

**3. Nội dung thảo luận & Quyết định**
- **Vấn đề 1: Postman Assertions & Schema** 
  - *Thảo luận:* Script test do AI gen đang bị lỏng lẻo (dùng `==` thay vì `===`) và JSON schema bị rỗng dẫn đến False Positive cho API Checkout.
- **Vấn đề 2: Pact Contract Testing**
  - *Thảo luận:* Script test contract của Nam bị kẹt ở phần chứng thực (Auth) do token bị mock cứng.
  - *Quyết định:* Thống nhất dùng `requestFilter` để chèn token động mỗi lần chạy verify.
- **Vấn đề 3: CI/CD Pipeline bị gãy**
  - *Thảo luận:* Pipeline của Luân báo lỗi không upload được artifact nếu test trước đó fail.
  - *Quyết định:* Sửa lại step upload artifact với cờ `if: always()` để log lại lỗi phục vụ debug.

**4. Kế hoạch**
- Fix các lỗi trong tuần.
- Deadline quay demo video: 04/08/2026
