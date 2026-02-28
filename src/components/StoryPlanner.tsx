import React, { useState } from 'react';
import { KanbanData, Chapter, ChapterStatus } from '../types';
import { theme } from '../theme';
import { FileEdit, MessageSquare, BookOpen, User, GitCommit } from 'lucide-react';
import { POV } from '../types';

interface StoryPlannerProps {
    data: KanbanData;
    setData: (data: KanbanData) => void;
}

const columns: { id: ChapterStatus, title: string }[] = [
    { id: 'planned', title: 'Lên Kế Hoạch' },
    { id: 'in-progress', title: 'Đang Viết' },
    { id: 'needs-revision', title: 'Cần Sửa' },
    { id: 'written', title: 'Hoàn Thành' }
];

export const StoryPlanner: React.FC<StoryPlannerProps> = ({ data, setData }) => {
    const [selectedChapter, setSelectedChapter] = useState<Chapter | null>(null);

    const getAllChapters = (): (Chapter & { arcTitle: string, volumeTitle: string })[] => {
        let all: any[] = [];
        data.volumes.forEach(v => {
            v.arcs.forEach(a => {
                a.chapters.forEach(c => {
                    all.push({ ...c, arcTitle: a.title, volumeTitle: v.title });
                });
            });
        });
        return all.sort((a, b) => a.number - b.number);
    };

    const handleSaveChapter = () => {
        if (!selectedChapter) return;
        const newData = JSON.parse(JSON.stringify(data));
        newData.volumes.forEach((v: any) => {
            v.arcs.forEach((a: any) => {
                const idx = a.chapters.findIndex((ch: any) => ch.id === selectedChapter.id);
                if (idx !== -1) {
                    a.chapters[idx] = { ...a.chapters[idx], summary: selectedChapter.summary, notes: selectedChapter.notes, status: selectedChapter.status };
                }
            });
        });
        setData(newData);
        localStorage.setItem('co-nguyen-planner', JSON.stringify(newData));
        setSelectedChapter(null);
    };

    const allChapters = getAllChapters();
    const povs: { id: POV, color: string }[] = [
        { id: 'Chính', color: '#ff6b6b' }, // Crimson light
        { id: 'Diệp Tĩnh Sương', color: '#3498db' }, // Blue
        { id: 'Lâm Phong', color: '#2ecc71' }, // Jade base
        { id: 'Lệ Vô Tâm', color: '#9b59b6' }, // Purple
        { id: 'Hứa Nhược Thủy', color: '#e67e22' } // Orange
    ];

    const getPovColor = (povName: POV) => {
        const found = povs.find(p => p.id === povName);
        return found ? found.color : theme.colors.text.muted;
    };

    // Assuming chapters are roughly timeline points 1, 2, 3...
    const timelineMax = Math.max(10, allChapters.length + 2);

    return (
        <div style={{ display: 'flex', height: 'calc(100vh - 64px)', overflow: 'hidden' }}>
            {/* Sidebar (Left Pane) */}
            <div style={{
                width: '320px',
                backgroundColor: theme.colors.bg.secondary,
                borderRight: `1px solid ${theme.colors.border.subtle}`,
                display: 'flex',
                flexDirection: 'column',
                height: '100%',
                overflowY: 'auto'
            }}>
                {/* Góc Nhìn (Characters) Section */}
                <div style={{ padding: '24px', borderBottom: `1px solid ${theme.colors.border.subtle}` }}>
                    <div style={{ fontSize: '12px', fontWeight: 'bold', color: theme.colors.text.muted, letterSpacing: '1px', marginBottom: '16px' }}>
                        GÓC NHÌN (POVs)
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                        {povs.map(pov => (
                            <div key={pov.id} style={{ display: 'flex', alignItems: 'center', gap: '12px', fontSize: '14px', color: theme.colors.text.primary }}>
                                <div style={{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: pov.color }} />
                                {pov.id === 'Chính' ? 'Góc Nhìn Chính' : pov.id}
                            </div>
                        ))}
                    </div>
                </div>

                {/* Sự Kiện (Events/Chapters) Section */}
                <div style={{ padding: '24px', flex: 1 }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
                        <div style={{ fontSize: '12px', fontWeight: 'bold', color: theme.colors.text.muted, letterSpacing: '1px' }}>
                            SỰ KIỆN
                        </div>
                        <button style={{ background: 'none', border: 'none', color: theme.colors.gold.base, cursor: 'pointer', fontSize: '20px' }}>+</button>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                        {allChapters.map(chapter => (
                            <div
                                key={chapter.id}
                                onClick={() => setSelectedChapter(chapter)}
                                style={{
                                    backgroundColor: theme.colors.bg.card,
                                    border: `1px solid ${theme.colors.border.subtle}`,
                                    borderRadius: '8px',
                                    padding: '16px',
                                    cursor: 'pointer',
                                    transition: 'border-color 0.2s'
                                }}
                                onMouseEnter={e => e.currentTarget.style.borderColor = theme.colors.gold.base}
                                onMouseLeave={e => e.currentTarget.style.borderColor = theme.colors.border.subtle}
                            >
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '12px' }}>
                                    <div style={{ fontSize: '14px', fontWeight: 600, color: theme.colors.text.primary, lineHeight: '1.4', paddingRight: '12px' }}>
                                        {chapter.title}
                                    </div>
                                    <div style={{
                                        fontSize: '12px', color: theme.colors.text.muted,
                                        backgroundColor: theme.colors.bg.primary, padding: '2px 8px',
                                        borderRadius: '4px', border: `1px solid ${theme.colors.border.normal}`,
                                        whiteSpace: 'nowrap'
                                    }}>
                                        Ch {chapter.number}
                                    </div>
                                </div>
                                <div style={{ display: 'flex', gap: '8px' }}>
                                    {(chapter.povs && chapter.povs.length > 0 ? chapter.povs : ['Chính' as POV]).map(p => (
                                        <div key={p} style={{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: getPovColor(p) }} title={p} />
                                    ))}
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>

            {/* Timeline Graph (Right Pane) */}
            <div style={{ flex: 1, padding: '32px', backgroundColor: theme.colors.bg.primary, overflow: 'auto', display: 'flex', flexDirection: 'column' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px' }}>
                    <h1 style={{ fontFamily: theme.fonts.display, color: theme.colors.gold.base, margin: 0 }}>Storyline Planner</h1>
                    <div style={{ display: 'flex', gap: '12px' }}>
                         <button style={{
                            padding: '8px 16px',
                            backgroundColor: 'transparent',
                            border: `1px solid ${theme.colors.border.bright}`,
                            borderRadius: '4px',
                            color: theme.colors.text.primary,
                            cursor: 'pointer'
                        }}>Tải Xuống</button>
                    </div>
                </div>

                <div style={{
                    flex: 1,
                    backgroundColor: theme.colors.bg.card,
                    border: `1px solid ${theme.colors.border.subtle}`,
                    borderRadius: '12px',
                    padding: '40px 24px',
                    position: 'relative',
                    overflowX: 'auto',
                    minWidth: '800px'
                }}>
                    <div style={{ position: 'relative', height: `${povs.length * 100}px`, minWidth: `${timelineMax * 150}px` }}>

                        {/* Horizontal POV Tracks */}
                        {povs.map((pov, idx) => (
                            <div key={pov.id} style={{
                                position: 'absolute',
                                left: 0,
                                right: 0,
                                top: `${idx * 100 + 50}px`,
                                height: '2px',
                                borderTop: `2px dashed ${pov.color}`,
                                opacity: 0.3,
                                zIndex: 1
                            }}>
                                <span style={{
                                    position: 'absolute', left: 0, top: '-24px',
                                    color: pov.color, fontWeight: 'bold', fontSize: '14px',
                                    textShadow: `0 0 4px rgba(0,0,0,0.8)`
                                }}>
                                    {pov.id === 'Chính' ? 'Góc Nhìn Chính' : pov.id}
                                </span>
                            </div>
                        ))}

                        {/* X-Axis Timeline */}
                        <div style={{
                            position: 'absolute',
                            left: '150px',
                            right: 0,
                            bottom: 0,
                            height: '24px',
                            borderTop: `1px solid ${theme.colors.text.muted}`,
                            display: 'flex',
                            zIndex: 1
                        }}>
                            {Array.from({ length: timelineMax }).map((_, i) => (
                                <div key={i} style={{ width: '150px', position: 'relative' }}>
                                    <div style={{ position: 'absolute', top: 0, left: 0, height: '8px', width: '1px', backgroundColor: theme.colors.text.muted }} />
                                    <span style={{ position: 'absolute', top: '12px', left: '-4px', fontSize: '12px', color: theme.colors.text.muted }}>{i}</span>
                                </div>
                            ))}
                        </div>

                        {/* Nodes and Connections */}
                        {allChapters.map(chapter => {
                            const xPos = 150 + (chapter.number * 150);
                            const actPovs = chapter.povs && chapter.povs.length > 0 ? chapter.povs : ['Chính' as POV];

                            // Sort POVs by their vertical index to draw vertical connections correctly
                            const activePovIndices = actPovs.map(p => povs.findIndex(track => track.id === p)).filter(i => i !== -1).sort((a,b) => a - b);

                            if (activePovIndices.length === 0) return null;

                            const isShared = activePovIndices.length > 1;
                            const minIndex = activePovIndices[0];
                            const maxIndex = activePovIndices[activePovIndices.length - 1];

                            return (
                                <div key={chapter.id}>
                                    {/* Vertical dashed line for shared events */}
                                    {isShared && (
                                        <div style={{
                                            position: 'absolute',
                                            left: `${xPos}px`,
                                            top: `${minIndex * 100 + 50}px`,
                                            height: `${(maxIndex - minIndex) * 100}px`,
                                            borderLeft: `2px dashed ${theme.colors.border.bright}`,
                                            zIndex: 2,
                                            transform: 'translateX(5px)' // align to center of 12px node
                                        }} />
                                    )}

                                    {/* Nodes */}
                                    {activePovIndices.map(povIndex => {
                                        const povColor = povs[povIndex].color;
                                        return (
                                            <div
                                                key={`${chapter.id}-${povIndex}`}
                                                onClick={() => setSelectedChapter(chapter)}
                                                style={{
                                                    position: 'absolute',
                                                    left: `${xPos}px`,
                                                    top: `${povIndex * 100 + 50}px`,
                                                    width: '12px',
                                                    height: '12px',
                                                    backgroundColor: povColor,
                                                    borderRadius: '50%',
                                                    transform: 'translate(-50%, -50%)',
                                                    cursor: 'pointer',
                                                    zIndex: 10,
                                                    boxShadow: `0 0 0 4px ${theme.colors.bg.card}, 0 0 0 6px ${povColor}40`,
                                                    transition: 'transform 0.2s'
                                                }}
                                                onMouseEnter={e => {
                                                    e.currentTarget.style.transform = 'translate(-50%, -50%) scale(1.5)';
                                                    const titleEl = document.getElementById(`title-${chapter.id}`);
                                                    if (titleEl) titleEl.style.opacity = '1';
                                                }}
                                                onMouseLeave={e => {
                                                    e.currentTarget.style.transform = 'translate(-50%, -50%) scale(1)';
                                                    const titleEl = document.getElementById(`title-${chapter.id}`);
                                                    if (titleEl) titleEl.style.opacity = '0.7';
                                                }}
                                            />
                                        );
                                    })}

                                    {/* Chapter Title floating above the top node */}
                                    <div
                                        id={`title-${chapter.id}`}
                                        style={{
                                            position: 'absolute',
                                            left: `${xPos}px`,
                                            top: `${minIndex * 100 + 20}px`,
                                            transform: 'translateX(-50%)',
                                            fontSize: '13px',
                                            color: theme.colors.text.primary,
                                            whiteSpace: 'nowrap',
                                            pointerEvents: 'none',
                                            opacity: 0.7,
                                            transition: 'opacity 0.2s',
                                            zIndex: 20,
                                            textShadow: `0 2px 4px rgba(0,0,0,0.8)`
                                        }}
                                    >
                                        {chapter.title}
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                </div>
            </div>

            {selectedChapter && (
                <div style={{
                    position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
                    backgroundColor: 'rgba(0,0,0,0.8)', zIndex: 1000,
                    display: 'flex', justifyContent: 'center', alignItems: 'center'
                }} onClick={() => setSelectedChapter(null)}>
                    <div style={{
                        backgroundColor: theme.colors.bg.secondary,
                        width: '600px',
                        maxHeight: '90vh',
                        borderRadius: '8px',
                        border: `1px solid ${theme.colors.border.bright}`,
                        padding: '32px',
                        overflowY: 'auto',
                        boxShadow: `0 0 32px ${theme.colors.gold.glow}`
                    }} onClick={e => e.stopPropagation()}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '24px' }}>
                            <h2 style={{ fontFamily: theme.fonts.display, color: theme.colors.gold.base, margin: 0 }}>
                                {selectedChapter.title}
                            </h2>
                            <button onClick={() => setSelectedChapter(null)} style={{ background: 'none', border: 'none', color: theme.colors.text.muted, fontSize: '24px', cursor: 'pointer' }}>&times;</button>
                        </div>

                        <div style={{ marginBottom: '24px' }}>
                            <label style={{ display: 'block', color: theme.colors.text.secondary, marginBottom: '8px', fontSize: '14px' }}>Trạng Thái</label>
                            <select
                                value={selectedChapter.status}
                                onChange={e => setSelectedChapter({ ...selectedChapter, status: e.target.value as ChapterStatus })}
                                style={{
                                    width: '100%', padding: '8px', backgroundColor: theme.colors.bg.card,
                                    border: `1px solid ${theme.colors.border.normal}`, color: theme.colors.text.primary,
                                    borderRadius: '4px', fontFamily: theme.fonts.body
                                }}
                            >
                                {columns.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
                            </select>
                        </div>

                        <div style={{ marginBottom: '24px' }}>
                            <label style={{ display: 'block', color: theme.colors.text.secondary, marginBottom: '8px', fontSize: '14px' }}>Mô tả / Tóm tắt</label>
                            <textarea
                                value={selectedChapter.summary || ''}
                                onChange={e => setSelectedChapter({ ...selectedChapter, summary: e.target.value })}
                                placeholder="Tóm tắt chương..."
                                style={{
                                    width: '100%', minHeight: '100px', backgroundColor: theme.colors.bg.card,
                                    border: `1px solid ${theme.colors.border.normal}`, color: theme.colors.text.primary,
                                    padding: '12px', borderRadius: '4px', fontFamily: theme.fonts.body, boxSizing: 'border-box'
                                }}
                            />
                        </div>

                        {selectedChapter.julesNotes && (
                            <div style={{
                                backgroundColor: theme.colors.jade.glow,
                                borderLeft: `4px solid ${theme.colors.jade.base}`,
                                padding: '16px',
                                marginBottom: '24px',
                                borderRadius: '4px'
                            }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: theme.colors.jade.light, marginBottom: '8px', fontWeight: 'bold' }}>
                                    <MessageSquare size={16} /> Jules Tổng Quản Notes
                                </div>
                                <div style={{ color: theme.colors.text.primary, fontSize: '14px', whiteSpace: 'pre-wrap' }}>
                                    {selectedChapter.julesNotes}
                                </div>
                            </div>
                        )}

                        <div style={{ marginBottom: '24px' }}>
                            <label style={{ display: 'block', color: theme.colors.text.secondary, marginBottom: '8px', fontSize: '14px' }}>User Notes</label>
                            <textarea
                                value={selectedChapter.notes || ''}
                                onChange={e => setSelectedChapter({ ...selectedChapter, notes: e.target.value })}
                                placeholder="Ghi chú của bạn..."
                                style={{
                                    width: '100%', minHeight: '80px', backgroundColor: theme.colors.bg.card,
                                    border: `1px solid ${theme.colors.border.normal}`, color: theme.colors.text.primary,
                                    padding: '12px', borderRadius: '4px', fontFamily: theme.fonts.body, boxSizing: 'border-box'
                                }}
                            />
                        </div>

                        <div style={{ display: 'flex', gap: '16px' }}>
                            <button onClick={handleSaveChapter} style={{
                                flex: 1, padding: '12px', backgroundColor: theme.colors.gold.base,
                                color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold'
                            }}>Lưu Thay Đổi</button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};
