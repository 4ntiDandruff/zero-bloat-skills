---
name: portfolio-timeline-lightbox-skill
description: "Professional career milestone roadmap and accessible zero-bloat lightbox viewer: vertical gradient timeline with glowing milestone nodes, mobile collapsible phases, touch-swipe gestures, keyboard navigation, and focus trapping."
---

# Portfolio Timeline & Lightbox Skill

Engineering patterns for constructing high-trust technical portfolios, career milestones, certification showcases, and interactive high-resolution image viewers without heavy frontend dependencies (Fancybox, LightGallery, or React Modal bloat).

Battle-tested in the **Megapass Intra Solusindo** technician showcase (`megapass.web.id/teknisi/`).

---

## 1. Vertical Milestone Roadmap Pattern

### The Layout Architecture
A continuous vertical timeline linking multiple career phases. Uses a background gradient line (`tl-line`) and glowing circular milestone markers (`tl-dot-lg`) with pulsing cyan highlights:

```html
<div class="max-w-4xl mx-auto px-4">
  <div class="relative">
    <!-- Continuous Vertical Gradient Line -->
    <div class="tl-line absolute left-4 sm:left-6 top-0 bottom-0 w-px bg-gradient-to-b from-cyan-400/40 via-cyan-400/20 to-transparent"></div>

    <div class="space-y-8">
      <!-- Standard Career Phase -->
      <div class="relative pl-12 sm:pl-16">
        <!-- Connecting Dot -->
        <div class="tl-dot absolute left-2 sm:left-4 top-3 w-4 h-4 rounded-full bg-slate-900 border-2 border-cyan-400/50"></div>
        
        <!-- Content Card -->
        <div class="bg-slate-900/80 rounded-2xl p-5 border border-white/5">
          <div class="flex items-center gap-2 mb-1">
            <span class="px-2 py-0.5 rounded bg-cyan-400/10 text-cyan-400 text-[10px] font-bold uppercase tracking-wider">Fase 1</span>
            <span class="text-slate-400 text-xs font-semibold">2012 - 2016</span>
          </div>
          <h3 class="font-bold text-base text-white">Fondasi Vokasi & Elektronika Dasar</h3>
          <p class="text-slate-400 text-sm mt-2 leading-relaxed">
            Mulai mendalami teknik penyolderan presisi, perakitan sirkuit, dan instalasi sistem operasi Linux/Windows.
          </p>
        </div>
      </div>

      <!-- Hero Milestone Phase (Highlighted) -->
      <div class="relative pl-12 sm:pl-16">
        <!-- Glowing Dot with Cyan Shadow -->
        <div class="tl-dot-lg absolute left-2 sm:left-4 top-3 w-4 h-4 rounded-full bg-cyan-400 border-2 border-cyan-300 shadow-[0_0_12px_rgba(34,211,238,0.6)]"></div>
        
        <!-- Highlighted Card -->
        <div class="bg-slate-900/90 rounded-2xl p-5 border border-cyan-400/30 border-l-4 border-l-cyan-400 shadow-[0_0_24px_rgba(34,211,238,0.08)]">
          <div class="flex items-center gap-2 flex-wrap mb-1">
            <span class="px-2 py-0.5 rounded bg-cyan-400/15 text-cyan-400 text-[10px] font-bold uppercase tracking-wider">Fase 2</span>
            <span class="text-cyan-400 font-bold text-xs">2021 - 2024</span>
            <span class="px-2 py-0.5 rounded-full bg-cyan-400/20 text-cyan-300 text-[10px] font-bold uppercase tracking-wider">Milestone</span>
          </div>
          <h3 class="font-bold text-lg text-white">Sertifikasi Profesi BNSP & Spesialisasi</h3>
          <p class="text-slate-300 text-sm mt-2 leading-relaxed">
            Sertifikasi nasional BNSP Reparasi Telepon Seluler dengan skor teori 100/100, pelatihan skematik motherboard tingkat lanjut.
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## 2. Mobile-Collapsible Phases (Saving Mobile Viewport)

Long career trajectories cause vertical scrolling fatigue on mobile. Keep milestones collapsed by default on small screens with a smooth toggle:

```html
<div class="tl-collapsible relative pl-12 sm:pl-16" id="phase1">
  <div class="bg-slate-900/80 rounded-2xl p-5 border border-white/5">
    <div class="flex items-center justify-between">
      <span class="text-cyan-400 text-xs font-bold">2017 - 2020</span>
      <button type="button" class="tl-toggle-btn sm:hidden p-1 rounded-full bg-white/5 text-slate-400 hover:text-cyan-400" aria-expanded="false" aria-label="Buka detail">
        <svg class="w-4 h-4 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
      </button>
    </div>
    <h3 class="font-bold text-white mt-1">Pengalaman Operasional Lapangan</h3>
    
    <div class="tl-body mt-2 hidden sm:block">
      <ul class="text-slate-400 text-sm space-y-1.5 list-disc pl-4">
        <li>Maintenance jaringan komputer dan recovery sistem crash.</li>
        <li>Manajemen kelistrikan dan grounding meja servis.</li>
      </ul>
    </div>
  </div>
