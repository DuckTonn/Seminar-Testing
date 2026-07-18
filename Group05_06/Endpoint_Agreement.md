# 📋 Bảng Đặc tả Endpoint Dùng Chung (Endpoint Agreement Document)
---

## Mục đích
> [!IMPORTANT]
> **Quy ước chung:**
> - Endpoint thực tế dùng prefix `/api/` (ví dụ: `/api/login`, `/api/products`).
> - Token JWT được lấy từ `POST /api/login` với seed data: `test@eshop.com` / `Test1234!` (user) hoặc `admin@eshop.com` / `Admin123!` (admin).
> - Seed data có sẵn 5 products (ID 1–5), 2 users, 3 categories, 4 coupons.

---

## 1. POST /api/login — Authentication

| # | Tên Test Case / Scenario | Expected HTTP Status | Nhiệm vụ Postman — Toàn | Nhiệm vụ Pact — Nam (Provider State & Matchers) |
|---|---|---|---|---|
| 1.1 | **Happy Path** — Đăng nhập thành công với credentials đúng | `200 OK` | **Request:** `{"email": "test@eshop.com", "password": "Test1234!"}` · **Assert status:** `200` · **Assert body:** `message == "Login successful"`, `token` là string non-empty, `user` object chứa `id`, `name`, `email`, `role` · **Assert schema:** `token` (string), `user.id` (integer), `user.role` (string) · **Lưu `token` vào Collection Variable** | **Provider State:** `"a user exists with email test@eshop.com and password Test1234!"` · **Matchers:** `like("Login successful")` cho `message`, `like("eyJhbG...")` cho `token`, `like(1)` cho `user.id`, `like("user")` cho `user.role`, `eachKeyLike` cho user object |
| 1.2 | **Negative** — Sai password | `401 Unauthorized` | **Request:** `{"email": "test@eshop.com", "password": "WrongPass!"}` · **Assert status:** `401` · **Assert body:** `error == "Invalid email or password"` | **Provider State:** `"a user exists with email test@eshop.com but password is incorrect"` · **Matchers:** `like("Invalid email or password")` cho `error` |
| 1.3 | **Negative** — Email không tồn tại | `401 Unauthorized` | **Request:** `{"email": "noexist@eshop.com", "password": "any"}` · **Assert status:** `401` · **Assert body:** `error == "Invalid email or password"` | **Provider State:** `"no user exists with email noexist@eshop.com"` · **Matchers:** `like("Invalid email or password")` cho `error` |
| 1.4 | **Negative** — Thiếu field `email` | `401 Unauthorized` | **Request:** `{"password": "Test1234!"}` · **Assert status:** `401` · **Assert body chứa** `error` | **Provider State:** `"login request is missing email field"` · **Matchers:** `like("Invalid email or password")` cho `error` |
| 1.5 | **Negative** — Thiếu field `password` | `401 Unauthorized` | **Request:** `{"email": "test@eshop.com"}` · **Assert status:** `401` · **Assert body chứa** `error` | **Provider State:** `"login request is missing password field"` · **Matchers:** `like("Invalid email or password")` cho `error` |
| 1.6 | **Negative** — Body rỗng / không gửi body | `401 Unauthorized` | **Request:** `{}` · **Assert status:** `401` · **Assert body chứa** `error` | **Provider State:** `"login request has empty body"` · **Matchers:** `like("Invalid email or password")` cho `error` |
| 1.7 | **Edge** — Tài khoản bị khóa (locked) | `403 Forbidden` | **Pre-condition:** Login sai 3+ lần trước đó · **Request:** `{"email": "test@eshop.com", "password": "Test1234!"}` · **Assert status:** `403` · **Assert body:** `error` chứa "bị khóa" | **Provider State:** `"user test@eshop.com account is locked"` · **Matchers:** `term("Tài khoản đã bị khóa. Vui lòng thử lại sau.")` cho `error` |

---

## 2. GET /api/products — Lấy Danh Sách Sản Phẩm

