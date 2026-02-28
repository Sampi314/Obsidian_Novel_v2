export const theme = {
  colors: {
    // Backgrounds
    bg: {
      primary: '#0a0a0f',        // Đen tuyền như đêm tu luyện
      secondary: '#0f0f1a',      // Nền panel
      card: '#13131f',           // Nền card
      hover: '#1a1a2e',          // Hover state
    },
    // Accent — Vàng ngọc cổ phong
    gold: {
      light: '#f5d485',
      base: '#d4a843',
      dark: '#a07820',
      glow: 'rgba(212, 168, 67, 0.15)',
    },
    // Jade xanh ngọc
    jade: {
      light: '#7fffd4',
      base: '#2ecc71',
      dark: '#1a8a4a',
      glow: 'rgba(46, 204, 113, 0.15)',
    },
    // Crimson — Máu chiến trường
    crimson: {
      light: '#ff6b6b',
      base: '#c0392b',
      dark: '#7b241c',
      glow: 'rgba(192, 57, 43, 0.15)',
    },
    // Text
    text: {
      primary: '#e8dcc8',         // Vàng kem cổ thư
      secondary: '#9e9e7e',       // Xám vàng
      muted: '#5a5a4a',           // Mờ
      accent: '#d4a843',          // Gold accent
    },
    // Border
    border: {
      subtle: 'rgba(212, 168, 67, 0.1)',
      normal: 'rgba(212, 168, 67, 0.25)',
      bright: 'rgba(212, 168, 67, 0.5)',
    }
  },
  // Hoa văn SVG background (dạng string để dùng trong CSS)
  patterns: {
    // Hoa văn lặp lại nhẹ ở background chính
    mainBg: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23d4a843' fill-opacity='0.03'%3E%3Cpath d='M30 0L60 30L30 60L0 30z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
  },
  fonts: {
    display: '"Noto Serif", "Times New Roman", serif',   // Cho titles
    body: '"Inter", system-ui, sans-serif',              // Cho content
    mono: '"JetBrains Mono", monospace',
  }
};