</div>
```

```javascript
document.querySelectorAll('.tl-collapsible').forEach(function(item) {
  var btn = item.querySelector('.tl-toggle-btn');
  var body = item.querySelector('.tl-body');
  if (!btn || !body) return;
  btn.addEventListener('click', function() {
    var isOpen = !body.classList.contains('hidden');
    body.classList.toggle('hidden', isOpen);
    btn.setAttribute('aria-expanded', !isOpen);
    var svg = btn.querySelector('svg');
    if (svg) svg.style.transform = isOpen ? 'rotate(0deg)' : 'rotate(180deg)';
  });
});
```

---

## 3. Single-Instance Standalone Lightbox Modal

### Memory Efficiency Principle
Never create a separate modal element for every image or certificate. Use **one single modal container** in the DOM root. When a thumbnail is clicked, dynamically inject image source, alt text, and caption:

```html
<!-- Single DOM Lightbox Modal (Fixed overlay) -->
<div id="lightbox" class="fixed inset-0 z-[100] bg-black/90 backdrop-blur-sm hidden items-center justify-center p-4 select-none" role="dialog" aria-modal="true" aria-label="Penampil Gambar">
  <div class="relative max-w-5xl w-full flex flex-col items-center">
    <!-- Close Button -->
    <button type="button" id="lbClose" class="absolute -top-12 right-0 text-slate-400 hover:text-white p-2" aria-label="Tutup">
      <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
    </button>

    <!-- Prev / Next Desktop Controls -->
    <button type="button" id="lbPrev" class="hidden sm:flex absolute left-0 top-1/2 -translate-y-1/2 -translate-x-12 p-3 text-slate-400 hover:text-white" aria-label="Sebelumnya">
      <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
    </button>
    <button type="button" id="lbNext" class="hidden sm:flex absolute right-0 top-1/2 -translate-y-1/2 translate-x-12 p-3 text-slate-400 hover:text-white" aria-label="Berikutnya">
      <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
    </button>

    <!-- Main Image Display with Opacity Cross-Fade -->
    <img id="lbImg" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="" class="max-w-full max-h-[80vh] rounded-xl object-contain shadow-2xl transition-opacity duration-150">
    
    <!-- Meta Info -->
    <p id="lbCaption" class="text-center text-white text-sm font-bold mt-4"></p>
    <p id="lbCounter" class="text-center text-slate-400 text-xs mt-1 font-mono"></p>
  </div>
