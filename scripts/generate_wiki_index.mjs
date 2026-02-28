import fs from 'fs';
import path from 'path';

const DAO_DIR = path.join(process.cwd(), 'Đạo');
const OUTPUT_FILE = path.join(process.cwd(), 'public', 'wiki-index.json');

// Folders to include as categories
const CATEGORIES = [
    'Nhân_Vật',
    'Thế_Giới_Và_Thời_Gian',
    'Tu_Luyện',
    'Thế_Lực',
    'Kỳ_Vật',
    'Chủng_Tộc',
    'Công_Pháp',
    'Đan_Dược',
    'Trận_Pháp',
    'Phù_Lục',
    'Luyện_Khí'
];

function generateIndex() {
    const wikiFiles = [];

    // Also include root markdown files if needed, e.g., HỒ_SƠ_THẾ_GIỚI.md
    if (fs.existsSync(path.join(DAO_DIR, 'HỒ_SƠ_THẾ_GIỚI.md'))) {
        wikiFiles.push({
            id: 'ho-so-the-gioi',
            title: 'Hồ Sơ Thế Giới',
            category: 'Tổng Quan',
            path: '/Đạo/HỒ_SƠ_THẾ_GIỚI.md'
        });
    }

    CATEGORIES.forEach(category => {
        const catPath = path.join(DAO_DIR, category);
        if (fs.existsSync(catPath) && fs.statSync(catPath).isDirectory()) {
            const files = fs.readdirSync(catPath);
            files.forEach(file => {
                if (file.endsWith('.md')) {
                    const title = file.replace('.md', '').replace(/_/g, ' ');
                    wikiFiles.push({
                        id: `${category.toLowerCase()}-${file.replace('.md', '').toLowerCase()}`,
                        title: title,
                        category: category.replace(/_/g, ' '),
                        path: `/Đạo/${category}/${file}`
                    });
                }
            });
        }
    });

    fs.writeFileSync(OUTPUT_FILE, JSON.stringify(wikiFiles, null, 2));
    console.log(`Successfully generated wiki index at ${OUTPUT_FILE} with ${wikiFiles.length} files.`);
}

generateIndex();
