import React, { useState, useEffect } from 'react';
import { WikiPage } from '../types';
import { theme } from '../theme';
import { WikiPageView } from './WikiPage';
import { BookOpen, Plus, Search, Folder } from 'lucide-react';

export const Wiki: React.FC = () => {
  const [pages, setPages] = useState<WikiPage[]>([]);
  const [selectedPageId, setSelectedPageId] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    const loadWikiData = async () => {
      try {
        const response = await fetch('./wiki-index.json');
        if (!response.ok) throw new Error('Failed to load wiki index');
        const data = await response.json();

        // Convert loaded json index to WikiPage format, with empty initial content.
        // We'll load content dynamically when a user selects a page, or we could leave it to the WikiPage component.
        const basePages: WikiPage[] = data.map((item: any) => ({
            id: item.id,
            title: item.title,
            category: item.category,
            content: '', // Let WikiPageView fetch this if it's empty but has a path
            path: item.path,
            lastEditedBy: 'jules'
        }));

        // Now merge with local storage customizations
        const storedWiki = localStorage.getItem('co-nguyen-wiki');
        if (storedWiki) {
            const localPages: WikiPage[] = JSON.parse(storedWiki);

            // Overwrite base pages with local modifications, and append new local pages
            const mergedPages = [...basePages];
            localPages.forEach(localPage => {
                const index = mergedPages.findIndex(p => p.id === localPage.id);
                if (index !== -1) {
                    // Update content and lastEditedBy
                    mergedPages[index] = { ...mergedPages[index], content: localPage.content, lastEditedBy: localPage.lastEditedBy || 'user' };
                } else {
                    mergedPages.push(localPage);
                }
            });
            setPages(mergedPages);
            if (mergedPages.length > 0) setSelectedPageId(mergedPages[0].id);
        } else {
            setPages(basePages);
            if (basePages.length > 0) setSelectedPageId(basePages[0].id);
        }
      } catch (e) {
         console.error("Wiki Index Error:", e);
         // Fallback to purely local
         const storedWiki = localStorage.getItem('co-nguyen-wiki');
         if (storedWiki) {
            const parsedPages = JSON.parse(storedWiki);
            setPages(parsedPages);
            if (parsedPages.length > 0) setSelectedPageId(parsedPages[0].id);
         }
      }
    };

    loadWikiData();
  }, []);

  const handleSavePage = (updatedPage: WikiPage) => {
    const newPages = pages.map(p => p.id === updatedPage.id ? updatedPage : p);
    setPages(newPages);
    localStorage.setItem('co-nguyen-wiki', JSON.stringify(newPages));
  };

  const filteredPages = pages.filter(p => p.title.toLowerCase().includes(searchQuery.toLowerCase()));
  const categories = Array.from(new Set(pages.map(p => p.category)));

  return (
    <div style={{ display: 'flex', height: 'calc(100vh - 64px)' }}>
      {/* Sidebar */}
      <div style={{
        width: '300px',
        backgroundColor: theme.colors.bg.secondary,
        borderRight: `1px solid ${theme.colors.border.subtle}`,
        display: 'flex',
        flexDirection: 'column',
        height: '100%',
      }}>
        <div style={{ padding: '24px', borderBottom: `1px solid ${theme.colors.border.subtle}` }}>
          <h2 style={{ fontFamily: theme.fonts.display, color: theme.colors.gold.base, margin: '0 0 16px 0', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <BookOpen size={20} /> Wiki
          </h2>
          <div style={{ position: 'relative' }}>
            <Search size={16} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: theme.colors.text.muted }} />
            <input
              type="text"
              placeholder="Tìm kiếm wiki..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              style={{
                width: '100%', padding: '8px 12px 8px 36px', backgroundColor: theme.colors.bg.card,
                border: `1px solid ${theme.colors.border.normal}`, borderRadius: '4px',
                color: theme.colors.text.primary, fontFamily: theme.fonts.body, boxSizing: 'border-box'
              }}
            />
          </div>
        </div>

        <div style={{ flex: 1, overflowY: 'auto', padding: '16px' }}>
          {categories.map(category => (
            <div key={category} style={{ marginBottom: '24px' }}>
              <div style={{
                fontSize: '12px', fontWeight: 'bold', color: theme.colors.text.muted,
                textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '8px',
                display: 'flex', alignItems: 'center', gap: '8px'
              }}>
                <Folder size={12} /> {category}
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                {filteredPages.filter(p => p.category === category).map(page => (
                  <button
                    key={page.id}
                    onClick={() => setSelectedPageId(page.id)}
                    style={{
                      textAlign: 'left', padding: '8px 12px', backgroundColor: selectedPageId === page.id ? theme.colors.gold.glow : 'transparent',
                      border: 'none', borderRadius: '4px', color: selectedPageId === page.id ? theme.colors.gold.light : theme.colors.text.primary,
                      cursor: 'pointer', fontFamily: theme.fonts.body, fontSize: '14px', transition: 'all 0.2s',
                      display: 'flex', justifyContent: 'space-between', alignItems: 'center'
                    }}
                  >
                    <span>{page.title}</span>
                    {page.lastEditedBy === 'jules' && <span style={{ color: theme.colors.jade.base, fontSize: '12px' }}>🐉</span>}
                  </button>
                ))}
              </div>
            </div>
          ))}
        </div>

        <div style={{ padding: '16px', borderTop: `1px solid ${theme.colors.border.subtle}` }}>
          <button style={{
            width: '100%', padding: '10px', backgroundColor: theme.colors.gold.dark,
            color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer',
            display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px', fontWeight: 'bold'
          }}>
            <Plus size={16} /> Tạo Trang Mới
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div style={{ flex: 1, backgroundColor: theme.colors.bg.primary, display: 'flex', flexDirection: 'column' }}>
        {selectedPageId ? (
          <WikiPageView
            page={pages.find(p => p.id === selectedPageId)!}
            onSave={handleSavePage}
            onClose={() => setSelectedPageId(null)}
          />
        ) : (
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%', color: theme.colors.text.muted }}>
            Chọn một trang wiki để xem
          </div>
        )}
      </div>
    </div>
  );
};
