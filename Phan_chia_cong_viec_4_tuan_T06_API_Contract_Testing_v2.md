# Phân chia công việc 4 tuần còn lại -- T06 API & Contract Testing
*(Bản v2 – đã bổ sung theo rubric T06 brief và checklist milestones M1–M5)*

## Thành viên

-   Toàn -- API Testing (Postman & Newman)
-   Khoa -- AI Testing
-   Luân -- CI/CD
-   Nam -- Contract Testing & Documentation

------------------------------------------------------------------------

# Tuần 0 (đầu Tuần 1) -- Bước chuẩn bị bắt buộc

> **Mới bổ sung:** nếu giảng viên có feedback ở Stage S2 (Instructor Review), cả nhóm cần xử lý trước khi bắt tay vào code/test.

## Cả nhóm

-   Rà soát lại `Tool_Survey_Proposal.md` theo comment của giảng viên ở Stage S2 (nếu có), chốt lại tool chính thức trước khi triển khai.
-   Toàn & Nam thống nhất **danh sách endpoint dùng chung** cho Postman và Pact (ví dụ: `POST /cart`, `POST /orders`) để Contract Test của Nam khớp với API Test của Toàn, tránh làm lệch nhau.

**Deliverables** - Tool_Survey_Proposal_final.md - Bảng endpoint dùng chung (Postman ⇄ Pact)

------------------------------------------------------------------------

# Tuần 1

## Toàn

-   Cài đặt Postman, tạo Workspace, Collection, Environment.
-   Import OpenAPI Specification.
-   Viết API test:
    -   POST /auth/login
    -   GET /products
    -   GET /products/{id}
-   Cấu hình Authentication bằng JWT.
-   Lưu Token bằng Collection Variables.
-   **Bàn giao sớm bản collection nháp cho Luân** để Luân không phải chờ đến tuần 2 mới tích hợp Newman.

**Deliverables** - Postman Collection v1 - Environment - Authentication hoạt động

## Khoa

-   Chuẩn bị OpenAPI Specification.
-   Dùng ChatGPT và Claude sinh:
    -   Test Cases
    -   Postman Collection
    -   Assertions
-   Thu thập Prompt.

**Deliverables** - AI Generated Test Cases - Prompt Library

## Luân

-   Tạo GitHub Repository.
-   Setup GitHub Actions.
-   Tạo workflow đầu tiên.
-   Cài Newman CLI.
-   Pipeline:
    -   Checkout source
    -   Setup Node
    -   Install dependencies
    -   Chạy Newman

**Deliverables** - GitHub Actions Workflow v1 - Pipeline chạy thành công

## Nam

-   Setup Pact.
-   Tạo Consumer Test **trên endpoint đã thống nhất với Toàn** (cart/orders).
-   Tìm hiểu Provider Verification.
-   Chạy project mẫu.

**Deliverables** - Pact Demo - Consumer Contract

------------------------------------------------------------------------

# Tuần 2

## Toàn

-   Viết test cho:
    -   POST /cart
    -   POST /orders
-   Thêm Assertions.
-   Schema Validation.
-   Negative Test.
-   Xuất Newman HTML Report.
-   **Bắt đầu ghi chú lại các "failure mode" của Postman** khi test (VD: assertion sai vẫn pass, token hết hạn không báo rõ) — để dùng cho User Guide tuần 3.

**Deliverables** - Postman Collection hoàn chỉnh - Newman Report - Ghi chú Failure Modes (Postman)

## Khoa

-   So sánh AI vs Manual.
-   Bổ sung Edge Cases.
-   Viết AI Evaluation.
-   Viết Failure Modes (phần AI).

**Deliverables** - AI Comparison Report - Failure Modes (AI)

## Luân

-   Tích hợp Newman vào GitHub Actions.
-   Tích hợp Pact Verification.
-   Upload HTML Reports làm Artifact.
-   Kiểm tra pipeline tự động.

**Deliverables** - CI/CD Pipeline hoàn chỉnh - HTML Reports

## Nam

-   Hoàn thiện Provider Verification.
-   Ghi nhận tối thiểu 5 Contract Violations.
-   Chuẩn bị demo Contract Testing.
-   **Ghi chú lại failure mode của Pact** (VD: verification pass nhưng không phát hiện thay đổi schema ngầm) — dùng cho User Guide tuần 3.

**Deliverables** - Provider Verification - Contract Violations Report - Ghi chú Failure Modes (Pact)

------------------------------------------------------------------------

# Tuần 3

## Toàn

-   Review Collection.
-   Fix bug.
-   Viết User Guide phần Postman.
-   Chuẩn bị Demo API.
-   **Viết phần slide của mình** (API Testing) để đóng góp vào Seminar Slides chung.

## Khoa

-   Viết User Guide phần AI.
-   Hoàn thiện Prompt.
-   Chuẩn bị Demo AI.
-   **Viết phần slide của mình** (AI Testing).

## Luân

