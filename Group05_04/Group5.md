# Weekly Report

## General Information

- **Group ID:** Group 05
- **Project Name:** API & Contract Testing
- **Date Range:** 2026-06-27 – 2026-07-04

---

# Tasks Completed This Week

## Phạm Đức Toàn – 23127540

- Nghiên cứu các công cụ Postman, Claude/ChatGPT và Karate phục vụ đề tài API & Contract Testing.
- Tổng hợp thông tin về tính năng, ưu điểm, hạn chế và khả năng áp dụng của từng công cụ đối với hệ thống EShop.
- Xây dựng bảng so sánh các công cụ dựa trên các tiêu chí: License/Cost, Learning Curve, EShop Fit, AI Capability, Community & Documentation.
- Phân tích kết quả khảo sát và đề xuất lựa chọn **Postman kết hợp Claude** làm bộ công cụ chính của nhóm.
- Hoàn thiện phần **Giới thiệu đề tài**, **Khảo sát công cụ**, **Ma trận so sánh** và **Lý do lựa chọn công cụ** trong tài liệu Tool Survey Proposal.
- Evidence: `Tool_Research.md` (bao gồm bảng so sánh công cụ và tài liệu tổng hợp khảo sát).

---

## Nguyễn Nhật Nam – 23127092

**Prompt đã sử dụng**

> "Hãy nghiên cứu quy trình API Testing cho hệ thống E-Shop, đề xuất workflow phù hợp, xây dựng kế hoạch triển khai theo các milestone (M1–M5) và viết phần Risk Analysis (bao gồm rủi ro kỹ thuật, quy trình, và AI) theo chuẩn báo cáo học thuật/chuyên nghiệp. Xuất toàn bộ kết quả với cấu trúc rõ ràng, sử dụng tiêu đề (#, ##, ###), bảng, danh sách."

**AI đã thực hiện**

- Nghiên cứu và đề xuất quy trình API Testing 3 lớp (Functional, AI-Augmented, Contract Testing) cho hệ thống E-Shop.
- Đề xuất Workflow 4 bước triển khai kết hợp Postman, AI (Claude/ChatGPT), và Pact.
- Xây dựng kế hoạch triển khai chi tiết theo 5 milestone (M1–M5) dưới dạng bảng.
- Phân tích các rủi ro (kỹ thuật, quy trình, từ AI) và đề xuất phương án giảm thiểu (Mitigation Strategies).

**Sinh viên đã thực hiện**

- Xây dựng yêu cầu (prompt) chi tiết bám sát vào mục tiêu của dự án kiểm thử API & Contract.
- Đánh giá, kiểm duyệt thủ công các nội dung báo cáo do AI sinh ra để đảm bảo phù hợp với thực tế và yêu cầu đồ án.
- Tổng hợp nội dung và định dạng lại kết quả để đưa vào báo cáo nhóm.
- Evidence: `API_Testing_Workflow_Report.md` (bao gồm quy trình API Testing, bảng kế hoạch triển khai M1–M5, và phân tích rủi ro).

---

## Nguyễn Quang Đăng Khoa – 23127212

- Nghiên cứu công cụ Postman và khả năng import OpenAPI Specification.
- Xây dựng các ví dụ kiểm thử (test cases) cho các endpoint: `POST /api/login`, `GET /api/products`, `GET /api/categories`, `POST /api/categories`.
- Evidence: `Postman_Proposal.md` (bao gồm hình ảnh các ví dụ kiểm thử).

---

## Huỳnh Sĩ Luân – 23127086

- Nghiên cứu chi tiết về **AI Test Generation** và **Karate DSL**.
- Chuẩn bị các ví dụ thực tế về việc sử dụng AI sinh test từ    OpenAPI.
- Đánh giá khả năng áp dụng, ưu và nhược điểm của các công cụ này cho nội dung báo cáo và demo seminar.
- Biên soạn nội dung đóng góp vào tài liệu Proposal của nhóm.
- Evidence: `Karate_AI_Test_Research.md` (tài liệu nghiên cứu AI Test Generation & Karate DSL, bao gồm ví dụ mẫu kịch bản test).

---

# AI Usage Declaration

Trong tuần này, nhóm sử dụng AI (ChatGPT/Claude) để:

- Hỗ trợ khảo sát và so sánh các công cụ kiểm thử API.
- Tổng hợp ưu điểm, hạn chế và khả năng áp dụng của từng công cụ.
- Hỗ trợ xây dựng bảng so sánh và đề xuất workflow.
- Hỗ trợ rà soát, chỉnh sửa và cải thiện nội dung tài liệu.

Toàn bộ kết quả do AI sinh ra đều được các thành viên kiểm tra, đối chiếu với tài liệu chính thức trước khi đưa vào báo cáo.

---

# Tasks Planned for Next Week

- Xây dựng Postman Collection cho các API chính của EShop.
- Thiết lập Collection Variables và Authentication.
- Sinh test case từ OpenAPI bằng AI.
- So sánh bộ test AI với bộ test viết thủ công.
- Hoàn thiện tài liệu và chuẩn bị cho milestone tiếp theo.

---

# Issues

- Các thành viên còn đang làm quen với một số công cụ mới (Karate, Pact).
- AI đôi khi sinh ra test case chưa phù hợp với business logic của hệ thống.
- Nhóm thống nhất sẽ review thủ công toàn bộ nội dung do AI hỗ trợ trước khi sử dụng.