| # | Tên Test Case / Scenario | Expected HTTP Status | Nhiệm vụ Postman — Toàn | Nhiệm vụ Pact — Nam (Provider State & Matchers) |
|---|---|---|---|---|
| 2.1 | **Happy Path** — Lấy toàn bộ danh sách sản phẩm | `200 OK` | **Request:** `GET /api/products` (no query) · **Assert status:** `200` · **Assert body:** là JSON array, `length >= 1` · **Assert schema mỗi item:** `id` (integer), `name` (string), `price` (integer), `description` (string), `imageUrl` (string), `category_id` (integer) | **Provider State:** `"products exist in the database"` · **Matchers:** `eachLike({id: like(1), name: like("iPhone 15"), price: like(30000000), description: like("..."), imageUrl: like("https://..."), category_id: like(1)})` — min 1 item |
| 2.2 | **Happy Path** — Tìm kiếm sản phẩm bằng `?search=` (có kết quả) | `200 OK` | **Request:** `GET /api/products?search=iPhone` · **Assert status:** `200` · **Assert body:** là JSON array, `length >= 1`, mỗi item `name` chứa "iPhone" | **Provider State:** `"a product with name containing 'iPhone' exists"` · **Matchers:** `eachLike({id: like(1), name: term({generate: "iPhone 15 Pro Max", matcher: ".*iPhone.*"})})` |
| 2.3 | **Edge** — Tìm kiếm không có kết quả | `200 OK` | **Request:** `GET /api/products?search=XYZNONEXIST` · **Assert status:** `200` · **Assert body:** là JSON array rỗng `[]` | **Provider State:** `"no product matches search term 'XYZNONEXIST'"` · **Matchers:** Response body = `[]` (empty array) |
| 2.4 | **Edge** — Tìm kiếm với query string rỗng `?search=` | `200 OK` | **Request:** `GET /api/products?search=` · **Assert status:** `200` · **Assert body:** là JSON array (trả về tất cả sản phẩm) | **Provider State:** `"products exist and search query is empty"` · **Matchers:** `eachLike({...})` — same as 2.1 |

---

## 3. GET /api/products/:id — Xem Chi Tiết Sản Phẩm

| # | Tên Test Case / Scenario | Expected HTTP Status | Nhiệm vụ Postman — Toàn | Nhiệm vụ Pact — Nam (Provider State & Matchers) |
|---|---|---|---|---|
| 3.1 | **Happy Path** — Lấy sản phẩm với ID hợp lệ (ID lẻ) | `200 OK` | **Request:** `GET /api/products/1` · **Assert status:** `200` · **Assert body:** `id == 1`, `name` là string, `price` là integer, `description` là string · **Assert schema:** tất cả fields đúng type | **Provider State:** `"a product with id 1 exists"` · **Matchers:** `like(1)` cho `id`, `like("iPhone 15 Pro Max")` cho `name`, `like(30000000)` cho `price` (integer) |
| 3.2 | **Edge/Bug** — Lấy sản phẩm với ID chẵn (price trả về string thay vì integer) | `200 OK` | **Request:** `GET /api/products/2` · **Assert status:** `200` · **Assert body:** `id == 2` · ⚠️ **Lưu ý bug:** `price` trả về dạng string `"28000000"` thay vì integer `28000000` khi `id` là số chẵn · **Assert ghi nhận bug** | **Provider State:** `"a product with id 2 exists (even id — known bug: price returned as string)"` · **Matchers:** Tùy mục đích: `like("28000000")` nếu test contract đúng behavior hiện tại, hoặc `like(28000000)` nếu test contract mong đợi (sẽ fail → ghi Contract Violation) |
| 3.3 | **Negative** — ID không tồn tại | `200 OK` ⚠️ | **Request:** `GET /api/products/99999` · **Assert status:** `200` (⚠️ server trả `200` với body `{}` thay vì `404` — đây là bug tiềm ẩn) · **Assert body:** `{}` (empty object) | **Provider State:** `"no product with id 99999 exists"` · **Matchers:** Response body = `{}` · ⚠️ **Ghi nhận bug:** Lẽ ra phải trả `404` |
| 3.4 | **Edge** — ID là string không hợp lệ | `200 OK` ⚠️ | **Request:** `GET /api/products/abc` · **Assert status:** Kiểm tra response (server có thể trả `200 {}` hoặc error) · **Ghi nhận behavior** | **Provider State:** `"product id is non-numeric string 'abc'"` · **Matchers:** Ghi nhận actual response |

