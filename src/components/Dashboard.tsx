import React from 'react';
import { KanbanData } from '../types';
import { theme } from '../theme';

interface DashboardProps {
    data: KanbanData;
}

export const Dashboard: React.FC<DashboardProps> = ({ data }) => {
    let totalVolumes = data.volumes.length;
    let totalArcs = data.volumes.reduce((sum, v) => sum + v.arcs.length, 0);
    let totalChapters = data.volumes.reduce((sum, v) => sum + v.arcs.reduce((arcSum, a) => arcSum + a.chapters.length, 0), 0);
    let writtenChapters = data.volumes.reduce((sum, v) => sum + v.arcs.reduce((arcSum, a) => arcSum + a.chapters.filter(c => c.status === 'written').length, 0), 0);

    const StatCard = ({ label, value }: { label: string, value: number | string }) => (
        <div style={{
            backgroundColor: theme.colors.bg.card,
            border: `1px solid ${theme.colors.border.bright}`,
            borderRadius: '8px',
            padding: '24px',
            flex: 1,
            textAlign: 'center',
            boxShadow: `0 4px 12px ${theme.colors.gold.glow}`
        }}>
            <div style={{ fontSize: '14px', color: theme.colors.text.muted, marginBottom: '8px', fontFamily: theme.fonts.body }}>{label}</div>
            <div style={{ fontSize: '32px', color: theme.colors.gold.base, fontFamily: theme.fonts.display, fontWeight: 'bold' }}>{value}</div>
        </div>
    );

    return (
        <div style={{ padding: '32px', maxWidth: '1200px', margin: '0 auto' }}>
            <h1 style={{ fontFamily: theme.fonts.display, color: theme.colors.gold.base, borderBottom: `1px solid ${theme.colors.border.subtle}`, paddingBottom: '16px', marginBottom: '32px' }}>
                Tổng Quan Câu Chuyện
            </h1>

            <div style={{ display: 'flex', gap: '24px', marginBottom: '48px' }}>
                <StatCard label="Tổng Volume" value={totalVolumes} />
                <StatCard label="Tổng Arc" value={totalArcs} />
                <StatCard label="Tổng Chương" value={totalChapters} />
                <StatCard label="Đã Viết" value={`${writtenChapters} / ${totalChapters}`} />
            </div>

            <h2 style={{ fontFamily: theme.fonts.display, color: theme.colors.text.primary, marginBottom: '24px' }}>Cấu Trúc Tác Phẩm</h2>

            {data.volumes.map(volume => {
                const volChapters = volume.arcs.reduce((sum, a) => sum + a.chapters.length, 0);
                const volWritten = volume.arcs.reduce((sum, a) => sum + a.chapters.filter(c => c.status === 'written').length, 0);
                const progress = volChapters > 0 ? (volWritten / volChapters) * 100 : 0;

                return (
                    <div key={volume.id} style={{
                        backgroundColor: theme.colors.bg.secondary,
                        border: `1px solid ${theme.colors.border.subtle}`,
                        borderRadius: '8px',
                        padding: '24px',
                        marginBottom: '24px'
                    }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
                            <h3 style={{ fontFamily: theme.fonts.display, color: theme.colors.gold.light, margin: 0 }}>{volume.title}</h3>
                            <span style={{ color: theme.colors.text.secondary, fontSize: '14px' }}>
                                Tiến độ: {volWritten}/{volChapters} ({progress.toFixed(0)}%)
                            </span>
                        </div>
                        <div style={{
                            height: '6px',
                            backgroundColor: theme.colors.bg.primary,
                            borderRadius: '3px',
                            overflow: 'hidden',
                            marginBottom: '24px'
                        }}>
                            <div style={{
                                width: `${progress}%`,
                                height: '100%',
                                background: `linear-gradient(90deg, ${theme.colors.gold.base}, ${theme.colors.jade.base})`,
                                transition: 'width 0.5s ease'
                            }} />
                        </div>

                        {volume.arcs.map(arc => (
                            <div key={arc.id} style={{ marginLeft: '16px', marginBottom: '16px' }}>
                                <h4 style={{ color: theme.colors.text.secondary, margin: '0 0 8px 0', fontSize: '16px' }}>{arc.title}</h4>
                                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                                    {arc.chapters.map(chapter => {
                                        let bg = theme.colors.bg.card;
                                        let border = theme.colors.border.subtle;
                                        let color = theme.colors.text.muted;
                                        let icon = '○';

                                        if (chapter.status === 'written') {
                                            bg = theme.colors.jade.glow;
                                            border = theme.colors.jade.base;
                                            color = theme.colors.jade.light;
                                            icon = '✓';
                                        } else if (chapter.status === 'in-progress') {
                                            bg = theme.colors.gold.glow;
                                            border = theme.colors.gold.base;
                                            color = theme.colors.gold.light;
                                            icon = '◐';
                                        }

                                        return (
                                            <div key={chapter.id} style={{
                                                padding: '4px 12px',
                                                backgroundColor: bg,
                                                border: `1px solid ${border}`,
                                                borderRadius: '16px',
                                                fontSize: '12px',
                                                color: color,
                                                display: 'flex',
                                                alignItems: 'center',
                                                gap: '6px'
                                            }}>
                                                <span>{icon}</span>
                                                <span>{chapter.number ? `${chapter.number}: ` : ''}{chapter.title}</span>
                                            </div>
                                        )
                                    })}
                                </div>
                            </div>
                        ))}
                    </div>
                )
            })}
        </div>
    );
};
