import re
import os

# 1. Fill [AI-02] Audit Report
file2 = 'Group05_08/[AI-02] - FIT@HCMUS - AI Audit Report_Vn.docx.md'
with open(file2, 'r', encoding='utf-8') as f:
    c2 = f.read()

c2 = c2.replace('| **Họ tên sinh viên (in hoa):** |  |', '| **Họ tên sinh viên (in hoa):** | NHÓM 05 (Đại diện: PHẠM ĐỨC TOÀN) |')
c2 = c2.replace('| **MSSV:** |  |', '| **MSSV:** | 23127540 |')
c2 = c2.replace('| **Lớp / Khoá:** |  |', '| **Lớp / Khoá:** | K23 |')
c2 = c2.replace('| **Mã bài tập (ví dụ HW#00, HW#02):** |  |', '| **Mã bài tập (ví dụ HW#00, HW#02):** | T06_API_and_Contract_Testing |')
c2 = c2.replace('| **Ngày làm bài:** |  |', '| **Ngày làm bài:** | 2026-07-31 |')
c2 = c2.replace('| **Công cụ AI đã dùng:** |  |', '| **Công cụ AI đã dùng:** | Gemini 3.1 Pro, Gemini 3.5 Flash |')
c2 = c2.replace('| **Công cụ AI đã dùng:** | [ ] Có  [ ] Không |', '| **Có sử dụng AI không?:** | [x] Có  [ ] Không |')

artifacts = """| **Artifact #1** | **Tool: Gemini 3.1 Pro**<br>Prompt: Viết kịch bản thuyết trình demo Postman... | Kịch bản demo Postman cơ bản | INCOMPLETE | Thiếu timing chi tiết cho các thao tác click chuột. | Thêm timing chi tiết và hành động thực tế. |
| **Artifact #2** | **Tool: Gemini 3.1 Pro**<br>Prompt: Viết tài liệu tổng hợp nội dung... | Dàn ý 5 file tài liệu tổng hợp | VALID | Đúng cấu trúc tài liệu yêu cầu. | Giữ nguyên cấu trúc, chỉnh sửa một số nội dung. |
| **Artifact #3** | **Tool: Gemini 3.1 Pro**<br>Prompt: Tại sao JSON Schema gen ra gây lỗi... | Giải thích lỗi False Positive | VALID | Logic test đúng, thuật ngữ chuẩn xác. | Diễn đạt lại cho dễ hiểu hơn. |
| **Artifact #4** | **Tool: Gemini 3.5 Flash**<br>Prompt: Sườn tài liệu hướng dẫn CI/CD... | Các steps YAML cho Github Actions | INCOMPLETE | Chưa khớp hoàn toàn với cấu trúc thư mục project. | Cấu hình lại các path và branch trong YAML. |"""

c2 = re.sub(r'\| \*\*Artifact #1\*\*.*', artifacts, c2, flags=re.DOTALL)
# Cut off everything after Artifact #4 up to Section 4
c2 = re.sub(r'\| \*\*Artifact #5\*\*.*?## \*\*4', '## **4', c2, flags=re.DOTALL)

# Fill section 4
c2 = c2.replace('| **Tổng artifact AI sinh đã audit** |  |  |', '| **Tổng artifact AI sinh đã audit** | 4 | 100% |')
c2 = c2.replace('| **VALID (đúng, dùng nguyên)** |  | % |', '| **VALID (đúng, dùng nguyên)** | 2 | 50% |')
c2 = c2.replace('| **INVALID (sai; loại bỏ)** |  | % |', '| **INVALID (sai; loại bỏ)** | 0 | 0% |')
c2 = c2.replace('| **INCOMPLETE (chưa đủ; phải sửa/thêm)** |  | % |', '| **INCOMPLETE (chưa đủ; phải sửa/thêm)** | 2 | 50% |')

with open(file2, 'w', encoding='utf-8') as f:
    f.write(c2)

# 2. Fill [AI-03] Disclosure Form
file3 = 'Group05_08/[AI-03] - FIT@HCMUS - AI Disclosure Form_Vn.docx.md'
with open(file3, 'r', encoding='utf-8') as f:
    c3 = f.read()

