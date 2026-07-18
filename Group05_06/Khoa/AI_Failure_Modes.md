# AI Failure Modes & Human Mitigations
## Kịch bản thất bại của AI và các biện pháp khắc phục thủ công

## Mục đích

Trong quá trình sử dụng AI để tự động sinh **Postman Collection** phục vụ kiểm thử hệ thống **EShop**, nhóm đã phát hiện nhiều **blind spots** có thể dẫn đến **False Positive**, bỏ sót lỗi nghiệp vụ hoặc tạo cảm giác sai lệch về chất lượng hệ thống.

Tài liệu này tổng hợp:

- Các **AI Failure Modes**.
- Các **Manual Edge Cases** cần QA Engineer bổ sung thủ công nhằm tăng độ bao phủ kiểm thử và đảm bảo độ tin cậy của hệ thống.

---

# Phần 1. AI Failure Modes

## 1. Schema Validation vô giá trị (False Positives)

### Hiện tượng

Trong request **Checkout**, AI sinh ra đoạn kiểm tra JSON Schema như sau:

```javascript
var schema = {
    "type": "object",
    "properties": {},
    "additionalProperties": true
};
```

### Vấn đề

Schema trên không định nghĩa bất kỳ thuộc tính nào.

Điều này đồng nghĩa với việc:

- Object rỗng (`{}`)
- Object chứa thông báo lỗi
- Object chứa dữ liệu sai cấu trúc

đều được xem là **hợp lệ**.

### Hậu quả

Pipeline CI/CD có thể báo **PASS** mặc dù API đang trả về dữ liệu hoàn toàn sai định dạng hoặc lỗi nội bộ.

Ví dụ AI không kiểm tra các trường bắt buộc như:

- `order_id`
- `total_amount`
- `items`
- `status`

=> Đây là một dạng **False Positive** rất nguy hiểm.

---

## 2. Data Hallucination & Bỏ qua ràng buộc nghiệp vụ

### Hiện tượng

AI thường chỉ sinh payload đúng cú pháp theo API Specification nhưng bỏ qua "Business Rules".

### Ví dụ

API:

```
POST /api/apply-coupon
```

Theo Specification (Section 6.4), mã giảm giá có các điều kiện:

- `min_order_amount`
- `max_uses_per_user`

Tuy nhiên AI chỉ tạo request đúng cấu trúc mà không kiểm thử:

- Đơn hàng chưa đạt giá trị tối thiểu.
- Người dùng đã vượt quá số lần sử dụng.
- Mã giảm giá đã hết hiệu lực.
- Mã giảm giá áp dụng sai đối tượng.

### Hậu quả

Collection vẫn PASS nhưng không xác minh được Business Logic của hệ thống.

---

## 3. Thiếu tư duy kiểm thử phân quyền (RBAC Failure)

### Hiện tượng

Toàn bộ Collection được AI sinh ra chỉ sử dụng chung một biến:

```
{{token}}
```

AI mặc định mọi API đều được gọi trong môi trường đáng tin cậy.

### Những trường hợp AI bỏ sót

Ví dụ:

```
DELETE /api/admin/users/:id
```

AI không tạo các kịch bản như:

- User thường gọi API của Admin.
- Seller gọi API của Admin.
- Guest truy cập API yêu cầu xác thực.

### Hậu quả

Không phát hiện được các lỗi:

- Broken Access Control
- Privilege Escalation
- IDOR
- RBAC Misconfiguration

Đây đều là các lỗ hổng bảo mật thuộc nhóm **OWASP Top 10**.

---

## 4. Thiên kiến Happy-path (Thiếu Edge Cases)

### Hiện tượng

AI gần như luôn giả định người dùng nhập dữ liệu hợp lệ.

Collection chủ yếu bao gồm các trường hợp:

- Đúng kiểu dữ liệu
- Đúng định dạng
- Giá trị hợp lệ
- Luồng nghiệp vụ chuẩn

### Những trường hợp AI thường bỏ sót

