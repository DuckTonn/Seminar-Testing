# Kịch Bản Demo: AI-Augmented API Testing
**Thời lượng:** ~3 phút  
**Đối tượng:** Người chưa biết gì về AI testing  
**Môi trường:** Agent IDE (Cursor/VS Code + Claude/ChatGPT) mở tại thư mục repo SUT

---

## Trước khi bắt đầu quay

**Chuẩn bị sẵn trên màn hình:**
1. Agent IDE đang mở tại thư mục gốc của repo SUT (eshop backend).
2. File `api_specification.md` đã được mở trong IDE.
3. Postman Desktop đang chạy, chuẩn bị workspace trống.
4. File `prompt_AI.md` mở sẵn ở tab bên cạnh để copy-paste nhanh.

---

## Bước 0 — Mở đầu & Bối cảnh (15 giây)

**[Camera nhìn vào màn hình IDE]**

> **Thoại:** "Mình đang đứng tại thư mục repo của hệ thống EShop — đây chính là SUT, hệ thống chúng ta cần kiểm thử. Thay vì gõ từng API request tốn hàng giờ, mình sẽ dùng AI Agent ngay bên trong IDE này để sinh ra bộ test Postman trong chưa đầy 1 phút. Và sau đó — mình sẽ chỉ cho bạn thấy tại sao bạn không nên tin hoàn toàn vào AI."

---

## Bước 1 — Mô tả ngữ cảnh & Chạy Prompt 1 (45 giây)

**[Hành động]: Mở chat agent trong IDE (ví dụ: Cursor Composer). Paste `Prompt 1` từ `prompt_AI.md` vào — kèm theo nội dung file `api_specification.md` đính kèm bên dưới.**

> **Thoại:** "Đây là Prompt 1 từ Thư viện Prompt của nhóm — mình ép AI đóng vai Senior QA Engineer. Quan trọng là mình đính kèm toàn bộ API Specification của hệ thống — đây là nguyên liệu để AI hiểu hệ thống đang có gì, thay vì bịa đặt."

**[Hành động]: Nhấn Enter. Chờ AI trả ra khối JSON. Copy toàn bộ khối JSON.**

> **Thoại:** "Trong chưa đầy 1 phút, AI đã phân tích toàn bộ đặc tả và sinh ra một Postman Collection hoàn chỉnh — có đủ các nhóm API, header xác thực, body JSON, và test script cơ bản."

**[Hành động]: Mở Postman → Import → Paste Raw Text → Import. Collection xuất hiện với đầy đủ folder và request.**

> **Thoại:** "Bộ test skeleton đã vào Postman. Công việc tốn hàng giờ nếu làm tay, AI làm xong trong 60 giây."

---

## Bước 2 — Vạch trần Failure Mode: False Positive (40 giây)

**[Hành động]: Trong Postman, mở một request liên quan đến luồng tạo dữ liệu hoặc giao dịch (ví dụ: request đặt hàng). Click vào tab Scripts / Tests.**

> **Thoại:** "Nhưng bây giờ nhìn vào tab Scripts của request này — tab trống hoàn toàn. Không có dòng test nào. Nếu mình chỉ bấm Send..."

**[Hành động]: Bấm Send. Response trả về HTTP 200. Tab Test Results hiện `0 tests passed`.**

> **Thoại:** "Server trả về 200 OK — nhưng Postman không có gì để kiểm tra. Nếu backend trả về dữ liệu sai cấu trúc, thiếu trường, hoặc tính toán nhầm, Postman vẫn im lặng. Đây chính là False Positive — cảm giác an toàn giả cực kỳ nguy hiểm."

**[Hành động]: Quay lại chat AI trong IDE. Paste `Prompt 2` từ `prompt_AI.md`, kèm mô tả endpoint vừa test.**

> **Thoại:** "Mình dùng Prompt 2 để ép AI viết lại Schema Validation đúng chuẩn — phải định nghĩa rõ từng trường bắt buộc, đúng kiểu dữ liệu, và chặn data rò rỉ."

**[Hành động]: Copy đoạn JavaScript mà AI trả ra. Paste vào tab Tests của request trong Postman. Bấm Send lại — lần này hiện test script đang chạy.**

---

## Bước 3 — Bổ sung Security & Negative Tests với Prompt 3 (35 giây)

**[Hành động]: Quay lại chat AI trong IDE. Paste `Prompt 3` từ `prompt_AI.md` + API Spec.**

> **Thoại:** "Điểm mù thứ hai của AI: nó chỉ test luồng thành công. AI không biết rằng một tài khoản bình thường không được phép gọi API của quản trị viên. Prompt 3 ép AI đóng vai Penetration Tester để sinh các kịch bản tấn công phân quyền và dữ liệu bất thường."

**[Hành động]: AI trả ra folder "Negative & Security Tests" dạng JSON. Import vào Postman. Mở một request kiểm tra phân quyền. Bấm Send — kết quả hiện đúng status 403 Forbidden, test Pass màu xanh.**

> **Thoại:** "Giờ chúng ta đã có cả kịch bản tấn công — và AI không thể tự làm điều này nếu không có Prompt đúng."

---

## Bước 4 — Liên kết chuỗi API với Prompt 4 (30 giây)

**[Hành động]: Quay lại chat AI trong IDE. Paste `Prompt 4` + API Spec.**

> **Thoại:** "Vấn đề cuối: AI hay gắn cứng dữ liệu — email tĩnh, ID tĩnh. Khi CI/CD chạy lần 2, sẽ báo lỗi Conflict vì email đã tồn tại. Prompt 4 yêu cầu AI sinh dữ liệu ngẫu nhiên và liên kết chuỗi request — ID từ bước trước tự động truyền sang bước sau."

**[Hành động]: Import collection từ Prompt 4. Chạy Collection Runner — thấy biến môi trường tự động được cập nhật giữa các request liên tiếp. Chạy lần 2 — không còn lỗi Conflict.**

> **Thoại:** "Collection này có thể chạy lặp lại an toàn trên CI/CD pipeline vì dữ liệu mới được sinh ra mỗi lần chạy."

---

## Bước 5 — Kết luận (15 giây)

> **Thoại:** "Tổng kết lại: 4 prompt — 4 vấn đề khác nhau được giải quyết từng bước. AI tiết kiệm 80% thời gian setup, nhưng tư duy của QA Engineer mới là thứ quyết định liệu test có thực sự chất lượng. Đây chính là chiến lược Human-in-the-loop. Tiếp theo, mời Nam trình bày về Contract Testing với Pact."

---

## Checklist kỹ thuật trước khi quay

- [ ] Repo SUT đã được clone về máy, server chạy được ở `localhost:3000`
- [ ] Agent IDE (Cursor / VS Code + extension AI) đã mở tại thư mục repo
- [ ] File `api_specification.md` đã mở trong tab IDE
- [ ] File `prompt_AI.md` đã mở sẵn để copy-paste từng prompt
- [ ] Postman Desktop đã mở, workspace mới trống
- [ ] Tắt thông báo hệ thống trước khi quay để không bị gián đoạn