c3 = c3.replace('| **Mã bài tập:** |  |', '| **Mã bài tập:** | T06_API_and_Contract_Testing |')
c3 = c3.replace('| **Tên bài tập:** |  |', '| **Tên bài tập:** | Seminar - API & Contract Testing |')
c3 = c3.replace('| **Cấp độ AI (1–5):** | Cấp ____ |', '| **Cấp độ AI (1–5):** | Cấp 3 |')
c3 = c3.replace('| **Ngày:** |  |', '| **Ngày:** | 2026-07-31 |')
c3 = c3.replace('| **Họ tên sinh viên:** |  |', '| **Họ tên sinh viên:** | NHÓM 05 (Đại diện: Phạm Đức Toàn) |')
c3 = c3.replace('| **MSSV:** |  |', '| **MSSV:** | 23127540 |')

c3 = re.sub(r'\*Liệt kê mọi công cụ AI dùng cho bài tập này.*?\n\n_{10,}', '*Liệt kê mọi công cụ AI dùng cho bài tập này:*\n\nGemini 3.1 Pro, Gemini 3.5 Flash', c3, count=1, flags=re.DOTALL)
c3 = re.sub(r'_{10,}', '', c3)

c3 = c3.replace('Tick tất cả: [ ] brainstorm  [ ] outline  [ ] viết nháp  [ ] phản hồi  [ ] sửa chữa  [ ] code  [ ] phân tích dữ liệu  [ ] thiết kế đồ hoạ  [ ] khác (ghi rõ).*', 
                'Tick tất cả: [x] brainstorm  [x] outline  [x] viết nháp  [ ] phản hồi  [x] sửa chữa  [x] code  [x] phân tích dữ liệu  [ ] thiết kế đồ hoạ  [ ] khác (ghi rõ).*')

c3 = c3.replace('### **3\\. Prompt / nhiệm vụ chính cho AI:**\n\n*Dán nguyên văn 2–3 prompt quan trọng nhất. Để xem đầy đủ, đính kèm Phụ lục A (prompt_log.md).*\n\n\n\n\n\n\n\n', 
                '### **3\\. Prompt / nhiệm vụ chính cho AI:**\n\n1. "Viết giúp tôi kịch bản thuyết trình chi tiết (kèm hành động chuột)..."\n2. "Tại sao đoạn script JSON Schema do AI gen có \'properties\': {} lại gây ra lỗi False Positive..."\n3. "Viết sườn tài liệu hướng dẫn sử dụng và vận hành CI/CD GitHub Actions chạy Newman và Pact."\n\n')

c3 = c3.replace('### **4\\. Phần cụ thể AI đóng góp:**\n\n*Mô tả chi tiết những gì AI tạo ra mà bạn đã giữ lại trong bài nộp cuối (ví dụ: đoạn code nào, đoạn văn nào, hình ảnh nào).*',
                '### **4\\. Phần cụ thể AI đóng góp:**\n\nAI đã đóng góp vào việc tạo dàn ý cho các tài liệu Hướng dẫn sử dụng (User Guide), kịch bản Demo Postman, và cấu trúc cơ bản của file CI/CD YAML. Toàn bộ nội dung logic, giải pháp kĩ thuật chi tiết và tích hợp đều do sinh viên tự hoàn thiện.\n\n')

# cleanup extra newlines
c3 = re.sub(r'\n{3,}', '\n\n', c3)

with open(file3, 'w', encoding='utf-8') as f:
    f.write(c3)

# 3. Fill [AI-04] Reflective Statement
file4 = 'Group05_08/[AI-04] - FIT@HCMUS - AI Reflective Statement_Vn.docx.md'
with open(file4, 'r', encoding='utf-8') as f:
    c4 = f.read()

c4 = c4.replace('| **Tên Project / Đồ án:** |  |', '| **Tên Project / Đồ án:** | Seminar - API & Contract Testing |')
c4 = c4.replace('| **Thành viên nhóm (nếu là nhóm):** |  |', '| **Thành viên nhóm (nếu là nhóm):** | Toàn, Nam, Khoa, Luân |')
c4 = c4.replace('| **Họ tên sinh viên:** |  |', '| **Họ tên sinh viên:** | NHÓM 05 (Đại diện: Phạm Đức Toàn) |')
c4 = c4.replace('| **MSSV:** |  |', '| **MSSV:** | 23127540 |')
c4 = c4.replace('| **Ngày nộp:** |  |', '| **Ngày nộp:** | 2026-07-31 |')

# Remove blank lines _____
c4 = re.sub(r'_{10,}', '', c4)

