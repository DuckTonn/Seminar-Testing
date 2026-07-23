# Tổng hợp Failure Modes: Câu chuyện từ Postman, AI đến Contract Testing

Trong hành trình đảm bảo chất lượng hệ thống API của EShop, nhóm đã áp dụng lần lượt Postman cho Manual API Testing, AI Test Generation để tăng tốc tự động hóa, và Pact cho Contract Testing. Ở mỗi giai đoạn, chúng ta không chỉ nhận được lợi ích mà còn đối mặt với những "điểm mù" (Failure Modes) đặc trưng. Điểm chung đáng sợ nhất của các công cụ này là hiện tượng **False Positive** – hệ thống báo Pass nhưng thực chất lỗi vẫn đang tồn tại. Dưới đây là bức tranh toàn cảnh về những điểm yếu này.

## 1. Postman: Cạm bẫy của cấu hình thủ công và "Silent Failure"
Khi bắt đầu với Postman, rủi ro lớn nhất đến từ yếu tố con người và cơ chế thực thi script ngầm:
- **Cấu hình sai môi trường:** Quên chọn Environment khiến biến `{{token}}` không được resolve. Postman không báo lỗi biến chưa khởi tạo mà gửi nguyên chuỗi text đi, dẫn đến lỗi 401 hoặc 404 tốn thời gian debug.
- **Silent Failure trong Script:** Nếu mã JS trong tab Tests bị lỗi cú pháp, Postman không hiển thị cảnh báo đỏ rực mà âm thầm bỏ qua các hàm `pm.test` bên dưới. Test Runner vẫn báo Pass màu xanh, tạo cảm giác an toàn giả tạo.
- **So sánh kiểu dữ liệu ngầm định:** Lỗi ép kiểu (trả về String thay vì Number) thường gây bối rối do thông báo lỗi của Chai Assertion khá mơ hồ.

*=> Điểm yếu của Postman nằm ở tính dễ tổn thương trước thao tác thủ công và cơ chế báo lỗi kịch bản thiếu minh bạch.*

## 2. AI Test Gen: Ảo giác dữ liệu và "Thiên kiến Happy-path"
Để khắc phục sự chậm chạp khi viết script Postman thủ công, nhóm dùng AI sinh test case. Nhưng AI lại mang đến những điểm mù nguy hiểm ở cấp độ logic:
- **Schema Validation vô giá trị:** AI có thể sinh ra schema rỗng (`additionalProperties: true`). Điều này khiến API trả về object lỗi hay thiếu field bắt buộc vẫn Pass toàn bộ. AI chỉ quan tâm đến "có đoạn code test schema" chứ không hiểu "schema đúng là gì".
- **Bỏ qua Business Logic và Bảo mật (RBAC):** AI sinh payload đúng cú pháp HTTP nhưng bỏ qua các quy tắc nghiệp vụ (ví dụ: áp mã giảm giá khi đơn hàng chưa đủ điều kiện, hoặc không test các case leo thang đặc quyền). AI sử dụng chung một `{{token}}` cho mọi request, bỏ ngỏ hoàn toàn lỗ hổng IDOR.
- **Thiên kiến Happy-Path:** AI chỉ tập trung vào luồng thành công. Các Edge cases như giá trị âm, chuỗi rỗng, hay sai kiểu dữ liệu gần như bị lờ đi, khiến tầng Validation của Backend không được thử thách.

*=> So với Postman (lỗi do người dùng thiết lập), AI lại sai lầm ở chiều sâu nghiệp vụ: nó "bắt chước" việc tạo test case rất nhanh nhưng hoàn toàn hời hợt về mặt logic kinh doanh.*

## 3. Pact Contract Testing: Thay đổi ngầm và Áp lực bảo trì
Để chốt chặt giao tiếp giữa Frontend và Backend, Pact được đưa vào để đảm bảo API không bị phá vỡ. Tuy nhiên, Pact không phải là viên đạn bạc:
- **Silent Schema Change (Postel's Law):** Khác với sự chặt chẽ của Postman hay sự "hời hợt" của AI, Pact chỉ kiểm tra đúng những gì Consumer yêu cầu. Nếu Backend thêm trường dữ liệu mới (làm thay đổi ngầm luồng nghiệp vụ), Pact vẫn Pass.
- **Phụ thuộc 100% vào Consumer Test:** Tương tự như "Thiên kiến Happy-path" của AI, nếu Consumer quên viết contract cho trường hợp báo lỗi (VD: 401 Unauthorized), thì việc Backend vô tình gỡ bỏ xác thực vẫn sẽ lọt qua mắt Pact. 
- **Bùng nổ chi phí bảo trì (State Handlers):** Khi số lượng API tăng, việc duy trì trạng thái test (`stateHandlers`) phía Provider trở thành ác mộng. Nếu thiếu cơ chế teardown dọn dẹp data, dữ liệu rác sẽ gây xung đột, tạo ra "Flaky tests" (lỗi ngẫu nhiên), điều mà Postman hay AI ít gặp hơn trên môi trường test dùng một lần.
- **Bỏ qua Performance:** Dù API phản hồi chậm gấp 50 lần, Pact vẫn Pass miễn là schema đúng, trái ngược với Postman có thể set timeout cứng trong script.

## Tổng kết
- **Postman** yếu ở tính ổn định khi thực thi script thủ công.
- **AI** yếu ở khả năng nắm bắt logic nghiệp vụ sâu và negative cases.
- **Pact** yếu ở chi phí bảo trì state và chỉ bảo vệ được những gì Consumer chủ động yêu cầu.

Chất lượng hệ thống không đến từ việc phụ thuộc vào một công cụ duy nhất, mà là sự kết hợp: Dùng **AI** để dựng khung test nhanh, dùng QA để thêm Negative Test vào **Postman**, và dùng **Pact** để làm chốt chặn cuối ở luồng CI/CD ngăn chặn thay đổi breaking changes.
