# Nghiên cứu Postman và khả năng import OpenAPI

## 1. Nghiên cứu Postman và khả năng import OpenAPI Specification

**Postman** là một nền tảng mạnh mẽ và phổ biến được sử dụng để xây dựng và sử dụng API. Công cụ này cung cấp nhiều tính năng hữu ích cho vòng đời phát triển API, từ việc thiết kế, kiểm thử, cho đến việc lập tài liệu (documentation).

**Khả năng import OpenAPI Specification vào Postman:**
Postman hỗ trợ import trực tiếp các file đặc tả API theo chuẩn **OpenAPI Specification** (trước đây gọi là Swagger). Đây là định dạng tiêu chuẩn mô tả cấu trúc của REST API bao gồm: các endpoint, phương thức HTTP, tham số, cấu trúc request/response, và mã lỗi. Hệ thống EShop sử dụng file `api_specification.md` để mô tả toàn bộ API backend.

Để import file OpenAPI vào Postman, người dùng thực hiện theo các bước sau:
1. **Mở Postman** và chọn **Import** (hoặc nhấn `Ctrl + O`).
2. **Chọn file đặc tả:** Kéo thả hoặc chọn file OpenAPI dạng `.yaml`, `.json`, hoặc `.md` từ máy tính.
3. **Xác nhận import:** Postman sẽ tự động phân tích file và tạo ra một **Collection** chứa tất cả các endpoint được khai báo trong file đặc tả, bao gồm đường dẫn, phương thức, tham số, và cấu trúc body mẫu.
4. **Sử dụng Collection:** Sau khi import, người dùng có thể chỉnh sửa các request, thêm test script (JavaScript), thiết lập biến môi trường (Environment Variables), và chạy toàn bộ collection bằng Collection Runner hoặc Newman CLI.

*Nguồn tham khảo: [Importing API specifications | Postman Learning Center](https://learning.postman.com/docs/designing-and-developing-your-api/importing-an-api/)*

## 2. Xây dựng ví dụ kiểm thử cho các endpoint

Dựa trên đặc tả API của hệ thống E-Shop, các ví dụ kiểm thử cơ bản (test scenarios) được xây dựng cho các endpoint sau:

### 2.1. POST `/login`
- **Mục đích:** Kiểm tra chức năng đăng nhập của người dùng và nhận lại token xác thực.
![Login](https://res.cloudinary.com/dhctxuupz/image/upload/v1783166163/Screenshot_2026-07-04_185639_pnttmo.png)

### 2.2. GET `/products`
- **Mục đích:** Lấy danh sách các sản phẩm hiện có trong hệ thống E-Shop.
![Products](https://res.cloudinary.com/dhctxuupz/image/upload/v1783166163/Screenshot_2026-07-04_185647_fpptyg.png)

### 2.3. GET `/categories`
- **Mục đích:** Lấy danh sách các danh mục sản phẩm hiện có trong hệ thống E-Shop.
![Categories](https://res.cloudinary.com/dhctxuupz/image/upload/v1783166163/Screenshot_2026-07-04_185653_e7ofee.png)

### 2.4. POST `/categories`
- **Mục đích:** Thêm một danh mục sản phẩm mới vào hệ thống E-Shop. (Yêu cầu Authorization và Forbidden - Quyền `ADMIN`).
![Categories](https://res.cloudinary.com/dhctxuupz/image/upload/v1783166163/Screenshot_2026-07-04_185705_vidwoy.png)

## 3. Nguồn tài liệu tham khảo
- Postman Documentation (Introduction): [https://learning.postman.com/docs/getting-started/introduction/](https://learning.postman.com/docs/getting-started/introduction/)
- Importing API specifications | Postman: [https://learning.postman.com/docs/designing-and-developing-your-api/importing-an-api/](https://learning.postman.com/docs/designing-and-developing-your-api/importing-an-api/)
