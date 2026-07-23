# Activity Worksheet: API & Contract Testing (10 Phút)

**Mục tiêu:** Sinh viên tự tay cấu hình Postman để nhận diện "Điểm mù" kịch bản, sau đó trải nghiệm luồng chạy Contract Testing thực tế bằng Pact.

**Yêu cầu chuẩn bị:**

- Đã cài đặt Postman, Node.js.
- Đã clone source code `eshop-sut` và chạy backend ở `localhost:3000`.

---

## PHẦN 1: API TESTING BẰNG POSTMAN (5 Phút)

**Bước 1: Trải nghiệm "Silent Failure" trong Postman**

1. Mở Postman, import file `EShop_Collection.json`. Chọn Environment là **EShop_Environment**.
2. Mở request **"GET Product List"**, mở tab **Tests** và dán đoạn code sau:

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

3. Nhấn **Send** và quan sát tab **Test Results**.
   - _Câu hỏi:_ Bạn có thấy Postman báo lỗi cú pháp đỏ rực không? Có bao nhiêu test case thực sự được chạy?
   - _Đáp án:_ Postman báo Pass màu xanh nhưng thực chất đã bỏ qua test case thứ 2.
4. Xóa dòng lỗi đi, chạy lại để đảm bảo cả 2 test case đều Pass. Đừng bao giờ tin nút Pass màu xanh nếu chưa đếm số lượng Test Case!

---

## PHẦN 2: CONTRACT TESTING BẰNG PACT (5 Phút)

**Bước 2: Chạy Consumer Test (Tạo hợp đồng)**

1. Mở terminal mới, di chuyển vào thư mục dự án `eshop-sut`.
2. Chạy lệnh:
   ```bash
   npx jest contract_testing/test/*.consumer.test.js
   ```
3. Xem thông báo thành công. Mở thư mục `contract_testing/pacts/`, bạn sẽ thấy một file JSON (ví dụ: `EshopConsumer-EShopBackend.json`). Mở file này ra để xem cấu trúc "Hợp đồng" mà Pact vừa sinh ra (chứa các Matchers, Rules).

**Bước 3: Chạy Provider Verification (Xác minh hợp đồng)**

1. Chắc chắn rằng server Backend của bạn vẫn đang chạy ở port 3000.
2. Tại terminal, chạy tiếp lệnh:
   ```bash
   npx jest contract_testing/test/provider.test.js
   ```
3. Quan sát kết quả trên terminal. Pact đã tự động đọc file JSON, setup trạng thái, gửi request vào localhost:3000 và so sánh kết quả.
4. Nếu màn hình hiển thị Pass xanh lá cho tất cả các `interactions`, chúc mừng bạn đã hoàn thành vòng lặp Contract Testing!

---

**Kết luận:** Postman giúp kiểm tra nhanh chóng bằng tay, nhưng Contract Testing (Pact) mới là chốt chặn tự động hóa an toàn để Frontend và Backend không vô tình "phá vỡ" kết nối của nhau.
