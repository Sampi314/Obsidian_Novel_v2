import os
import re

# Dictionary of direct replacements
REPLACEMENTS = {
    # .jules and .jules_memory related technical terms
    r'\bAgent\b': 'Đại Diện',
    r'\bSkill\b': 'Kỹ Năng',
    r'\bLevel\b': 'Cấp Độ',
    r'\bSystem\b': 'Hệ Thống',
    r'\bName\b': 'Tên Gọi',
    r'\bMemory\b': 'Ký Ức',
    r'\bBackground\b': 'Bối Cảnh',
    r'\bStory\b': 'Câu Truyện',
    r'\bCharacter\b': 'Nhân Vật',
    r'\bChapter\b': 'Chương',
    r'\bWorld\b': 'Thế Giới',
    r'\bBuilding\b': 'Kiến Trúc',
    r'\bTimeline\b': 'Dòng Thời Gian',
    r'\bAction\b': 'Hành Động',
    r'\bDirector\b': 'Đạo Diễn',
    r'\bQuality\b': 'Chất Lượng',
    r'\bControl\b': 'Kiểm Soát',
    r'\bReview\b': 'Đánh Giá',
    r'\bPlot\b': 'Cốt Truyện',
    r'\bHole\b': 'Lỗ Hổng',
    r'\bBug\b': 'Lỗi',
    r'\bProfile\b': 'Hồ Sơ',
    r'\bFile\b': 'Tệp Tin',
    r'\bFolder\b': 'Thư Mục',
    r'\bPath\b': 'Đường Dẫn',
    r'\bTitle\b': 'Tiêu Đề',
    r'\bHeading\b': 'Đề Mục',
    r'\bContent\b': 'Nội Dung',
    r'\bDescription\b': 'Mô Tả',
    r'\bRole\b': 'Vai Trò',
    r'\bTask\b': 'Nhiệm Vụ',
    r'\bProcess\b': 'Quy Trình',
    r'\bStructure\b': 'Cấu Trúc',
    r'\bFormat\b': 'Định Dạng',
    r'\bOutput\b': 'Kết Quả',
    r'\bNote\b': 'Lưu Ý',
    r'\bDetail\b': 'Chi Tiết',
    r'\bSummary\b': 'Tóm Tắt',
    r'\bReport\b': 'Báo Cáo',
    r'\bUpdate\b': 'Cập Nhật',
    r'\bCreate\b': 'Tạo Mới',
    r'\bEdit\b': 'Chỉnh Sửa',
    r'\bDelete\b': 'Xóa',
    r'\bAdd\b': 'Thêm',
    r'\bRemove\b': 'Gỡ Bỏ',
    r'\bFix\b': 'Sửa',
    r'\bCheck\b': 'Kiểm Tra',
    r'\bTest\b': 'Thử Nghiệm',
    r'\bStatus\b': 'Trạng Thái',
    r'\bAuthor\b': 'Tác Giả',
    r'\bType\b': 'Loại',
    r'\bLocation\b': 'Địa Điểm',
    r'\bDate\b': 'Ngày',
    r'\bTime\b': 'Thời Gian',
    r'\bState\b': 'Trạng Thái',
    r'\bUser\b': 'Người Dùng',
    r'\bOrchestrator\b': 'Người Điều Phối',
    r'\bPrompt\b': 'Chỉ Lệnh',

    # Also match lowercase/mixed cases using re.IGNORECASE dynamically
}

def replace_in_content(content):
    # Regex for translating generic English headers/terms outside of markdown links/code blocks
    # Avoid replacing inside paths like `Đạo/Chương_Truyện/...`

    # We first split the text into code blocks, links, and regular text
    parts = re.split(r'(```.*?```|`.*?`|\[.*?\]\(.*?\)|<.*?>)', content, flags=re.DOTALL)

    for i, part in enumerate(parts):
        # Even indexes are normal text, odd indexes are the matched exclusions
        if i % 2 == 0:
            for eng, vie in REPLACEMENTS.items():
                part = re.sub(eng, vie, part, flags=re.IGNORECASE)
            parts[i] = part

    return "".join(parts)

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = replace_in_content(content)

        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    dirs_to_check = ['.', '.jules', '.jules_memory', 'Đạo']
    modified_files = []

    for d in dirs_to_check:
        for root, _, files in os.walk(d):
            if '.git' in root or 'scripts' in root:
                continue
            for file in files:
                if file.endswith('.md'):
                    filepath = os.path.join(root, file)
                    if update_file(filepath):
                        modified_files.append(filepath)

    print(f"\nTotal files updated with term replacements: {len(modified_files)}")
    with open('Đạo/Báo_Cáo_Chất_Lượng.md', 'a', encoding='utf-8') as f:
        f.write("\n\n---")
        f.write("\n### [System] - Review Dịch Thuật Tiếng Anh")
        f.write(f"\n**Hành Động:** Đã thay thế tự động các từ khóa Tiếng Anh sang Tiếng Việt (Tiếng Trung) trong {len(modified_files)} tệp tin.\n")

if __name__ == '__main__':
    main()
