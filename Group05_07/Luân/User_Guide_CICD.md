# Hướng dẫn tích hợp tự động hóa (CI/CD User Guide)
**Người phụ trách:** Huỳnh Sĩ Luân
**Dự án:** EShop — API & Contract Testing

Tài liệu này hướng dẫn cách thiết lập, cấu hình và vận hành quy trình Tích hợp liên tục (CI/CD) tự động hóa kiểm thử cho dự án EShop thông qua GitHub Actions. Quy trình tự động chạy toàn bộ các kịch bản Newman API Testing và Pact Contract Testing.

---

## 1. Thiết lập GitHub Actions Workflow

Quy trình CI/CD được định nghĩa hoàn chỉnh trong file cấu hình `.github/workflows/newman.yml`. Nó tự động kích hoạt (trigger) mỗi khi có một thay đổi code được push lên hoặc khi một Pull Request được tạo hướng về nhánh `main`.

### Cấu hình Workflow (`newman.yml`)
Dưới đây là tóm tắt cấu trúc chính của workflow:
* **Trigger:** Chạy khi push hoặc pull request vào branch `main`.
* **Runner Environment:** Hệ điều hành `ubuntu-latest` (Linux).
* **Caching:** Tự động lưu cache cho `node_modules` giúp tăng tốc độ build giữa các lần chạy.

---

## 2. Các bước thực thi tự động trong Pipeline

Khi pipeline kích hoạt, nó sẽ lần lượt thực hiện các bước sau một cách tuần tự:

1. **Checkout source code:** Lấy mã nguồn mới nhất từ GitHub.
2. **Setup Node.js:** Thiết lập môi trường chạy Node.js v20.
3. **Cài đặt thư viện:** Chạy lệnh `npm ci` độc lập cho cả Backend và thư mục Contract Testing.
4. **Cài đặt công cụ kiểm thử:** Cài đặt toàn cục Newman và plugin sinh báo cáo HTML `newman-reporter-htmlextra`.
5. **Chạy Pact Consumer Tests:** Thực thi lệnh `npm run test:pact` trong thư mục `contract_testing` để chạy tất cả các test consumer (`*.consumer.test.js`) và tự động tái tạo file hợp đồng JSON mới nhất (`EshopConsumer-EShopBackend.json`).
6. **Khởi động Backend Server:** Khởi chạy ngầm API backend (`node server.js &`).
7. **Đợi Server sẵn sàng:** Dùng công cụ `wait-on` thăm dò cổng `3000` của localhost để đảm bảo server đã khởi động hoàn toàn trước khi kiểm thử.
8. **Chạy Newman API Tests:** Thực thi bộ kiểm thử API `EShop_Collection_v2.json` dựa trên file môi trường `EShop_Environment.json` và xuất báo cáo dưới dạng HTML  vào thư mục `reports/newman-report.html`.
9. **Chạy Pact Verification:** Thực thi lệnh xác minh hợp đồng (`npm run test:provider`), so khớp trực tiếp hành vi của server backend thực tế với các giao kèo trong file hợp đồng JSON. Kết quả log được ghi nhận lại vào `reports/pact-verification-report.txt`. Bước này chạy ở chế độ `always()` để thu thập log ngay cả khi test trước đó thất bại.
10. **Đóng gói và tải Artifacts lên GitHub:** Đóng gói thư mục `reports/` chứa cả HTML report và file txt log, đẩy lên GitHub Artifacts với tên `EShop-Test-Reports`.

---

## 3. Hướng dẫn theo dõi và xem kết quả trên GitHub Actions

Để giám sát quy trình chạy CI/CD và tải báo cáo minh chứng:

### 3.1. Theo dõi tiến trình chạy (Execution logs)
1. Truy cập vào repository dự án trên GitHub.
2. Click chọn tab **Actions** ở thanh menu phía trên.
3. Nhấp chọn run mới nhất (hoặc run tương ứng với commit của bạn).
4. Click chọn job **test-api** ở sidebar bên trái để xem log thời gian thực của từng bước chạy.

### 3.2. Đọc báo cáo lỗi và kết quả
* **Nếu bước chạy nào bị lỗi:** Bước đó sẽ hiển thị dấu chéo đỏ, nhấp vào bước đó để xem chi tiết log lỗi (ví dụ: Newman assertion failed hoặc Pact Contract mismatch).
* **Tải báo cáo kiểm thử:**
  1. Cuộn xuống cuối trang run của Actions (phần **Artifacts**).
  2. Click tải xuống file **`EShop-Test-Reports`** (đây là file nén `.zip`).
  3. Giải nén file zip bạn sẽ nhận được:
     * `newman-report.html`: Mở trực tiếp trên trình duyệt để xem giao diện đồ họa phân tích chi tiết kết quả test từng API.
     * `pact-verification-report.txt`: File logs chi tiết của Pact Provider Verification chứa thông tin chi tiết về các lỗi vi phạm hợp đồng (Contract Violations).