- Giá trị âm
- Giá trị bằng 0
- Chuỗi rỗng
- Sai kiểu dữ liệu
- Thiếu trường bắt buộc
- Boundary Value
- Invalid Enum
- Null Value
- Payload bất thường

### Hậu quả

Validation Layer của Backend không được kiểm thử đầy đủ.

---

# Phần 2. Manual Edge Cases

Để khắc phục các hạn chế của AI, QA Engineer cần bổ sung các **Negative Test** và **Edge Cases** sau.

---

## 1. API Add to Cart

**Endpoint**

```
POST /api/cart
```

### Type Mismatch

- Truyền `product_id` dưới dạng String (`"1"`) thay vì Integer.

### Boundary Value

Kiểm thử trường `quantity` với các giá trị:

- `-1`
- `0`
- `1.5`

### Logic Validation

- Truyền `product_id` không tồn tại trong Database.

---

## 2. Order Lifecycle & Cart Logic

### Empty Cart

**Endpoint**

```
POST /api/checkout
```

**Kịch bản**

Người dùng chưa có sản phẩm trong giỏ hàng nhưng vẫn thực hiện Checkout.

**Kỳ vọng**

```
HTTP 400 Bad Request
```

Backend phải từ chối yêu cầu.

---

### Invalid Order Cancellation

**Endpoint**

```
PUT /api/orders/:id/cancel
```

**Kịch bản**

Thực hiện hủy đơn khi đơn hàng đã ở trạng thái:

- `shipping`
- `delivered`

**Kỳ vọng**

```
HTTP 400 Bad Request
```

Không được phép hủy.

---

### Invalid Order Status

Thông qua API của Admin, cố tình cập nhật trạng thái:

```json
{
    "status": "lost_in_space"
}
```

**Kỳ vọng**

Backend từ chối giá trị Enum không hợp lệ.

---

## 3. Security & Authorization

### Privilege Escalation

Sử dụng Bearer Token của **User** để gọi:

```
POST /api/admin/import-products
```

**Kỳ vọng**

```
HTTP 403 Forbidden
```

---

### IDOR (Insecure Direct Object Reference)

Sử dụng Token của **User A** để truy cập:

```
GET /api/orders/:id
```

trong đó `id` thuộc về **User B**.

**Kỳ vọng**

```
HTTP 403 Forbidden
```

hoặc

```
HTTP 404 Not Found
```

---

### Invalid Authentication

Thực hiện các trường hợp:

- Token sai chữ ký.
- Token hết hạn.
- Không gửi Header `Authorization`.

**Kỳ vọng**

```
HTTP 401 Unauthorized
```

---

## 4. Coupon Edge Cases

### Minimum Order Validation

Áp dụng mã giảm giá khi:

```
total_amount < min_order_amount
```

**Kỳ vọng**

Backend từ chối áp dụng mã.

---

### Maximum Usage Validation

Áp dụng mã giảm giá đã vượt quá:

```
max_uses_per_user
```

**Kỳ vọng**

Backend từ chối yêu cầu.

---

### Duplicate Coupon Request

Gửi liên tiếp hai request áp dụng cùng một mã giảm giá vào cùng một đơn hàng.

**Mục tiêu kiểm thử**

Kiểm tra Backend có:

- Cộng dồn phần trăm giảm giá.
- Tính toán sai tổng tiền.
- Sinh lỗi Race Condition hoặc Logic Error.

---

# Kết luận

Các Postman Collection do AI sinh tự động có thể giúp tăng tốc quá trình xây dựng test ban đầu, nhưng **không thể thay thế hoàn toàn tư duy kiểm thử của QA Engineer**.

Để đảm bảo chất lượng hệ thống, Collection cần được bổ sung thủ công các nhóm kiểm thử sau:

- Business Logic Validation
- Negative Testing
- Boundary Value Analysis
- Security Testing
- RBAC Verification
- IDOR Testing
- Authentication & Authorization Testing
- Order Lifecycle Validation
- Coupon Rule Validation

Việc kết hợp **AI-generated Test Cases** với **Manual Edge Cases** giúp nâng cao độ bao phủ kiểm thử, giảm False Positive và tăng độ tin cậy của quy trình CI/CD.
