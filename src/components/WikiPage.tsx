import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { WikiPage } from '../types';
import { theme } from '../theme';
import { Edit2, Save, X, Image as ImageIcon } from 'lucide-react';

interface WikiPageProps {
  page: WikiPage;
  onSave: (page: WikiPage) => void;
  onClose: () => void;
}

export const WikiPageView: React.FC<WikiPageProps> = ({ page, onSave, onClose }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editedContent, setEditedContent] = useState(page.content);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const loadContent = async () => {
        if (!page.content && page.path) {
            setIsLoading(true);
            try {
                // Determine base path from process/env if necessary, but here we assume we are running from root /
                // Because Vite serves from public folder, /Đạo/... won't be available unless we copy it.
                // Alternatively, if this app is deployed as a subpath, we should fetch relative to it.
                // Wait, if we use GitHub Pages, it's relative. Let's try fetching the path directly.
                // The index has paths like "/Đạo/...". Since public/ is the root in Vite, we'd need Đạo copied to public.
                // Actually, wait, when we run locally `Đạo` is NOT in public.
                // We will write a step in build to copy `Đạo` to `dist/Đạo`.
                // In dev, we can set up vite to serve `Đạo`.

                // Remove leading slash to make it relative to root
                // Vite subpath base means we should fetch from relative path
                const base = import.meta.env.BASE_URL; // e.g., /Obsidian_Novel_v2/
                const cleanPath = page.path.startsWith('/') ? page.path.substring(1) : page.path;
                // Important: Ensure URI encoding for paths with unicode/spaces like /Đạo/Nhân_Vật/...
                const encodedPath = cleanPath.split('/').map(segment => encodeURIComponent(segment)).join('/');
                const response = await fetch(`${base}${encodedPath}`);
                if (response.ok) {
                    const text = await response.text();
                    setEditedContent(text);
                    // Also update the parent so it caches it
                    onSave({ ...page, content: text });
                } else {
                    setEditedContent("# Content not found\n\nCould not load content from " + page.path);
                }
            } catch (error) {
                console.error("Error fetching markdown:", error);
                setEditedContent("# Error\n\nFailed to fetch content.");
            } finally {
                setIsLoading(false);
            }
        } else {
            setEditedContent(page.content);
        }
    };

    loadContent();
    setIsEditing(false);
  }, [page]);

  const handleSave = () => {
    onSave({ ...page, content: editedContent, lastEdited: new Date().toISOString(), lastEditedBy: 'user' });
    setIsEditing(false);
  };

  const handleImagePaste = (e: React.ClipboardEvent<HTMLTextAreaElement>) => {
    const items = e.clipboardData.items;
    for (let i = 0; i < items.length; i++) {
      if (items[i].type.indexOf('image') !== -1) {
        e.preventDefault();
        const file = items[i].getAsFile();
        if (file) {
          const reader = new FileReader();
          reader.onload = (event) => {
            const base64 = event.target?.result as string;
            setEditedContent(prev => `${prev}\n![image](${base64})\n`);
          };
          reader.readAsDataURL(file);
        }
      }
    }
  };

  return (
    <div style={{ padding: '32px', maxWidth: '800px', margin: '0 auto', flex: 1, overflowY: 'auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px', borderBottom: `1px solid ${theme.colors.border.subtle}`, paddingBottom: '16px' }}>
        <div>
          <h1 style={{ fontFamily: theme.fonts.display, color: theme.colors.gold.base, margin: '0 0 8px 0' }}>{page.title}</h1>
          <div style={{ display: 'flex', gap: '12px', fontSize: '12px', color: theme.colors.text.muted }}>
            <span>Category: {page.category}</span>
            {page.lastEditedBy === 'jules' && (
              <span style={{ color: theme.colors.jade.light, display: 'flex', alignItems: 'center', gap: '4px' }}>
                 🐉 Jules updated
              </span>
            )}
          </div>
        </div>

        <div style={{ display: 'flex', gap: '8px' }}>
          {isEditing ? (
            <>
              <button onClick={handleSave} style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '8px 16px', backgroundColor: theme.colors.jade.base, color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
                <Save size={16} /> Lưu
              </button>
              <button onClick={() => setIsEditing(false)} style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '8px 16px', backgroundColor: 'transparent', color: theme.colors.text.secondary, border: `1px solid ${theme.colors.border.normal}`, borderRadius: '4px', cursor: 'pointer' }}>
                <X size={16} /> Hủy
              </button>
            </>
          ) : (
            <button onClick={() => setIsEditing(true)} style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '8px 16px', backgroundColor: theme.colors.bg.secondary, color: theme.colors.gold.base, border: `1px solid ${theme.colors.border.bright}`, borderRadius: '4px', cursor: 'pointer' }}>
              <Edit2 size={16} /> Edit
            </button>
          )}
        </div>
      </div>

      {isLoading ? (
        <div style={{ color: theme.colors.gold.base, fontStyle: 'italic', padding: '24px' }}>Đang tải nội dung...</div>
      ) : isEditing ? (
        <div style={{ position: 'relative' }}>
             <div style={{
                position: 'absolute', top: '-40px', right: 0,
                display: 'flex', gap: '8px',
                color: theme.colors.text.muted, fontSize: '12px',
                backgroundColor: theme.colors.bg.card,
                padding: '4px 8px', borderRadius: '4px',
                border: `1px solid ${theme.colors.border.subtle}`
             }}>
                 <ImageIcon size={14} /> Paste image to upload
             </div>
            <textarea
            value={editedContent}
            onChange={(e) => setEditedContent(e.target.value)}
            onPaste={handleImagePaste}
            style={{
                width: '100%',
                minHeight: '600px',
                backgroundColor: theme.colors.bg.card,
                color: theme.colors.text.primary,
                border: `1px solid ${theme.colors.gold.dark}`,
                borderRadius: '8px',
                padding: '16px',
                fontFamily: theme.fonts.mono,
                fontSize: '14px',
                lineHeight: '1.6',
                boxSizing: 'border-box',
                resize: 'vertical',
                outline: 'none',
                boxShadow: `inset 0 2px 4px rgba(0,0,0,0.5)`
            }}
            />
        </div>
      ) : (
        <div className="markdown-body" style={{
          color: theme.colors.text.primary,
          lineHeight: '1.8',
          fontSize: '16px'
        }}>
          <ReactMarkdown
            remarkPlugins={[remarkGfm]}
            components={{
              h1: ({node, ...props}) => <h1 style={{ color: theme.colors.gold.light, borderBottom: `1px solid ${theme.colors.border.subtle}`, paddingBottom: '8px' }} {...props} />,
              h2: ({node, ...props}) => <h2 style={{ color: theme.colors.gold.base, marginTop: '24px' }} {...props} />,
              h3: ({node, ...props}) => <h3 style={{ color: theme.colors.text.primary, marginTop: '20px' }} {...props} />,
              a: ({node, ...props}) => <a style={{ color: theme.colors.jade.light, textDecoration: 'underline' }} {...props} />,
              code: ({node, ...props}: any) => props.inline ?
                <code style={{ backgroundColor: theme.colors.bg.card, padding: '2px 4px', borderRadius: '4px', color: theme.colors.crimson.light }} {...props} /> :
                <pre style={{ backgroundColor: theme.colors.bg.card, padding: '16px', borderRadius: '8px', overflowX: 'auto', border: `1px solid ${theme.colors.border.normal}` }}><code style={{ color: theme.colors.text.secondary }} {...props} /></pre>,
              blockquote: ({node, ...props}) => <blockquote style={{ borderLeft: `4px solid ${theme.colors.gold.dark}`, margin: '0 0 16px 0', padding: '0 16px', color: theme.colors.text.secondary, fontStyle: 'italic' }} {...props} />,
              img: ({node, ...props}) => <img style={{ maxWidth: '100%', borderRadius: '8px', border: `1px solid ${theme.colors.border.subtle}` }} {...props} />
            }}
          >
            {page.content || '*Chưa có nội dung*'}
          </ReactMarkdown>
        </div>
      )}
    </div>
  );
};
