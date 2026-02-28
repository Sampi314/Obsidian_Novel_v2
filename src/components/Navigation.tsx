import React from 'react';
import { GitBranch, LayoutDashboard, Kanban, BookOpen, MessageSquare, Download } from 'lucide-react';
import { theme } from '../theme';

type Tab = 'timeline' | 'dashboard' | 'planner' | 'wiki' | 'annotations';

interface NavigationProps {
  activeTab: Tab;
  setActiveTab: (tab: Tab) => void;
  onSync: () => void;
}

export const Navigation: React.FC<NavigationProps> = ({ activeTab, setActiveTab, onSync }) => {
  const tabs: { id: Tab; label: string; icon: React.ReactNode }[] = [
    { id: 'timeline', label: 'Timeline', icon: <GitBranch size={18} /> },
    { id: 'dashboard', label: 'Dashboard', icon: <LayoutDashboard size={18} /> },
    { id: 'planner', label: 'Story Planner', icon: <Kanban size={18} /> },
    { id: 'wiki', label: 'Wiki', icon: <BookOpen size={18} /> },
    { id: 'annotations', label: 'Annotations', icon: <MessageSquare size={18} /> },
  ];

  return (
    <nav style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '0 24px',
      backgroundColor: theme.colors.bg.secondary,
      borderBottom: `1px solid ${theme.colors.border.normal}`,
      height: '64px',
      position: 'sticky',
      top: 0,
      zIndex: 100,
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '32px' }}>
        <div style={{
          fontFamily: theme.fonts.display,
          color: theme.colors.gold.base,
          fontSize: '24px',
          fontWeight: 'bold',
          letterSpacing: '2px',
          textShadow: `0 0 10px ${theme.colors.gold.glow}`,
        }}>
          故源 · Cố Nguyên
        </div>

        <div style={{ display: 'flex', gap: '8px' }}>
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                padding: '12px 16px',
                backgroundColor: 'transparent',
                border: 'none',
                borderBottom: `2px solid ${activeTab === tab.id ? theme.colors.gold.base : 'transparent'}`,
                color: activeTab === tab.id ? theme.colors.text.primary : theme.colors.text.muted,
                cursor: 'pointer',
                fontFamily: theme.fonts.body,
                fontSize: '14px',
                fontWeight: activeTab === tab.id ? 600 : 400,
                transition: 'all 0.2s',
                textShadow: activeTab === tab.id ? `0 0 8px rgba(232, 220, 200, 0.3)` : 'none',
              }}
              onMouseEnter={(e) => {
                if (activeTab !== tab.id) {
                  e.currentTarget.style.color = theme.colors.text.secondary;
                  e.currentTarget.style.textShadow = `0 0 8px ${theme.colors.gold.glow}`;
                }
              }}
              onMouseLeave={(e) => {
                if (activeTab !== tab.id) {
                  e.currentTarget.style.color = theme.colors.text.muted;
                  e.currentTarget.style.textShadow = 'none';
                }
              }}
            >
              {tab.icon}
              {tab.label}
              {tab.id === 'annotations' && (
                 <span style={{
                     background: theme.colors.crimson.base,
                     color: 'white',
                     borderRadius: '50%',
                     padding: '2px 6px',
                     fontSize: '10px',
                     marginLeft: '4px'
                 }}>1</span>
              )}
            </button>
          ))}
        </div>
      </div>

      <button
        onClick={onSync}
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          padding: '8px 16px',
          backgroundColor: 'transparent',
          border: `1px solid ${theme.colors.border.bright}`,
          borderRadius: '4px',
          color: theme.colors.gold.base,
          cursor: 'pointer',
          fontFamily: theme.fonts.body,
          fontSize: '14px',
          transition: 'all 0.2s',
        }}
        onMouseEnter={(e) => {
          e.currentTarget.style.backgroundColor = theme.colors.gold.glow;
        }}
        onMouseLeave={(e) => {
          e.currentTarget.style.backgroundColor = 'transparent';
        }}
      >
        <Download size={16} />
        Sync với Jules
      </button>
    </nav>
  );
};
