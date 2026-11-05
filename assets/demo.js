// Subvexa redesign demo — FULL demo shop logic. DEMO ONLY:
// no real API calls, no real payments, no real auth. Everything is
// client-side with localStorage and clearly fake SAMPLE data.
(function () {
  'use strict';

  // ---------- storage ----------
  var K = { cart: 'svdemo:cart', orders: 'svdemo:orders', user: 'svdemo:user',
            notify: 'svdemo:notify', overrides: 'svdemo:overrides',
            settings: 'svdemo:settings', prefs: 'svdemo:prefs' };
  var store = (typeof localStorage !== 'undefined') ? localStorage : null;
  var mem = {};
  function lsGet(k, d) {
    try {
      var raw = store ? store.getItem(k) : mem[k];
      return raw ? JSON.parse(raw) : d;
    } catch (e) { return d; }
  }
  function lsSet(k, v) {
    try {
      if (store) store.setItem(k, JSON.stringify(v)); else mem[k] = JSON.stringify(v);
    } catch (e) { /* demo: ignore storage errors */ }
  }

  // ---------- catalog (mirrors build.py) ----------
  function p(id, name, price, section, note, out, low) {
    return { id: id, name: name, price: price, section: section, note: note || '', out: !!out, low: low || 0 };
  }
  var CATALOG = [
    // AI & Tools (22)
    p('ai-adobe-express', 'Adobe Express Premium 12M', 0.70, 'ai-tools', 'Coupons · Auto delivery'),
    p('ai-autodesk', 'Autodesk Admin Panel 3000 Invites 3 Yr', 12.00, 'ai-tools', 'Auto delivery'),
    p('ai-capcut', 'Capcut Team 1M · 1200 credits', 2.20, 'ai-tools', 'Auto delivery'),
    p('ai-duolingo', 'Duolingo Super 12M', 0.70, 'ai-tools', 'Coupons · Auto delivery'),
    p('ai-elevenlabs', 'Elevenlabs Creator 3M', 10.00, 'ai-tools', 'Auto delivery'),
    p('ai-figma', 'Figma Pro Edu 2 Yr', 5.30, 'ai-tools', 'Auto delivery'),
    p('ai-framer', 'Framer Basic Plan 12M', 9.00, 'ai-tools', 'Auto delivery'),
    p('ai-gemini-12m', 'Gemini Plus 12m Links', 0.60, 'ai-tools', 'Auto delivery', false, 3),
    p('ai-jetbrains', 'JetBrains Edu Pack 12M', 4.50, 'ai-tools', 'Auto delivery'),
    p('ai-miro', 'Miro Edu Panel 100 Invites · Lifetime', 12.00, 'ai-tools', 'Auto delivery'),
    p('ai-claude-stable', 'Muse AI stable Account — 1B Tokens', 0.30, 'ai-tools', 'Auto delivery'),
    p('ai-notion-biz', 'Notion Business 3M Coupon', 0.80, 'ai-tools', 'Auto delivery'),
    p('ai-notion-plus', 'Notion Plus 12M', 3.00, 'ai-tools', 'Auto delivery'),
    p('ai-replit', 'Replit Core $40 Credits 1M', 4.50, 'ai-tools', 'Auto delivery'),
    p('ai-udemy', 'Udemy Personal Plan 1M', 1.70, 'ai-tools', 'Auto delivery'),
    p('ai-wispr', 'Wispr Flow Pro 2 Months', 0.30, 'ai-tools', 'Auto delivery'),
    p('ai-youtube-premium', 'YouTube Premium 3m', 1.40, 'ai-tools', 'Out of stock', true),
    p('ai-surfshark', 'Surfshark VPN 2M', 4.50, 'ai-tools', 'Out of stock', true),
    p('ai-chatgpt', 'ChatGPT Plus 1M', 5.10, 'ai-tools', 'Out of stock', true),
    p('ai-canva', 'Canva Pro Edu Panel 500 Invites', 4.20, 'ai-tools', 'Out of stock', true),
    p('ai-lovable-pro', 'Lovable Pro 10k Credits 2M', 37.00, 'ai-tools', 'Out of stock', true),
    p('ai-lovable-lite', 'Lovable Lite 12M', 6.50, 'ai-tools', 'Out of stock', true),
    p('ai-claude-30b', 'Muse AI Account — 30 Billion Tokens', 2.30, 'ai-tools', 'Out of stock', true),
    p('ai-gemini-3m', 'Gemini Plus 3m Links', 0.50, 'ai-tools', 'Out of stock', true),
    // Other Tools (13)
    p('ot-prime-1m', 'Amazon Prime Video 1M', 0.60, 'other-tools', 'Auto delivery'),
    p('ot-prime-6m', 'Amazon Prime Video 6M', 1.30, 'other-tools', 'Auto delivery'),
    p('ot-nord', 'Nord VPN 3M Accounts', 2.90, 'other-tools', 'Auto delivery'),
    p('ot-proton', 'Proton VPN 1 Month', 2.00, 'other-tools', 'Auto delivery'),
    p('ot-office', 'Microsoft Office 365 Plus 12M', 0.80, 'other-tools', 'Auto delivery'),
    p('ot-apple-music', 'Apple Music 5M Redeem Link', 0.80, 'other-tools', 'Auto delivery'),
    p('ot-ilovepdf', 'iLovePdf Premium 1 Yr', 1.20, 'other-tools', 'Auto delivery'),
    p('ot-linkedin-sales', 'LinkedIn Sales Navigator Core 2M', 1.50, 'other-tools', 'Auto delivery'),
    p('ot-linkedin-career', 'LinkedIn Career 3M', 1.10, 'other-tools', 'Auto delivery'),
    p('ot-crunchyroll', 'Crunchyroll 1 Month Link', 0.80, 'other-tools', 'Auto delivery'),
    p('ot-outlook', 'Outlook Mail', 0.10, 'other-tools', 'Auto delivery', false, 5),
    p('ot-youtube-premium', 'YouTube Premium 3-month Coupons', 1.40, 'other-tools', 'Out of stock', true),
    p('ot-surfshark', 'Surfshark VPN 2M Private Accounts', 4.50, 'other-tools', 'Out of stock', true),
    // Gift cards
    p('gc-steam-10', 'Steam Wallet — USA $10', 10.00, 'gift-cards', 'Gift card · Instant delivery'),
    p('gc-steam-25', 'Steam Wallet — USA $25', 25.00, 'gift-cards', 'Gift card · Instant delivery'),
    p('gc-steam-50', 'Steam Wallet — USA $50', 50.00, 'gift-cards', 'Gift card · Instant delivery'),
    p('gc-steam-100', 'Steam Wallet — USA $100', 100.00, 'gift-cards', 'Gift card · Instant delivery', false, 2),
    p('gc-psn-25', 'PlayStation Store — USA $25', 25.00, 'gift-cards', 'Gift card · Instant delivery'),
    p('gc-xbox-25', 'Xbox Live — USA $25', 25.00, 'gift-cards', 'Gift card · Instant delivery'),
    p('gc-pubg-600', 'PUBG Mobile UC 600', 9.99, 'gift-cards', 'Top-up · Instant delivery')
  ];
  var BRANDS = ['Steam', 'PlayStation', 'Xbox', 'Apple', 'Google Play', 'Amazon',
    'PUBG Mobile', 'Roblox', 'Netflix', 'Spotify', 'Nintendo', 'Razer Gold'];
  var SECTION_PAGE = { 'ai-tools': 'ai-tools.html', 'other-tools': 'other-tools.html', 'gift-cards': 'gift-cards.html' };
  var SECTION_LABEL = { 'ai-tools': 'AI & Tools', 'other-tools': 'Other Tools', 'gift-cards': 'Gift Cards' };

  function findProduct(id) {
    for (var i = 0; i < CATALOG.length; i++) if (CATALOG[i].id === id) return CATALOG[i];
    return null;
  }
  function getOverrides() { return lsGet(K.overrides, {}); }
  function effectiveProduct(prod) {
    var ov = getOverrides()[prod.id];
    if (!ov) return prod;
    var copy = {}; for (var k in prod) copy[k] = prod[k];
    if (typeof ov.price === 'number') copy.price = ov.price;
    if (typeof ov.out === 'boolean') copy.out = ov.out;
    return copy;
  }
  function fmt(n) { return '$' + (Math.round(n * 100) / 100).toFixed(2); }
  function money(n) { return (Math.round(n * 100) / 100).toFixed(2); }
  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // ---------- helpers: region, time, loyalty ----------
  var REGIONS = ['USA', 'Europe', 'KSA', 'UAE', 'India', 'Turkey', 'Hong Kong', 'Singapore'];
  function regionOf(item) {
    var name = item.name || '';
    for (var i = 0; i < REGIONS.length; i++) if (name.indexOf(REGIONS[i]) !== -1) return REGIONS[i];
    return 'Account / Global';
  }
  function stamp(d) {
    try { return d.toLocaleTimeString('en-GB', { hour12: false }); }
    catch (e) { return String(d); }
  }
  function stampOffset(base, sec) { return stamp(new Date(base.getTime() + sec * 1000)); }
  function loyaltyPoints() {
    return getOrders().filter(function (o) { return o.status === 'DELIVERED'; })
      .reduce(function (n, o) { return n + Math.round(o.total * 5); }, 0);
  }

  // ---------- demo codes / orders ----------
  var CODE_CHARS = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  function genCode() {
    var out = 'DEMO-';
    for (var g = 0; g < 3; g++) {
      for (var i = 0; i < 4; i++) out += CODE_CHARS[Math.floor(Math.random() * CODE_CHARS.length)];
      if (g < 2) out += '-';
    }
    return out;
  }
  function genOrderCode() {
    var d = new Date();
    var ymd = '' + d.getFullYear() + String(d.getMonth() + 1).padStart(2, '0') + String(d.getDate()).padStart(2, '0');
    return 'DG-' + ymd + '-' + Math.floor(1000 + Math.random() * 9000);
  }
  function deliveredItemsFor(items) {
    return items.map(function (it) {
      return { label: it.name + ' × ' + it.qty, code: genCode(), note: 'Demo sample code — not a real code' };
    });
  }
  function seedOrders() {
    var existing = lsGet(K.orders, null);
    if (existing) return existing;
    var seed = [
      { code: 'DG-STEAM-001', date: '5 Nov 2026', status: 'DELIVERED', method: 'USDT (BEP20)',
        tl: { ordered: '14:02:01', paid: '14:02:21', issued: '14:02:26', delivered: '14:02:31' },
        items: [{ id: 'gc-steam-50', name: 'Steam Wallet — USA $50', price: 50.00, qty: 1, section: 'gift-cards' }],
        total: 50.00, delivered: [{ label: 'Steam Wallet — USA $50', code: 'DEMO-7K2Q-9X4M-3P8W', note: 'Demo sample code — not a real code' }] },
      { code: 'DG-9441BD8ECC', date: '5 Nov 2026', status: 'DELIVERED', method: 'USDT (BEP20)',
        tl: { ordered: '10:49:03', paid: '10:49:24', issued: '10:49:29', delivered: '10:49:34' },
        items: [{ id: 'ot-outlook', name: 'Outlook Mail', price: 0.10, qty: 1, section: 'other-tools' }],
        total: 0.10, delivered: [{ label: 'Outlook Mail account', code: 'demo-account@example.com', note: 'Demo account — not real credentials' }] },
      { code: 'DG-20261105-002', date: '5 Nov 2026', status: 'AWAITING_PAYMENT', method: 'USDT (BEP20)',
        tl: { ordered: '15:20:00' },
        items: [{ id: 'ai-gemini-12m', name: 'Gemini Plus 12m Links', price: 0.60, qty: 1, section: 'ai-tools' }],
        total: 0.60, delivered: [] },
      { code: 'DG-20261104-009', date: '4 Nov 2026', status: 'FAILED', method: 'USDT (BEP20)',
        tl: { ordered: '09:11:00' },
        items: [{ id: 'ai-canva', name: 'Canva Pro Edu Panel 500 Invites', price: 4.20, qty: 1, section: 'ai-tools' }],
        total: 4.20, delivered: [], failReason: 'Demo: payment window expired before payment was confirmed.' }
    ];
    lsSet(K.orders, seed);
    return seed;
  }
  function getOrders() { return seedOrders(); }
  function saveOrders(o) { lsSet(K.orders, o); }
  function getUser() { return lsGet(K.user, null); }
  function getSettings() {
    var s = lsGet(K.settings, {});
    return { shopName: s.shopName || 'Subvexa', supportEmail: s.supportEmail || 'support@subvexa.shop',
             wallet: s.wallet || '0xDEMO7a1f3c9e5b2d8a4f6c0e1a2b3c4d5e6f7a8b',
             note: 'Demo wallet address — never send real funds here.' };
  }

  // ---------- cart ----------
  function getCart() { return lsGet(K.cart, []); }
  function saveCart(c) { lsSet(K.cart, c); updateCartCount(); }
  function cartCount() {
    return getCart().reduce(function (n, it) { return n + it.qty; }, 0);
  }
  function cartTotal() {
    return getCart().reduce(function (n, it) { return n + it.price * it.qty; }, 0);
  }
  function addToCart(id, qty) {
    var prod = effectiveProduct(findProduct(id) || {});
    if (!prod || !prod.id) return { ok: false, error: 'Unknown product (demo).' };
    if (prod.out) return { ok: false, error: prod.name + ' is out of stock — use Notify me instead (demo).' };
    qty = qty || 1;
    var cart = getCart(), found = false;
    cart.forEach(function (it) { if (it.id === id) { it.qty += qty; found = true; } });
    if (!found) cart.push({ id: prod.id, name: prod.name, price: prod.price, qty: qty, section: prod.section });
    saveCart(cart);
    return { ok: true, count: cartCount() };
  }
  function setQty(id, qty) {
    var cart = getCart().filter(function (it) { return it.id !== id || qty > 0; });
    cart.forEach(function (it) { if (it.id === id) it.qty = qty; });
    saveCart(cart.filter(function (it) { return it.qty > 0; }));
  }
  function removeFromCart(id) { saveCart(getCart().filter(function (it) { return it.id !== id; })); }
  function clearCart() { saveCart([]); }
  function updateCartCount() {
    if (typeof document === 'undefined') return;
    var el = document.getElementById('cart-count');
    if (el) el.textContent = String(cartCount());
  }

  // ---------- checkout / delivery ----------
  function createOrder(method) {
    var cart = getCart();
    if (!cart.length) return { ok: false, error: 'Your cart is empty (demo).' };
    var order = { code: genOrderCode(), date: new Date().toDateString(), status: 'AWAITING_PAYMENT',
      method: method || 'USDT (BEP20)', items: cart, total: cartTotal(), delivered: [],
      tl: { ordered: stamp(new Date()) } };
    var orders = getOrders(); orders.unshift(order); saveOrders(orders);
    clearCart();
    return { ok: true, order: order };
  }
  function markOrderDelivered(code) {
    var orders = getOrders(), done = null;
    orders.forEach(function (o) {
      if (o.code === code) {
        o.status = 'DELIVERED'; o.delivered = deliveredItemsFor(o.items);
        var now = new Date(); o.tl = o.tl || {};
        o.tl.paid = stampOffset(now, -10); o.tl.issued = stampOffset(now, -5); o.tl.delivered = stamp(now);
        done = o;
      }
    });
    if (done) saveOrders(orders);
    return done;
  }
  function fmtTime(sec) {
    var m = Math.floor(sec / 60), s = sec % 60;
    return String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
  }
  // Deterministic pseudo-QR pattern (demo placeholder, not a real QR code).
  function qrPattern(seedStr, size) {
    var h = 0;
    for (var i = 0; i < seedStr.length; i++) h = (h * 31 + seedStr.charCodeAt(i)) >>> 0;
    var cells = [];
    for (var y = 0; y < size; y++) for (var x = 0; x < size; x++) {
      var edge = x < 2 || y < 2 || x >= size - 2 || y >= size - 2;
      var v = ((h >> ((x * 7 + y * 13) % 24)) & 1) ^ ((x * y) % 3 === 0 ? 1 : 0);
      cells.push(edge ? 1 : v);
    }
    return cells;
  }

  function filterCatalog(q) {
    q = (q || '').toLowerCase().trim();
    if (!q) return CATALOG.slice();
    return CATALOG.filter(function (prod) {
      return (prod.name + ' ' + prod.section + ' ' + (SECTION_LABEL[prod.section] || '')).toLowerCase().indexOf(q) !== -1;
    }).concat(BRANDS.filter(function (b) { return b.toLowerCase().indexOf(q) !== -1; })
      .map(function (b) { return { id: 'brand-' + b.toLowerCase().replace(/[^a-z0-9]+/g, '-'), name: b + ' gift cards', price: null, section: 'gift-cards', note: 'Browse the brand page', brand: true }; }));
  }

  // ---------- modal ----------
  function openDemoModal(title, text) {
    if (typeof document === 'undefined') return;
    var t = document.getElementById('demo-modal-title'), b = document.getElementById('demo-modal-text');
    if (t) t.textContent = title;
    if (b) b.textContent = text;
    var m = document.getElementById('demo-modal'); if (m) m.classList.add('open');
  }
  function closeDemoModal() {
    if (typeof document === 'undefined') return;
    var m = document.getElementById('demo-modal'); if (m) m.classList.remove('open');
  }

  // ---------- page renderers (browser only) ----------
  function productCardHTML(prod, depth) {
    var pfx = depth === 1 ? '../' : '';
    var eff = effectiveProduct(prod);
    if (eff.out) {
      return '<div class="card out" data-pid="' + eff.id + '"><h3>' + esc(eff.name) + '</h3>' +
        '<div class="price">' + fmt(eff.price) + '</div><div class="tag">Currently out of stock</div>' +
        '<div class="buy"><button class="notify" data-notify="' + esc(eff.name) + '">🔔 Notify me</button></div></div>';
    }
    return '<div class="card" data-pid="' + eff.id + '"><div class="card-meta"><span class="pill-instant">⚡ Instant</span><span class="stars-sm">★★★★★</span></div><h3>' + esc(eff.name) + '</h3>' +
      '<div class="price">' + fmt(eff.price) + '</div>' +
      (eff.low ? '<div class="low-stock">⚡ Only ' + eff.low + ' left</div>' : '') +
      '<div class="tag">' + esc(eff.note || 'Auto delivery') + '</div>' +
      '<div class="buy"><button class="btn btn-green" data-add="' + eff.id + '">Add to cart</button> ' +
      '<button class="btn btn-ghost" data-buynow="' + eff.id + '">Buy now</button></div></div>';
  }
  function applyOverrides() {
    if (typeof document === 'undefined') return;
    var ov = getOverrides();
    document.querySelectorAll('[data-pid]').forEach(function (card) {
      var o = ov[card.getAttribute('data-pid')]; if (!o) return;
      var priceEl = card.querySelector('.price');
      if (typeof o.price === 'number' && priceEl) priceEl.textContent = fmt(o.price);
      if (o.out === true && !card.classList.contains('out')) {
        card.classList.add('out');
        var buy = card.querySelector('.buy');
        if (buy) buy.innerHTML = '<button class="notify" data-notify="' + esc(card.querySelector('h3').textContent) + '">🔔 Notify me</button>';
      }
      if (o.out === false && card.classList.contains('out')) { /* static out-of-stock stays as built */ }
    });
  }
  function statusClass(s) {
    return s === 'DELIVERED' ? 'delivered' : (s === 'AWAITING_PAYMENT' ? 'awaiting' : (s === 'FAILED' ? 'failed' : 'issued'));
  }
  function orderCardHTML(o, depth) {
    var pfx = depth === 1 ? '../' : '';
    var items = o.items.map(function (it) { return esc(it.name) + ' × ' + it.qty; }).join(', ');
    var head = '<div class="order" data-order="' + esc(o.code) + '"><div class="order-head"><div><strong>' +
      esc(o.items[0] ? o.items[0].name : 'Order') + (o.items.length > 1 ? ' +' + (o.items.length - 1) + ' more' : '') +
      '</strong><br><span class="tag">Order ' + esc(o.code) + ' · ' + esc(o.date) +
      ' · ' + esc(o.method) + '</span></div><span class="status ' + statusClass(o.status) + '">' + esc(o.status.replace('_', ' ')) + '</span></div>' +
      '<p>' + esc(items) + '</p><p>Total: <strong>' + fmt(o.total) + '</strong></p>';
    var body = '';
    if (o.status === 'DELIVERED') {
      body = o.delivered.map(function (d) {
        return '<div class="codebox"><span>' + esc(d.label) + ': <strong>' + esc(d.code) + '</strong><br><span style="font-size:12px;color:#94a3b8">' + esc(d.note || '') + '</span></span>' +
          '<button class="copybtn" data-copy="' + esc(d.code) + '">Copy</button></div>';
      }).join('') +
        '<p><button class="btn btn-ghost" data-resend="' + esc(o.code) + '">📧 Resend code</button> <span class="tag resend-note" id="resend-' + esc(o.code) + '"></span></p>' +
        '<p class="tag">Delivered items are shown only when the order is DELIVERED. Resend re-sends the demo delivery email (not actually sent).</p>';
    } else if (o.status === 'AWAITING_PAYMENT') {
      var page = SECTION_PAGE[o.items[0].section] || 'gift-cards.html';
      body = '<p class="tag">No items yet — they appear here only after payment is confirmed and the order is DELIVERED.</p>' +
        '<a class="btn btn-green" href="' + pfx + page + '">Resume — back to ' + esc(SECTION_LABEL[o.items[0].section] || 'shop') + ' →</a>';
    } else if (o.status === 'FAILED') {
      body = '<p class="tag">' + esc(o.failReason || 'This demo order failed.') + '</p>' +
        '<a class="btn btn-ghost" href="' + pfx + 'support.html">Contact support →</a>';
    }
    var tl = o.tl || {};
    var tracker = '<div class="tracker">' +
      '<span class="' + (o.status === 'FAILED' ? 'failed' : (tl.paid ? 'done' : '')) + '">Paid' + (tl.paid ? '<br><small>' + esc(tl.paid) + '</small>' : '<br><small>pending</small>') + '</span>' +
      '<span class="' + (o.status === 'DELIVERED' ? 'done' : '') + '">Code issued' + (tl.issued ? '<br><small>' + esc(tl.issued) + '</small>' : '<br><small>pending</small>') + '</span>' +
      '<span class="' + (o.status === 'DELIVERED' ? 'done' : '') + '">Delivered' + (tl.delivered ? '<br><small>' + esc(tl.delivered) + '</small>' : '<br><small>pending</small>') + '</span>' +
      '</div>';
    var timeline = '<details class="timeline"><summary>Order timeline</summary><ol>' +
      '<li>✅ Ordered — ' + esc(o.date) + (tl.ordered ? ' ' + esc(tl.ordered) : '') + '</li>' +
      (o.status === 'FAILED' ? '<li>❌ Payment not confirmed — order expired (demo)</li>'
        : '<li>' + (o.status === 'DELIVERED' ? '✅' : '⏳') + ' Payment ' + (o.status === 'DELIVERED' ? 'confirmed' + (tl.paid ? ' at ' + esc(tl.paid) : '') : 'awaiting confirmation') + '</li>' +
          '<li>' + (o.status === 'DELIVERED' ? '✅ Cards issued' + (tl.issued ? ' at ' + esc(tl.issued) : '') : '⏳ Cards being issued') + '</li>' +
          '<li>' + (o.status === 'DELIVERED' ? '✅ Delivered — Show Code' + (tl.delivered ? ' at ' + esc(tl.delivered) : '') + ' · delivered in ~30 seconds (demo)' : '⏳ Delivery pending') + '</li>') +
      '</ol></details>';
    return head + body + tracker + timeline + '</div>';
  }
  function renderOrders(rootId, filter) {
    var root = document.getElementById(rootId); if (!root) return;
    var orders = getOrders();
    var list = filter && filter !== 'all' ? orders.filter(function (o) { return o.status === filter; }) : orders;
    if (!list.length) { root.innerHTML = '<p class="tag">No orders in this view (demo).</p>'; return; }
    var depth = (window.location.pathname.indexOf('/admin/') !== -1) ? 1 : 0;
    root.innerHTML = list.map(function (o) { return orderCardHTML(o, depth); }).join('');
  }
  function renderCart() {
    var root = document.getElementById('cart-root'); if (!root) return;
    var cart = getCart();
    if (!cart.length) {
      root.innerHTML = '<div class="box"><h3 style="margin-top:0">Your cart is empty</h3><p>Add a gift card or tool from the shop, then come back here to check out. (Demo — nothing is charged.)</p><a class="btn btn-green" href="gift-cards.html">Browse gift cards →</a> <a class="btn btn-ghost" href="ai-tools.html">AI &amp; Tools →</a></div>';
      var t = document.getElementById('cart-total'); if (t) t.textContent = fmt(0);
      return;
    }
    root.innerHTML = cart.map(function (it) {
      return '<div class="order"><div class="order-head"><div><strong>' + esc(it.name) + '</strong><br><span class="tag">' +
        esc(SECTION_LABEL[it.section] || it.section) + ' · ' + fmt(it.price) + ' each</span></div><strong>' + fmt(it.price * it.qty) + '</strong></div>' +
        '<div class="qty"><button data-qtyminus="' + esc(it.id) + '">−</button><span>Qty: ' + it.qty + '</span><button data-qtyplus="' + esc(it.id) + '">+</button>' +
        '<button class="btn btn-ghost" data-remove="' + esc(it.id) + '">Remove</button></div></div>';
    }).join('');
    var tot = document.getElementById('cart-total'); if (tot) tot.textContent = fmt(cartTotal());
    var cnt = document.getElementById('cart-count-line'); if (cnt) cnt.textContent = cartCount() + ' item' + (cartCount() === 1 ? '' : 's');
  }
  function renderSearch() {
    var root = document.getElementById('search-results'); if (!root) return;
    var q = '';
    try { q = new URLSearchParams(window.location.search).get('q') || ''; } catch (e) { /* demo */ }
    var input = document.getElementById('search-page-input'); if (input) input.value = q;
    var results = filterCatalog(q);
    var title = document.getElementById('search-title');
    if (title) title.textContent = q ? ('Results for “' + q + '” — ' + results.length + ' found') : 'Search the demo catalog';
    root.innerHTML = results.length ? '<div class="grid">' + results.map(function (prod) {
      if (prod.brand) return '<div class="card"><h3>' + esc(prod.name) + '</h3><div class="tag">' + esc(prod.note) + '</div><div class="buy"><a class="btn btn-purple" href="gift-cards.html">Browse brand →</a></div></div>';
      return productCardHTML(prod, 0);
    }).join('') + '</div>' : '<p class="tag">No matches in the demo catalog. Try “Steam”, “VPN”, “Gemini” or “Outlook”.</p>';
  }
  // Region check + express consent (EU digital-goods rule) for checkout.
  function regionListHTML(cart) {
    return '<ul>' + cart.map(function (it) {
      return '<li>' + esc(it.name) + ' — region: <strong>' + esc(regionOf(it)) + '</strong></li>';
    }).join('') + '</ul>';
  }
  function updateRegionCheck() {
    if (typeof document === 'undefined') return;
    var sel = document.getElementById('region-check-select');
    var res = document.getElementById('region-check-result');
    if (!sel || !res) return;
    var picked = sel.value;
    if (!picked) { res.textContent = 'Pick your account region above to check for mismatches (demo).'; res.style.color = ''; return; }
    var warns = [];
    getCart().forEach(function (it) {
      var r = regionOf(it);
      if (r !== 'Account / Global' && r !== picked) warns.push(it.name + ' is a ' + r + ' code — it will not redeem on a ' + picked + ' account.');
    });
    if (warns.length) { res.innerHTML = '⚠️ ' + warns.map(esc).join('<br>⚠️ '); res.style.color = '#b45309'; }
    else { res.textContent = '✓ All regions match your ' + picked + ' account (demo check).'; res.style.color = '#047857'; }
  }
  function updatePayButton() {
    if (typeof document === 'undefined') return;
    var c = document.getElementById('consent-check'), a = document.getElementById('age-check'), b = document.getElementById('pay-now');
    if (b) b.disabled = !(c && c.checked && a && a.checked);
  }
  function renderCheckout() {
    var root = document.getElementById('checkout-root'); if (!root) return;
    var cart = getCart();
    var user = getUser();
    var settings = getSettings();
    if (!cart.length) {
      root.innerHTML = '<div class="box"><h3 style="margin-top:0">Nothing to check out yet</h3><p>Your demo cart is empty. Add a product first — out-of-stock items can never be checked out.</p><a class="btn btn-green" href="gift-cards.html">Browse gift cards →</a></div>';
      return;
    }
    var items = cart.map(function (it) {
      return '<tr><td>' + esc(it.name) + '</td><td>× ' + it.qty + '</td><td>' + fmt(it.price * it.qty) + '</td></tr>';
    }).join('');
    root.innerHTML =
      '<div class="box"><h3 style="margin-top:0">Step 1 · Your account (demo)</h3>' +
      (user ? '<p>Signed in as <strong>' + esc(user.name) + '</strong> (' + esc(user.email) + ') — demo account, stored only in this browser. <a href="account.html">Manage account →</a></p>'
        : '<p>No demo account yet. Continue as the demo user — no real sign-up happens.</p><button class="btn btn-purple" id="demo-signin">Continue as demo user</button>') +
      '</div>' +
      '<div class="box"><h3 style="margin-top:0">Step 2 · Review your order</h3><table><tr><th>Product</th><th>Qty</th><th>Total</th></tr>' + items +
      '</table><p style="margin-top:12px">Total: <strong id="checkout-total">' + fmt(cartTotal()) + '</strong> · Pay exactly this amount in USDT.</p></div>' +
      '<div class="box"><h3 style="margin-top:0">Step 2.5 · Region check (demo)</h3>' +
      '<p>Region mismatch is the #1 reason gift-card orders fail. Each item below shows the region it works on — make sure it matches your account:</p>' +
      regionListHTML(cart) +
      '<p><label>My account region<br><select id="region-check-select"><option value="">— Select your account region —</option><option>USA</option><option>Europe</option><option>KSA</option><option>UAE</option><option>India</option><option>Turkey</option><option>Hong Kong</option><option>Singapore</option></select></label></p>' +
      '<div id="region-check-result" class="tag">Pick your account region above to check for mismatches (demo).</div></div>' +
      '<div class="box"><h3 style="margin-top:0">Step 3 · Payment method (demo)</h3>' +
      '<label class="payopt"><input type="radio" name="paymethod" value="USDT (BEP20)" checked> <strong>USDT (BEP20)</strong> — demo, recommended</label>' +
      '<label class="payopt"><input type="radio" name="paymethod" value="USDT (TRC20)"> USDT (TRC20) — demo, not live</label>' +
      '<label class="payopt"><input type="radio" name="paymethod" value="Card (demo)"> Card — demo only, not live</label>' +
      '<p class="tag">Demo checkout: no real payment is taken and no funds move.</p>' +
      '<label class="payopt consent"><input type="checkbox" id="consent-check"> I agree to instant delivery and understand the code cannot be returned once revealed (demo — EU digital-content rule).</label>' +
      '<label class="payopt consent"><input type="checkbox" id="age-check"> I confirm I am 18 or older.</label>' +
      '<button class="btn btn-green" id="pay-now" disabled>Pay ' + fmt(cartTotal()) + ' (demo) →</button> <a class="btn btn-ghost" href="cart.html">← Back to cart</a></div>' +
      '<div class="box" id="pay-box" style="display:none"></div>' +
      '<div class="box" id="delivery-box" style="display:none"></div>';
    var signin = document.getElementById('demo-signin');
    if (signin) signin.addEventListener('click', function () {
      lsSet(K.user, { name: 'Demo User', email: 'demo@subvexa.shop', phone: '+91 90000 00000' });
      renderCheckout();
    });
    var payBtn = document.getElementById('pay-now');
    if (payBtn) payBtn.addEventListener('click', function () { startPayment(); });
    var consent = document.getElementById('consent-check');
    if (consent) consent.addEventListener('change', updatePayButton);
    var age = document.getElementById('age-check');
    if (age) age.addEventListener('change', updatePayButton);
    var regionSel = document.getElementById('region-check-select');
    if (regionSel) regionSel.addEventListener('change', updateRegionCheck);
    updatePayButton();
  }
  var payTimer = null;
  function startPayment() {
    if (typeof document !== 'undefined') {
      var c = document.getElementById('consent-check'), a = document.getElementById('age-check');
      if ((c && !c.checked) || (a && !a.checked)) {
        openDemoModal('Consent needed (demo)', 'Please tick both boxes — instant-delivery consent and the 18+ confirmation — before paying (demo).');
        return;
      }
    }
    var method = 'USDT (BEP20)';
    var sel = document.querySelector('input[name="paymethod"]:checked');
    if (sel) method = sel.value;
    var created = createOrder(method);
    if (!created.ok) { openDemoModal('Checkout — demo', created.error); return; }
    var order = created.order;
    var settings = getSettings();
    var box = document.getElementById('pay-box');
    if (!box) return;
    box.style.display = 'block';
    var cells = qrPattern(order.code + order.total, 21).map(function (v) {
      return '<i class="' + (v ? 'on' : '') + '"></i>';
    }).join('');
    box.innerHTML = '<h3 style="margin-top:0">Pay ' + fmt(order.total) + ' USDT (' + esc(method) + ') — demo</h3>' +
      '<p class="tag">Order ' + esc(order.code) + ' · Demo payment — do NOT send real funds. This wallet address and QR are fake demo placeholders.</p>' +
      '<div class="paygrid"><div><div class="qr" title="Demo QR placeholder — not a real payment code">' + cells + '</div>' +
      '<p class="tag">Demo QR placeholder (not scannable for a real payment).</p></div>' +
      '<div><p>Send exactly:</p><p class="big-amount">' + money(order.total) + ' USDT</p>' +
      '<p>To wallet (' + esc(method) + '):</p><div class="codebox"><span>' + esc(settings.wallet) + '</span>' +
      '<button class="copybtn" data-copy="' + esc(settings.wallet) + '">Copy</button></div>' +
      '<p>Time left: <strong id="pay-timer">30:00</strong></p>' +
      '<p class="tag">' + esc(settings.note) + '</p>' +
      '<button class="btn btn-green" id="i-paid">I have paid (demo)</button> ' +
      '<button class="btn btn-ghost" id="cancel-pay">Cancel</button></div></div>' +
      '<div class="progress" id="pay-progress" style="display:none"><span data-step="1">Validating payment</span><span data-step="2">Cards are being issued</span><span data-step="3">Show Code</span></div>';
    var secs = 30 * 60;
    var timerEl = document.getElementById('pay-timer');
    if (payTimer) clearInterval(payTimer);
    payTimer = setInterval(function () {
      secs -= 1;
      if (timerEl) timerEl.textContent = fmtTime(Math.max(secs, 0));
      if (secs <= 0) { clearInterval(payTimer); openDemoModal('Demo payment window ended', 'The 30-minute demo window ended. In the live shop an unpaid order expires. Start again from the cart (demo).'); }
    }, 1000);
    document.getElementById('i-paid').addEventListener('click', function () { confirmPaidDemo(order.code); });
    document.getElementById('cancel-pay').addEventListener('click', function () { box.style.display = 'none'; });
  }
  function confirmPaidDemo(code) {
    if (payTimer) clearInterval(payTimer);
    var prog = document.getElementById('pay-progress');
    if (prog) prog.style.display = 'flex';
    var steps = prog ? prog.querySelectorAll('span') : [];
    function mark(i) { if (steps[i]) steps[i].classList.add('done'); }
    setTimeout(function () { mark(0); }, 600);
    setTimeout(function () { mark(1); }, 1800);
    setTimeout(function () {
      mark(2);
      var order = markOrderDelivered(code);
      showDelivery(order);
    }, 3000);
  }
  function showDelivery(order) {
    var box = document.getElementById('delivery-box');
    if (!box || !order) return;
    box.style.display = 'block';
    var user = getUser() || { name: 'Demo User', email: 'demo@subvexa.shop' };
    var tl = order.tl || {};
    var tracker = '<div class="tracker">' +
      '<span class="done">Paid' + (tl.paid ? '<br><small>' + esc(tl.paid) + '</small>' : '') + '</span>' +
      '<span class="done">Code issued' + (tl.issued ? '<br><small>' + esc(tl.issued) + '</small>' : '') + '</span>' +
      '<span class="done">Delivered in ~30s' + (tl.delivered ? '<br><small>' + esc(tl.delivered) + '</small>' : '') + '</span>' +
      '</div>';
    var pts = Math.round(order.total * 5);
    box.innerHTML = '<h3 style="margin-top:0">✅ Delivered — order ' + esc(order.code) + '</h3>' +
      '<p>Your demo codes are below. They are SAMPLE codes — not real.</p>' +
      tracker +
      '<p class="tag">⏱️ Delivered in ~30 seconds after payment confirmation (demo).</p>' +
      order.delivered.map(function (d) {
        return '<div class="codebox"><span>' + esc(d.label) + ': <strong>' + esc(d.code) + '</strong></span>' +
          '<button class="copybtn" data-copy="' + esc(d.code) + '">Copy</button></div>';
      }).join('') +
      '<p class="tag">🎁 You earned <strong>' + pts + ' demo Subvexa Rewards points</strong> (5% back, demo) — see your balance in <a href="account.html">My Account</a>.</p>' +
      '<h4>📧 Email preview (demo)</h4><div class="email-preview"><p><strong>From:</strong> Subvexa &lt;support@subvexa.shop&gt;<br>' +
      '<strong>To:</strong> ' + esc(user.email) + '<br><strong>Subject:</strong> Your Subvexa order ' + esc(order.code) + ' is delivered</p>' +
      '<p>Hi ' + esc(user.name) + ',</p><p>Your order ' + esc(order.code) + ' (' + fmt(order.total) + ') is delivered. ' +
      'Your code(s) are in <a href="my-orders.html">My Orders</a> — click Show Code, copy and redeem.</p>' +
      '<p>— Subvexa (demo email, not actually sent)</p></div>' +
      '<p><a class="btn btn-purple" href="my-orders.html">See it in My Orders →</a> <a class="btn btn-ghost" href="gift-cards.html">Continue shopping →</a></p>';
    box.scrollIntoView();
  }

  // ---------- admin ----------
  function renderAdminStats() {
    var root = document.getElementById('admin-stats'); if (!root) return;
    var orders = getOrders();
    var delivered = orders.filter(function (o) { return o.status === 'DELIVERED'; });
    var revenue = delivered.reduce(function (n, o) { return n + o.total; }, 0);
    var today = orders.filter(function (o) { return (o.date || '').indexOf('Nov 2026') !== -1 || (o.date || '').indexOf(new Date().getFullYear()) !== -1; }).length;
    var rate = orders.length ? Math.round(delivered.length / orders.length * 100) : 0;
    root.innerHTML =
      '<div class="stat"><b>' + fmt(revenue) + '</b><span>demo revenue (delivered)</span></div>' +
      '<div class="stat"><b>' + orders.length + '</b><span>total demo orders</span></div>' +
      '<div class="stat"><b>' + today + '</b><span>orders (this period)</span></div>' +
      '<div class="stat"><b>' + rate + '%</b><span>delivered rate</span></div>';
  }
  function renderAdminOrders() {
    var root = document.getElementById('admin-orders-root'); if (!root) return;
    var filter = root.getAttribute('data-filter') || 'all';
    var orders = getOrders();
    var list = filter === 'all' ? orders : orders.filter(function (o) { return o.status === filter; });
    if (!list.length) { root.innerHTML = '<p class="tag">No demo orders with this status.</p>'; return; }
    root.innerHTML = '<table><tr><th>Order</th><th>Items</th><th>Total</th><th>Status</th><th>Action</th></tr>' +
      list.map(function (o) {
        return '<tr><td><strong>' + esc(o.code) + '</strong><br><span class="tag">' + esc(o.date) + '</span></td>' +
          '<td>' + esc(o.items.map(function (i) { return i.name; }).join(', ')) + '</td>' +
          '<td>' + fmt(o.total) + '</td><td><span class="status ' + statusClass(o.status) + '">' + esc(o.status.replace('_', ' ')) + '</span></td>' +
          '<td>' + (o.status === 'AWAITING_PAYMENT' ? '<button class="btn btn-green" data-mark-delivered="' + esc(o.code) + '">Mark delivered (demo)</button>' : '<span class="tag">—</span>') + '</td></tr>';
      }).join('') + '</table><p class="tag">Demo admin: marking delivered creates sample codes, exactly like the demo checkout does.</p>';
  }
  function renderAdminProducts() {
    var root = document.getElementById('admin-products-root'); if (!root) return;
    var ov = getOverrides();
    root.innerHTML = '<table><tr><th>Product</th><th>Section</th><th>Price (USD)</th><th>Stock</th><th></th></tr>' +
      CATALOG.map(function (prod) {
        var eff = effectiveProduct(prod);
        return '<tr data-pid="' + eff.id + '"><td>' + esc(eff.name) + '</td><td>' + esc(SECTION_LABEL[eff.section]) + '</td>' +
          '<td><input type="number" step="0.10" min="0" value="' + eff.price.toFixed(2) + '" data-price-input="' + eff.id + '" style="width:90px"></td>' +
          '<td><select data-stock-select="' + eff.id + '"><option value="in"' + (eff.out ? '' : ' selected') + '>In stock</option>' +
          '<option value="out"' + (eff.out ? ' selected' : '') + '>Out of stock</option></select></td>' +
          '<td><button class="btn btn-purple" data-save-product="' + eff.id + '">Save (demo)</button></td></tr>';
      }).join('') + '</table><p class="tag">Demo admin: price and stock edits are stored only in this browser (localStorage) and are picked up by the shop pages on their next load.</p>';
  }
  function renderAccount() {
    var root = document.getElementById('account-root'); if (!root) return;
    var user = getUser() || { name: 'Demo User', email: 'demo@subvexa.shop', phone: '' };
    var prefs = lsGet(K.prefs, { email: true, sms: false, offers: true });
    root.innerHTML =
      '<div class="box loyalty"><h3 style="margin-top:0">🎁 Subvexa Rewards (demo)</h3>' +
      '<p>Your demo points balance: <strong>' + loyaltyPoints() + ' points</strong> — you earn 5% back on every delivered order. 100 points = $1 off your next order (demo). Points are stored only in this browser.</p></div>' +
      '<div class="box"><h3 style="margin-top:0">Profile (demo)</h3>' +
      '<p><label>Name<br><input id="acc-name" value="' + esc(user.name) + '"></label></p>' +
      '<p><label>Email<br><input id="acc-email" value="' + esc(user.email) + '"></label></p>' +
      '<p><label>Phone<br><input id="acc-phone" value="' + esc(user.phone || '') + '" placeholder="+91 ..."></label></p>' +
      '<button class="btn btn-purple" id="acc-save">Save profile (demo)</button> <a class="btn btn-ghost" href="my-orders.html">Order history →</a></div>' +
      '<div class="box"><h3 style="margin-top:0">Notification preferences (demo)</h3>' +
      '<label class="payopt"><input type="checkbox" id="pref-email"' + (prefs.email ? ' checked' : '') + '> Order &amp; delivery emails</label>' +
      '<label class="payopt"><input type="checkbox" id="pref-sms"' + (prefs.sms ? ' checked' : '') + '> SMS updates</label>' +
      '<label class="payopt"><input type="checkbox" id="pref-offers"' + (prefs.offers ? ' checked' : '') + '> Offers &amp; price drops</label>' +
      '<button class="btn btn-purple" id="pref-save">Save preferences (demo)</button></div>' +
      '<div class="box"><h3 style="margin-top:0">Demo account</h3><p class="tag">This is a demo account stored only in this browser. Nothing is sent to a server. <a href="login.html">Sign in as a different demo user →</a></p>' +
      '<button class="btn btn-ghost" id="acc-logout">Log out (demo)</button></div>';
    document.getElementById('acc-save').addEventListener('click', function () {
      lsSet(K.user, { name: document.getElementById('acc-name').value || 'Demo User',
        email: document.getElementById('acc-email').value || 'demo@subvexa.shop',
        phone: document.getElementById('acc-phone').value || '' });
      openDemoModal('Saved (demo)', 'Profile saved in this browser only.');
    });
    document.getElementById('pref-save').addEventListener('click', function () {
      lsSet(K.prefs, { email: document.getElementById('pref-email').checked,
        sms: document.getElementById('pref-sms').checked, offers: document.getElementById('pref-offers').checked });
      openDemoModal('Saved (demo)', 'Notification preferences saved in this browser only.');
    });
    document.getElementById('acc-logout').addEventListener('click', function () {
      lsSet(K.user, null); window.location.href = 'login.html';
    });
  }

  // ---------- init (browser only) ----------
  function init() {
    if (typeof document === 'undefined') return;
    updateCartCount();
    applyOverrides();
    // Loyalty balance on the homepage strip (demo).
    var lb = document.getElementById('loyalty-balance');
    if (lb) lb.textContent = loyaltyPoints() + ' points';
    // Steam region checker (demo): highlight the matching region card.
    var regionSel = document.getElementById('region-select');
    if (regionSel) {
      regionSel.addEventListener('change', function () {
        var picked = regionSel.value;
        var res = document.getElementById('region-result');
        document.querySelectorAll('#main-grid [data-region]').forEach(function (card) {
          var r = card.getAttribute('data-region');
          if (!picked) { card.classList.remove('region-match'); card.classList.remove('region-dim'); return; }
          if (r === picked) { card.classList.add('region-match'); card.classList.remove('region-dim'); }
          else { card.classList.add('region-dim'); card.classList.remove('region-match'); }
        });
        if (res) res.textContent = picked ? ('✓ ' + picked + ' highlighted — buy the ' + picked + ' card for a ' + picked + ' Steam account (demo).') : 'Select your Steam account country to highlight the matching region.';
      });
    }
    // 24/7 support chat widget (demo — canned bot replies, nothing leaves the browser).
    var chatFab = document.getElementById('chat-fab');
    var chatPanel = document.getElementById('chat-panel');
    function chatToggle(show) { if (chatPanel) chatPanel.style.display = show ? 'block' : 'none'; }
    if (chatFab) chatFab.addEventListener('click', function () { chatToggle(!chatPanel || chatPanel.style.display === 'none'); });
    var chatClose = document.getElementById('chat-close');
    if (chatClose) chatClose.addEventListener('click', function () { chatToggle(false); });
    function chatReply(q) {
      var s = (q || '').toLowerCase();
      if (s.indexOf('deliver') !== -1 || s.indexOf('code') !== -1) return 'Demo answer: codes are delivered in ~30 seconds after payment — check My Orders and click Show Code. If nothing arrives in 30 minutes, email support@subvexa.shop with your order number.';
      if (s.indexOf('refund') !== -1) return 'Demo answer: if you paid but no code was delivered, you can get a refund. After a valid code is delivered, change-of-mind returns are not accepted — see the Return Policy.';
      if (s.indexOf('region') !== -1) return 'Demo answer: buy the region that matches your account — a USA code only works on a USA account. Use the region checker on the Steam page.';
      if (s.indexOf('pay') !== -1 || s.indexOf('usdt') !== -1 || s.indexOf('price') !== -1) return 'Demo answer: this demo accepts USDT (BEP20) only, and no real payment is taken. Pay the exact amount shown at checkout.';
      return 'Demo answer: I can help with delivery, refunds, regions and payments. For anything else, email support@subvexa.shop (demo chat — no human replies).';
    }
    var chatSend = document.getElementById('chat-send');
    var chatText = document.getElementById('chat-text');
    function chatSubmit() {
      if (!chatText || !chatText.value.trim()) return;
      var body = document.getElementById('chat-body');
      var q = chatText.value.trim(); chatText.value = '';
      if (body) {
        body.innerHTML += '<p class="chat-msg user">' + esc(q) + '</p>';
        body.innerHTML += '<p class="chat-msg bot">' + esc(chatReply(q)) + '</p>';
        body.scrollTop = body.scrollHeight;
      }
    }
    if (chatSend) chatSend.addEventListener('click', chatSubmit);
    if (chatText) chatText.addEventListener('keydown', function (e) { if (e.key === 'Enter') chatSubmit(); });
    renderCart();
    renderSearch();
    renderCheckout();
    renderAccount();
    renderAdminStats();
    renderAdminOrders();
    renderAdminProducts();
    var ordersRoot = document.getElementById('orders-root');
    if (ordersRoot) renderOrders('orders-root', 'all');
    document.querySelectorAll('[data-order-filter]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        document.querySelectorAll('[data-order-filter]').forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        renderOrders('orders-root', btn.getAttribute('data-order-filter'));
      });
    });
    document.querySelectorAll('[data-admin-order-filter]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        document.querySelectorAll('[data-admin-order-filter]').forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var root = document.getElementById('admin-orders-root');
        if (root) { root.setAttribute('data-filter', btn.getAttribute('data-admin-order-filter')); renderAdminOrders(); }
      });
    });
    // Search box in header: Enter goes to the search page.
    var siteSearch = document.getElementById('site-search');
    if (siteSearch) {
      siteSearch.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') {
          e.preventDefault();
          var depth = (window.location.pathname.indexOf('/admin/') !== -1 || window.location.pathname.indexOf('/blog/') !== -1 || window.location.pathname.indexOf('/brand/') !== -1) ? '../' : '';
          window.location.href = depth + 'search.html?q=' + encodeURIComponent(siteSearch.value);
        }
      });
    }
    // Login form (demo)
    var loginForm = document.getElementById('login-form');
    if (loginForm) {
      loginForm.addEventListener('submit', function (e) {
        e.preventDefault();
        var email = (document.getElementById('login-email') || {}).value || 'demo@subvexa.shop';
        var name = (document.getElementById('login-name') || {}).value || 'Demo User';
        lsSet(K.user, { name: name, email: email, phone: '' });
        openDemoModal('Signed in (demo)', 'Welcome, ' + name + '! This is a demo account stored only in this browser.');
        setTimeout(function () { window.location.href = 'account.html'; }, 900);
      });
    }
    // Admin settings form (demo)
    var settingsForm = document.getElementById('settings-form');
    if (settingsForm) {
      var s = getSettings();
      var sn = document.getElementById('set-shop'); if (sn) sn.value = s.shopName;
      var se = document.getElementById('set-email'); if (se) se.value = s.supportEmail;
      var sw = document.getElementById('set-wallet'); if (sw) sw.value = s.wallet;
      settingsForm.addEventListener('submit', function (e) {
        e.preventDefault();
        lsSet(K.settings, { shopName: document.getElementById('set-shop').value || 'Subvexa',
          supportEmail: document.getElementById('set-email').value || 'support@subvexa.shop',
          wallet: document.getElementById('set-wallet').value || s.wallet });
        openDemoModal('Saved (demo)', 'Admin settings saved in this browser only.');
      });
      var reset = document.getElementById('reset-demo');
      if (reset) reset.addEventListener('click', function () {
        Object.keys(K).forEach(function (k) { try { if (store) store.removeItem(K[k]); else delete mem[K[k]]; } catch (e) {} });
        openDemoModal('Demo reset', 'All demo data (cart, orders, account, admin edits) was cleared in this browser.');
        setTimeout(function () { window.location.href = '../index.html'; }, 900);
      });
    }
    // Click delegation
    document.addEventListener('click', function (e) {
      var t;
      if ((t = e.target.closest('[data-demo-buy]'))) {
        e.preventDefault();
        openDemoModal('Demo only — no payment', 'This is a design demo of the redesigned Subvexa shop. No order is created and no payment is taken. Product: ' + t.getAttribute('data-demo-buy'));
        return;
      }
      if ((t = e.target.closest('[data-add]'))) {
        e.preventDefault();
        var r = addToCart(t.getAttribute('data-add'), 1);
        if (r.ok) { openDemoModal('Added to cart (demo)', 'Added to your demo cart. Cart now has ' + r.count + ' item(s).'); renderCart(); }
        else openDemoModal('Cannot add (demo)', r.error);
        return;
      }
      if ((t = e.target.closest('[data-buynow]'))) {
        e.preventDefault();
        var r2 = addToCart(t.getAttribute('data-buynow'), 1);
        if (!r2.ok) { openDemoModal('Cannot buy (demo)', r2.error); return; }
        var depth2 = (window.location.pathname.indexOf('/admin/') !== -1 || window.location.pathname.indexOf('/blog/') !== -1 || window.location.pathname.indexOf('/brand/') !== -1) ? '../' : '';
        window.location.href = depth2 + 'checkout.html';
        return;
      }
      if ((t = e.target.closest('[data-notify]'))) {
        e.preventDefault();
        var list = lsGet(K.notify, []);
        var nm = t.getAttribute('data-notify');
        if (list.indexOf(nm) === -1) list.push(nm);
        lsSet(K.notify, list);
        openDemoModal('Notify me — demo', 'Thanks! In the live shop you would get an email as soon as ' + nm + ' is back in stock. This demo only saves it in this browser.');
        return;
      }
      if ((t = e.target.closest('[data-resend]'))) {
        var note = document.getElementById('resend-' + t.getAttribute('data-resend'));
        if (note) note.textContent = 'Demo email resent just now — check your inbox (demo, not actually sent).';
        openDemoModal('Code resent (demo)', 'A demo copy of the delivery email was “resent”. Nothing was actually emailed.');
        return;
      }
      if ((t = e.target.closest('[data-copy]'))) {
        var v = t.getAttribute('data-copy');
        if (navigator.clipboard) { navigator.clipboard.writeText(v); }
        t.textContent = 'Copied ✓';
        setTimeout(function () { t.textContent = 'Copy'; }, 1500);
        return;
      }
      if ((t = e.target.closest('[data-show-code]'))) {
        e.preventDefault();
        var box = document.getElementById(t.getAttribute('data-show-code'));
        if (box) { box.style.display = box.style.display === 'none' ? 'flex' : 'none'; }
        return;
      }
      if ((t = e.target.closest('[data-qtyplus]'))) { setQty(t.getAttribute('data-qtyplus'), (getCart().find(function (i) { return i.id === t.getAttribute('data-qtyplus'); }) || { qty: 0 }).qty + 1); renderCart(); return; }
      if ((t = e.target.closest('[data-qtyminus]'))) { setQty(t.getAttribute('data-qtyminus'), (getCart().find(function (i) { return i.id === t.getAttribute('data-qtyminus'); }) || { qty: 1 }).qty - 1); renderCart(); return; }
      if ((t = e.target.closest('[data-remove]'))) { removeFromCart(t.getAttribute('data-remove')); renderCart(); return; }
      if ((t = e.target.closest('[data-mark-delivered]'))) {
        var done = markOrderDelivered(t.getAttribute('data-mark-delivered'));
        if (done) { openDemoModal('Delivered (demo)', 'Order ' + done.code + ' is now DELIVERED with sample codes.'); renderAdminOrders(); renderAdminStats(); }
        return;
      }
      if ((t = e.target.closest('[data-save-product]'))) {
        var id = t.getAttribute('data-save-product');
        var priceInput = document.querySelector('[data-price-input="' + id + '"]');
        var stockSel = document.querySelector('[data-stock-select="' + id + '"]');
        var ov = getOverrides();
        ov[id] = { price: parseFloat(priceInput.value), out: stockSel.value === 'out' };
        lsSet(K.overrides, ov);
        openDemoModal('Saved (demo)', 'Product settings saved in this browser. Shop pages pick them up on next load.');
        return;
      }
      if (e.target.closest('#demo-modal')) { /* backdrop click closes */ }
    });
    document.getElementById('demo-modal').addEventListener('click', function (e) {
      if (e.target.id === 'demo-modal') closeDemoModal();
    });
  }

  function filterCards(inputId, gridId) {
    if (typeof document === 'undefined') return;
    var el = document.getElementById(inputId); if (!el) return;
    var q = (el.value || '').toLowerCase();
    document.querySelectorAll('#' + gridId + ' .card').forEach(function (card) {
      card.style.display = card.textContent.toLowerCase().indexOf(q) !== -1 ? '' : 'none';
    });
  }
  function filterBy(btn, cat) {
    if (typeof document === 'undefined') return;
    document.querySelectorAll('.filters button').forEach(function (b) { b.classList.remove('active'); });
    btn.classList.add('active');
    document.querySelectorAll('#pay-grid .card').forEach(function (card) {
      card.style.display = (cat === 'all' || card.getAttribute('data-cat') === cat) ? '' : 'none';
    });
  }

  // Testable API
  var API = { CATALOG: CATALOG, BRANDS: BRANDS, getCart: getCart, addToCart: addToCart,
    setQty: setQty, removeFromCart: removeFromCart, clearCart: clearCart, cartTotal: cartTotal,
    cartCount: cartCount, createOrder: createOrder, markOrderDelivered: markOrderDelivered,
    getOrders: getOrders, seedOrders: seedOrders, filterCatalog: filterCatalog, genCode: genCode,
    fmtTime: fmtTime, qrPattern: qrPattern, effectiveProduct: effectiveProduct,
    getOverrides: getOverrides, fmt: fmt, getUser: getUser, getSettings: getSettings,
    regionOf: regionOf, loyaltyPoints: loyaltyPoints, stamp: stamp, productCardHTML: productCardHTML,
    _lsGet: lsGet, _lsSet: lsSet, _K: K };
  if (typeof module !== 'undefined' && module.exports) { module.exports = API; }
  if (typeof globalThis !== 'undefined') { globalThis.SVDemo = API; }
  if (typeof window !== 'undefined') { window.SVDemo = API; window.filterCards = filterCards; window.filterBy = filterBy; window.closeDemoModal = closeDemoModal; }
  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
    else init();
  }
})();
