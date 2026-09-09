---
name: browser-pdf-canvas-skill
description: "Arsitektur PDF.js HTML5 Canvas viewer kustom: lazy virtualized rendering via IntersectionObserver, eliminasi feedback loop animasi scroll hantu, dan in-document text search."
---

# Browser PDF Canvas Engine Skill

Solusi arsitektur web viewer PDF untuk dokumen teknis besar (skema boardview 50-150 halaman) tanpa menggunakan iframe bawaan browser yang membatasi kontrol mouse dan event.

---

## 1. Kegagalan Iframe Bawaan Browser

- Tag `<iframe>` PDF standar browser berjalan di dalam sandbox native C++ terisolasi.
- Event mouse (drag pan, click, selection, scroll zoom) ditelan habis oleh viewer browser dan tidak dapat diakses oleh JavaScript aplikasi utama.
- Fitur pencarian `Ctrl+F` browser menelusuri seluruh DOM halaman web (label sidebar, riwayat chat AI, tombol navigasi), bukan hanya teks dalam dokumen PDF.

---

## 2. Solusi: HTML5 Canvas + Virtualized Lazy Rendering

Rendering seluruh halaman PDF (100+ halaman) sekaligus ke Canvas akan membuat browser crash atau memakan memori berlebih. Gunakan pola virtualisasi berikut:

```javascript
// 1. Buat placeholder div kosong dengan atribut data-page-num
const placeholder = document.createElement('div');
placeholder.className = 'pdf-page-container relative';
placeholder.dataset.pageNum = pageNum;
placeholder.style.minHeight = `${estimatedHeight}px`;

// 2. Pasang IntersectionObserver untuk lazy-rendering
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    const pageNumber = parseInt(entry.target.dataset.pageNum, 10);
    if (entry.isIntersecting) {
      renderPageCanvas(pageNumber, entry.target);
    } else {
      // Bersihkan canvas yang keluar dari viewport untuk hemat RAM
      cleanupPageCanvas(entry.target);
    }
  });
}, {
  rootMargin: '400px 0px' // Buffer pre-fetch 1 halaman sebelum masuk layar
});
```

---

## 3. Eliminasi Bug "Scroll Hantu" (Infinite Feedback Loop)

### Akar Masalah:
Observer mendeteksi posisi halaman baru → memanggil callback `onPageChange(p)` → state parent berubah → memicu `scrollIntoView({ behavior: 'smooth' })` → browser beranimasi melewati halaman lain → observer terpicu lagi berulang kali hingga halaman melompat tanpa kendali.

### Solusi Sekring Ganda (`lastPageRef` + `jumpTargetRef`):
```javascript
let isProgrammaticScroll = false;
let targetPage = null;

function navigateToPage(pageNum) {
  isProgrammaticScroll = true;
  targetPage = pageNum;
  
  const el = document.querySelector(`[data-page-num="${pageNum}"]`);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' });
  }
}

// Di dalam observer handler:
if (isProgrammaticScroll) {
  if (detectedPage === targetPage) {
    isProgrammaticScroll = false; // Buka kunci sekring setelah target tercapai
  }
  return; // Abaikan event transisi selama animasi scroll berlangsung
}
```

---

## 4. In-Document Text Search Mandiri

Alih-alih bergantung pada pencarian browser:
1. Panggil `page.getTextContent()` per halaman untuk membaca seluruh string teks dan koordinatnya.
2. Buat array indeks kata kunci lokal (`[{ page: 12, count: 3 }]`).
3. Sediakan kontrol navigasi Previous/Next khusus pada toolbar viewer untuk melompat langsung ke halaman yang memiliki kecocokan kata kunci.
