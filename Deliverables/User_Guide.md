# Báo cáo Chuyên đề & Sổ tay Hướng dẫn Cốt lõi (User Guide)
**Đề tài:** T06 - API & Contract Testing  
**Hệ thống:** EShop Backend (Node.js/Express)  
**Nhóm thực hiện:** Group 05 (Phạm Đức Toàn, Nguyễn Quang Đăng Khoa, Nguyễn Nhật Nam, Huỳnh Sĩ Luân)

---

## Mục lục
1. [Tóm tắt Cấp cao & Kiến trúc Hệ thống (Executive Summary)](#1-tóm-tắt-cấp-cao--kiến-trúc-hệ-thống)
2. [Nhập môn API Testing (Dành cho người mới)](#2-nhập-môn-api-testing-dành-cho-người-mới)
3. [Nền tảng Lý thuyết & Chiến lược Kiểm thử (Theoretical Foundations)](#3-nền-tảng-lý-thuyết--chiến-lược-kiểm-thử)
4. [Yêu cầu Hệ thống & Thiết lập Môi trường (Prerequisites & Setup)](#4-yêu-cầu-hệ-thống--thiết-lập-môi-trường)
5. [Kiểm thử API Chuyên sâu với Postman (Manual & Scripted Testing)](#5-kiểm-thử-api-chuyên-sâu-với-postman)
   - [5.6 Data-Driven Testing với CSV](#56-data-driven-testing-với-csv-chạy-1-test-với-nhiều-bộ-dữ-liệu)
   - [5.7 Diff AI Scaffold vs Manual (Milestone M3)](#57-milestone-m3-diff-ai-scaffold-vs-manual-collection)
6. [Sinh kịch bản tự động bằng Trí tuệ Nhân tạo (AI-Augmented Generation)](#6-sinh-kịch-bản-tự-động-bằng-trí-tuệ-nhân-tạo)
   - [6.3 Postbot — AI Inline trong Postman](#63-postbot--ai-inline-ngay-trong-postman)
7. [Kiểm thử Hợp đồng Giao tiếp với Pact (Contract Testing)](#7-kiểm-thử-hợp-đồng-giao-tiếp-với-pact)
8. [Tích hợp Liên tục (Continuous Integration với GitHub Actions)](#8-tích-hợp-liên-tục-với-github-actions)
9. [Phân tích Điểm mù (Failure Modes - 5 Case Studies)](#9-phân-tích-điểm-mù-failure-modes---5-case-studies)
10. [Đúc kết và Bài học Kinh nghiệm (Lessons Learned)](#10-đúc-kết-và-bài-học-kinh-nghiệm)

---



<!-- ================================================================ -->
<!-- # PHAN CUA TOAN (1) - Section 1,2,3,4: Executive Summary / Intro / Theory / Setup -->
<!-- Toan chiu trach nhiem: Section 1 den Section 4 (phan kien truc va setup chung) -->
<!-- Xoa comment nay khi da hoan thien va ready to merge -->
<!-- ================================================================ -->


## 1. Tóm tắt Cấp cao & Kiến trúc Hệ thống
Hệ thống EShop được xây dựng dựa trên kiến trúc Microservices (hoặc Client-Server tách rời hoàn toàn). Toàn bộ giao tiếp giữa Frontend (Web/Mobile) và Backend đều diễn ra thông qua RESTful APIs. Mặc dù kiến trúc này mang lại sự linh hoạt trong việc mở rộng quy mô (scaling), nó lại đặt ra một bài toán hóc búa về đảm bảo chất lượng: **"Làm sao để đảm bảo Server không bất ngờ thay đổi cấu trúc dữ liệu khiến Client bị sập (crash)?"**

Để giải quyết bài toán này, nhóm nghiên cứu đã triển khai một hệ sinh thái kiểm thử 3 lớp (3-Tier Testing Architecture):
1. **API Testing truyền thống (Postman):** Đóng vai trò là công cụ kiểm tra độ chính xác của logic nghiệp vụ (Functional Testing).
2. **AI-Augmented Testing (LLMs):** Đóng vai trò xúc tác (Catalyst) để sinh ra bộ khung (scaffold) kiểm thử từ file đặc tả OpenAPI, giúp tiết kiệm 80% thời gian setup.
3. **Contract Testing (Pact):** Đóng vai trò như một bản cam kết pháp lý giữa Frontend và Backend, ngăn chặn các thay đổi phá vỡ kiến trúc (Breaking Changes).

Sự kết hợp của 3 phương pháp này không chỉ bù trừ khuyết điểm cho nhau mà còn tạo ra một "mạng lưới an toàn" (safety net) tuyệt đối khi được đưa lên môi trường Tích hợp liên tục (CI/CD).

---

## 2. Nhập môn API Testing 

Nếu bạn là người mới tiếp cận với lĩnh vực kiểm thử phần mềm, hãy tưởng tượng API giống như một **người phục vụ (waiter)** trong nhà hàng.
- **Frontend (Website/App):** Là bạn, người ngồi xem thực đơn và gọi món.
- **Backend (Database/Server):** Là nhà bếp, nơi chứa nguyên liệu và nấu ăn.
- **API:** Người phục vụ chạy đi chạy lại giữa bạn và nhà bếp. Bạn yêu cầu "Cho tôi 1 ly cafe" (Request), người phục vụ mang thông tin vào bếp, bếp làm xong, người phục vụ mang ly cafe ra cho bạn (Response).

**Vậy API Testing là gì?**
Thay vì bạn phải dùng Website (nhấn nút Mua hàng) để nhờ người phục vụ, bạn có thể tự mình viết các đoạn lệnh để "nói chuyện" trực tiếp với người phục vụ đó. Việc này giúp bạn kiểm tra xem nhà bếp có làm đúng món không, có tính nhầm tiền không, *trước cả khi Website được thiết kế xong*.

**Tại sao chúng ta phải test API?**
Nếu không test kỹ, một lỗi tính toán tiền ở nhà bếp (Backend) có thể khiến toàn bộ khách hàng mua đồ với giá 0 đồng, gây thiệt hại hàng tỷ đồng cho công ty.

**Làm sao để bắt đầu?**
1. Bạn cần một công cụ gọi là **Postman** (hoặc Insomnia). Đây là nơi bạn nhập các "yêu cầu" (Request) để gửi cho API.
2. Bạn cần biết địa chỉ của API (ví dụ: `http://localhost:3000/api/login`).
3. Bạn gửi yêu cầu và nhận kết quả trả về, so sánh xem kết quả có đúng như mong đợi không. (Ví dụ: Đăng nhập sai mật khẩu thì API phải trả về lỗi 401 chứ không phải là cho phép vào).

---

## 3. Nền tảng Lý thuyết & Chiến lược Kiểm thử
*(Dựa trên lý thuyết cốt lõi từ sách "Testing Web APIs" của tác giả Mark Winteringham và tài liệu chính thức của Pact)*

### 3.1 Chiến lược kiểm thử dựa trên rủi ro (Risk-Driven Testing)
Theo Mark Winteringham, kiểm thử toàn bộ 100% các API là một sự lãng phí tài nguyên và không thực tế trong các chu kỳ Agile ngắn hạn. Thay vào đó, nhóm đã áp dụng **Chiến lược kiểm thử dựa trên rủi ro (Risk-Driven Testing)** để phân loại và ưu tiên các endpoint của EShop:

- **Rủi ro mức độ Cao (High Risk):** `POST /api/checkout` và `POST /api/apply-coupon`. Đây là các API liên quan trực tiếp đến luồng thanh toán và dòng tiền. Nếu logic trừ tiền sai, hậu quả business là cực kỳ nghiêm trọng. Đối với nhóm này, test case phải bao phủ toàn bộ Happy Path, Negative Path (nhập coupon sai, nhập mã hết hạn) và Edge Cases (nhập số tiền âm, spam request).
- **Rủi ro mức độ Trung bình (Medium Risk):** `POST /api/cart` (Thêm vào giỏ). Nếu lỗi, người dùng bị gián đoạn trải nghiệm mua sắm. Cần test kiểm tra số lượng tồn kho (inventory boundary).
- **Rủi ro mức độ Thấp (Low Risk):** `GET /api/categories`. API này chỉ đọc dữ liệu tĩnh, rất hiếm khi thay đổi. Chỉ cần test Happy Path để đảm bảo Status 200 và cấu trúc mảng trả về là đủ.

### 3.2 Tự động hóa trong Continuous Integration
Một bộ test tốt nhất thế giới cũng trở nên vô dụng nếu nó chỉ chạy trên máy cá nhân của Developer. Winteringham nhấn mạnh tầm quan trọng của việc đưa API Test vào hệ thống CI/CD để tạo ra **Vòng lặp phản hồi nhanh (Fast Feedback Loop)**.
Bằng cách cô lập môi trường (Sử dụng Database test riêng biệt, chạy server dưới dạng background service trên GitHub Actions), chúng ta đảm bảo rằng:
1. Môi trường chạy test là "sạch" (Clean State).
2. Mọi thay đổi code của Developer đều phải đi qua "chốt chặn" API Test trước khi được phép merge vào nhánh `main`.

### 3.3 Lý thuyết Contract Testing (Pact Provider Verification)
Pact hoạt động dựa trên nguyên lý **Consumer-Driven Contracts (Hợp đồng do người tiêu dùng dẫn dắt)**. Thay vì Backend định nghĩa trả về cái gì, Frontend sẽ định nghĩa *"Tôi cần cái gì"*.
- **Pact Broker:** Là máy chủ trung tâm lưu trữ các bản hợp đồng JSON.
- **Provider Verification:** Backend (EShop API) sẽ tải hợp đồng này về. Công cụ Pact sẽ giả lập các request hệt như Frontend đã yêu cầu và kiểm tra xem Backend có trả về đúng cấu trúc (schema) và định dạng dữ liệu (types) hay không. Điểm khác biệt lớn nhất giữa Pact và Postman là Pact KHÔNG quan tâm đến giá trị thực (Ví dụ: `price: 10000`), Pact chỉ quan tâm đó có phải là kiểu số nguyên (Integer) hay không.

---

## 4. Yêu cầu Hệ thống & Thiết lập Môi trường

### 4.1 Cài đặt phần mềm
Đảm bảo máy trạm của bạn đã được cài đặt:
- **Node.js (v16+):** Runtime để chạy EShop backend và Jest.
- **npm hoặc yarn:** Trình quản lý thư viện.
- **Postman Desktop Client:** (Hoặc dùng bản Web) để chạy API test thủ công.
- **Newman:** Cài đặt toàn cục qua lệnh `npm install -g newman`.

### 4.2 Khởi động hệ thống Backend (SUT - System Under Test)
1. Mở Terminal / PowerShell.
2. Clone repository của nhóm về máy.
3. Di chuyển vào thư mục mã nguồn: `cd eshop-sut/backend`
4. Cài đặt các gói phụ thuộc: `npm install`
5. Khởi động server: `node server.js`
6. Nếu Terminal hiển thị `Server is running on http://localhost:3000`, SUT đã sẵn sàng để nhận request.

---



<!-- ================================================================ -->
<!-- # PHAN CUA TOAN (2) - Section 5: Postman Testing (cac subsection 5.0 -> 5.7) -->
<!-- Toan chiu trach nhiem: Postman Collection, Request Chaining, Data-Driven, Newman -->
<!-- Xoa comment nay khi da hoan thien va ready to merge -->
<!-- ================================================================ -->


## 5. Kiểm thử API Chuyên sâu với Postman
Đây là phương pháp kiểm thử cốt lõi (Traditional Tool). Chúng tôi không chỉ dùng Postman để gửi các request rời rạc, mà sử dụng **Postman Sandbox** (môi trường thực thi JavaScript) để mô phỏng một chuỗi hành vi người dùng cực kỳ phức tạp.

### 5.0 Hướng dẫn Step-by-step cho người mới (Chạy thử API đầu tiên)
Nếu bạn vừa mới cài Postman, hãy làm theo 4 bước cực nhanh sau đây để test thử API lấy danh sách sản phẩm:
1. **Mở Postman**, bấm dấu `+` để tạo một Request mới.
2. Đổi phương thức thành `GET` (mặc định đã là GET).
3. Nhập đường dẫn vào thanh URL: `http://localhost:3000/api/products`
4. Bấm nút **Send** màu xanh dương.
*Kết quả:* Bạn sẽ thấy một bảng dữ liệu (JSON) hiện ra bên dưới chứa danh sách các sản phẩm (Laptop, Chuột, Bàn phím...). Chúc mừng, bạn vừa thực hiện thành công API Test đầu tiên của mình!

### 5.1 Import OpenAPI Specification vào Postman
Hệ thống EShop có sẵn file đặc tả API (OpenAPI/Swagger) tên là `api_specification.md`. Bạn có thể import trực tiếp file này vào Postman để tiết kiệm thời gian:
1. Nhấn nút **Import** ở góc trái trên cùng của Postman.
2. Kéo thả file `api_specification.md` (hoặc dán nội dung văn bản của file đó).
3. Postman sẽ tự động phân tích và tạo ra một Collection hoàn chỉnh chứa đầy đủ các endpoint (GET, POST, PUT, DELETE), các tham số và cấu trúc JSON mẫu. Nhóm EShop đã dùng cách này để xây dựng bộ khung ban đầu cực kỳ nhanh chóng.

### 5.2 Khái niệm về Variables & Environments
Để test không bị gắn cứng (hardcode) với máy local, toàn bộ đường dẫn được cấu hình dưới dạng biến `{{baseUrl}}`.
Tạo một Environment tên là `EShop_Local` với các biến:
- `baseUrl`: `http://localhost:3000/api`
- `token`: (Để trống, sẽ được script tự động điền)
- `order_id`: (Để trống)

### 5.3 Lập trình Request Chaining (Gọi luồng liên hoàn)
Một trong những kỹ thuật mạnh nhất của Postman là trích xuất dữ liệu từ Response của API trước, làm đầu vào (Input) cho API sau.
**Kịch bản mô phỏng:** Đăng nhập -> Thêm sản phẩm vào giỏ -> Lấy giỏ hàng.

**Bước 1: API Đăng nhập (`POST /login`)**
Trong tab **Tests** của API login, chúng ta dùng Chai Assertion để bắt token:
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Trích xuất Token
let jsonData = pm.response.json();
if (jsonData.token) {
    // Lưu thẳng vào Environment để các API sau xài lại
    pm.environment.set("token", jsonData.token);
    console.log("Token đã được lưu: " + jsonData.token);
} else {
    console.error("Không tìm thấy Token trong response!");
}
```

**Bước 2: API Thêm giỏ hàng (`POST /cart`)**
Ở tab **Authorization**, cấu hình Type là `Bearer Token`, và mục Token điền `{{token}}`. Hệ thống sẽ tự lấy Token vừa lưu ở Bước 1 để xác thực.

### 5.4 Viết Data-Driven & Edge Case Assertions
Trong tab **Tests** của API `POST /apply-coupon`, nhóm viết logic kiểm tra toán học khắt khe nhằm chống lại lỗi business logic (Chương 4 của Winteringham):
```javascript
pm.test("Toán học: Tiền giảm giá phải chính xác", function () {
    let reqBody = JSON.parse(pm.request.body.raw);
    let resData = pm.response.json();
    
    // Yêu cầu Backend trả về 200 OK
    pm.response.to.have.status(200);
    
    // Kiểm tra định dạng dữ liệu (Typing)
    pm.expect(resData.discount_amount).to.be.a("number");
    pm.expect(resData.final_amount).to.be.a("number");
    
    // Thuật toán kiểm tra chéo (Cross-validation)
    let expectedFinal = reqBody.total_amount - resData.discount_amount;
    pm.expect(resData.final_amount).to.eql(expectedFinal, "Tổng tiền sau giảm giá bị tính sai!");
});
```
*Ghi chú:* Cách viết này ngăn chặn triệt để lỗi Backend trả về số tiền giảm giá lớn hơn cả tổng tiền giỏ hàng (Một bug cực kỳ kinh điển trong ngành E-commerce).

### 5.5 Chạy tự động hàng loạt với Collection Runner
Để không phải bấm nút Send từng API một, Postman cung cấp tính năng **Collection Runner**:
1. Click vào dấu `...` bên cạnh tên Collection và chọn **Run collection**.
2. Một màn hình liệt kê toàn bộ các kịch bản sẽ hiện ra. Bạn nhấn nút **Run**.
3. Postman sẽ tự động chạy lần lượt tất cả các API từ trên xuống dưới (có kế thừa Token nhờ Request Chaining) và in ra một báo cáo tổng quan (Run Summary) cực kỳ trực quan với màu Xanh (Pass) và Đỏ (Fail). Nhóm EShop dùng tính năng này để bắt các lỗi logic ngầm của Backend.

**Bảng tổng kết Test Coverage của EShop Collection:**

| Endpoint | Happy Path | Negative Path | Edge Case | Schema Validation |
|---|---|---|---|---|
| `POST /api/login` | ✅ | ✅ (sai mật khẩu, thiếu field) | ✅ (SQL injection payload) | ✅ |
| `GET /api/products` | ✅ | — | ✅ (query param rỗng) | ✅ |
| `GET /api/products/:id` | ✅ | ✅ (id không tồn tại → 404) | ✅ (id = -1, id = "abc") | ✅ |
| `POST /api/cart` | ✅ | ✅ (thiếu token → 401) | ✅ (số lượng = 0, số lượng âm) | ✅ |
| `POST /api/orders` | ✅ | ✅ (giỏ hàng rỗng → 400) | ✅ (đặt hàng 2 lần liên tiếp) | ✅ |
| `POST /api/apply-coupon` | ✅ | ✅ (coupon hết hạn, sai mã) | ✅ (coupon dùng vượt limit) | ✅ |

### 5.6 Data-Driven Testing với CSV (Chạy 1 test với nhiều bộ dữ liệu)
Thay vì viết riêng từng test case cho từng trường hợp coupon, nhóm sử dụng kỹ thuật **Data-Driven Testing** của Collection Runner để chạy cùng một API với nhiều bộ dữ liệu đầu vào khác nhau chỉ trong một lần bấm Run.

**Bước 1: Tạo file dữ liệu `coupon_testdata.csv`**
```csv
coupon_code,total_amount,expected_status,expected_discount
SALE10,200000,200,20000
SALE50,500000,200,250000
EXPIRED,100000,400,0
INVALIDXYZ,100000,400,0
SALE10,0,400,0
```
*Mỗi dòng là một kịch bản test: coupon hợp lệ, coupon hết hạn, coupon sai, tổng tiền bằng 0...*

**Bước 2: Viết Test Script dùng biến CSV trong tab Tests**
```javascript
pm.test("Status code khớp với expected", function () {
    pm.response.to.have.status(parseInt(pm.iterationData.get("expected_status")));
});

pm.test("Discount amount chính xác (nếu thành công)", function () {
    if (pm.response.code === 200) {
        let resData = pm.response.json();
        let expectedDiscount = parseFloat(pm.iterationData.get("expected_discount"));
        pm.expect(resData.discount_amount).to.eql(expectedDiscount, "Số tiền giảm giá sai!");
    }
});
```
*Chú ý: Dùng `pm.iterationData.get("tên_cột")` để đọc giá trị từ file CSV tại mỗi vòng lặp.*

**Bước 3: Chạy trong Collection Runner**
1. Mở Collection Runner, chọn **Select File** và upload file `coupon_testdata.csv`.
2. Runner tự động phát hiện số dòng (5 dòng = 5 lần lặp) và hiển thị preview.
3. Nhấn **Run** — Postman sẽ gửi 5 request liên tiếp, mỗi request dùng một bộ dữ liệu khác nhau.
4. Báo cáo sẽ phân biệt rõ **Iteration 1**, **Iteration 2**... để dễ dàng trace lỗi.

**Lợi ích:** Kỹ thuật này thay thế 5 request riêng lẻ bằng 1 request duy nhất + 1 file CSV, giúp dễ bảo trì khi nghiệp vụ thay đổi (chỉ cần sửa CSV, không cần sửa code).

### 5.7 Milestone M3: Diff AI Scaffold vs Manual Collection
*(Đây là bằng chứng thực tế cho Milestone M3 của đề bài: "Generate scaffold from /api_specification.yaml using an AI tool; diff vs your collection")*

Sau khi nhóm dùng Claude để sinh Postman Collection từ file `api_specification.md`, chúng tôi tiến hành so sánh trực tiếp kết quả AI tạo ra với bộ Collection được viết tay:

| Tiêu chí so sánh | Manual Collection (Viết tay) | AI-Generated Scaffold (Claude) |
|---|---|---|
| **Thời gian tạo** | ~3 giờ | < 2 phút |
| **Số endpoint có sẵn** | 6/6 | 6/6 |
| **Happy Path test cases** | 6 | 6 (✅ tương đương) |
| **Negative Path test cases** | 12 | 2 (❌ thiếu 10 kịch bản) |
| **Edge Case test cases** | 8 | 0 (❌ AI bỏ hoàn toàn) |
| **Schema Validation chặt** | ✅ `required` + `additionalProperties: false` | ❌ Schema rỗng (cho phép mọi thứ) |
| **Business Rule (coupon limit)** | ✅ Có kịch bản test `max_uses_per_user` | ❌ Hoàn toàn bỏ qua |
| **Authentication chaining** | ✅ Token tự động truyền qua env variable | ⚠️ Token hardcode cứng |
| **Data-Driven Testing** | ✅ Hỗ trợ CSV | ❌ Không có |
| **Xử lý race condition** | ✅ Test đặt hàng 2 lần liên tiếp | ❌ Không nhận biết |

**Kết luận từ bảng diff:**
AI sinh ra bộ khung (scaffold) đầy đủ về mặt cấu trúc endpoint, giúp tiết kiệm ~80% thời gian setup ban đầu. Tuy nhiên, AI mắc phải **Happy-Path Bias** nghiêm trọng — toàn bộ kịch bản Negative, Edge Case và Business Rule phải do QA tự tay bổ sung. Điều này khẳng định: AI là công cụ tăng tốc, không phải công cụ thay thế tư duy kiểm thử.

---



<!-- ================================================================ -->
<!-- # PHAN CUA KHOA (1) - Section 6: AI-Augmented Testing (6.1 -> 6.3) -->
<!-- Khoa chiu trach nhiem: Prompt Engineering, AI Scaffold Refining, Postbot -->
<!-- Xoa comment nay khi da hoan thien va ready to merge -->
<!-- ================================================================ -->


## 6. Sinh kịch bản tự động bằng Trí tuệ Nhân tạo
Sử dụng AI không nhằm mục đích "thay thế" Tester, mà để tự động hóa khâu tạo Boilerplate (mã lặp lại). Nhóm sử dụng mô hình "Spec-to-Test Generation".

### 6.1 Kỹ thuật Prompt Engineering
Để AI (Claude/ChatGPT) sinh ra bộ test Postman có thể chạy được ngay, nhóm không dùng prompt chung chung. Nhóm sử dụng kỹ thuật **Zero-shot with Context Injection**.
**Cấu trúc Prompt:**
> "Tôi có một file OpenAPI specification của hệ thống EShop (dán nội dung file `api_specification.md` vào đây). Dựa vào đặc tả này, hãy sinh cho tôi một file Postman Collection v2.1.0 chuẩn JSON. 
> Yêu cầu: Bao gồm tất cả các endpoints. Đối với các API POST/PUT, hãy tạo sẵn Body JSON giả lập. Tại mỗi API, hãy viết sẵn một test script kiểm tra status code 200 bằng cú pháp `pm.test`."

### 6.2 Quá trình Tinh chỉnh (Refining the Scaffold)
Khi AI nhả ra file `.json` và import vào Postman, nhóm nhận thấy tốc độ hoàn thành là dưới 1 phút (Nhanh gấp 10 lần gõ tay). Tuy nhiên, AI gặp phải hiện tượng **Happy-Path Bias** (Thiên kiến luồng chuẩn):
- AI chỉ sinh các trường hợp tài khoản đúng, mật khẩu đúng, coupon hợp lệ.
- QA của nhóm phải trực tiếp vào tab **Tests** để thiết kế các kịch bản Negative (Ví dụ: Bắn payload chữ cái vào trường tính tiền `total_amount: "hai mươi ngàn"` để ép API văng lỗi 400 Bad Request, và dùng Postman verify rằng API thực sự văng lỗi 400 chứ không văng 500 sập server).

### 6.3 Postbot — AI Inline ngay trong Postman
Ngoài việc dùng Claude/ChatGPT bên ngoài, Postman còn tích hợp sẵn tính năng AI gọi là **Postbot** (biểu tượng ngôi sao ở góc phải dưới màn hình Postman). Đây là một AI trợ lý có thể sinh test script, giải thích response, và tự động tạo documentation — tất cả mà không cần rời khỏi Postman.

**Các tính năng chính của Postbot:**

| Tính năng | Cách dùng | Kết quả |
|---|---|---|
| **Add tests to this request** | Click Postbot → chọn tùy chọn | Tự sinh pm.test() dựa trên response thực tế |
| **Visualize response** | Click Postbot → "Visualize" | Tạo bảng HTML trực quan từ JSON response |
| **Fix this error** | Khi test bị Fail, click Postbot | AI đọc error message và đề xuất cách sửa script |
| **Add documentation** | Click Postbot → "Document" | Tự viết mô tả cho request (method, params, example) |

**Workflow thực tế nhóm đã dùng:**
1. Gửi request `POST /api/apply-coupon`, nhận response thực.
2. Click **Postbot** → chọn `Add tests to this request`.
3. Postbot phân tích response JSON đang hiển thị và sinh ra test script kiểm tra status 200, kiểu dữ liệu của `discount_amount` và `final_amount`.
4. QA review script do Postbot sinh ra, bổ sung thêm phần kiểm tra cross-validation toán học (phần AI bỏ qua).

**Lưu ý quan trọng:** Postbot chỉ dựa vào response *hiện tại đang hiển thị* để sinh test — nếu bạn test với coupon hợp lệ, Postbot sẽ chỉ sinh Happy Path. Hãy chạy thêm request với coupon sai để Postbot nhìn thấy response lỗi và sinh thêm Negative test.

---



<!-- ================================================================ -->
<!-- # PHAN CUA NAM (1) - Section 7: Contract Testing voi Pact (7.1 -> 7.3) -->
<!-- Nam chiu trach nhiem: Consumer Test, Provider Verification, requestFilter -->
<!-- Xoa comment nay khi da hoan thien va ready to merge -->
<!-- ================================================================ -->


## 7. Kiểm thử Hợp đồng Giao tiếp với Pact
Nếu như Postman dùng để test Logic, thì Pact dùng để test Cấu trúc Dữ liệu (Schema/Contract).

### 7.1 Tổng quan về Provider Verification
Đề bài yêu cầu triển khai luồng Provider Verification cho Node backend. Ở bước này, Backend (Provider) đóng vai trò bị động: Nó đứng yên, chờ công cụ Pact đọc file hợp đồng `.json` (do Frontend - Consumer tạo ra từ trước) và bắn request vào.

### 7.2 Thiết lập Provider States (Quản lý trạng thái)
Đây là phần khó nhất của Contract Testing. Trong hợp đồng, Frontend yêu cầu: *"Khi tôi gửi ID = 1, anh phải trả về tên sản phẩm"*. 
Nhưng nếu Database test đang trống rỗng thì API sẽ văng 404 Not Found, dẫn đến Fail hợp đồng dù API không hề code sai!
**Cách giải quyết:** Nhóm lập trình các `stateHandlers` trong file `provider.test.js`.
```javascript
const { Verifier } = require('@pact-foundation/pact');

const opts = {
  providerBaseUrl: 'http://localhost:3000',
  pactUrls: ['./pacts/frontend-eshop_backend.json'],
  stateHandlers: {
    "Sản phẩm có ID 1 tồn tại": async () => {
      // Logic cấy dữ liệu giả vào Database
      await db.query("INSERT INTO products (id, name, price) VALUES (1, 'Sản phẩm Test', 50000)");
      return Promise.resolve();
    },
    "Giỏ hàng trống": async () => {
      await db.query("DELETE FROM cart");
      return Promise.resolve();
    }
  },
  requestFilter: (req, res, next) => {
    // Đánh chặn request để tiêm Token tươi mới vào Header
    req.headers['authorization'] = `Bearer ${global.TEST_TOKEN}`;
    next();
  }
};

new Verifier(opts).verifyProvider().then(() => {
    console.log('Contract Verification Passed!');
});
```

### 7.3 Giải quyết vấn đề Token hết hạn (requestFilter)
Như thấy ở code trên, hàm `requestFilter` là cứu cánh cực kỳ quan trọng. Bản hợp đồng được tạo ra vào ngày hôm qua chứa một chuỗi Token đã hết hạn. Khi Pact bắn chuỗi Token cũ mèm đó vào Backend hôm nay, Backend sẽ trả về `401 Unauthorized`. Việc dùng `requestFilter` giúp ta đánh tráo Token cũ thành Token vừa đăng nhập trước khi gửi vào Backend.

---



<!-- ================================================================ -->
<!-- # PHAN CUA LUAN (1) - Section 8: CI/CD voi GitHub Actions (8.1 -> 8.2) -->
<!-- Luan chiu trach nhiem: Workflow YAML, Newman pipeline, HTML Extra report, Artifacts -->
<!-- Xoa comment nay khi da hoan thien va ready to merge -->
<!-- ================================================================ -->


## 8. Tích hợp Liên tục với GitHub Actions
Mọi đoạn script trên máy cá nhân đều không có ý nghĩa nếu code lỗi vẫn được merge vào server chính. Nhóm đã tích hợp toàn bộ Postman (thông qua Newman) và Pact vào file `.github/workflows/test.yml`.

### 8.1 Luồng CI/CD Pipeline
1. Cài đặt Node.js v16 trên Ubuntu server của GitHub.
2. Chạy lệnh `npm ci` để cài thư viện.
3. Kích hoạt Backend chạy ngầm: `node server.js &` (Dấu `&` giúp server chạy ở background mà không làm treo pipeline).
4. Đợi 3 giây cho server sẵn sàng: `sleep 3`.
5. Chạy Newman: `newman run EShop_Collection_v2.json -e EShop_Environment.json --reporters cli,htmlextra`
6. Chạy Pact: `npm run test:pact`

### 8.2 Cấu hình Báo cáo Đẹp (HTML Extra) & Artifacts
Sử dụng plugin `newman-reporter-htmlextra`, báo cáo xuất ra không chỉ là những dòng text nhàm chán mà là một giao diện Dashboard cực đẹp.
Để lấy được file báo cáo kể cả khi luồng bị gãy (Failed), nhóm cấu hình block `if: always()`:
```yaml
      - name: Upload HTML Report
        uses: actions/upload-artifact@v3
        if: always() # Luôn luôn chạy bước này dù lệnh newman phía trên có bị báo đỏ
        with:
          name: EShop-Test-Reports
          path: newman/
```
Developer chỉ cần vào giao diện GitHub Actions, tải file Zip chứa report HTML về và mở bằng trình duyệt để xem tận mắt API nào đang lỗi, lỗi ở dòng nào.

---



<!-- ================================================================ -->
<!-- # PHAN CUA NAM (2) - Section 9: Failure Modes (tong hop tu Toan + Khoa + Luan) -->
<!-- Nam tong hop: Failure Modes cua ca 3 tool: Postman (Toan), AI (Khoa), Pact (Luan) -->
<!-- Toan: viet Case Study 1 & 4 | Khoa: viet Case Study 2 | Luan: kiem tra Case Study 5 -->
<!-- Xoa comment nay khi da hoan thien va ready to merge -->
<!-- ================================================================ -->


## 9. Phân tích Điểm mù (Failure Modes - 5 Case Studies)
Đây là phần cốt lõi chứng minh tính thực tiễn của đồ án. Máy móc/Công cụ đôi khi "nói dối" và khiến kỹ sư kiểm thử (QA) rơi vào cái bẫy False Positive (Tưởng là đúng nhưng thực ra là sai). Dưới đây là 5 "cú lừa" kinh điển:

### Case Study 1 (Postman): Cái bẫy Silent Failure trong Sandbox
- **Ngữ cảnh:** Kỹ sư QA viết đoạn mã kiểm tra logic tính tổng tiền giỏ hàng. Nhưng trong lúc gõ phím, họ gõ sai chính tả hàm JSON: `let data = pm.response.jsson();` (Dư chữ s).
- **Hiện tượng:** Môi trường Sandbox của Postman âm thầm văng lỗi nội bộ (Uncaught Exception) và DỪNG THỰC THI toàn bộ các câu lệnh `pm.test` bên dưới. Đáng sợ nhất là giao diện Postman **không hề báo đỏ (Fail)** mà vẫn hiển thị các pass màu xanh của những test case bên trên đoạn bị lỗi. Kỹ sư nhìn lướt qua, tưởng test case tính tiền đã Pass và tự tin giao hàng.
- **Bài học (Cách khắc phục):** Luôn mở giao diện **Postman Console (Ctrl + Alt + C)** để rà soát lỗi đỏ của JavaScript. Không bao giờ tin tưởng hoàn toàn vào giao diện Runner nếu chưa check Console log.

### Case Study 2 (AI-Augmented): Schema Validation rỗng và Bỏ qua Business Rules
- **Ngữ cảnh:** Sử dụng AI để sinh test case cho API `/api/apply-coupon` (Áp mã giảm giá). Trả về của API lúc bị lỗi nghiệp vụ (ví dụ hết hạn) là một file JSON rỗng hoặc báo lỗi 400.
- **Hiện tượng:** AI thường lười biếng và sinh ra khối schema validation thế này:
  ```javascript
  const schema = { "type": "object", "properties": {}, "additionalProperties": true };
  pm.expect(tv4.validate(pm.response.json(), schema)).to.be.true;
  ```
  Schema này định nghĩa rằng: "Trả về một Object bất kỳ, không cần có trường dữ liệu nào bắt buộc, và cho phép chứa bất kỳ trường gì cũng được".
  Kết quả là: Backend code sai, tính tiền sai lòi, văng ra object rác rưởi, nhưng đoạn code do AI sinh ra VẪN ĐÁNH GIÁ LÀ PASS vì nó quá lỏng lẻo. Ngoài ra, AI hoàn toàn bỏ qua việc test giới hạn `max_uses_per_user` (Quy tắc kinh doanh ngầm).
- **Bài học (Cách khắc phục):** AI sinh code chỉ là bản nháp. Kỹ sư phải tự định nghĩa chặt chẽ Schema (ví dụ `required: ["discount_amount", "final_amount"]`) và tự tay bổ sung các kịch bản tấn công nghiệp vụ (Coupon abuse).

### Case Study 3 (Pact Contract Testing): Postel's Law và Rủi ro Lộ lọt dữ liệu (Data Leakage)
- **Ngữ cảnh:** Frontend định nghĩa hợp đồng yêu cầu Backend trả về API Lấy thông tin cá nhân (`/api/users/me`) với 2 trường: `name` và `email`.
- **Hiện tượng:** Lập trình viên Backend code lười, truy vấn thẳng câu `SELECT * FROM users` và ném toàn bộ dữ liệu ra API. Cấu trúc JSON trả về bao gồm cả `password_hash`, `otp_code` cực kỳ nhạy cảm.
  Khi chạy Provider Verification, công cụ Pact lại **BÁO PASS 100%**. Tại sao?
  Vì Pact tuân thủ quy tắc Postel's Law trong thiết kế API: *"Hãy bảo thủ với những gì bạn gửi đi, nhưng khoan dung với những gì bạn nhận lại"*. Miễn là Backend trả ĐỦ `name` và `email`, việc dư thừa bao nhiêu trường rác khác Pact không quan tâm.
- **Bài học (Cách khắc phục):** Tuyệt đối không dùng Contract Testing để kiểm tra Bảo mật (Security/Penetration Testing). Phải kết hợp với JSON Schema Validation của Postman (thêm cờ `"additionalProperties": false`) để bắt lỗi rò rỉ trường dữ liệu ngoài ý muốn.

### Case Study 4 (Postman): Lỗi so sánh kiểu dữ liệu ngầm định (Type Mismatch)
- **Ngữ cảnh:** API backend trả về dữ liệu bị sai kiểu (ví dụ trả về `price` dạng chuỗi `"28000000"` thay vì số nguyên `28000000`).
- **Hiện tượng:** Nếu trong tab Tests sử dụng `pm.expect(price).to.eql(28000000);`, test sẽ báo fail với thông báo mơ hồ như *AssertionError: expected '28000000' to deeply equal 28000000*. Người mới dùng rất dễ nhầm lẫn rằng logic API tính toán sai giá tiền, chứ không nhận ra đó là lỗi ép kiểu dữ liệu do khác biệt ở dấu nháy đơn.
- **Bài học (Cách khắc phục):** Tester phải dùng strict equality hoặc các hàm kiểm tra type rõ ràng (ví dụ: `.to.be.a('number')`) mới bắt lỗi một cách minh bạch.

### Case Study 5 (Postman): Quên cấu hình Environment/Token (Unresolved Variables)
- **Ngữ cảnh:** Quên chọn Environment ở góc phải trên cùng (đang ở trạng thái "No Environment"), khiến các biến như `{{baseUrl}}` hay `{{token}}` không có giá trị.
- **Hiện tượng:** Postman **không báo lỗi cú pháp ngay** mà gửi nguyên cái chuỗi chữ `{{baseUrl}}` đi làm URL thực tế. Kết quả là hệ thống trả về lỗi `404 Not Found` hoặc `401 Unauthorized`. Người test sẽ mất hàng giờ đồng hồ để debug API backend trong khi nguyên nhân thực sự chỉ là quên cấu hình môi trường.
- **Bài học (Cách khắc phục):** Luôn tập thói quen kiểm tra góc phải màn hình xem Environment đã được kích hoạt đúng hay chưa trước khi bấm Send. Viết Pre-request script để cảnh báo nếu phát hiện thiếu biến cục bộ.

---



<!-- ================================================================ -->
<!-- # PHAN CUA NAM (3) - Section 10: Lessons Learned (tong hop ca nhom) -->
<!-- Nam tong hop: Duc ket kinh nghiem chung cua ca 4 nguoi -->
<!-- Xoa comment nay khi da hoan thien va ready to merge -->
<!-- ================================================================ -->


## 10. Đúc kết và Bài học Kinh nghiệm
Quãng thời gian 2 tháng nghiên cứu và triển khai đề tài T06 mang lại cái nhìn sâu sắc cho toàn nhóm về hệ sinh thái QA hiện đại.
1. **Tooling không phải là tất cả:** Postman hay Karate chỉ là công cụ. Tư duy thiết kế test (Test Design Thinking) để tìm ra các Edge Cases mới là yếu tố quyết định chất lượng phần mềm.
2. **AI là Trợ lý, không phải Trọng tài:** Việc nhắm mắt tin tưởng đoạn code do AI sinh ra là con đường ngắn nhất dẫn đến thảm họa False Positives trên production. Human-in-the-loop là quy trình bắt buộc.
3. **Pact bảo vệ Kiến trúc, Postman bảo vệ Nghiệp vụ:** Việc ứng dụng Pact giúp dập tắt hoàn toàn các cuộc cãi vã giữa team Frontend và Backend về việc "Ai đổi API làm sập app?". Hợp đồng JSON trở thành tài liệu giao tiếp trung tâm (Single source of truth).

*Dự án EShop là minh chứng rõ nét cho việc: Kiểm thử API không chỉ là "Gửi request - Nhận 200 OK". Đó là một nghệ thuật đảm bảo rủi ro kinh doanh được kiểm soát ở mức thấp nhất, bằng những dòng code tự động hóa sắc bén nhất.*
