# Báo cáo các trường hợp vi phạm hợp đồng (Contract Violations Report)

Tài liệu này ghi nhận 5 trường hợp vi phạm hợp đồng (Contract Violations) có thể xảy ra hoặc đã phát hiện trong quá trình chạy Provider Verification cho endpoint `POST /api/cart`.

---

### 1. Vi phạm mã trạng thái HTTP (Wrong Status Code)
- **Mô tả**: Consumer mong đợi HTTP status 201 (Created) khi thêm sản phẩm vào giỏ hàng thành công, nhưng Backend (Provider) thực tế lại trả về HTTP status 200 (OK).
- **Endpoint bị ảnh hưởng**: `POST /api/cart`
- **Loại violation**: Wrong status code
- **Cách phát hiện**: Pact verification output báo lỗi `StatusMismatch`.
  ```log
  Failures:
  1.2) has status code 201
         expected 201 but was 200
  ```
- **Mức độ nghiêm trọng**: Medium (Consumer có thể không nhận diện được giao dịch thành công nếu kiểm tra strict `=== 201`).

---

### 2. Thiếu trường dữ liệu bắt buộc trong phản hồi (Missing Required Field)
- **Mô tả**: Consumer mong đợi phản hồi trả về đối tượng chứa `productId` và `quantity`. Tuy nhiên, Backend lại trả về `{ "message": "Added to cart" }`, dẫn đến việc Consumer không nhận được các trường cần thiết để xử lý logic tiếp theo.
- **Endpoint bị ảnh hưởng**: `POST /api/cart`
- **Loại violation**: Missing field
- **Cách phát hiện**: Pact verification output báo lỗi `BodyMismatch`.
  ```log
  1.1) has a matching body
         $ -> Actual map is missing the following keys: productId, quantity
  ```
- **Mức độ nghiêm trọng**: Critical (Consumer bị crash hoặc không thể hiển thị giỏ hàng sau khi thêm).

---

### 3. Sai kiểu dữ liệu (Wrong Data Type)
- **Mô tả**: Backend thay đổi kiểu dữ liệu của trường `quantity` trong response từ `integer` sang `string` (ví dụ: `"2"` thay vì `2`). Consumer đang strict kiểm tra kiểu `integer` (sử dụng `MatchersV3.integer`).
- **Endpoint bị ảnh hưởng**: `POST /api/cart`
- **Loại violation**: Wrong data type (Schema mismatch)
- **Cách phát hiện**: Pact verification output báo lỗi `TypeMismatch`.
  ```log
  1.1) has a matching body
         $.quantity -> Expected an integer but got a string: "2"
  ```
- **Mức độ nghiêm trọng**: High (Có thể gây lỗi tính toán hoặc ép kiểu sai ở phía frontend/consumer).

---

### 4. Thay đổi tên trường dữ liệu (Field Name Change)
- **Mô tả**: Backend quyết định đổi tên trường trả về từ `productId` thành `product_id` (để chuẩn hóa theo chuẩn snake_case), nhưng Consumer chưa được cập nhật và vẫn mong đợi `productId`.
- **Endpoint bị ảnh hưởng**: `POST /api/cart`
- **Loại violation**: Breaking change / Missing field
- **Cách phát hiện**: Pact verification output.
  ```log
  1.1) has a matching body
         $ -> Actual map is missing the following keys: productId
  ```
- **Mức độ nghiêm trọng**: High (Consumer không thể truy xuất đúng thuộc tính, dữ liệu hiển thị `undefined`).

---

### 5. Backend thêm trường bắt buộc vào Request (Extra Required Request Field)
- **Mô tả**: Backend được nâng cấp và yêu cầu Consumer phải gửi thêm trường `deviceId` trong request body để chống fraud. Consumer gửi request theo contract cũ (chỉ có `productId` và `quantity`), dẫn đến Backend từ chối request (trả về 400 Bad Request).
- **Endpoint bị ảnh hưởng**: `POST /api/cart`
- **Loại violation**: Breaking change (Request validation failure)
- **Cách phát hiện**: Pact verification output.
  ```log
  1.2) has status code 201
         expected 201 but was 400
  ```
- **Mức độ nghiêm trọng**: Critical (API hoàn toàn không thể sử dụng được đối với Consumer cũ).
