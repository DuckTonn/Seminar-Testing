# Báo cáo so sánh kiểm thử tự động: AI vs Manual

Dưới đây là bảng đánh giá so sánh hiệu quả giữa bộ API test Postman do AI tự động sinh và bộ test do kĩ sư trực tiếp phân tích, thiết kế cho hệ thống EShop.

## Bảng So Sánh Chi Tiết

| Tiêu chí so sánh | Khả năng của AI | Kỹ sư trực tiếp |
| :--- | :--- | :--- |
| **Tốc độ khởi tạo (Boilerplate)** | **< 1 phút**. Tự động parse URL, Header, Body và cấu trúc JSON chuẩn xác ngay lập tức. | **Hàng giờ.** Tốn nhiều thời gian gõ phím, cấu hình môi trường, thiết lập biến thủ công. |
| **Độ bao phủ Edge/Negative Case** | **Thấp.** AI có thiên kiến "Happy-path", mặc định giả định người dùng nhập đúng chuẩn. | **Cao.** Dựa vào tư duy phản biện để tìm Boundary values, Type mismatch, và Security risks. |
| **Kiểm tra trạng thái (Statefulness)** | **Nông.** Thường đánh giá độc lập từng request (VD: Gửi Checkout thấy 200 là pass). | **Sâu.** Test Chaining: Thêm Cart -> Checkout -> Lấy OrderID gọi Get Detail để xác nhận DB đã ghi đúng trạng thái. |
| **Xử lý Dynamic Data (Dữ liệu động)**| **Yếu.** Có xu hướng hardcode dữ liệu (`id: 1`, email tĩnh), gây lỗi Conflict khi chạy lặp lại trên CI/CD Pipeline. | **Hiệu quả.** Biết vận dụng Pre-request scripts để sinh dữ liệu ngẫu nhiên (UUID, Timestamp) phục vụ Automation Test dài hạn. |
| **Độ chính xác của Schema Validation** | **Kém.** Thường gen schema dạng `type: "object", properties: {}` dẫn đến Pass giả (False Positive). | **Tốt.** Định nghĩa rõ ràng kiểu dữ liệu, các trường bắt buộc và cấm data rác (`additionalProperties: false`). |

## Kết Luận & Chiến Lược Tích Hợp

Dựa trên quá trình đánh giá thực tiễn, nhóm rút ra kết luận:

1. **AI không phải là "Test Designer":** AI thiếu ngữ cảnh hệ thống để tự động nhận diện các lỗ hổng logic nghiệp vụ, phân quyền hay vòng đời dữ liệu.
2. **AI là "Code Generator" tốt:** AI loại bỏ hoàn toàn các tác vụ nhàm chán như thiết lập API skeleton, viết các đoạn script parse JSON hay lấy biến cơ bản.
3. **Chiến lược áp dụng tối ưu (Human-in-the-loop):** 
   - Kỹ sư viết Spec thật chuẩn.
   - Dùng AI sinh bộ Postman Collection khung (Boilerplate) giúp tiết kiệm 70% thời gian setup.
   - Kỹ sư đóng vai trò **Reviewer**, trực tiếp viết bổ sung các Request Chaining (liên kết chuỗi API), Dynamic Data, Schema validation chặt chẽ và Security tests để đưa vào Pipeline chạy qua Newman.
