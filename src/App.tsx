import React, { useState, useEffect } from 'react';
import { Navigation } from './components/Navigation';
import { Dashboard } from './components/Dashboard';
import { StoryPlanner } from './components/StoryPlanner';
import { Wiki } from './components/Wiki';
import { AnnotationPanel } from './components/AnnotationPanel';
import { KanbanData } from './types';
import { exportStoryPlannerToMarkdown, downloadTextFile } from './utils/markdownSync';
import { theme } from './theme';

type Tab = 'timeline' | 'dashboard' | 'planner' | 'wiki' | 'annotations';

const initialData: KanbanData = {
  volumes: [
    {
      id: 'vol-1',
      title: 'Quyển 1: Khởi Nguồn',
      arcs: [
        {
          id: 'arc-1',
          title: 'Arc 1: Sơn Thôn Thiếu Niên',
          chapters: [
            { id: 'ch-1', number: 1, title: 'Bóng Đêm Thôn Trang', status: 'written', povs: ['Lâm Phong'], wordCount: 2000, summary: 'Lâm Phong chứng kiến thôn làng bị tàn sát.', characters: ['Lâm Phong', 'Cố Đức Thiên'] },
            { id: 'ch-2', number: 2, title: 'Kẻ Sống Sót Duy Nhất', status: 'in-progress', povs: ['Lâm Phong', 'Diệp Tĩnh Sương'], wordCount: 1500, summary: 'Cố Đức Thiên tìm thấy Lâm Phong và nhận làm đệ tử.', julesNotes: 'Cần mô tả chi tiết hơn biểu cảm của Cố Đức Thiên.' },
            { id: 'ch-3', number: 3, title: 'Bước Đầu Tu Luyện', status: 'planned', povs: ['Lâm Phong'], wordCount: 2200, summary: 'Lâm Phong bắt đầu tu luyện Thanh Mộc Trường Sinh Quyết.' }
          ]
        },
        {
           id: 'arc-2',
           title: 'Arc 2: Huyết Trì Thử Thách',
           chapters: [
                { id: 'ch-4', number: 4, title: 'Huyết Trì Hiện Thế', status: 'planned', povs: ['Lâm Phong', 'Lệ Vô Tâm'], wordCount: 2500, summary: 'Sự kiện mở ra Huyết Trì.' },
                { id: 'ch-5', number: 5, title: 'Sinh Tử Một Đường', status: 'planned', povs: ['Lâm Phong'], wordCount: 3000, summary: 'Trận chiến sinh tử trong Huyết Trì.' }
           ]
        }
      ]
    },
    {
      id: 'vol-2',
      title: 'Quyển 2: Vạn Độc Môn',
      arcs: [
          {
             id: 'arc-3',
             title: 'Arc 3: Tranh Đoạt Thánh Tử',
             chapters: [
                { id: 'ch-6', number: 6, title: 'Đối Mặt Quần Hùng', status: 'planned', povs: ['Lâm Phong', 'Diệp Tĩnh Sương', 'Lệ Vô Tâm'], wordCount: 2800, summary: 'Lâm Phong đối mặt với các cao thủ Vạn Độc Môn.' }
             ]
          }
      ]
    }
  ]
};

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<Tab>('planner');
  const [data, setData] = useState<KanbanData>(initialData);

  useEffect(() => {
    // Load data from localStorage if available
    const storedData = localStorage.getItem('co-nguyen-planner');
    if (storedData) {
      setData(JSON.parse(storedData));
    }
  }, []);

  const handleSync = async () => {
    try {
      const JSZip = (await import('jszip')).default;
      const zip = new JSZip();

      // Export planner
      zip.file('story-planner.md', exportStoryPlannerToMarkdown(data));

      // Load and export annotations
      const storedAnnotations = localStorage.getItem('co-nguyen-annotations');
      if (storedAnnotations) {
          const { exportAnnotationsToMarkdown } = await import('./utils/markdownSync');
          zip.file('annotations.md', exportAnnotationsToMarkdown(JSON.parse(storedAnnotations)));
      }

      // Load and export wiki
      const storedWiki = localStorage.getItem('co-nguyen-wiki');
      if (storedWiki) {
          const { exportWikiPageToMarkdown } = await import('./utils/markdownSync');
          const wikiPages: any[] = JSON.parse(storedWiki);
          const wikiFolder = zip.folder('wiki');
          if (wikiFolder) {
              wikiPages.forEach(page => {
                  wikiFolder.file(`${page.id}.md`, exportWikiPageToMarkdown(page));
              });
          }
      }

      const blob = await zip.generateAsync({ type: 'blob' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `jules-memory-sync-${new Date().toISOString().slice(0, 10)}.zip`;
      a.click();
      URL.revokeObjectURL(url);

      alert('📥 Đã export! Giải nén và commit đè các file này vào .Jules-Memory/ trong repo.');
    } catch (e) {
      console.error('Error syncing:', e);
      alert('Lỗi export data.');
    }
  };

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard':
        return <Dashboard data={data} />;
      case 'planner':
        return <StoryPlanner data={data} setData={setData} />;
      case 'wiki':
        return <Wiki />;
      case 'annotations':
        return <AnnotationPanel />;
      case 'timeline':
        return (
          <div style={{ padding: '32px', textAlign: 'center', color: theme.colors.text.muted, fontFamily: theme.fonts.body }}>
             <h2 style={{ color: theme.colors.gold.base, fontFamily: theme.fonts.display }}>Timeline View</h2>
             <p>Tính năng Timeline đang được nâng cấp theo giao diện dark theme.</p>
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: theme.colors.bg.primary,
      color: theme.colors.text.primary,
      fontFamily: theme.fonts.body,
      backgroundImage: theme.patterns.mainBg
    }}>
      <Navigation activeTab={activeTab} setActiveTab={setActiveTab} onSync={handleSync} />
      <main style={{ position: 'relative', zIndex: 1 }}>
        {renderContent()}
      </main>
    </div>
  );
};

export default App;