---

## 4. POST /api/cart — Thêm Vào Giỏ Hàng

| # | Tên Test Case / Scenario | Expected HTTP Status | Nhiệm vụ Postman — Toàn | Nhiệm vụ Pact — Nam (Provider State & Matchers) |
|---|---|---|---|---|
| 4.1 | **Happy Path** — Thêm sản phẩm vào giỏ hàng thành công | `200 OK` | **Request:** Header `Authorization: Bearer {{token}}` · Body: `{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 2}` · **Assert status:** `200` · **Assert body:** `message == "Added to cart"` | **Provider State:** `"user is authenticated and cart is accessible"` · **Matchers:** `like("Added to cart")` cho `message` |
| 4.2 | **Negative** — Không có token (Unauthorized) | `401 Unauthorized` | **Request:** Không gửi header `Authorization` · Body: `{"id": 1, "name": "Test", "price": 100, "quantity": 1}` · **Assert status:** `401` · **Assert body:** `error == "Unauthorized"` | **Provider State:** `"no authentication token is provided"` · **Matchers:** `like("Unauthorized")` cho `error` |
| 4.3 | **Negative** — Token không hợp lệ / hết hạn | `403 Forbidden` | **Request:** Header `Authorization: Bearer INVALID_TOKEN_123` · **Assert status:** `403` · **Assert body:** `error == "Forbidden"` | **Provider State:** `"authentication token is invalid or expired"` · **Matchers:** `like("Forbidden")` cho `error` |
| 4.4 | **Edge** — Body rỗng (vẫn add được — no validation) | `200 OK` ⚠️ | **Request:** Header `Authorization: Bearer {{token}}` · Body: `{}` · **Assert status:** `200` · **Assert body:** `message == "Added to cart"` · ⚠️ **Ghi nhận bug:** Server không validate body, chấp nhận empty object | **Provider State:** `"user is authenticated, cart request has empty body"` · **Matchers:** `like("Added to cart")` · ⚠️ **Ghi nhận Contract Violation tiềm ẩn:** API chấp nhận body không hợp lệ |
| 4.5 | **Edge** — Thiếu các field bắt buộc (ví dụ thiếu `id`, `quantity`) | `200 OK` ⚠️ | **Request:** Header `Authorization: Bearer {{token}}` · Body: `{"name": "Test"}` · **Assert status:** `200` · ⚠️ **Ghi nhận:** Server push body trực tiếp vào cart mà không validate | **Provider State:** `"user is authenticated, cart request missing required fields"` · **Matchers:** `like("Added to cart")` · **Ghi nhận:** Behavior bất thường — thiếu validation |
| 4.6 | **Edge** — Quantity âm hoặc bằng 0 | `200 OK` ⚠️ | **Request:** Header `Authorization: Bearer {{token}}` · Body: `{"id": 1, "name": "Test", "price": 100, "quantity": -1}` · **Assert status:** `200` · ⚠️ **Ghi nhận bug:** Quantity âm được chấp nhận | **Provider State:** `"user is authenticated, quantity is negative"` · **Matchers:** `like("Added to cart")` · **Ghi nhận Contract Violation** |

---

## 5. POST /api/checkout — Đặt Hàng (Orders)

> [!NOTE]
> Theo API spec, endpoint đặt hàng thực tế là `POST /api/checkout` (không phải `POST /api/orders`). Tài liệu phân công ghi `POST /orders` nhưng implementation thực tế là `/api/checkout`. **Cả hai bên cần thống nhất dùng `/api/checkout`.**

