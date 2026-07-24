# User Guide: EShop API & Contract Testing
**Nhóm thực hiện:** Group 05

*Lưu ý cho nhóm: Đây là file User Guide dùng chung (bản hoàn chỉnh nộp cho giảng viên). Các thành viên hãy copy/viết phần nội dung do mình phụ trách vào các mục tương ứng dưới đây.*

---

## 1. Giới thiệu (Introduction)
*(Cả nhóm cùng viết)*
Tài liệu này hướng dẫn chi tiết cách thiết lập, chạy thử nghiệm và kiểm thử tự động hệ thống backend EShop bằng các công cụ Postman (API Testing), AI Test Generation và Pact (Contract Testing) thông qua CI/CD Pipeline.

## 2. Yêu cầu hệ thống và Cài đặt (Prerequisites)
- **Node.js & npm:** Phiên bản 16.x trở lên.
- **Postman:** Dùng để import và chạy API tests.
- **Newman CLI:** Dùng để chạy Postman trong CI/CD.
- **Git:** Dùng để pull mã nguồn.

## 3. Hướng dẫn chạy Hệ thống Backend (SUT)
1. Mở terminal và chuyển hướng vào thư mục `eshop-sut/backend`.
2. Chạy lệnh: `npm install`
3. Chạy lệnh: `node server.js` (hoặc `npm start`).
4. Hệ thống sẽ lắng nghe ở địa chỉ: `http://localhost:3000`.

---

## 4. Hướng dẫn kiểm thử bằng Postman (API Testing) 
**(Phụ trách: Phạm Đức Toàn)**


### 1. Cài đặt và Thiết lập cơ bản

