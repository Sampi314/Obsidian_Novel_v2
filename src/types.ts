import { theme } from './theme';

export type ChapterStatus = 'written' | 'in-progress' | 'planned' | 'needs-revision';

export type POV = 'Lâm Phong' | 'Diệp Tĩnh Sương' | 'Lệ Vô Tâm' | 'Hứa Nhược Thủy' | 'Chính';

export type Chapter = {
  id: string;
  number: number;
  title: string;
  status: ChapterStatus;
  povs: POV[];
  wordCount?: number;
  summary?: string;
  notes?: string;
  julesNotes?: string;
  characters?: string[];
  arcId?: string;
  volumeId?: string;
};

export type Arc = {
  id: string;
  title: string;
  chapters: Chapter[];
  description?: string;
};

export type Volume = {
  id: string;
  title: string;
  arcs: Arc[];
};

export type KanbanData = {
  volumes: Volume[];
};

export type WikiPage = {
  id: string;
  title: string;
  category: string;
  content: string;
  lastEdited?: string;
  lastEditedBy?: 'user' | 'jules';
  path?: string;
};

export type Annotation = {
  id: string;
  timestamp: string;
  author: 'jules' | 'user';
  context: string;
  content: string;
};
