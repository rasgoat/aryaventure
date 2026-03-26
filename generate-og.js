const { createCanvas } = require('canvas');
const fs = require('fs');
const path = require('path');

const W = 1200, H = 630;
const canvas = createCanvas(W, H);
const ctx = canvas.getContext('2d');

// Black background
ctx.fillStyle = '#000000';
ctx.fillRect(0, 0, W, H);

// Wordmark — Clash Display not available in node-canvas, use bold sans-serif
ctx.fillStyle = '#ffffff';
ctx.font = 'bold 72px sans-serif';
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';
ctx.letterSpacing = '12px';
ctx.fillText('ARYAVENTURE', W / 2, H / 2 - 30);

// Subtitle
ctx.fillStyle = 'rgba(255,255,255,0.4)';
ctx.font = '400 24px sans-serif';
ctx.letterSpacing = '2px';
ctx.fillText('Premium Digital Agency', W / 2, H / 2 + 40);

// URL bottom right
ctx.fillStyle = '#c8ff00';
ctx.font = '400 18px sans-serif';
ctx.textAlign = 'right';
ctx.textBaseline = 'bottom';
ctx.fillText('aryaventure.com', W - 48, H - 36);

// Save
const buf = canvas.toBuffer('image/png');
fs.writeFileSync(path.join(__dirname, 'og-image.png'), buf);
console.log('og-image.png generated (1200x630)');