c4 = c4.replace('### **1\\. AI đã hỗ trợ công việc của bạn như thế nào?**\n\n*Mô tả cụ thể AI đóng góp ở đâu trong project: thiết kế test, brainstorm scenario, sinh code, phân tích log, triage defect, viết tài liệu, chuẩn bị slide, v.v.*\n\n\n\n\n\n\n\n\n\n',
                '### **1\\. AI đã hỗ trợ công việc của bạn như thế nào?**\n\nAI hỗ trợ mạnh mẽ nhất trong việc brainstorm kịch bản thuyết trình, phân tích và giải thích cặn kẽ các cơ chế lỗi sâu của JSON Schema, cũng như cung cấp bộ khung (outline) cho các tài liệu kĩ thuật phức tạp như CI/CD và Contract Testing. Điều này giúp nhóm tiết kiệm đáng kể thời gian trong khâu định hình cấu trúc và format văn bản.\n\n')

c4 = c4.replace('### **2\\. Bạn chấp nhận / từ chối / sửa gì từ đầu ra AI?**\n\n*Liệt kê đề xuất AI bạn dùng, đề xuất bạn loại bỏ, và cách bạn điều chỉnh cho phù hợp với spec, nguyên tắc ISTQB, hoặc phân tích của bạn.*\n\n\n\n\n\n\n\n\n\n\n\n',
                '### **2\\. Bạn chấp nhận / từ chối / sửa gì từ đầu ra AI?**\n\nChúng tôi chấp nhận các khung dàn ý tài liệu và cách giải thích thuật ngữ lỗi của AI. Tuy nhiên, chúng tôi từ chối các đoạn mã cấu hình CI/CD có sẵn vì chúng không tương thích với cấu trúc thư mục thực tế của EShop. Chúng tôi đã cấu hình lại YAML và kiểm thử độc lập các Edge Cases theo tiêu chuẩn ISTQB.\n\n')

c4 = c4.replace('### **3\\. Bạn nhận ra lỗi / bias / giới hạn nào trong đầu ra AI?**\n\n*Ví dụ cụ thể: AI bịa hàm, sai boundary, miss security case, hiểu sai metric (p95 vs top 5%), bịa trích dẫn, v.v.*\n\n\n\n\n\n\n\n\n\n\n\n',
                '### **3\\. Bạn nhận ra lỗi / bias / giới hạn nào trong đầu ra AI?**\n\nNhóm nhận thấy AI thường bịa ra các thư viện không tồn tại hoặc các thuộc tính không có thực trong API Spec (ảo giác). Ngoài ra, khi viết script test, AI có xu hướng chỉ cover các trường hợp Happy Path và bỏ qua hoàn toàn việc xác thực lỗi Business Logic (ví dụ: giỏ hàng trống, lạm dụng mã giảm giá).\n\n')

c4 = c4.replace('### **4\\. Kỹ năng nào của BẠN được cải thiện khi dùng AI?**\n\n*Ví dụ: "Tôi học được cách viết prompt rõ ràng hơn để tránh việc AI sinh test case vô lý," hoặc "Tôi phải ôn lại FL để biết AI đang bắt sai equivalence class."*\n\n\n\n\n\n\n\n\n\n\n\n',
                '### **4\\. Kỹ năng nào của BẠN được cải thiện khi dùng AI?**\n\nChúng tôi học được cách viết prompt để ép buộc AI tuân thủ đúng định dạng JSON thay vì sinh code tùy tiện, đồng thời kỹ năng Review Code/Log cũng được nâng cao vì phải luôn giữ tinh thần hoài nghi với mọi output mà AI tạo ra.\n\n')

c4 = c4.replace('### **5\\. Nếu làm lại không có AI, bạn sẽ thay đổi cách làm thế nào?**\n\n*Bài học rút ra về cân bằng giữa tự động hoá (AI) và chuyên môn kỹ thuật phần mềm (bạn).*\n\n\n\n\n\n\n\n\n\n\n\n',
                '### **5\\. Nếu làm lại không có AI, bạn sẽ thay đổi cách làm thế nào?**\n\nNếu không có AI, nhóm sẽ tốn nhiều thời gian hơn cho việc định dạng tài liệu và tìm kiếm trên Google/StackOverflow các keyword lỗi. Dù vậy, phần lõi kiến thức về kiểm thử vẫn luôn phải do con người kiểm soát. Bài học lớn nhất là AI chỉ là công cụ gia tốc (accelerator), không thể thay thế năng lực tư duy Test Design của kĩ sư QA.\n\n')

# cleanup
c4 = re.sub(r'\n{3,}', '\n\n', c4)

with open(file4, 'w', encoding='utf-8') as f:
    f.write(c4)

print("Filled all forms.")
