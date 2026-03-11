import os
import re

def update_jules_instructions():
    jules_dir = '.jules'
    if not os.path.exists(jules_dir):
        return

    rule_text = """
## QUY TẮC NGÔN NGỮ (BẮT BUỘC)
- **TUYỆT ĐỐI KHÔNG SỬ DỤNG TIẾNG ANH** trong nội dung được tạo ra (trừ tên file/đường dẫn kỹ thuật).
- Các tiêu đề, danh xưng phải dùng định dạng Tiếng Việt (Tiếng Trung), ví dụ: `Hồ Sơ Thế Giới (世界档案)`.
- Đối với Thơ Ca, Công Pháp, Lời Bài Hát, phải trình bày theo 3 phần:
  1. **Bản Tiếng Trung:** (Văn bản tiếng Trung)
  2. **Dịch Hán Việt:** (Phiên âm Hán Việt)
  3. **Dịch Sát Nghĩa:** (Bản dịch nghĩa Tiếng Việt)
- Các thuật ngữ chung phải được dịch sang Tiếng Việt hoặc Hán Việt tương ứng (VD: Agent -> Đại Diện / Sứ Giả, Skill -> Kỹ Năng / Pháp Thuật, Level -> Cấp Độ / Cảnh Giới).
"""

    for filename in os.listdir(jules_dir):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(jules_dir, filename)

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # If already added, skip
        if "TUYỆT ĐỐI KHÔNG SỬ DỤNG TIẾNG ANH" in content:
            continue

        # Add the new rule near the end, before final notes or at the end
        if "## LƯU Ý" in content:
            content = content.replace("## LƯU Ý", rule_text + "\n## LƯU Ý")
        else:
            content += "\n" + rule_text

        # Translate generic terms in the prompts (Agent, Memory, Skill, Level, etc.)
        content = content.replace("Agent", "Tổng Quản" if "INSTRUCTIONS" in filename else "Đại Diện")
        content = content.replace("Agent System", "Hệ Thống Đại Diện")
        content = content.replace("Orchestrator", "Người Điều Phối")
        content = content.replace("Timeline", "Dòng Thời Gian")
        content = content.replace("Quality Control", "Kiểm Soát Chất Lượng")
        content = content.replace("Review", "Đánh Giá")
        content = content.replace("bug", "lỗi")
        content = content.replace("Skill", "Kỹ Năng")
        content = content.replace("Memory", "Ký Ức")
        content = content.replace("Prompt", "Chỉ Lệnh")
        content = content.replace("Mermaid chart", "Biểu Đồ Tiên Sinh")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated instructions in: {filepath}")

if __name__ == '__main__':
    update_jules_instructions()
