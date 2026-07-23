# Hướng dẫn kiểm thử bằng Pact (Contract Testing)
**Phụ trách:** Nguyễn Nhật Nam

Tài liệu này hướng dẫn chi tiết cách chạy Consumer Test để sinh file hợp đồng (Pact file) và Provider Verification để kiểm chứng hợp đồng đối với hệ thống EShop.

## 1. Consumer Test (Tạo Hợp Đồng)

Nhiệm vụ của Consumer (Client) là định nghĩa các kỳ vọng (expectations) đối với API và sinh ra bản hợp đồng dưới dạng file JSON.

**Các bước thực hiện:**
1. **Khởi tạo cấu hình Pact:** Sử dụng `PactV3` để khai báo tên `consumer` và `provider`.
2. **Định nghĩa Interactions:**
   - `.given(...)`: Thiết lập trạng thái giả định (VD: "Giỏ hàng rỗng").
   - `.uponReceiving(...)`: Đặt tên kịch bản kiểm thử.
   - `.withRequest(...)`: Cấu hình request (Method, Path, Headers).
   - `.willRespondWith(...)`: Định nghĩa response mong đợi. **Lưu ý:** Luôn sử dụng các Matchers (như `MatchersV3.like`) thay vì gán giá trị cứng để tránh Flaky test.
3. **Thực thi Test:** Gửi request thực tế thông qua thư viện Axios hoặc Fetch tới Mock Server của Pact.
4. **Kết quả:** Nếu test Pass, Pact sẽ tự động sinh/cập nhật file JSON contract vào thư mục `pacts/`.

**Lệnh chạy Consumer Test:**
```bash
npx jest Group05_07/Nam/test/*.consumer.test.js
```

## 2. Provider Verification (Xác Minh Hợp Đồng)

Nhiệm vụ của Provider (Backend) là khởi chạy server API thực tế và xác minh lại các yêu cầu từ file Contract đã được Consumer tạo ra.

**Các bước thực hiện:**
1. **Chuẩn bị Server:** Khởi động backend server trên một port test (VD: 3000) cùng database chuyên dụng cho test.
2. **Cấu hình Verifier:** Khởi tạo `Verifier` từ thư viện `@pact-foundation/pact`.
3. **Thiết lập thông số Verification:**
   - `providerBaseUrl`: Trỏ tới server API đang chạy.
   - `pactUrls`: Trỏ tới file JSON contract.
   - **`stateHandlers` (Quan trọng nhất):** Viết các hàm logic setup/teardown dữ liệu khớp chính xác 100% với chuỗi trạng thái (`given`) mà Consumer đã định nghĩa.
4. **Thực thi Xác minh:** Gọi hàm `verifyProvider()`. Pact sẽ đọc file contract, tự động gọi state handler tương ứng, gửi request vào server thật và so sánh kết quả.

**Lệnh chạy Provider Test:**
```bash
npx jest Group05_07/Nam/test/provider.test.js
```
