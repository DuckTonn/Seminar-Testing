# Khung Seminar Slides: API & Contract Testing

**Tổng số lượng:** 14 Slides
**Cấu trúc 4 phần:** API Testing (Postman) -> AI Test Gen -> Contract Testing (Pact) -> CI/CD.

---

### Slide 1: Title Slide
- **Tiêu đề:** Tự động hóa Kiểm thử API & Contract Testing 
- **Phụ đề:** Từ Postman, AI Generation đến tích hợp CI/CD với Pact
- **Nhóm trình bày:** Group 05

### Slide 2: Agenda (Nội dung chính)
- Phần 1: API Testing với Postman & Các điểm mù
- Phần 2: AI Test Generation - Cơ hội & Rủi ro
- Phần 3: Contract Testing với Pact (V3)
- Phần 4: Tự động hóa quy trình với CI/CD

---
**PHẦN 1: API TESTING (POSTMAN)**

### Slide 3: Tổng quan về SUT (EShop) & API Testing
- Kiến trúc hệ thống EShop (Node.js Backend, Mock Database).
- Các luồng nghiệp vụ cốt lõi: Auth -> Cart -> Checkout.
- Vai trò của Postman trong việc kiểm thử Black-box API.

### Slide 4: Tổ chức Postman Collection & Automation
- Tách biệt Environment Variables (`{{baseUrl}}`, `{{token}}`).
- Khái niệm Test Scripts (JavaScript) trong pre-request và test tabs.
- Chạy End-to-End với Collection Runner.

### Slide 5: Postman Failure Modes (Lưu ý quan trọng)
- **Silent Failure:** Lỗi cú pháp JS làm sập script ngầm, Test vẫn báo Pass.
- **Unresolved Variables:** Quên set môi trường, Postman không báo lỗi ngay.
- **Type Mismatch:** Assertions của Chai đôi khi gây lú lẫn về kiểu dữ liệu.

---
**PHẦN 2: AI TEST GENERATION**

### Slide 6: Ứng dụng AI sinh kịch bản test
- Quy trình: OpenAPI Specification + Prompts -> Postman Script.
- Ưu điểm: Tiết kiệm thời gian gõ boilerplate code, tự động sinh JSON schema validator.

### Slide 7: Điểm mù của AI (AI Failure Modes)
- **Schema Validation vô giá trị:** Sinh schema rỗng, cái gì cũng Pass (False Positive).
- **Thiên kiến Happy-path:** Bỏ qua Negative/Edge cases (giá trị âm, null, thiếu field).
- **Lỗ hổng RBAC:** Không biết cách giả lập các kịch bản phân quyền, IDOR.

### Slide 8: Giải pháp từ Con người (Manual Mitigations)
- Nguyên tắc: AI làm phần khung, Tester làm phần hồn.
- Bổ sung Edge Cases thủ công: Boundary values, Invalid State, Security Testing.

---
**PHẦN 3: CONTRACT TESTING (PACT)**

### Slide 9: Vấn đề của Integration Test truyền thống
- Test trên môi trường staging quá tốn kém và cồng kềnh.
- Backend sửa API, Frontend sập mà không ai biết trước lúc deploy.
- Giải pháp: Contract Testing - Chốt hợp đồng giao tiếp giữa Consumer và Provider.

### Slide 10: Pact Workflow - Phía Consumer
- Consumer định nghĩa kỳ vọng (Expectations).
- Sử dụng Matchers thay vì Hard-coded values.
- Sinh ra file Hợp đồng (Pact JSON).

### Slide 11: Pact Workflow - Phía Provider
- Provider đọc file JSON và tự động gửi request vào server test.
- Tầm quan trọng của `stateHandlers`: Setup/Teardown dữ liệu khớp với Consumer.

### Slide 12: Pact Failure Modes
- **Silent Schema Change (Postel's Law):** Provider thêm field dư thừa thì Pact vẫn Pass.
- **Bùng nổ bảo trì:** StateHandlers phức tạp dần theo thời gian, nguy cơ Flaky tests nếu dọn rác DB không kỹ.
- **Thiếu Performance Test:** Pact chỉ kiểm tra cấu trúc, không kiểm tra tốc độ.

---
**PHẦN 4: CI/CD & TỔNG KẾT**

### Slide 13: CI/CD Pipeline Integration
- Tích hợp Newman CLI để chạy Postman trên GitHub Actions.
- Tích hợp Pact verification vào CI Pipeline chặn deploy nếu vỡ Contract.
- Tự động xuất HTML Reports cho team theo dõi.

### Slide 14: Q&A và Lời Cảm Ơn
- Tóm tắt: Không có công cụ nào hoàn hảo.
- Mời giảng viên và các bạn sinh viên đặt câu hỏi.
