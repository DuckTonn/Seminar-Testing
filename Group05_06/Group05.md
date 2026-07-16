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
- Lưu kết quả minh chứng (minh chứng bao gồm collection v2, environment file).

**Minh chứng**
- `EShop_Collection_v2.json`
- `EShop_Environment.json`

---

## Nguyễn Nhật Nam – 23127092

**Prompt đã sử dụng**


**AI đã thực hiện**


**Sinh viên đã thực hiện**


---

## Nguyễn Quang Đăng Khoa – 23127212


**Prompt đã sử dụng**


**AI đã thực hiện**


**Sinh viên đã thực hiện**



## Huỳnh Sĩ Luân – 23127086


**Prompt đã sử dụng**


**AI đã thực hiện**


**Sinh viên đã thực hiện**


---

# AI Usage Declaration


# Tasks Planned for Next Week

---

# Issues
