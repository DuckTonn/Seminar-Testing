# Báo cáo Chuyên đề & Sổ tay Hướng dẫn Cốt lõi (User Guide)
**Đề tài:** T06 - API & Contract Testing  
**Hệ thống:** EShop Backend (Node.js/Express)  
**Nhóm thực hiện:** Group 05 (Phạm Đức Toàn, Nguyễn Quang Đăng Khoa, Nguyễn Nhật Nam, Huỳnh Sĩ Luân)

---

## Mục lục
1. [Tóm tắt Cấp cao & Kiến trúc Hệ thống (Executive Summary)](#1-tóm-tắt-cấp-cao--kiến-trúc-hệ-thống)
2. [Nền tảng Lý thuyết & Chiến lược Kiểm thử (Theoretical Foundations)](#2-nền-tảng-lý-thuyết--chiến-lược-kiểm-thử)
3. [Yêu cầu Hệ thống & Thiết lập Môi trường (Prerequisites & Setup)](#3-yêu-cầu-hệ-thống--thiết-lập-môi-trường)
4. [Kiểm thử API Chuyên sâu với Postman (Manual & Scripted Testing)](#4-kiểm-thử-api-chuyên-sâu-với-postman)
5. [Sinh kịch bản tự động bằng Trí tuệ Nhân tạo (AI-Augmented Generation)](#5-sinh-kịch-bản-tự-động-bằng-trí-tuệ-nhân-tạo)
6. [Kiểm thử Hợp đồng Giao tiếp với Pact (Contract Testing)](#6-kiểm-thử-hợp-đồng-giao-tiếp-với-pact)
7. [Tích hợp Liên tục (Continuous Integration với GitHub Actions)](#7-tích-hợp-liên-tục-với-github-actions)
8. [Phân tích Điểm mù (Failure Modes - 3 Case Studies)](#8-phân-tích-điểm-mù-failure-modes---3-case-studies)
9. [Đúc kết và Bài học Kinh nghiệm (Lessons Learned)](#9-đúc-kết-và-bài-học-kinh-nghiệm)

---

## 1. Tóm tắt Cấp cao & Kiến trúc Hệ thống
Hệ thống EShop được xây dựng dựa trên kiến trúc Microservices (hoặc Client-Server tách rời hoàn toàn). Toàn bộ giao tiếp giữa Frontend (Web/Mobile) và Backend đều diễn ra thông qua RESTful APIs. Mặc dù kiến trúc này mang lại sự linh hoạt trong việc mở rộng quy mô (scaling), nó lại đặt ra một bài toán hóc búa về đảm bảo chất lượng: **"Làm sao để đảm bảo Server không bất ngờ thay đổi cấu trúc dữ liệu khiến Client bị sập (crash)?"**

Để giải quyết bài toán này, nhóm nghiên cứu đã triển khai một hệ sinh thái kiểm thử 3 lớp (3-Tier Testing Architecture):
1. **API Testing truyền thống (Postman):** Đóng vai trò là công cụ kiểm tra độ chính xác của logic nghiệp vụ (Functional Testing).
2. **AI-Augmented Testing (LLMs):** Đóng vai trò xúc tác (Catalyst) để sinh ra bộ khung (scaffold) kiểm thử từ file đặc tả OpenAPI, giúp tiết kiệm 80% thời gian setup.
3. **Contract Testing (Pact):** Đóng vai trò như một bản cam kết pháp lý giữa Frontend và Backend, ngăn chặn các thay đổi phá vỡ kiến trúc (Breaking Changes).

Sự kết hợp của 3 phương pháp này không chỉ bù trừ khuyết điểm cho nhau mà còn tạo ra một "mạng lưới an toàn" (safety net) tuyệt đối khi được đưa lên môi trường Tích hợp liên tục (CI/CD).

---

## 2. Nền tảng Lý thuyết & Chiến lược Kiểm thử
*(Dựa trên lý thuyết cốt lõi từ sách "Testing Web APIs" của tác giả Mark Winteringham và tài liệu chính thức của Pact)*

### 2.1 Chiến lược kiểm thử dựa trên rủi ro (Risk-Driven Testing - Chapter 4)
Theo Mark Winteringham, kiểm thử toàn bộ 100% các API là một sự lãng phí tài nguyên và không thực tế trong các chu kỳ Agile ngắn hạn. Thay vào đó, nhóm đã áp dụng **Chiến lược kiểm thử dựa trên rủi ro (Risk-Driven Testing)** để phân loại và ưu tiên các endpoint của EShop:

- **Rủi ro mức độ Cao (High Risk):** `POST /api/checkout` và `POST /api/apply-coupon`. Đây là các API liên quan trực tiếp đến luồng thanh toán và dòng tiền. Nếu logic trừ tiền sai, hậu quả business là cực kỳ nghiêm trọng. Đối với nhóm này, test case phải bao phủ toàn bộ Happy Path, Negative Path (nhập coupon sai, nhập mã hết hạn) và Edge Cases (nhập số tiền âm, spam request).
- **Rủi ro mức độ Trung bình (Medium Risk):** `POST /api/cart` (Thêm vào giỏ). Nếu lỗi, người dùng bị gián đoạn trải nghiệm mua sắm. Cần test kiểm tra số lượng tồn kho (inventory boundary).
- **Rủi ro mức độ Thấp (Low Risk):** `GET /api/categories`. API này chỉ đọc dữ liệu tĩnh, rất hiếm khi thay đổi. Chỉ cần test Happy Path để đảm bảo Status 200 và cấu trúc mảng trả về là đủ.

### 2.2 Tự động hóa trong Continuous Integration (Chapter 9)
Một bộ test tốt nhất thế giới cũng trở nên vô dụng nếu nó chỉ chạy trên máy cá nhân của Developer. Winteringham nhấn mạnh tầm quan trọng của việc đưa API Test vào hệ thống CI/CD để tạo ra **Vòng lặp phản hồi nhanh (Fast Feedback Loop)**.
Bằng cách cô lập môi trường (Sử dụng Database test riêng biệt, chạy server dưới dạng background service trên GitHub Actions), chúng ta đảm bảo rằng:
1. Môi trường chạy test là "sạch" (Clean State).
2. Mọi thay đổi code của Developer đều phải đi qua "chốt chặn" API Test trước khi được phép merge vào nhánh `main`.

### 2.3 Lý thuyết Contract Testing (Pact Provider Verification)
Pact hoạt động dựa trên nguyên lý **Consumer-Driven Contracts (Hợp đồng do người tiêu dùng dẫn dắt)**. Thay vì Backend định nghĩa trả về cái gì, Frontend sẽ định nghĩa *"Tôi cần cái gì"*.
- **Pact Broker:** Là máy chủ trung tâm lưu trữ các bản hợp đồng JSON.
- **Provider Verification:** Backend (EShop API) sẽ tải hợp đồng này về. Công cụ Pact sẽ giả lập các request hệt như Frontend đã yêu cầu và kiểm tra xem Backend có trả về đúng cấu trúc (schema) và định dạng dữ liệu (types) hay không. Điểm khác biệt lớn nhất giữa Pact và Postman là Pact KHÔNG quan tâm đến giá trị thực (Ví dụ: `price: 10000`), Pact chỉ quan tâm đó có phải là kiểu số nguyên (Integer) hay không.

---

## 3. Yêu cầu Hệ thống & Thiết lập Môi trường

### 3.1 Cài đặt phần mềm
Đảm bảo máy trạm của bạn đã được cài đặt:
- **Node.js (v16+):** Runtime để chạy EShop backend và Jest.
- **npm hoặc yarn:** Trình quản lý thư viện.
- **Postman Desktop Client:** (Hoặc dùng bản Web) để chạy API test thủ công.
- **Newman:** Cài đặt toàn cục qua lệnh `npm install -g newman`.

### 3.2 Khởi động hệ thống Backend (SUT - System Under Test)
1. Mở Terminal / PowerShell.
2. Clone repository của nhóm về máy.
3. Di chuyển vào thư mục mã nguồn: `cd eshop-sut/backend`
4. Cài đặt các gói phụ thuộc: `npm install`
5. Khởi động server: `node server.js`
6. Nếu Terminal hiển thị `Server is running on http://localhost:3000`, SUT đã sẵn sàng để nhận request.

---

## 4. Kiểm thử API Chuyên sâu với Postman
Đây là phương pháp kiểm thử cốt lõi (Traditional Tool). Chúng tôi không chỉ dùng Postman để gửi các request rời rạc, mà sử dụng **Postman Sandbox** (môi trường thực thi JavaScript) để mô phỏng một chuỗi hành vi người dùng cực kỳ phức tạp.

### 4.1 Khái niệm về Variables & Environments
Để test không bị gắn cứng (hardcode) với máy local, toàn bộ đường dẫn được cấu hình dưới dạng biến `{{baseUrl}}`.
Tạo một Environment tên là `EShop_Local` với các biến:
- `baseUrl`: `http://localhost:3000/api`
- `token`: (Để trống, sẽ được script tự động điền)
- `order_id`: (Để trống)

### 4.2 Lập trình Request Chaining (Gọi luồng liên hoàn)
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

### 4.3 Viết Data-Driven & Edge Case Assertions
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

---

## 5. Sinh kịch bản tự động bằng Trí tuệ Nhân tạo
Sử dụng AI không nhằm mục đích "thay thế" Tester, mà để tự động hóa khâu tạo Boilerplate (mã lặp lại). Nhóm sử dụng mô hình "Spec-to-Test Generation".

### 5.1 Kỹ thuật Prompt Engineering
Để AI (Claude/ChatGPT) sinh ra bộ test Postman có thể chạy được ngay, nhóm không dùng prompt chung chung. Nhóm sử dụng kỹ thuật **Zero-shot with Context Injection**.
**Cấu trúc Prompt:**
> "Tôi có một file OpenAPI specification của hệ thống EShop (dán nội dung file `api_specification.md` vào đây). Dựa vào đặc tả này, hãy sinh cho tôi một file Postman Collection v2.1.0 chuẩn JSON. 
> Yêu cầu: Bao gồm tất cả các endpoints. Đối với các API POST/PUT, hãy tạo sẵn Body JSON giả lập. Tại mỗi API, hãy viết sẵn một test script kiểm tra status code 200 bằng cú pháp `pm.test`."

### 5.2 Quá trình Tinh chỉnh (Refining the Scaffold)
Khi AI nhả ra file `.json` và import vào Postman, nhóm nhận thấy tốc độ hoàn thành là dưới 1 phút (Nhanh gấp 10 lần gõ tay). Tuy nhiên, AI gặp phải hiện tượng **Happy-Path Bias** (Thiên kiến luồng chuẩn):
- AI chỉ sinh các trường hợp tài khoản đúng, mật khẩu đúng, coupon hợp lệ.
- QA của nhóm phải trực tiếp vào tab **Tests** để thiết kế các kịch bản Negative (Ví dụ: Bắn payload chữ cái vào trường tính tiền `total_amount: "hai mươi ngàn"` để ép API văng lỗi 400 Bad Request, và dùng Postman verify rằng API thực sự văng lỗi 400 chứ không văng 500 sập server).

---

## 6. Kiểm thử Hợp đồng Giao tiếp với Pact
Nếu như Postman dùng để test Logic, thì Pact dùng để test Cấu trúc Dữ liệu (Schema/Contract).

### 6.1 Tổng quan về Provider Verification
Đề bài yêu cầu triển khai luồng Provider Verification cho Node backend. Ở bước này, Backend (Provider) đóng vai trò bị động: Nó đứng yên, chờ công cụ Pact đọc file hợp đồng `.json` (do Frontend - Consumer tạo ra từ trước) và bắn request vào.

### 6.2 Thiết lập Provider States (Quản lý trạng thái)
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

### 6.3 Giải quyết vấn đề Token hết hạn (requestFilter)
Như thấy ở code trên, hàm `requestFilter` là cứu cánh cực kỳ quan trọng. Bản hợp đồng được tạo ra vào ngày hôm qua chứa một chuỗi Token đã hết hạn. Khi Pact bắn chuỗi Token cũ mèm đó vào Backend hôm nay, Backend sẽ trả về `401 Unauthorized`. Việc dùng `requestFilter` giúp ta đánh tráo Token cũ thành Token vừa đăng nhập trước khi gửi vào Backend.

---

## 7. Tích hợp Liên tục với GitHub Actions
Mọi đoạn script trên máy cá nhân đều không có ý nghĩa nếu code lỗi vẫn được merge vào server chính. Nhóm đã tích hợp toàn bộ Postman (thông qua Newman) và Pact vào file `.github/workflows/test.yml`.

### 7.1 Luồng CI/CD Pipeline
1. Cài đặt Node.js v16 trên Ubuntu server của GitHub.
2. Chạy lệnh `npm ci` để cài thư viện.
3. Kích hoạt Backend chạy ngầm: `node server.js &` (Dấu `&` giúp server chạy ở background mà không làm treo pipeline).
4. Đợi 3 giây cho server sẵn sàng: `sleep 3`.
5. Chạy Newman: `newman run EShop_Collection_v2.json -e EShop_Environment.json --reporters cli,htmlextra`
6. Chạy Pact: `npm run test:pact`

### 7.2 Cấu hình Báo cáo Đẹp (HTML Extra) & Artifacts
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

## 8. Phân tích Điểm mù (Failure Modes - 3 Case Studies)
Đây là phần cốt lõi chứng minh tính thực tiễn của đồ án. Máy móc/Công cụ đôi khi "nói dối" và khiến kỹ sư kiểm thử (QA) rơi vào cái bẫy False Positive (Tưởng là đúng nhưng thực ra là sai). Dưới đây là 3 "cú lừa" kinh điển:

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

---

## 9. Đúc kết và Bài học Kinh nghiệm
Quãng thời gian 2 tháng nghiên cứu và triển khai đề tài T06 mang lại cái nhìn sâu sắc cho toàn nhóm về hệ sinh thái QA hiện đại.
1. **Tooling không phải là tất cả:** Postman hay Karate chỉ là công cụ. Tư duy thiết kế test (Test Design Thinking) để tìm ra các Edge Cases mới là yếu tố quyết định chất lượng phần mềm.
2. **AI là Trợ lý, không phải Trọng tài:** Việc nhắm mắt tin tưởng đoạn code do AI sinh ra là con đường ngắn nhất dẫn đến thảm họa False Positives trên production. Human-in-the-loop là quy trình bắt buộc.
3. **Pact bảo vệ Kiến trúc, Postman bảo vệ Nghiệp vụ:** Việc ứng dụng Pact giúp dập tắt hoàn toàn các cuộc cãi vã giữa team Frontend và Backend về việc "Ai đổi API làm sập app?". Hợp đồng JSON trở thành tài liệu giao tiếp trung tâm (Single source of truth).

*Dự án EShop là minh chứng rõ nét cho việc: Kiểm thử API không chỉ là "Gửi request - Nhận 200 OK". Đó là một nghệ thuật đảm bảo rủi ro kinh doanh được kiểm soát ở mức thấp nhất, bằng những dòng code tự động hóa sắc bén nhất.*