-   Viết tài liệu CI/CD.
-   Vẽ Pipeline Diagram.
-   Demo GitHub Actions.
-   **Viết phần slide của mình** (CI/CD).

## Nam

-   Viết User Guide phần Pact.
-   **Tổng hợp 3 phần Failure Modes (Postman, AI, Pact) thành 1 mục "Failure Modes" chung** trong User Guide — đúng yêu cầu rubric (không tách rời từng phần).
-   Làm Activity Worksheet.
-   Quay Demo Video — **checklist bắt buộc: phải có ít nhất 1 tính năng Postman VÀ 1 tính năng AI test gen trong cùng video** (yêu cầu rubric live demo).
-   Tổng hợp khung Seminar Slides từ phần của 3 người còn lại (không tự làm hết một mình).

**Deliverables tuần 3** - User Guide bản nháp (đã có mục Failure Modes tổng hợp) - Slides bản nháp (đóng góp từ cả 4 người) - Activity Worksheet (bản nháp) - Demo Video bản nháp (đủ Postman + AI)

------------------------------------------------------------------------

# Tuần 4

## Toàn

-   Kiểm thử lại toàn bộ Collection.
-   Sửa lỗi.
-   Hỗ trợ tổng hợp.
-   **Chủ trì viết [AI-02]/[AI-03]/[AI-04]**: tổng hợp AI usage log của cả 4 thành viên trong suốt project (theo format "AI Usage Declaration" đã dùng ở Weekly Report).

## Khoa

-   Rà soát AI Report.
-   Hoàn thiện tài liệu.
-   Cung cấp AI usage log của mình cho Toàn để đưa vào [AI-02]/[AI-03]/[AI-04].

## Luân

-   Kiểm tra toàn bộ CI/CD Pipeline.
-   Tối ưu Workflow.
-   Kiểm tra Reports.
-   **Nhờ 1 nhóm khác chạy thử Activity Worksheet**, đo thời gian thực tế (phải ≤ 25 phút không cần trợ giúp), ghi nhận chỗ gây khó hiểu để Nam chỉnh sửa.

## Nam

-   Hoàn thiện Slides (tổng hợp từ 4 phần, không tự viết lại từ đầu).
-   Hoàn thiện User Guide (đảm bảo đủ ≥ 6 mục + mục Failure Modes tổng hợp).
-   Chỉnh sửa Activity Worksheet dựa trên phản hồi từ nhóm test thử (do Luân thu thập).
-   Ghép Demo Video.
-   **Đóng gói sản phẩm cuối cùng — việc chung cả nhóm, không phải một mình Nam** (mỗi người tự kiểm tra deliverable của phần mình trước khi Nam ghép).

## Cả nhóm (2–3 ngày cuối tuần 4)

> **Mới bổ sung — buffer bắt buộc**, tránh dồn hết việc vào phút chót.

-   Rehearsal seminar toàn nhóm.
-   Review chéo toàn bộ deliverables theo rubric Section 6 (Seminar_Guide.docx).
-   Dự phòng xử lý sự cố nếu Pact hoặc CI/CD lỗi phút chót (tham khảo phương án dự phòng đã nêu trong Tool_Survey_Proposal: dành thêm buổi riêng, tham khảo `pact-js` official examples).

------------------------------------------------------------------------

# Deliverables cuối cùng

## Toàn

-   Postman Collection
-   Environment
-   Newman Report
-   API Test Scripts
-   User Guide (Postman) + Failure Modes (Postman)
-   [AI-02]/[AI-03]/[AI-04] (tổng hợp)

## Khoa

-   AI Generated Tests
-   Prompt Library
-   AI vs Manual Report
-   Failure Modes (AI)
-   User Guide (AI)

## Luân

-   GitHub Actions Workflow
-   CI/CD Pipeline
-   Automated Test Reports
-   CI/CD Documentation
-   Biên bản test thử Activity Worksheet với nhóm khác

## Nam

-   Pact Consumer Test
-   Provider Verification
-   Contract Violations Report
-   Failure Modes (Pact)
-   User Guide (Pact + mục Failure Modes tổng hợp)
-   Seminar Slides (tổng hợp)
-   Activity Worksheet (đã kiểm chứng bởi nhóm khác)
-   Demo Video (có đủ Postman + AI)

# Sản phẩm cuối cùng của nhóm

-   Postman Collection hoàn chỉnh.
-   AI Generated Tests từ OpenAPI.
-   Báo cáo AI vs Manual.
-   Pact Contract Testing.
-   GitHub Actions CI/CD Pipeline.
-   Automated Test Reports.
-   User Guide (đủ ≥ 6 mục, có mục Failure Modes tổng hợp cả 3 tool).
-   Seminar Slides (≤ 15 slides).
-   Activity Worksheet (đã kiểm chứng bởi nhóm khác, ≤ 25 phút).
-   Demo Video (5–8 phút, có đủ traditional tool + AI tool).
-   [AI-02]/[AI-03]/[AI-04].
