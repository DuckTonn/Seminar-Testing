# Hướng dẫn chạy Demo GitHub Actions (Demo Script)
**Người phụ trách:** Huỳnh Sĩ Luân
**Dự án:** EShop — API & Contract Testing

Tài liệu này cung cấp các kịch bản demo chạy thực tế quy trình CI/CD trên GitHub Actions để chuẩn bị cho buổi Seminar thuyết trình.

---

## 1. Kịch bản Demo 1: Trigger Pipeline tự động qua Pull Request

### Mục tiêu:
Minh họa khả năng tự động hóa phát hiện lỗi (API & Contract) ngay trên giao diện GitHub trước khi code được gộp vào nhánh chính.

### Các bước thực hiện:
1. **Tạo thay đổi nhỏ hoặc code mới:** Trên một nhánh nhánh phụ (VD: `feature/add-checkout-test`), tiến hành thay đổi một API spec hoặc sửa nhẹ logic test trong `contract_testing/test/checkout.consumer.test.js`.
2. **Commit và Push:**
   ```bash
   git add .
   git commit -m "test: update checkout contract for seminar demo"
   git push origin feature/add-checkout-test
   ```
3. **Tạo Pull Request (PR):**
   * Truy cập GitHub, tạo PR từ `feature/add-checkout-test` vào `main`.
4. **Trình diễn trên GitHub:**
   * Chiếu màn hình PR, chỉ ra phần **"Checks"** ở cuối trang. Lúc này, job `test-api` sẽ tự động chuyển sang trạng thái đang chạy (biểu tượng màu vàng xoay tròn).
   * Click vào nút **Details** của check `test-api` để chuyển đến trang log chi tiết.

---

## 2. Kịch bản Demo 2: Đọc Log và Tải Báo Cáo Artifacts

### Mục tiêu:
Trình bày cách phân tích lỗi test và cách tải, đọc báo cáo HTML / TXT log từ Artifacts của Actions.

### Các bước thực hiện:
1. **Kiểm tra tiến trình chạy trên tab Actions:**
   * Truy cập tab **Actions** của repository.
   * Chọn lần chạy (run) tương ứng với PR vừa tạo.
   * Chỉ ra các bước chạy thành công (xanh) và bước chạy thất bại (đỏ) như Pact Verification hoặc Newman Test do lỗi cấu trúc dữ liệu cố tình (Ví dụ: lỗi schema ở giỏ hàng).
2. **Tải Artifacts:**
   * Cuộn xuống mục **Artifacts** ở dưới cùng của trang tóm tắt run.
   * Click vào link **`EShop-Test-Reports`** để tải file zip về máy.
3. **Đọc báo cáo:**
   * **Newman HTML Report:** Giải nén và mở file `newman-report.html` bằng trình duyệt. Chỉ ra các thông số: Tổng số request, số assertion pass/fail, thời gian phản hồi trung bình, và chi tiết request/response của API bị lỗi.
   * **Pact Verification log:** Mở file `pact-verification-report.txt` bằng text editor. Chỉ ra dòng thông báo lỗi mismatch (ví dụ: *expected status code 201 but got 200* hoặc thiếu trường `productId` trong response).
