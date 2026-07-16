# Tool Survey Proposal
## T06 – API & Contract Testing
**CS423 / CSC15003 – Software Testing Seminar Track**

---

## 1. Giới thiệu đề tài

Đề tài T06 tập trung vào kiểm thử API và kiểm thử hợp đồng (contract testing) cho hệ thống **EShop** — một ứng dụng thương mại điện tử có REST API được tài liệu hoá theo chuẩn OpenAPI. Mục tiêu là so sánh phương pháp truyền thống (viết test thủ công, dùng công cụ chuyên dụng) với hướng tiếp cận tăng cường bởi AI (sinh test tự động từ spec), đồng thời triển khai contract testing để đảm bảo provider và consumer luôn đồng bộ.

Báo cáo này đề xuất bộ công cụ sẽ được sử dụng trong seminar, kèm phân tích so sánh và lý do lựa chọn.

---

## 2. Các công cụ đề xuất

Nhóm đề xuất **ba công cụ** theo ba vai trò: một công cụ truyền thống, một công cụ AI-augmented, và một công cụ dự phòng.

### 2.1 Công cụ truyền thống – **Postman**

Postman là nền tảng kiểm thử API phổ biến nhất hiện nay. Người dùng có thể tạo collection, viết test script bằng JavaScript (chai-based), cấu hình biến môi trường, và chạy test tự động qua Newman (CLI runner).

**Tính năng nổi bật:**
- Giao diện đồ hoạ trực quan, phù hợp cho cả thủ công lẫn tự động hoá
- Hỗ trợ chained-token auth qua Collection Variables
- Tích hợp Monitor để chạy test định kỳ trên cloud
- Import trực tiếp từ OpenAPI spec (`.yaml` / `.json`) để tạo collection scaffold

**Phạm vi áp dụng cho EShop:**
- `POST /auth/login` → kiểm thử xác thực, lưu token vào biến
- `GET /products` → kiểm thử phân trang, filter, response schema
- `POST /cart` → kiểm thử logic giỏ hàng (thêm, xoá, cập nhật)
- `POST /orders` → kiểm thử đặt hàng end-to-end, validate status code + body

---

### 2.2 Công cụ AI-Augmented – **Claude / ChatGPT (AI Test Generation từ OpenAPI)**

Cung cấp file `api_specification.yaml` của EShop cho một LLM (Claude hoặc ChatGPT), sau đó yêu cầu sinh ra bộ test cases bao gồm happy path, negative tests, edge cases và security checks. Output có thể là Postman collection JSON hoặc Karate Gherkin script.

**Tính năng nổi bật:**
- Sinh test nhanh từ spec mà không cần đọc toàn bộ tài liệu
- Có thể yêu cầu adversarial payloads (SQL injection, malformed JSON, coupon abuse, race condition)
- Dễ dàng diff với collection viết tay để tìm điểm mù
- Hỗ trợ viết documentation và assertion explanation inline

**Giới hạn cần lưu ý:**
- AI chỉ đọc được những gì có trong spec; business rules ngầm định (ví dụ: giới hạn số lượng coupon per user) thường bị bỏ qua
- Cần human review để loại bỏ false positives và bổ sung domain-specific logic
- Không tự chạy được test — vẫn cần export sang Postman/Karate để execute

---

### 2.3 Công cụ dự phòng – **Karate (DSL)**

Karate là framework kiểm thử API mã nguồn mở dùng cú pháp Gherkin, tích hợp sẵn runner, assertion và report. Phù hợp cho nhóm quen BDD hoặc muốn kiểm thử REST + GraphQL + WebSocket trong cùng một framework.

**Tính năng nổi bật:**
- Không cần viết Java boilerplate — test script là `.feature` file thuần Gherkin
- Hỗ trợ parallel execution và HTML report tích hợp sẵn
- Dễ kết hợp với output sinh từ AI (AI có thể trực tiếp sinh `.feature` files)
- Tích hợp JUnit 5, chạy được trong CI/CD pipeline

**Vai trò trong đề tài:**
Karate được dùng làm backup nếu nhóm gặp khó khăn với RestAssured (Java boilerplate) hoặc muốn có một format thứ hai để so sánh với Postman collection trong phần diff AI vs Manual.

---

## 3. Ma trận so sánh công cụ

| Tiêu chí | Postman | AI (Claude/ChatGPT) | Karate |
|---|---|---|---|
| **Licence / Chi phí** | Free tier đủ dùng; Postbot cần Pro ($12/tháng) | Free tier (Claude.ai / ChatGPT Free) đủ cho seminar | Mã nguồn mở, Apache 2.0, hoàn toàn miễn phí |
| **Learning Curve** | Thấp — GUI trực quan, nhiều tutorial | Rất thấp — chỉ cần biết cách đặt prompt | Trung bình — cần học Gherkin + cú pháp Karate riêng |
| **EShop Fit** | Cao — import OpenAPI trực tiếp, chained auth dễ cấu hình | Cao — sinh test từ `api_specification.yaml` ngay lập tức | Cao — hỗ trợ REST đầy đủ, parallel test cho nhiều endpoint |
| **AI Capability** | Postbot tích hợp inline (giới hạn ở free) | Native — đây chính là mục tiêu của công cụ | Thấp — không có tính năng AI built-in, phụ thuộc output từ LLM |
| **Community & Tài liệu** | Rất lớn — docs phong phú, Stack Overflow active | Rộng nhưng phân tán — phụ thuộc vào prompt engineering community | Trung bình — GitHub active, docs tốt nhưng ít ví dụ tiếng Việt |