| # | Tên Test Case / Scenario | Expected HTTP Status | Nhiệm vụ Postman — Toàn | Nhiệm vụ Pact — Nam (Provider State & Matchers) |
|---|---|---|---|---|
| 5.1 | **Happy Path** — Checkout thành công | `200 OK` | **Request:** Header `Authorization: Bearer {{token}}` · Body: `{"total_amount": 200000, "shipping_address": "123 Le Loi, TP.HCM"}` · **Assert status:** `200` · **Assert body:** `message == "Checkout successful"`, `orderId` là integer > 0 · **Assert schema:** `orderId` (integer) | **Provider State:** `"user is authenticated and ready to checkout"` · **Matchers:** `like("Checkout successful")` cho `message`, `like(1)` cho `orderId` (integer matcher) |
| 5.2 | **Negative** — Không có token (Unauthorized) | `401 Unauthorized` | **Request:** Không gửi `Authorization` · Body: `{"total_amount": 200000, "shipping_address": "..."}` · **Assert status:** `401` · **Assert body:** `error == "Unauthorized"` | **Provider State:** `"no authentication token is provided for checkout"` · **Matchers:** `like("Unauthorized")` cho `error` |
| 5.3 | **Negative** — Token không hợp lệ | `403 Forbidden` | **Request:** Header `Authorization: Bearer BAD_TOKEN` · **Assert status:** `403` · **Assert body:** `error == "Forbidden"` | **Provider State:** `"checkout with invalid authentication token"` · **Matchers:** `like("Forbidden")` cho `error` |
| 5.4 | **Edge** — Body thiếu `total_amount` | `200 OK` ⚠️ | **Request:** Header `Authorization: Bearer {{token}}` · Body: `{"shipping_address": "123 ABC"}` · **Assert status:** Kiểm tra (server có thể accept với `total_amount = null`) · ⚠️ **Ghi nhận behavior** | **Provider State:** `"user is authenticated, checkout missing total_amount"` · **Matchers:** Ghi nhận actual behavior · ⚠️ Đây là bug tiềm ẩn nếu accept |
| 5.5 | **Edge** — Body thiếu `shipping_address` | `200 OK` ⚠️ | **Request:** Header `Authorization: Bearer {{token}}` · Body: `{"total_amount": 100000}` · **Assert status:** Kiểm tra · ⚠️ **Ghi nhận behavior** | **Provider State:** `"user is authenticated, checkout missing shipping_address"` · **Matchers:** Ghi nhận actual behavior |
| 5.6 | **Edge** — Body rỗng | `200 OK` ⚠️ | **Request:** Header `Authorization: Bearer {{token}}` · Body: `{}` · **Assert status:** Kiểm tra · ⚠️ **Ghi nhận bug nếu accept** | **Provider State:** `"user is authenticated, checkout with empty body"` · **Matchers:** Ghi nhận actual behavior |
| 5.7 | **Edge** — `total_amount` là số âm | `200 OK` ⚠️ | **Request:** Header `Authorization: Bearer {{token}}` · Body: `{"total_amount": -50000, "shipping_address": "..."}` · **Assert status:** Kiểm tra · ⚠️ **Ghi nhận bug nếu accept** | **Provider State:** `"user is authenticated, checkout with negative total_amount"` · **Matchers:** Ghi nhận actual behavior |

---

## Tổng hợp: Danh Sách Bugs / Contract Violations Tiềm Ẩn Cần Ghi Nhận

> [!WARNING]

| # | Bug / Anomaly | Endpoint | Mô tả |
|---|---|---|---|
| B1 | `price` trả về string cho ID chẵn | `GET /api/products/:id` | Line 162: `if (row.id % 2 === 0) row.price = row.price.toString()` — Cố tình tạo bug, `price` trả về string thay vì integer khi product ID là số chẵn |
| B2 | Product không tồn tại trả `200 {}` | `GET /api/products/:id` | Line 161: `if (!row) return res.status(200).json({})` — Lẽ ra phải trả `404` |
| B3 | Cart không validate body | `POST /api/cart` | Line 293: `userCarts[userId].push(req.body)` — Chấp nhận bất kỳ body nào, kể cả `{}` |
| B4 | Checkout không validate fields | `POST /api/checkout` | Không kiểm tra `total_amount` hay `shipping_address` có tồn tại / hợp lệ |
| B5 | Login tăng `login_attempts` sai | `POST /api/login` | Line 54: `const newAttempts = user.login_attempts + 2` — Tăng 2 thay vì 1 mỗi lần sai |
| B6 | Canceled → Delivered valid | `PUT /api/admin/orders/:id/status` | Line 550-551: Cho phép chuyển từ `canceled` sang `delivered` (bug logic) |

---
