# Tài liệu Nghiên cứu: AI Test Generation và Karate DSL


---

## 1. Tổng quan về Karate DSL

**Karate DSL** là một framework kiểm thử mã nguồn mở rất mạnh mẽ dùng cho việc tự động hóa kiểm thử API (REST, GraphQL, SOAP), kiểm thử UI, và kiểm thử hiệu năng (Performance Testing). 

### Đặc điểm nổi bật:
- **Gherkin-style**: Sử dụng cú pháp BDD (Behavior-Driven Development) giúp các kịch bản test dễ đọc, dễ viết ngay cả với những người không chuyên lập trình.
- **Không cần viết code Java glue-code**: Khác với Cucumber cần phải viết code binding (glue-code) bằng Java/C#, Karate đã xây dựng sẵn tất cả các bước (steps) cần thiết cho API Testing (gửi request, kiểm tra status, assert JSON/XML body...).
- **Native JSON & XML support**: Việc xử lý, so sánh và assert các dữ liệu JSON/XML được thực hiện vô cùng đơn giản và trực quan.
- **Tích hợp mạnh mẽ**: Dễ dàng chạy qua Maven/Gradle, tích hợp vào các pipeline CI/CD (Jenkins, GitHub Actions...).

### Cú pháp Karate DSL cơ bản:
```gherkin
Feature: API Testing example with Karate
  Background:
    * url 'http://localhost:3000'

  Scenario: Verify login endpoint
    Given path '/api/login'
    And request { email: 'test@domain.com', password: 'Password123!' }
    When method post
    Then status 200
    And match response.token == '#present'
```

---

## 2. Phương pháp AI Test Generation từ OpenAPI Spec

**AI Test Generation** là việc tận dụng các mô hình ngôn ngữ lớn (LLM như Claude, GPT) để phân tích đặc tả API (OpenAPI Specification / Swagger) và tự động sinh ra các kịch bản kiểm thử (Karate feature files, Postman collections...).

### Quy trình thực hiện:
1. **Đọc OpenAPI Spec**: Cung cấp file đặc tả API dạng JSON/YAML cho AI.
2. **Thiết kế Prompt**: Hướng dẫn AI hiểu cấu trúc Karate DSL và các quy tắc nghiệp vụ (Business Rules).
3. **Sinh kịch bản**: AI phân tích đường dẫn (paths), phương thức (methods), tham số (parameters), và cấu trúc response để sinh ra file test mẫu (scaffold).
4. **Kiểm duyệt và Tinh chỉnh**: Thành viên nhóm kiểm tra tính đúng đắn của logic nghiệp vụ và chạy thử nghiệm.

---

## 3. Ví dụ Minh họa: AI sinh Test Karate từ OpenAPI của EShop

Dưới đây là một phần đặc tả OpenAPI và kịch bản Karate DSL tương ứng được sinh ra bởi AI.

### OpenAPI Specification Snippet (EShop Products)
```yaml
paths:
  /api/products:
    get:
      summary: Lấy danh sách sản phẩm
      parameters:
        - name: search
          in: query
          required: false
          schema:
            type: string
          description: Tìm kiếm sản phẩm theo tên
      responses:
        '200':
          description: Thành công
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                    name:
                      type: string
                    price:
                      type: number
                    description:
                      type: string
                    imageUrl:
                      type: string
                    category_id:
                      type: integer
```

### Kịch bản Karate DSL sinh bởi AI
```gherkin
Feature: EShop Products API Verification

Background:
  * url 'http://localhost:3000'

Scenario: Get list of all products
  Given path '/api/products'
  When method get
  Then status 200
  And match response == '#[]'
  And match each response == { id: '#number', name: '#string', price: '#number', description: '#string', imageUrl: '#string', category_id: '#number' }

Scenario: Search products by keyword
  Given path '/api/products'
  And param search = 'phone'
  When method get
  Then status 200
  And match response == '#[]'
  And match each response.name contains 'phone'
```

---

## 4. Đánh giá Khả năng Áp dụng cho Seminar

### Ưu điểm của việc kết hợp AI và Karate:
1. **Tốc độ vượt trội**: Tạo khung test (scaffold) cho hàng chục endpoint chỉ trong vài giây.
2. **Giảm thiểu lỗi cú pháp**: AI viết cú pháp Karate DSL rất chuẩn, tránh các lỗi gõ nhầm.
3. **Tự động hóa bao phủ (Schema Coverage)**: Đảm bảo kiểm thử đầy đủ các kiểu dữ liệu khai báo trong Spec.

### Hạn chế:
1. **Thiếu logic nghiệp vụ**: AI không tự hiểu các ràng buộc logic phức tạp (ví dụ: không thể thêm hàng vào giỏ nếu số lượng tồn kho bằng 0, trừ khi được cung cấp thêm ngữ cảnh).
2. **Dữ liệu giả lập**: Các giá trị đầu vào do AI sinh ra đôi khi không hợp lệ trong database thực tế.

### Đề xuất áp dụng vào Seminar nhóm:
* **Phần Demo Live**: Trình diễn quy trình đưa file `api_specification.md` của EShop vào AI (Claude/ChatGPT) để sinh nhanh file `.feature`, sau đó chạy file này bằng Karate để chứng minh hiệu quả thực tế.
* **In-class Activity (Spec-to-Tests Sprint)**: Cho các đội tham gia seminar thi tài: Một nửa viết tay kiểm thử cho 1 endpoint, nửa còn lại dùng AI sinh. Sau đó đối chiếu để rút ra kết luận về sự hỗ trợ của AI và vai trò của con người trong viết test case.
