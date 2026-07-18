# Kịch bản Demo Contract Testing (Thời lượng: 3-5 phút)

Kịch bản này hướng dẫn chi tiết các bước để demo quá trình thực hiện Contract Testing bằng Pact cho nhóm trong buổi seminar.

## 1. Giới thiệu nhanh (30 giây)
**Presenter (Nam):**
> "Chào mọi người. Hôm nay mình sẽ demo về Consumer-Driven Contract Testing sử dụng Pact. Ý tưởng cốt lõi là: Consumer (Frontend) sẽ định nghĩa ra những gì họ mong đợi (contract) từ Provider (Backend). Sau đó, chúng ta sẽ lấy contract này để verify xem Backend có thực sự đáp ứng đúng hay không, giúp phát hiện lỗi tích hợp từ sớm mà không cần chạy toàn bộ hệ thống (end-to-end)."

## 2. Chạy Consumer Test để tạo Pact Contract (1 phút)
**Presenter (Nam):**
> "Bước đầu tiên, chúng ta đang ở vị trí của Consumer (Frontend). Mình có một bài test định nghĩa rằng khi gọi `POST /api/cart`, mình mong đợi Backend trả về status `201` cùng với `productId` và `quantity`."

**Thao tác thực hành:**
1. Mở terminal, trỏ vào thư mục `contract_testing/`.
2. Chạy lệnh: `npm run test:pact`
3. Chỉ ra cho mọi người thấy test pass.
4. Mở file `pacts/EshopConsumer-EShopBackend.json` và giải thích nhanh cấu trúc của nó (bao gồm request, response, status).

**Presenter (Nam):**
> "Khi test này pass, Pact tự động sinh ra một file JSON được gọi là Contract. File này đóng vai trò như một bản hợp đồng cam kết giữa 2 bên."

## 3. Chạy Provider Verification - Verification Pass (1.5 phút)
*(Lưu ý chuẩn bị: Trước buổi demo, code backend trong `server.js` cần tạm thời được sửa để trả về status `201` và `{ productId, quantity }` nhằm mô phỏng trạng thái 'Hoàn hảo' ban đầu của hệ thống).*

**Presenter (Nam):**
> "Tiếp theo, chúng ta đứng ở vị trí Backend (Provider). Mình sẽ chạy server thực tế lên và xác thực xem Backend của mình có vi phạm bản hợp đồng JSON kia không."

**Thao tác thực hành:**
1. Đảm bảo server đang chạy (`node backend/server.js`).
2. Mở một terminal mới, chạy lệnh: `npm run test:provider`.
3. Chỉ cho mọi người xem log báo thành công: `Pact Verification Complete!`

**Presenter (Nam):**
> "Như các bạn thấy, verification pass. Điều này chứng tỏ backend của chúng ta hiện tại đang cung cấp chính xác những gì consumer cần."

## 4. Mô phỏng Breaking Change ở Backend (1 phút)
**Presenter (Nam):**
> "Bây giờ, giả sử một dev Backend vô tình sửa code. Thay vì trả về `201` và thông tin sản phẩm, họ lại trả về `200` và một câu message đơn giản là 'Added to cart'. Thay đổi này trông có vẻ vô hại nhưng sẽ làm sập Frontend."

**Thao tác thực hành:**
1. Mở file `backend/server.js`.
2. Tìm đến endpoint `POST /api/cart`.
3. Sửa `res.status(201).json({ productId: req.body.productId, quantity: req.body.quantity })` thành `res.status(200).json({ message: "Added to cart" })`.
4. Khởi động lại server.
5. Chạy lại lệnh: `npm run test:provider`.
6. Chỉ vào thông báo lỗi trên màn hình.

**Presenter (Nam):**
> "Như mọi người thấy, Provider Verification lập tức thất bại. Pact báo lỗi rõ ràng: Nó kỳ vọng status 201 nhưng nhận 200, và kỳ vọng body có `productId` nhưng thực tế bị thiếu. Nhờ Pact, chúng ta chặn được lỗi này ngay trong lúc chạy Unit/Integration Test trên máy của Backend dev hoặc trên CI/CD, trước khi code được deploy."

## 5. Kết luận (30 giây)
**Presenter (Nam):**
> "Đó là sức mạnh của Contract Testing: giúp cả 2 team Frontend và Backend giao tiếp qua 'hợp đồng', biết ngay khi có thay đổi phá vỡ hệ thống mà không cần tốn nhiều nguồn lực setup môi trường E2E."