</div>
```

---

## 4. Gestures, Keyboard Navigation & Focus Trap (A11y)

Zero-bloat vanilla JavaScript handling mobile swipe, desktop keyboard arrow navigation, and strict keyboard focus trapping:

```javascript
(function() {
  var galleryData = [];
  var activeIdx = 0;
  var modal = document.getElementById('lightbox');
  var img = document.getElementById('lbImg');
  var caption = document.getElementById('lbCaption');
  var counter = document.getElementById('lbCounter');
  var closeBtn = document.getElementById('lbClose');
  var prevBtn = document.getElementById('lbPrev');
  var nextBtn = document.getElementById('lbNext');

  // Collect all gallery items
  document.querySelectorAll('[data-gallery-src]').forEach(function(el, idx) {
    galleryData.push({
      src: el.getAttribute('data-gallery-src'),
      title: el.getAttribute('data-gallery-title') || el.getAttribute('alt') || ''
    });
    el.addEventListener('click', function(e) {
      e.preventDefault();
      openLightbox(idx);
    });
  });

  function openLightbox(idx) {
    activeIdx = idx;
    updateModal();
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }

  function closeLightbox() {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
  }

  function updateModal() {
    var item = galleryData[activeIdx];
    if (!item) return;
    img.style.opacity = '0';
    setTimeout(function() {
      img.src = item.src;
      img.alt = item.title;
      caption.textContent = item.title;
      counter.textContent = (activeIdx + 1) + ' / ' + galleryData.length;
      img.style.opacity = '1';
    }, 50);
  }

  function next() {
    activeIdx = (activeIdx + 1) % galleryData.length;
    updateModal();
  }

  function prev() {
    activeIdx = (activeIdx - 1 + galleryData.length) % galleryData.length;
    updateModal();
  }

  // Click handlers
  closeBtn.addEventListener('click', closeLightbox);
  prevBtn.addEventListener('click', prev);
  nextBtn.addEventListener('click', next);
  modal.addEventListener('click', function(e) {
    if (e.target === modal) closeLightbox();
  });

  // Keyboard navigation
  window.addEventListener('keydown', function(e) {
    if (modal.classList.contains('hidden')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') next();
    if (e.key === 'ArrowLeft') prev();
    
    // Focus Trap
    if (e.key === 'Tab') {
      var focusables = modal.querySelectorAll('button:not([disabled])');
      var first = focusables[0];
      var last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        last.focus();
        e.preventDefault();
      } else if (!e.shiftKey && document.activeElement === last) {
        first.focus();
        e.preventDefault();
      }
    }
  });

  // Mobile Touch Swipe
  var startX = 0;
  modal.addEventListener('touchstart', function(e) {
    startX = e.changedTouches[0].clientX;
  }, { passive: true });

  modal.addEventListener('touchend', function(e) {
    var diff = e.changedTouches[0].clientX - startX;
    if (Math.abs(diff) > 50) {
      if (diff < 0) next(); else prev();
    }
  }, { passive: true });
})();
```

---

## 5. Mixed Aspect-Ratio Responsive Certificate Grid

Render mixed portrait (3:4) and landscape (4:3) certificates cohesively without cropping critical signatures or stamps:

```html
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- Portrait Certificate (3:4) -->
  <figure class="group relative bg-slate-900 rounded-2xl overflow-hidden border border-white/5 hover:border-cyan-400/40 transition-all">
    <div class="aspect-[3/4] overflow-hidden bg-slate-950">
      <img src="/assets/cert-bnsp.jpg" alt="Sertifikat BNSP" data-gallery-src="/assets/cert-bnsp.jpg" data-gallery-title="Sertifikasi Nasional BNSP" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300 cursor-pointer" loading="lazy">
    </div>
    <figcaption class="p-4 text-center">
      <h4 class="text-sm font-bold text-white">BNSP Reparasi Ponsel</h4>
      <p class="text-xs text-slate-400 mt-0.5">Badan Nasional Sertifikasi Profesi</p>
    </figcaption>
  </figure>

  <!-- Landscape Certificate (4:3) - Spans 2 columns on tablet/desktop -->
  <figure class="group relative bg-slate-900 rounded-2xl overflow-hidden border border-white/5 hover:border-cyan-400/40 transition-all sm:col-span-2 lg:col-span-2">
    <div class="aspect-[16/10] overflow-hidden bg-slate-950">
      <img src="/assets/cert-bmy.jpg" alt="Sertifikat BMY Hardware" data-gallery-src="/assets/cert-bmy.jpg" data-gallery-title="Sertifikasi Hardware Motherboard BMY" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300 cursor-pointer" loading="lazy">
    </div>
    <figcaption class="p-4 text-center">
      <h4 class="text-sm font-bold text-white">BMY Hardware Laptop Motherboard</h4>
      <p class="text-xs text-slate-400 mt-0.5">Sertifikasi Analisis Sirkuit & Skematik Tingkat Lanjut</p>
    </figcaption>
  </figure>
</div>
```
