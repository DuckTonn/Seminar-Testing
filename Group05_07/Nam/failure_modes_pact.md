# Hạn chế và Failure Modes của Pact trong Contract Testing

Trong quá trình triển khai Contract Testing cho ứng dụng EShop, tôi (Nam) đã ghi nhận một số hạn chế (failure modes) của Pact. Tài liệu này liệt kê các tình huống mà Pact có thể không phát hiện được lỗi hoặc gây khó khăn trong quá trình sử dụng.

---

### 1. Verification Pass nhưng không phát hiện thay đổi schema ngầm (Silent Schema Change)
- **Mô tả chi tiết**: Pact mặc định hoạt động theo cơ chế "Postel's Law" (Robustness Principle): Consumer chỉ định nghĩa những trường mà nó cần. Nếu Provider trả về *nhiều trường hơn* so với contract yêu cầu, Pact vẫn sẽ báo Pass.
- **Ví dụ cụ thể**: Trong endpoint `POST /api/cart`, Consumer chỉ yêu cầu `productId` và `quantity`. Nếu Backend tự động thêm trường `discount_applied` vào response, Pact Verification sẽ pass. Điều này có thể che giấu sự thay đổi logic kinh doanh ngầm ở phía backend mà consumer đáng lẽ nên biết.
- **Workaround**: Để kiểm soát chặt chẽ schema, có thể sử dụng thêm các công cụ API Schema Testing chuyên dụng (như OpenAPI validator) kết hợp cùng Pact, hoặc quy định trong team phải cập nhật contract ngay khi thêm field quan trọng.

### 2. Pact không test được Performance hay Response Time
- **Mô tả chi tiết**: Pact chỉ xác nhận rằng request/response đúng format (schema, status code, headers). Nó hoàn toàn không kiểm tra được hệ thống mất bao lâu để xử lý request đó.
- **Ví dụ cụ thể**: Nếu endpoint `GET /api/products` bị lỗi truy vấn (N+1 query) làm thời gian phản hồi tăng từ 100ms lên 5000ms, Provider Verification của Pact vẫn đánh giá là thành công (Pass) miễn là data trả về đúng.
- **Workaround**: Phải kết hợp Contract Testing với các bài test hiệu năng (Performance/Load testing) dùng công cụ như JMeter, k6 hoặc Gatling.

### 3. Consumer Test không bao phủ hết các Edge Cases nếu chỉ định nghĩa Happy Path
- **Mô tả chi tiết**: Chất lượng của bản hợp đồng (Contract) phụ thuộc 100% vào những gì Consumer Test viết. Nếu Consumer dev lười biếng hoặc quên chỉ định nghĩa các case thành công (Happy Path), thì Pact cũng sẽ chỉ bắt backend phải phục vụ Happy Path.
- **Ví dụ cụ thể**: Consumer chỉ viết test cho `POST /api/cart` khi user đã login. Họ quên viết test cho trường hợp "Chưa đăng nhập" (Unauthorized - 401). Khi đó, backend vô tình xóa middleware `authenticateToken`, Pact Verification vẫn sẽ pass vì contract không hề đề cập đến case 401 này.
- **Workaround**: Dev Frontend (Consumer) cần được review kỹ các bài test (Code Review) để đảm bảo bao phủ cả Happy path và Sad/Error paths.

### 4. Khó mô phỏng Behavior phức tạp của hệ thống (như Timeout, Rate Limiting)
- **Mô tả chi tiết**: Pact Mock Server khởi tạo khi chạy Consumer Test được thiết kế đơn giản để verify contract. Nó rất khó để mô phỏng các lỗi hệ thống cấp thấp hoặc luồng dữ liệu phức tạp.
- **Ví dụ cụ thể**: Rất khó để dùng Pact mô phỏng trường hợp server EShop bị Rate Limit (429 Too Many Requests) hoặc connection bị timeout sau 30 giây để xem Frontend xử lý UI spinner như thế nào.
- **Workaround**: Contract testing không nên dùng để test lỗi infrastructure. Để test các lỗi này, frontend nên tự tạo mock/stub riêng ở mức ứng dụng (ví dụ MSW - Mock Service Worker) hoặc chạy Chaos testing trên môi trường staging.

### 5. Chi phí bảo trì (Maintenance Overhead) khi số lượng endpoint tăng cao
- **Mô tả chi tiết**: Việc thiết lập state handler (`stateHandlers`) phía Provider rất tốn công. Khi số lượng endpoint và states tăng lên, file `provider.test.js` sẽ phình to ra rất nhanh.
- **Ví dụ cụ thể**: Endpoint `/api/checkout` cần giỏ hàng có sẵn sản phẩm, user phải có địa chỉ, voucher (nếu có) phải hợp lệ. Việc setup `stateHandlers` cho mỗi case (giỏ hàng hợp lệ, voucher hết hạn, user bị khóa...) đòi hỏi phải chèn trực tiếp vào DB, làm tăng đáng kể độ phức tạp của bài test.
- **Workaround**: Cần xây dựng các helper/factory function tái sử dụng để setup dữ liệu DB cho provider test, thay vì viết code setup data thô cho mỗi state. Áp dụng Pact Broker để quản lý tự động các phiên bản hợp đồng (versioning) khi dự án lớn.

### 6. Cơn ác mộng quản lý phiên bản (Versioning Hell)
- **Mô tả chi tiết**: Dẫn đến False Positives nếu không có công cụ như Pact Broker kiểm soát version giữa nhánh Provider và Consumer. Việc chia sẻ file Pact JSON thủ công dễ khiến Provider test với contract cũ.
- **Ví dụ cụ thể**: Consumer cập nhật contract thêm trường mới ở nhánh tính năng, nhưng Provider vẫn chạy test với file JSON từ nhánh main. Provider test Pass nhưng khi deploy lên môi trường thật thì gây lỗi do Consumer gọi API theo chuẩn mới.
- **Workaround**: Sử dụng Pact Broker (hoặc PactFlow) tích hợp vào CI/CD để quản lý ma trận phiên bản và sử dụng tính năng `can-i-deploy` trước khi phát hành.

### 7. Stateful Data Dependency (Xung đột dữ liệu State) gây Flaky Tests
- **Mô tả chi tiết**: Do việc tự tạo data trong `stateHandler` nhưng thiếu cơ chế dọn dẹp (teardown), làm các test case rớt ngẫu nhiên (flaky tests) khi chạy chung, vì trạng thái của DB đã bị test case trước đó thay đổi.
- **Ví dụ cụ thể**: Test case 1 setup "Giỏ hàng có sản phẩm A". Test case 2 cần "Giỏ hàng rỗng". Nếu test 1 chạy trước không dọn dẹp, test 2 chạy sẽ thấy giỏ hàng vẫn còn sản phẩm A và rớt test một cách ngẫu nhiên.
- **Workaround**: Đảm bảo mỗi `stateHandler` độc lập bằng cách luôn có cơ chế teardown (xóa dữ liệu) sau mỗi test case, hoặc sử dụng database in-memory riêng biệt cho mỗi lần chạy.
