# Hướng dẫn Cài đặt & Thiết lập Pact (Contract Testing)

Tài liệu này tóm tắt các bước cơ bản để cài đặt và cấu hình Pact Contract Testing cho dự án, dựa trên kiến trúc của dự án EShop hiện tại (Sử dụng Pact V3 với Node.js & Jest).

## 1. Cài đặt Dependencies

Tại thư mục gốc của dự án, cài đặt thư viện Pact và các công cụ kiểm thử cần thiết (nếu chưa có):

```bash
npm install @pact-foundation/pact --save-dev
npm install jest axios --save-dev
```

*(Lưu ý: Bạn cũng có thể cần cài đặt thêm các thư viện hỗ trợ mock server hoặc API client tuỳ vào setup dự án)*

---

## 2. Thiết lập phía Consumer (Client / API Consumer)

Nhiệm vụ của Consumer là định nghĩa các "kỳ vọng" (expectations) đối với API, sau đó tạo ra bản hợp đồng (Contract - file JSON).

**File mẫu trong dự án:** `contract_testing/test/cart.consumer.test.js`

**Các bước chính:**
1. **Khởi tạo Pact:** Sử dụng `PactV3` để cấu hình thông tin định danh cho Consumer và Provider.
2. **Định nghĩa Interactions:** 
   - Sử dụng `.given(...)`: Mô tả trạng thái giả định của Provider (Ví dụ: "Một giỏ hàng trống").
   - Sử dụng `.uponReceiving(...)`: Tên của kịch bản test.
   - Sử dụng `.withRequest(...)`: Chi tiết Request (Method, Path, Headers, Body).
   - Sử dụng `.willRespondWith(...)`: Chi tiết Response mong đợi (Status, Headers, Body) - **Nên sử dụng Matchers (như `MatchersV3.like`, `MatchersV3.string`) thay vì giá trị cứng.**
3. **Thực thi Test:** Gửi request thực tế (thông qua Axios/Fetch) tới Mock Server do Pact tự động dựng lên ở cổng chỉ định.
4. **Kết quả:** Nếu request khớp với định nghĩa, Pact sẽ tự động sinh/cập nhật file contract (thường nằm trong thư mục `pacts/`).

---

## 3. Thiết lập phía Provider (Server / API Provider)

Nhiệm vụ của Provider là khởi chạy API nội bộ (cùng cơ sở dữ liệu test) và dùng Pact để xác minh (verify) lại các yêu cầu từ file Contract sinh ra ở Bước 2.

**File mẫu trong dự án:** `contract_testing/test/provider.test.js`

**Các bước chính:**
1. **Chuẩn bị Server:** Khởi động server API thực tế của Provider trên một cổng test (VD: 3000). Đảm bảo kết nối tới một test database sạch.
2. **Khởi tạo Verifier:** Import `Verifier` từ `@pact-foundation/pact`.
3. **Cấu hình Verify:**
   - `provider`: Tên của Provider (phải khớp với khai báo ở Consumer).
   - `providerBaseUrl`: Đường dẫn trỏ tới server API thực đang chạy.
   - `pactUrls`: Đường dẫn trỏ tới file file JSON contract đã được sinh ra.
   - **`stateHandlers`**: Rất quan trọng! Định nghĩa các hàm để setup/teardown dữ liệu tương ứng với từng chuỗi mô tả trạng thái (`given`) của Consumer.
4. **Thực thi Xác minh:** Gọi hàm `verifier.verifyProvider()`. Pact sẽ đọc Contract, thiết lập trạng thái, gửi request vào server thật và so sánh response với kỳ vọng.

---

## 4. Luồng thực thi tiêu chuẩn (Workflow)

Để thực hiện trọn vẹn một quy trình Contract Testing tại local:

1. **Sinh hợp đồng:** Chạy test phía Consumer.
   ```bash
   # Ví dụ lệnh chạy:
   npx jest contract_testing/test/cart.consumer.test.js
   ```
2. **Kiểm tra File:** Đảm bảo file `.json` đã được tạo thành công trong thư mục `pacts/`.
3. **Start Test Server:** Bật server của Provider (nếu provider test không tự bật).
4. **Xác minh hợp đồng:** Chạy test phía Provider.
   ```bash
   # Ví dụ lệnh chạy:
   npx jest contract_testing/test/provider.test.js
   ```

---

## 5. Các Best Practices cần nhớ

- **State Handlers:** Chuỗi tên trạng thái (`given`) ở Consumer và key của `stateHandlers` ở Provider phải **khớp chính xác 100%**. Hãy comment rõ ràng logic setup/teardown tại Provider.
- **Dùng Matchers, đừng Hard-code:** Dùng Regex (như format ngày tháng, chuỗi email) và Type matchers cho body, headers thay vì chuỗi tĩnh để tránh hiện tượng Flaky Test.
- **Log file độc lập:** Nên cấu hình để xuất log của Pact ra một thư mục riêng (vd: `logs/pact.log`) để dễ debug lỗi thay vì in hết ra terminal.
