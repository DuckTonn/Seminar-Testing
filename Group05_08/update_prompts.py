import re

file2 = 'Group05_08/[AI-02] - FIT@HCMUS - AI Audit Report_Vn.docx.md'
with open(file2, 'r', encoding='utf-8') as f:
    c2 = f.read()

artifacts = """| **Artifact #1** | **Tool: Gemini 3.1 Pro**<br>Prompt: "Viết giúp tôi kịch bản thuyết trình chi tiết khoảng 2 phút để demo tính năng lưu Token tự động và chạy Collection Runner của Postman. Ngoài ra, hãy phân tích 3 điểm mù (Failure modes) thường gặp nhất khi dùng Postman test API để tôi đưa vào tài liệu User Guide." | Khung sườn kịch bản demo Postman | INCOMPLETE | Thiếu timing chi tiết cho các thao tác click chuột. | Thêm timing chi tiết và hành động thực tế. |
| **Artifact #2** | **Tool: Gemini 3.1 Pro (High)**<br>Prompt: "Bạn là một Technical Writer và chuyên gia Software Testing. Tôi đang ở Tuần 3 của dự án nhóm về 'API & Contract Testing' và cần hoàn thành các tài liệu tổng hợp cuối cùng..." | Dàn ý 5 file tài liệu tổng hợp | VALID | Đúng cấu trúc tài liệu yêu cầu. | Giữ nguyên cấu trúc, chỉnh sửa một số nội dung. |
| **Artifact #3** | **Tool: Gemini 3.1 Pro**<br>Prompt: "Tôi đang tự viết báo cáo phân tích Failure Modes của AI khi test hệ thống EShop. Mày hãy giải thích ngắn gọn (dùng chuẩn thuật ngữ QA/Testing) tại sao đoạn script JSON Schema do AI gen có 'properties': {} và 'additionalProperties': true lại gây ra lỗi False Positive cực kỳ nghiêm trọng ở API Checkout?" | Giải thích lỗi False Positive của JSON Schema | VALID | Logic test đúng, thuật ngữ chuẩn xác. | Diễn đạt lại cho dễ hiểu hơn. |
| **Artifact #4** | **Tool: Gemini 3.5 Flash**<br>Prompt: "Viết sườn tài liệu hướng dẫn sử dụng và vận hành CI/CD GitHub Actions chạy Newman và Pact." | Các steps YAML cho Github Actions | INCOMPLETE | Chưa khớp hoàn toàn với cấu trúc thư mục project. | Cấu hình lại các path và branch trong YAML. |
"""

c2 = re.sub(r'\| \*\*Artifact #1\*\*.*?(?=## \*\*4)', artifacts + '\n', c2, flags=re.DOTALL)

with open(file2, 'w', encoding='utf-8') as f:
    f.write(c2)

file3 = 'Group05_08/[AI-03] - FIT@HCMUS - AI Disclosure Form_Vn.docx.md'
with open(file3, 'r', encoding='utf-8') as f:
    c3 = f.read()

c3 = re.sub(r'### \*\*3\\. Prompt / nhiệm vụ chính cho AI:\*\*.*?(?=### \*\*4)', 
            '### **3\\. Prompt / nhiệm vụ chính cho AI:**\n\n1. "Viết giúp tôi kịch bản thuyết trình chi tiết khoảng 2 phút để demo tính năng lưu Token tự động và chạy Collection Runner của Postman..."\n2. "Tôi đang tự viết báo cáo phân tích Failure Modes của AI khi test hệ thống EShop. Mày hãy giải thích ngắn gọn tại sao đoạn script JSON Schema do AI gen có \'properties\': {} lại gây ra lỗi False Positive..."\n3. "Bạn là một Technical Writer và chuyên gia Software Testing. Tôi đang ở Tuần 3 của dự án nhóm về \'API & Contract Testing\'..."\n\n', 
            c3, flags=re.DOTALL)

with open(file3, 'w', encoding='utf-8') as f:
    f.write(c3)

print("Updated prompts successfully.")
