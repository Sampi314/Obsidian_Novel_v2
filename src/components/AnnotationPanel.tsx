import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Annotation } from '../types';
import { theme } from '../theme';
import { MessageSquare, Send, Link as LinkIcon, Clock } from 'lucide-react';

export const AnnotationPanel: React.FC = () => {
    const [annotations, setAnnotations] = useState<Annotation[]>([]);
    const [newMessage, setNewMessage] = useState('');
    const [context, setContext] = useState('');

    useEffect(() => {
        const storedAnnotations = localStorage.getItem('co-nguyen-annotations');
        if (storedAnnotations) {
            setAnnotations(JSON.parse(storedAnnotations));
        } else {
            const mockData: Annotation[] = [
                { id: '1', timestamp: new Date().toISOString(), author: 'jules', context: 'Chapter 12', content: 'Cần thêm chi tiết về trận chiến.' },
                { id: '2', timestamp: new Date().toISOString(), author: 'user', context: 'Chapter 12', content: 'Đã sửa. Jules review lại giúp.' }
            ];
            setAnnotations(mockData);
            localStorage.setItem('co-nguyen-annotations', JSON.stringify(mockData));
        }
    }, []);

    const handleSend = () => {
        if (!newMessage.trim()) return;

        const newAnnotation: Annotation = {
            id: Math.random().toString(36).substr(2, 9),
            timestamp: new Date().toISOString(),
            author: 'user',
            context: context || 'General',
            content: newMessage
        };

        const newAnnotations = [...annotations, newAnnotation];
        setAnnotations(newAnnotations);
        localStorage.setItem('co-nguyen-annotations', JSON.stringify(newAnnotations));
        setNewMessage('');
    };

    return (
        <div style={{ padding: '32px', maxWidth: '800px', margin: '0 auto', display: 'flex', flexDirection: 'column', height: 'calc(100vh - 64px)' }}>
            <h1 style={{ fontFamily: theme.fonts.display, color: theme.colors.gold.base, borderBottom: `1px solid ${theme.colors.border.subtle}`, paddingBottom: '16px', marginBottom: '24px', display: 'flex', alignItems: 'center', gap: '12px' }}>
                <MessageSquare size={24} /> Thảo Luận Kế Hoạch
            </h1>

            {/* Chat Timeline */}
            <div style={{ flex: 1, overflowY: 'auto', paddingRight: '16px', display: 'flex', flexDirection: 'column', gap: '24px' }}>
                {annotations.map((ann) => {
                    const isJules = ann.author === 'jules';
                    return (
                        <div key={ann.id} style={{
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: isJules ? 'flex-start' : 'flex-end',
                            width: '100%'
                        }}>
                            <div style={{
                                maxWidth: '75%',
                                backgroundColor: isJules ? theme.colors.bg.secondary : theme.colors.bg.card,
                                border: `1px solid ${isJules ? theme.colors.jade.dark : theme.colors.gold.dark}`,
                                borderRadius: '8px',
                                padding: '16px',
                                boxShadow: `0 4px 12px rgba(0,0,0,0.2)`
                            }}>
                                <div style={{
                                    display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px',
                                    fontSize: '12px', color: theme.colors.text.muted
                                }}>
                                    <span style={{ fontWeight: 'bold', color: isJules ? theme.colors.jade.light : theme.colors.gold.light, fontSize: '14px' }}>
                                        {isJules ? '🐉 Jules Tổng Quản' : '👤 User'}
                                    </span>
                                    <span>•</span>
                                    <Clock size={12} /> {new Date(ann.timestamp).toLocaleDateString()} {new Date(ann.timestamp).toLocaleTimeString()}
                                </div>

                                {ann.context && (
                                    <div style={{ display: 'flex', alignItems: 'center', gap: '4px', fontSize: '12px', color: theme.colors.text.secondary, marginBottom: '8px', backgroundColor: 'rgba(255,255,255,0.05)', padding: '4px 8px', borderRadius: '4px', width: 'fit-content' }}>
                                        <LinkIcon size={12} /> {ann.context}
                                    </div>
                                )}

                                <div className="markdown-body" style={{ color: theme.colors.text.primary, fontSize: '14px', lineHeight: '1.6' }}>
                                    <ReactMarkdown remarkPlugins={[remarkGfm]}>{ann.content}</ReactMarkdown>
                                </div>
                            </div>
                        </div>
                    );
                })}
            </div>

            {/* Input Area */}
            <div style={{
                marginTop: '24px',
                backgroundColor: theme.colors.bg.secondary,
                border: `1px solid ${theme.colors.border.bright}`,
                borderRadius: '8px',
                padding: '16px',
                display: 'flex',
                flexDirection: 'column',
                gap: '12px'
            }}>
                <div style={{ display: 'flex', gap: '12px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flex: 1 }}>
                        <span style={{ color: theme.colors.text.muted, fontSize: '14px' }}>Liên quan đến:</span>
                        <input
                            type="text"
                            placeholder="Chapter 1, Arc 2, Cố Đức Thiên..."
                            value={context}
                            onChange={(e) => setContext(e.target.value)}
                            style={{
                                flex: 1, padding: '8px', backgroundColor: theme.colors.bg.card,
                                border: `1px solid ${theme.colors.border.normal}`, borderRadius: '4px',
                                color: theme.colors.text.primary, fontFamily: theme.fonts.body
                            }}
                        />
                    </div>
                </div>

                <div style={{ display: 'flex', gap: '12px', alignItems: 'flex-start' }}>
                    <textarea
                        value={newMessage}
                        onChange={(e) => setNewMessage(e.target.value)}
                        placeholder="Nhập tin nhắn cho Jules Tổng Quản (hỗ trợ Markdown)..."
                        style={{
                            flex: 1, minHeight: '80px', padding: '12px', backgroundColor: theme.colors.bg.card,
                            border: `1px solid ${theme.colors.border.normal}`, borderRadius: '4px',
                            color: theme.colors.text.primary, fontFamily: theme.fonts.body, resize: 'vertical'
                        }}
                    />
                    <button
                        onClick={handleSend}
                        style={{
                            padding: '12px 24px', backgroundColor: theme.colors.gold.base,
                            color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer',
                            display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 'bold', height: 'fit-content'
                        }}
                    >
                        <Send size={18} /> Gửi
                    </button>
                </div>
            </div>
        </div>
    );
};
