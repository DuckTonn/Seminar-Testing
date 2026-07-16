# Tool Research Report

## API & Contract Testing Tool Survey

---

# 1. Mục tiêu

Khảo sát các công cụ hỗ trợ kiểm thử API nhằm lựa chọn bộ công cụ phù hợp cho đề tài **API & Contract Testing** trên hệ thống EShop.

Các tiêu chí khảo sát:

- Chi phí sử dụng (License / Cost)
- Độ khó khi học (Learning Curve)
- Khả năng tích hợp OpenAPI
- Khả năng hỗ trợ AI
- Community và tài liệu
- Mức độ phù hợp với hệ thống EShop

---

# 2. Khảo sát công cụ

## 2.1 Postman

### Giới thiệu

Postman là công cụ phổ biến nhất hiện nay để kiểm thử REST API. Công cụ hỗ trợ cả kiểm thử thủ công và tự động thông qua Collection Runner và Newman.

### Tính năng

- Import OpenAPI Specification
- Collection
- Environment
- Variables
- JavaScript Test Script
- Newman CLI

### Ưu điểm

- Giao diện trực quan.
- Dễ học.
- Cộng đồng lớn.
- Tài liệu đầy đủ.
- Phù hợp với người mới.

### Hạn chế

- Một số tính năng nâng cao yêu cầu bản Pro.
- Automation chưa linh hoạt bằng framework.

### Đánh giá

Rất phù hợp để xây dựng bộ API Test cho EShop.

---

## 2.2 Claude / ChatGPT

### Giới thiệu

Claude và ChatGPT được sử dụng như công cụ AI hỗ trợ sinh test case từ OpenAPI Specification.

### Có thể hỗ trợ

- Happy Path Test
- Negative Test
- Edge Case
- Boundary Value
- Security Test
- Sinh tài liệu

### Ưu điểm

- Tiết kiệm thời gian.
- Sinh nhiều test case.
- Hỗ trợ brainstorming.
- Giải thích assertion.

### Hạn chế

- Không hiểu business rule.
- Có thể sinh sai endpoint hoặc field.
- Cần kiểm tra lại bằng con người.

### Đánh giá

Phù hợp để hỗ trợ thiết kế test nhưng không thay thế hoàn toàn tester.

---

## 2.3 Karate

### Giới thiệu

Karate là framework kiểm thử API sử dụng DSL theo cú pháp Gherkin.

### Tính năng

- REST API
- GraphQL
- WebSocket
- Parallel Execution
- HTML Report
- JUnit Integration

### Ưu điểm

- Không cần viết nhiều Java.
- Automation mạnh.
- Báo cáo đẹp.

### Hạn chế

- Learning Curve cao hơn Postman.
- Cần học DSL riêng.

### Đánh giá

Phù hợp khi triển khai automation hoặc CI/CD.

---

# 3. Bảng so sánh

| Tiêu chí | Postman | Claude / ChatGPT | Karate |
|-----------|----------|------------------|---------|
| License / Cost | Free (Pro cho một số tính năng) | Free Tier | Open Source |
| Learning Curve | Thấp | Rất thấp | Trung bình |
| OpenAPI Support | Có | Có | Có |
| AI Capability | Thấp | Rất cao | Không |
| Community & Documentation | Rất lớn | Lớn | Khá lớn |
| Khả năng áp dụng cho EShop | Rất phù hợp | Phù hợp để sinh test | Phù hợp cho automation |

---

# 4. Workflow đề xuất

Sau khi khảo sát, đề xuất workflow như sau:

1. Import OpenAPI Specification vào Postman.
2. Sử dụng Claude/ChatGPT để sinh bộ test case.
3. Chuyển kết quả thành Postman Collection.
4. Viết bổ sung các test case liên quan đến business rule.
5. So sánh bộ test AI và bộ test viết thủ công.
6. Chuẩn bị cho Contract Testing bằng Pact ở milestone tiếp theo.

---

# 5. Kết luận

Sau quá trình khảo sát, bộ công cụ được đề xuất gồm:

- **Postman**: Công cụ chính để thực hiện API Testing.
- **Claude / ChatGPT**: Hỗ trợ sinh test case và tài liệu.
- **Karate**: Công cụ dự phòng cho automation.

Việc kết hợp Postman với AI giúp giảm thời gian thiết kế test case, đồng thời vẫn đảm bảo chất lượng thông qua quá trình review và bổ sung các business rule bằng thủ công.

---

# 6. Tài liệu tham khảo

- Postman Documentation
- Karate Documentation
- OpenAPI Specification
- API Testing in Action – Mark Winteringham