#### 1.1. Cài đặt Postman
- Truy cập [trang chủ Postman](https://www.postman.com/downloads/) và tải phiên bản phù hợp với hệ điều hành của bạn.
- Cài đặt và đăng nhập vào tài khoản Postman (hoặc sử dụng không cần tài khoản bằng cách click "Skip and go to the app").

#### 1.2. Import Collection và Environment
- Mở Postman, chọn **Import** ở góc trái phía trên.
- Chọn file `EShop_Collection_v2.json` và `EShop_Environment.json` từ thư mục `Group05_06/Toàn/`.
- Sau khi import thành công, ở thanh bên trái (Sidebar) sẽ xuất hiện collection **EShop Collection v2**.
- Ở góc phải phía trên, click vào dropdown chọn Environment và đổi thành **EShop_Environment** (môi trường này chứa biến `{{baseUrl}}` trỏ đến `http://localhost:3000`).

---

### 2. Cấu trúc của Collection

Collection **EShop Collection v2** được tổ chức thành 4 thư mục chính, phản ánh các chức năng cốt lõi của EShop:
- **Authentication:** Chứa các API liên quan đến đăng nhập.
- **Products:** Chứa API lấy danh sách và chi tiết sản phẩm.
- **Cart:** Chứa API thêm sản phẩm vào giỏ hàng.
- **Checkout:** Chứa API đặt hàng và thanh toán.

Mỗi request bên trong đã được lập trình sẵn kịch bản kiểm thử (test scripts) trong tab **Tests** để tự động kiểm tra Status Code, Schema, và Logic dữ liệu trả về (cả trường hợp đúng - Happy Path, và trường hợp sai/cố tình bắt lỗi - Negative/Edge Path).

---

### 3. Cách chạy kiểm thử (Thực thi Test)

#### 3.1. Chạy một Request đơn lẻ
1. Mở thư mục chứa API bạn muốn test (VD: `Authentication`).
2. Click chọn request `1.1 Happy Path — Đăng nhập thành công`.
3. Nhấn nút **Send** màu xanh ở góc phải.
4. Xem kết quả ở phía dưới màn hình:
   - Tab **Body:** Hiển thị dữ liệu API trả về (JSON).
   - Tab **Test Results:** Hiển thị kết quả tự động kiểm tra (VD: `PASS: Status code is 200`).


#### 3.2. Chạy tự động toàn bộ Collection (Collection Runner)
Thay vì chạy từng API thủ công, bạn có thể chạy toàn bộ kịch bản kiểm thử bằng một click:
1. Click vào biểu tượng dấu 3 chấm `...` bên cạnh tên collection **EShop Collection v2**.
2. Chọn **Run collection**.
3. Màn hình Runner sẽ hiện ra, liệt kê toàn bộ các requests. Bạn có thể giữ nguyên cài đặt mặc định (Iterations: 1, Delay: 0).
4. Nhấn nút **Run EShop Collection v2**.
5. Đọc bảng tóm tắt kết quả (Run Summary): Postman sẽ báo có bao nhiêu test passed (xanh) và bao nhiêu test failed (đỏ). 
   - Những test failed có thể là do API backend có lỗi (đã được ghi chú là "Bug" trong tên request).

---



---

## 5. Hướng dẫn sinh kịch bản Test bằng AI
**(Phụ trách: Nguyễn Quang Đăng Khoa)**

*(Khoa viết hướng dẫn cách dùng prompt để sinh code từ OpenAPI spec, cách đưa kết quả vào Postman).*

---

## 6. Hướng dẫn kiểm thử bằng Pact (Contract Testing)
**(Phụ trách: Nguyễn Nhật Nam)**

Tài liệu này hướng dẫn chi tiết cách chạy Consumer Test để sinh file hợp đồng (Pact file) và Provider Verification để kiểm chứng hợp đồng đối với hệ thống EShop.

### 1. Consumer Test (Tạo Hợp Đồng)

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

### 2. Provider Verification (Xác Minh Hợp Đồng)

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

---

## 7. Hướng dẫn tự động hóa (CI/CD Pipeline)
**(Phụ trách: Huỳnh Sĩ Luân)**

Hệ thống CI/CD của EShop được triển khai qua **GitHub Actions** nhằm tự động hóa quá trình chạy kiểm thử API và xác thực hợp đồng Pact mỗi khi mã nguồn thay đổi.

### 7.1. Cách kích hoạt Pipeline (Trigger Pipeline)
Pipeline được thiết lập tự động chạy trong hai trường hợp chính:
1. **Push:** Khi có bất kỳ commit nào được đẩy trực tiếp lên nhánh `main`.
2. **Pull Request:** Khi một thành viên tạo Pull Request (PR) yêu cầu gộp code từ nhánh tính năng (nhánh phụ) vào nhánh `main`. Quy trình này hoạt động như một chốt chặn bảo vệ.

### 7.2. Cách theo dõi tiến trình chạy trên GitHub Actions
1. Truy cập trang GitHub của dự án EShop.
2. Nhấp chọn tab **Actions** trên menu thanh công cụ chính.
3. Chọn run mới nhất ở danh sách phía dưới (tên run trùng với tên commit).
4. Click chọn job **test-api** ở cột bên trái để chuyển vào giao diện xem log.
5. Tại đây, bạn có thể quan sát trực tiếp kết quả chạy từng bước: cài đặt môi trường, chạy Pact Consumer, khởi động server backend, quét Newman API Test v2, và chạy Pact Provider Verification.

### 7.3. Cách tải và xem kết quả báo cáo (Newman & Pact Logs)
Quy trình tự động gom toàn bộ các tệp báo cáo sinh ra trong quá trình kiểm thử vào một thư mục `reports/` để đẩy lên thành Artifact.
1. Ở trang tóm tắt lần chạy của Actions (Run Summary), cuộn xuống cuối cùng tìm phần **Artifacts**.
2. Click vào tên **`EShop-Test-Reports`** để tải về tệp tin nén dạng `.zip`.
3. Giải nén tệp tin này, bạn sẽ nhận được 2 tệp báo cáo chính:
   * **`newman-report.html` (Báo cáo Newman):** Mở tệp tin này bằng bất kỳ trình duyệt web nào (Chrome, Firefox, Edge). Giao diện trực quan sẽ hiển thị toàn bộ kết quả kiểm thử API v2, bao gồm: tỷ lệ pass/fail của các assertion, chi tiết gói tin request/response và thời gian phản hồi của từng endpoint API.
   * **`pact-verification-report.txt` (Log xác minh Pact):** Mở bằng text editor. Tệp tin ghi nhận kết quả so khớp hợp đồng của Pact Provider. Nếu backend làm sai cam kết hợp đồng với Consumer, chi tiết lỗi mismatch (như sai kiểu dữ liệu hay thiếu key dữ liệu) sẽ được ghi cụ thể tại đây.

---

## 8. Các "Điểm mù" của công cụ (Failure Modes)
*(Lưu ý từ Rubric: Mục này phải tổng hợp Failure Mode của tất cả các công cụ vào chung một nơi, KHÔNG ĐƯỢC tách rời rạc từng phần).*

### 8.1. Postman Failure Modes
- **Lỗi so sánh kiểu dữ liệu ngầm định (Type Mismatch):** Khi API backend trả về dữ liệu bị sai kiểu (ví dụ trả về `price` dạng chuỗi `"28000000"` thay vì số nguyên `28000000`), nếu trong tab Tests bạn dùng `pm.expect(price).to.eql(28000000);`, test sẽ báo fail với thông báo mơ hồ như *AssertionError: expected '28000000' to deeply equal 28000000*. Người mới dùng rất dễ nhầm lẫn rằng logic API tính toán sai giá tiền, chứ không nhận ra đó là lỗi ép kiểu dữ liệu.
- **Quên cấu hình Environment/Token (Unresolved Variables):** Nếu bạn quên chọn Environment (đang ở trạng thái "No Environment"), các biến như `{{baseUrl}}` hay `{{token}}` sẽ không có giá trị. Tuy nhiên, Postman **không báo lỗi ngay** mà gửi nguyên cái chuỗi chữ `{{baseUrl}}` đi làm URL. Kết quả là hệ thống trả về lỗi `404 Not Found` hoặc `401 Unauthorized`. Người test sẽ mất nhiều thời gian debug API trong khi nguyên nhân chỉ là quên chọn cấu hình môi trường.
- **Lỗi "Silent Failure" trong script JavaScript (Bỏ qua lỗi ngầm):** Tab **Tests** trong Postman sử dụng mã JavaScript. Nếu bạn lỡ tay viết sai cú pháp (syntax error) hoặc gọi một hàm không tồn tại ở nửa đầu đoạn script, đoạn script đó sẽ bị crash. Tuy nhiên, **Postman không báo lỗi cú pháp đỏ rực lên màn hình UI**, mà nó chỉ âm thầm skip (bỏ qua) các câu lệnh `pm.test` bên dưới. Hệ quả là số lượng Test Cases trong tab "Test Results" bị giảm đi, và nếu các test chạy được đều Pass, UI vẫn hiện màu xanh "Pass" đánh lừa người dùng rằng mọi thứ đều ổn định.

### 8.2. AI Generation Failure Modes
*(Khoa liệt kê các lỗi ảo giác, code sinh sai logic của AI).*

### 8.3. Pact Failure Modes (Nam)
- **Silent Schema Change (Postel's Law):** Khác với sự chặt chẽ của Postman hay sự "hời hợt" của AI, Pact chỉ kiểm tra đúng những gì Consumer yêu cầu. Nếu Backend thêm trường dữ liệu mới (làm thay đổi ngầm luồng nghiệp vụ), Pact vẫn Pass.
- **Phụ thuộc 100% vào Consumer Test:** Tương tự như "Thiên kiến Happy-path" của AI, nếu Consumer quên viết contract cho trường hợp báo lỗi (VD: 401 Unauthorized), thì việc Backend vô tình gỡ bỏ xác thực vẫn sẽ lọt qua mắt Pact. 
- **Bùng nổ chi phí bảo trì (State Handlers):** Khi số lượng API tăng, việc duy trì trạng thái test (`stateHandlers`) phía Provider trở thành ác mộng. Nếu thiếu cơ chế teardown dọn dẹp data, dữ liệu rác sẽ gây xung đột, tạo ra "Flaky tests" (lỗi ngẫu nhiên), điều mà Postman hay AI ít gặp hơn trên môi trường test dùng một lần.
- **Bỏ qua Performance:** Dù API phản hồi chậm gấp 50 lần, Pact vẫn Pass miễn là schema đúng, trái ngược với Postman có thể set timeout cứng trong script.