> **Ghi chú cột "EShop Fit":** Đánh giá dựa trên khả năng xử lý các endpoint trong checklist Stage S3: `POST /auth/login`, `GET /products`, `POST /cart`, `POST /orders`, và `POST /coupon/redeem` (từ in-class activity).

---

## 4. Công cụ được chọn và lý do

###  Công cụ chính: **Postman + AI (Claude)**

Nhóm sẽ kết hợp hai công cụ này theo workflow:

1. **AI (Claude) sinh scaffold** từ `api_specification.yaml` → xuất ra Postman Collection JSON
2. **Nhóm viết thủ công** một bộ collection song song (dùng Postman GUI)
3. **Diff hai bộ test** → phân tích điểm khác biệt, bổ sung business logic mà AI bỏ sót
4. **Pact** sẽ được thêm vào ở milestone 4 để kiểm thử hợp đồng giữa mobile consumer và Node backend

**Ba lý do chọn bộ đôi Postman + AI:**

- **Bao phủ cả hai hướng trong một workflow liền mạch:** Postman là ground truth; AI output là hypothesis. Việc diff chúng tạo ra insight thực sự về những gì AI làm được và không làm được — đây là trọng tâm học thuật của đề tài.
- **Không cần cấu hình môi trường phức tạp:** Postman có thể chạy ngay, AI có thể dùng free tier. Nhóm không mất thời gian setup Java/Maven (như RestAssured) trước khi bắt đầu kiểm thử thực sự.
- **Phù hợp với in-class activity "Spec-to-Tests Sprint":** Activity yêu cầu so sánh viết test bằng tay vs AI trong 25 phút — Postman + Claude là combo tự nhiên nhất để minh hoạ sự khác biệt trực tiếp trên cùng interface.

---

## 5. Kế hoạch triển khai theo Stage S3 Milestones

| Milestone | Công việc | Công cụ | Người phụ trách (dự kiến) |
|---|---|---|---|
| **M1** | Viết Postman collection: `POST /auth/login`, `GET /products`, `POST /cart`, `POST /orders` | Postman | Cả nhóm |
| **M2** | Cấu hình chained-token auth dùng Collection Variables | Postman | — |
| **M3** | Sinh scaffold từ `api_specification.yaml` bằng Claude; diff vs collection thủ công | Claude + Postman | — |
| **M4** | Cấu hình Pact provider verification trên Node backend | Pact | — |
| **M5** | Tài liệu hoá 5 contract violations có thể gặp | Markdown | Cả nhóm |

---

## 6. Rủi ro và phương án ứng phó

| Rủi ro | Mức độ | Phương án |
|---|---|---|
| AI sinh test có hallucination (endpoint không tồn tại, field sai) | Trung bình | Luôn validate output của AI bằng cách chạy thực tế qua Postman; không dùng AI output trực tiếp mà không review |
| Pact setup phức tạp trên Node backend | Cao | Dành ít nhất 2 buổi riêng cho Pact; tham khảo repo `pact-js` official examples |
| Free tier AI bị rate limit trong lúc live demo | Thấp | Chuẩn bị sẵn output đã sinh trước trong `.json` file; không demo live generation |
| Spec EShop không đầy đủ hoặc có lỗi | Trung bình | Document lại các gap trong spec như một phần của "failure modes" section trong User Guide |

---

## 7. AI Disclosure

| Mục | Chi tiết |
|---|---|
| **AI được dùng để nghiên cứu** | Claude (Anthropic) — dùng để tra cứu so sánh công cụ, tổng hợp ưu/nhược điểm, và sinh ví dụ test case minh hoạ |
| **Nội dung do AI sinh** | Phần tóm tắt tính năng công cụ (Section 2), ý tưởng cho phần ma trận so sánh (Section 3) |
| **Nội dung được cross-check** | Thông tin về Postman licensing → kiểm tra trên [postman.com/pricing](https://www.postman.com/pricing); thông tin về Karate license → kiểm tra trên [GitHub karatelabs/karate](https://github.com/karatelabs/karate); thông tin về Pact → kiểm tra trên [docs.pact.io](https://docs.pact.io) |
| **Những gì KHÔNG dùng AI** | Quyết định cuối cùng về công cụ, lý do lựa chọn (Section 4), và kế hoạch triển khai (Section 5) — đây là phán đoán của nhóm dựa trên context của EShop và yêu cầu của seminar |

---

## 8. Tài liệu tham khảo

- Mark Winteringham, *API Testing in Action*, Manning, Chapters 4 & 9.
- Pact Documentation — [Provider Verification](https://docs.pact.io/provider)
- EShop `/api_specification.md` — xem trong repository.
- Postman Documentation — [Collection Runner & Newman](https://learning.postman.com/docs/collections/running-collections/using-newman-cli/command-line-integration-with-newman/)
- Karate Labs — [Getting Started](https://github.com/karatelabs/karate#getting-started)
- T06 Brief — *2026 AI-First CS423/CSC15003 Software Testing Seminar Track*

---