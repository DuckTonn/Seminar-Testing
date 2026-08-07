# Activity Worksheet: AI, API & Contract Testing, CI/CD (15-20 Phút)

**Mục tiêu:** Sinh viên thực hành tự động tạo test bằng AI, nhận diện "Điểm mù" kịch bản trên Postman, trải nghiệm luồng chạy Contract Testing thực tế bằng Pact, và xem kết quả tích hợp CI/CD với Github Actions.

**Yêu cầu chuẩn bị:**
- Đã cài đặt Postman, Node.js, Git.
- Đã clone source code `eshop-sut` (có thể fork về tài khoản Github cá nhân).

---

## PHẦN 1: TẠO TEST BẰNG AI VÀ API TESTING VỚI POSTMAN (5 Phút)

**Bước 1: Sử dụng AI để tạo Test script**
1. Mở Postman, import file `EShop_Collection_v2.json`. Chọn Environment là **EShop_Environment**.
2. Mở request **"GET Product List"**, chọn tab **Tests**.
3. Nếu bạn đang có tính năng **Postbot** (biểu tượng AI góc phải dưới của Postman), hãy click vào và chọn `Add tests to this request`. AI sẽ tự động sinh ra các test case (ví dụ: kiểm tra status 200, thời gian phản hồi, kiểu dữ liệu).
   *(Nếu không có Postbot, hãy thử copy JSON response của API đưa cho ChatGPT/Gemini với prompt: "Viết test script cho Postman để kiểm tra status code, và validate response JSON schema của API này" rồi dán vào Postman).*

**Bước 2: Trải nghiệm "Silent Failure" trong Postman**
1. Chèn thêm đoạn code sau vào cuối tab **Tests** để cố ý tạo lỗi (Silent Failure):

   ```javascript
   pm.test("Status code is 200", function () {
     pm.response.to.have.status(200);
   });

   // Dòng code cố ý viết sai cú pháp để tạo Silent Failure
   pm.expect(abc).to.be.equal(123);

   pm.test("Dữ liệu là một mảng", function () {
     pm.expect(pm.response.json()).to.be.an("array");
   });
   ```

2. Nhấn **Send** và quan sát tab **Test Results**.
   - _Câu hỏi:_ Bạn có thấy Postman báo lỗi đỏ rực không? Có bao nhiêu test case thực sự được chạy?
   - _Đáp án:_ Postman báo Pass màu xanh nhưng thực chất đã bỏ qua test case thứ 2.
3. Xóa dòng lỗi đi, chạy lại để đảm bảo tất cả test case đều Pass. Đừng bao giờ tin nút Pass màu xanh nếu chưa đếm số lượng Test Case!

---

## PHẦN 2: CONTRACT TESTING BẰNG PACT (5 Phút)

**Bước 1: Khởi động Backend**
1. Mở terminal mới, di chuyển vào thư mục dự án `eshop-sut/backend`.
2. Chạy lệnh:
   ```bash
   npm install
   node server.js
   ```

**Bước 2: Chạy Consumer Test (Tạo hợp đồng)**
1. Mở một terminal khác, di chuyển vào thư mục `eshop-sut/contract_testing`.
2. Chạy lệnh:
   ```bash
   npm install
   npm run test:pact
   ```
3. Xem thông báo thành công. Mở thư mục `contract_testing/pacts/`, bạn sẽ thấy một file JSON (ví dụ: `EshopConsumer-EShopBackend.json`). Mở file này ra để xem cấu trúc "Hợp đồng" mà Pact vừa sinh ra (chứa các Matchers, Rules do Consumer mong đợi).

**Bước 3: Chạy Provider Verification (Xác minh hợp đồng)**
1. Đảm bảo rằng server Backend của bạn vẫn đang chạy ở port 3000.
2. Tại terminal (đang ở thư mục `contract_testing`), chạy tiếp lệnh:
   ```bash
   npm run test:provider
   ```
3. Quan sát kết quả trên terminal. Pact đã tự động đọc file JSON hợp đồng, gửi request vào localhost:3000 và so sánh kết quả.
4. Nếu màn hình hiển thị Pass màu xanh lá cho tất cả các `interactions`, chúc mừng bạn đã hoàn thành vòng lặp Contract Testing!

---

## PHẦN 3: TÍCH HỢP CI VỚI GITHUB ACTIONS (5 Phút)

**Bước 1: Khám phá Github Actions Workflow**
1. Mở thư mục `.github/workflows/` trong dự án `eshop-sut`.
2. Mở file `newman.yml`. Đây là kịch bản CI tự động sẽ làm các nhiệm vụ:
   - Cài đặt Node.js và các dependencies.
   - Chạy tự động **Pact Consumer Tests**.
   - Khởi động Backend server.
   - Chạy **Postman tests** bằng CLI `newman` và xuất report giao diện `htmlextra`.
   - Chạy **Pact Provider Verification**.
   - Tải các báo cáo (Test Reports) lên Github làm Artifacts.

**Bước 2: Kích hoạt CI Pipeline**
1. Đảm bảo bạn đang làm việc trên repo Github của riêng bạn (đã fork/push code lên repo cá nhân).
2. Tạo một thay đổi nhỏ vào code (ví dụ: sửa README.md hoặc file Worksheet này).
3. Commit và Push code lên nhánh `main`:
   ```bash
   git add .
   git commit -m "Trigger CI pipeline"
   git push origin main
   ```
4. Lên trang Github của bạn, chuyển sang tab **Actions**. Bạn sẽ thấy một workflow có tên "Newman API Tests" đang chạy tự động.
5. Sau khi workflow chạy thành công (mất khoảng 1-2 phút), bấm vào workflow đó, cuộn xuống dưới cùng phần **Artifacts** để tải về `EShop-Test-Reports.zip`. Giải nén và mở file `newman-report.html` để xem báo cáo kiểm thử rất chuyên nghiệp.

---

**Kết luận:** 
- AI hỗ trợ sinh test case nhanh chóng.
- Postman / Newman giúp kiểm tra API thực tế.
- Contract Testing (Pact) là chốt chặn phòng ngừa hai đầu Frontend/Backend vô tình làm gãy cấu trúc data của nhau.
- CI/CD (Github Actions) liên kết toàn bộ mọi thứ lại để chạy tự động mỗi khi có thay đổi.
