import { KanbanData, WikiPage, Annotation } from '../types';

export function exportStoryPlannerToMarkdown(data: KanbanData): string {
    let md = `# CỐ NGUYÊN — STORY PLANNER\n`;
    md += `<!-- Jules Tổng Quản: đây là file plan do User tạo. Hãy đọc và cập nhật phần "jules_notes" trong từng task. -->\n`;
    md += `<!-- Last updated by User: ${new Date().toISOString()} -->\n\n`;

    let totalVolumes = data.volumes.length;
    let totalArcs = data.volumes.reduce((sum, v) => sum + v.arcs.length, 0);
    let totalChapters = data.volumes.reduce((sum, v) => sum + v.arcs.reduce((arcSum, a) => arcSum + a.chapters.length, 0), 0);

    md += `## META\n`;
    md += `- Total Volumes: ${totalVolumes}\n`;
    md += `- Total Arcs: ${totalArcs}\n`;
    md += `- Total Planned Chapters: ${totalChapters}\n\n`;

    md += `## KANBAN STATE\n\n`;

    const statuses = ['LÊN KẾ HOẠCH', 'ĐANG VIẾT', 'CẦN SỬA', 'HOÀN THÀNH'];
    const statusMap = {
        'LÊN KẾ HOẠCH': 'planned',
        'ĐANG VIẾT': 'in-progress',
        'CẦN SỬA': 'needs-revision', // You might need to add this status to types.ts if you want it
        'HOÀN THÀNH': 'written'
    };

    statuses.forEach(statusName => {
        md += `### ${statusName}\n`;
        const mappedStatus = statusMap[statusName as keyof typeof statusMap];

        data.volumes.forEach(volume => {
            volume.arcs.forEach(arc => {
                arc.chapters.filter(c => c.status === mappedStatus || (statusName === 'LÊN KẾ HOẠCH' && c.status === 'planned')).forEach(chapter => {
                    md += `#### [${chapter.id}] ${chapter.title}\n`;
                    md += `- **Arc:** ${arc.title}\n`;
                    md += `- **Volume:** ${volume.title}\n`;
                    md += `- **POVs:** ${chapter.povs?.join(', ') || 'None'}\n`;
                    md += `- **Characters:** ${chapter.characters?.join(', ') || 'None'}\n`;
                    md += `- **Target Words:** ${chapter.wordCount || 0}\n`;
                    md += `- **User Notes:** ${chapter.notes || ''}\n`;
                    md += `- **Jules Notes:** ${chapter.julesNotes || '_(chưa có)_'}\n`;
                    md += `- **Status:** ${chapter.status}\n\n`;
                });
            });
        });
    });

    md += `## JULES SYNC LOG\n`;
    md += `<!-- Jules Tổng Quản: ghi log các lần bạn update file này -->\n`;
    md += `- ${new Date().toISOString()}: _(Jules chưa sync)_\n`;

    return md;
}

export function parseJulesNotes(markdown: string): Record<string, string> {
    const notes: Record<string, string> = {};
    const lines = markdown.split('\n');
    let currentChapterId: string | null = null;

    for (const line of lines) {
        const titleMatch = line.match(/^#### \[(.*?)\]/);
        if (titleMatch) {
            currentChapterId = titleMatch[1];
        } else if (currentChapterId && line.startsWith('- **Jules Notes:** ')) {
            notes[currentChapterId] = line.replace('- **Jules Notes:** ', '').trim();
        }
    }
    return notes;
}

export function parseAnnotations(markdown: string): Annotation[] {
    const annotations: Annotation[] = [];
    const blocks = markdown.split('## [');

    for (let i = 1; i < blocks.length; i++) {
        const block = blocks[i];
        const lines = block.split('\n');

        const headerMatch = lines[0].match(/^(.*?)] (.*?) → (.*?)$/);
        if (headerMatch) {
            const timestamp = headerMatch[1];
            const authorStr = headerMatch[2].trim().toLowerCase();
            const author = authorStr === 'jules' ? 'jules' : 'user';

            let context = '';
            let contentLines: string[] = [];

            for (let j = 1; j < lines.length; j++) {
                const line = lines[j];
                if (line.startsWith('**Context:**')) {
                    context = line.replace('**Context:**', '').trim();
                } else if (!line.startsWith('---') && line.trim() !== '') {
                    contentLines.push(line);
                }
            }

            annotations.push({
                id: Math.random().toString(36).substr(2, 9),
                timestamp,
                author,
                context,
                content: contentLines.join('\n').trim()
            });
        }
    }
    return annotations;
}

export function exportWikiPageToMarkdown(page: WikiPage): string {
    let md = `---\n`;
    md += `id: ${page.id}\n`;
    md += `title: ${page.title}\n`;
    md += `category: ${page.category}\n`;
    md += `lastEdited: ${page.lastEdited || new Date().toISOString()}\n`;
    md += `lastEditedBy: ${page.lastEditedBy || 'user'}\n`;
    md += `---\n\n`;
    md += `${page.content}\n`;
    return md;
}

export function parseWikiPageMarkdown(markdown: string): WikiPage | null {
    const match = markdown.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
    if (!match) return null;

    const frontmatter = match[1];
    const content = match[2].trim();

    const page: Partial<WikiPage> = { content };

    frontmatter.split('\n').forEach(line => {
        const [key, ...valueParts] = line.split(':');
        if (key && valueParts.length > 0) {
            const value = valueParts.join(':').trim();
            if (key === 'id') page.id = value;
            if (key === 'title') page.title = value;
            if (key === 'category') page.category = value;
            if (key === 'lastEdited') page.lastEdited = value;
            if (key === 'lastEditedBy') page.lastEditedBy = value as 'user' | 'jules';
        }
    });

    if (page.id && page.title && page.category) {
        return page as WikiPage;
    }
    return null;
}

export function exportAnnotationsToMarkdown(annotations: Annotation[]): string {
    let md = `# CỐ NGUYÊN — ANNOTATION LOG\n`;
    md += `<!-- Jules Tổng Quản: ghi note và reply vào đây. User sẽ thấy trên trang Annotations. -->\n\n`;

    annotations.forEach(ann => {
        const authorName = ann.author === 'jules' ? 'Jules' : 'User';
        const recipientName = ann.author === 'jules' ? 'User' : 'Jules';
        md += `## [${ann.timestamp}] ${authorName} → ${recipientName}\n`;
        md += `**Context:** ${ann.context}\n`;
        md += `${ann.content}\n\n`;
        md += `---\n\n`;
    });

    return md;
}

export function downloadTextFile(filename: string, content: string): void {
    const blob = new Blob([content], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
}
