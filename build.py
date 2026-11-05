#!/usr/bin/env python3
"""Build the Subvexa redesign demo (static HTML, demo only)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def asset(rel):
    return ("assets/" + rel) if not rel.startswith("../") else rel

def header(active, depth=0):
    p = "" if depth == 0 else "../"
    nav = [
        ("index.html", "Home"), ("gift-cards.html", "Gift Cards"),
        ("tools.html", "Tools"),
        ("my-orders.html", "My Orders"), ("how-to-buy.html", "Help & Support"),
        ("cart.html", "🛒 Cart"), ("search.html", "Search"),
        ("support.html", "Support"), ("admin/index.html", "Admin"),
    ]
    links = "".join(
        f'<a href="{p}{href}" class="{"active" if href == active else ""}">{label}</a>'
        for href, label in nav)
    return f'''<div class="demo-bar">DEMO REDESIGN — not the live shop<span>Preview only</span></div>
<div class="announce"><div class="announce-inner"><span>&#10022; Explore digital gift cards from global brands</span><span>Secure account access &middot; Customer support</span></div></div>
<header class="site"><div class="head">
<a class="brand" href="{p}index.html"><img src="{p}assets/logo.png" alt="Subvexa logo"><span>subvexa<em>.</em></span></a>
<div class="search"><input id="site-search" type="search" placeholder="Search gift cards, brands, tools&hellip;" oninput="filterCards('site-search','main-grid')"><button onclick="filterCards('site-search','main-grid')">Search</button></div>
<a class="account" href="{p}account.html">Account</a>
<a class="cart-link" href="{p}cart.html">🛒 Cart <span class="cart-count" id="cart-count">0</span></a>
</div></header>
<nav class="site"><div class="nav">{links}</div></nav>
<div class="info"><div class="info-inner"><span>&#128274; Secure checkout</span><span>&#9889; Instant digital delivery</span><span>&#128172; Support: support@subvexa.shop</span><span>&#127760; Pay with cryptocurrency (USDT)</span></div></div>'''

TRUST = '''<div class="trust"><div><strong>500+ gift cards</strong> &middot; <strong>50,000+ happy customers</strong> &middot; <strong>4.2/5 on Trustpilot</strong></div><div class="badges"><span class="badge">🔒 128-bit SSL secure</span><span class="badge blue">🛡️ PCI DSS compliant</span><span class="badge purple">💬 WhatsApp &amp; Telegram support</span><span class="badge">✉️ support@subvexa.shop</span></div></div>'''

# Real-site learnings (Eneba / Dundle / SEAGM): region mismatch is the #1
# dispute cause; buyer protection + reviews are the trust moat.
def region_warn(p=""):
    return f'''<div class="box warn region-warn"><h3 style="margin-top:0">⚠️ Region check — the #1 reason orders go wrong</h3><p>Buy the region that matches your account. A <strong>USA</strong> code only works on a <strong>USA</strong> account — a USA code will <strong>not</strong> redeem on a KSA, Europe or India account. Check the flag badge and the region on the card before you pay. Delivered codes cannot be refunded or exchanged.</p><p><a class="btn btn-ghost" href="{p}blog/steam-region-guide.html">Read the region guide →</a></p></div>'''

REGION_WARN_TOOLS = '''<div class="box warn region-warn"><h3 style="margin-top:0">⚠️ Before you buy — check region &amp; redemption</h3><p>Some tools are tied to an account region or a specific redemption method. Check the product note, the redemption requirements and the expiry before you pay. Delivered accounts and codes cannot be refunded or exchanged — see the <a href="blog/check-before-you-buy.html">pre-purchase checklist</a>.</p></div>'''

PROTECT = '''<div class="protect"><span class="protect-title">🛡️ Buyer Protection</span><span>✅ Activation guarantee — replace or refund if a code won&apos;t activate</span><span>↩️ Unviewed-code refund</span><span>🔒 Escrow-style hold — payment held until delivery is confirmed</span></div>'''

REVIEWS = '''<div class="reviews"><div class="reviews-head"><strong>★★★★★ 4.2/5 on Trustpilot</strong><span class="tag">Demo reviews — sample feedback shown for design; not real Trustpilot data.</span></div><div class="review-grid">
<div class="review-card"><div class="stars">★★★★★</div><p>“Steam $50 code arrived in about 30 seconds. Show Code worked first try.”</p><p class="tag">Rahul · India · Steam Wallet $50</p></div>
<div class="review-card"><div class="stars">★★★★★</div><p>“Almost bought the wrong region — the region checker caught it before I paid.”</p><p class="tag">Marta · Spain · Steam Europe €50</p></div>
<div class="review-card"><div class="stars">★★★★☆</div><p>“Outlook Mail for $0.10, delivered instantly to my account. Will buy again.”</p><p class="tag">Ken · Singapore · Outlook Mail</p></div>
</div></div>'''

LOYALTY = '''<div class="loyalty"><div><strong>🎁 Subvexa Rewards (demo)</strong> — earn <strong>5% back in demo points</strong> on every delivered order. 100 points = $1 off your next order (demo).</div><div>Your demo balance: <strong id="loyalty-balance">…</strong> · <a href="account.html">See rewards →</a></div></div>'''

def footer(depth=0):
    p = "" if depth == 0 else "../"
    return f'''<footer class="site"><div class="foot">
<div><h4>subvexa.</h4><p style="font-size:14px">Buy Gift Cards with Cryptocurrency | Subvexa</p><p style="font-size:14px">Digital gift cards, AI tools and more &mdash; delivered instantly by email and in your account.</p></div>
<div><h4>Shop</h4><a href="{p}gift-cards.html">Gift Cards</a><a href="{p}tools.html">Tools (37 products)</a><a href="{p}brand/steam.html">Steam Gift Cards</a><a href="{p}payment-methods.html">Payment Methods</a><a href="{p}cart.html">Cart</a><a href="{p}search.html">Search</a></div>
<div><h4>Help</h4><a href="{p}how-to-buy.html">How to Buy</a><a href="{p}my-orders.html">My Orders</a><a href="{p}support.html">Support &amp; FAQ</a><a href="{p}help.html">Help Center</a><a href="{p}account.html">My Account</a><a href="{p}login.html">Sign In (demo)</a><a href="{p}blog.html">Blog</a><a href="{p}blog/steam-region-guide.html">Steam Region Guide</a><a href="{p}terms.html">Terms &amp; Conditions</a></div>
<div><h4>Legal</h4><a href="{p}terms.html">Terms &amp; Conditions</a><a href="{p}privacy.html">Privacy Policy</a><a href="{p}returns.html">Return Policy</a><a href="{p}payment-methods.html">Payment Methods</a><a href="{p}how-to-buy.html">How to Buy</a><a href="{p}admin/index.html">Admin Panel (demo)</a></div>
</div><div class="foot-bottom">&copy; Subvexa &middot; Independent digital marketplace &middot; Availability and final pricing verified before payment &middot; Support: support@subvexa.shop</div></footer>
<button class="chat-fab" id="chat-fab">💬 24/7 Support</button>
<div class="chat-panel" id="chat-panel" style="display:none">
<div class="chat-head"><strong>Subvexa Support — demo chat</strong><span class="tag">24/7 · demo</span><button id="chat-close" class="chat-x">✕</button></div>
<div class="chat-body" id="chat-body"><p class="chat-msg bot">Hi! I&apos;m the demo support bot. Ask me about delivery, refunds, regions or payments — or email support@subvexa.shop.</p></div>
<div class="chat-input"><input id="chat-text" type="text" placeholder="Type your question… (demo)"><button id="chat-send" class="btn btn-purple">Send</button></div>
<p class="tag" style="padding:0 14px 12px;margin:0">Demo chat — no human replies; nothing leaves this browser.</p>
</div>
<div class="modal-back" id="demo-modal"><div class="modal"><h3 id="demo-modal-title">Demo</h3><p id="demo-modal-text"></p><button class="btn btn-purple" onclick="closeDemoModal()">Got it</button></div></div>'''

def page(title, active, body, depth=0):
    p = "" if depth == 0 else "../"
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Subvexa</title><link rel="stylesheet" href="{p}assets/style.css"></head>
<body>{header(active, depth)}
<main class="wrap" id="main-grid">{body}</main>
{footer(depth)}
<script src="{p}assets/demo.js"></script></body></html>'''

def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", rel, len(html), "bytes")

def pid_for(name):
    return PRODUCT_IDS.get(name) or ("prod-" + "".join(c if c.isalnum() else "-" for c in name.lower()).strip("-")[:40])

# Demo low-stock counts (real-site learning: "Only X left" urgency + stock honesty).
LOW_STOCK = {"ai-gemini-12m": 3, "ot-outlook": 5, "gc-steam-100": 2}

def buy_card(name, price, note="", out=False, notify_name=None):
    pid = pid_for(name)
    low = "" if out else (f'<div class="low-stock">⚡ Only {LOW_STOCK[pid]} left</div>' if pid in LOW_STOCK else "")
    if out:
        return (f'<div class="card out" data-pid="{pid}"><h3>{name}</h3><div class="price">{price}</div>'
                f'<div class="tag">{note or "Currently out of stock"}</div>'
                f'<div class="buy"><button class="notify" data-notify="{notify_name or name}">🔔 Notify me</button></div></div>')
    return (f'<div class="card" data-pid="{pid}"><div class="card-meta"><span class="pill-instant">⚡ Instant</span><span class="stars-sm">★★★★★</span></div><h3>{name}</h3><div class="price">{price}</div>{low}'
            f'<div class="tag">{note}</div>'
            f'<div class="buy"><button class="btn btn-green" data-add="{pid}">Add to cart</button> '
            f'<button class="btn btn-ghost" data-buynow="{pid}">Buy now</button></div></div>')

# Product IDs must match the demo.js CATALOG exactly.
PRODUCT_IDS = {
    "Adobe Express Premium 12M": "ai-adobe-express",
    "Autodesk Admin Panel 3000 Invites 3 Yr": "ai-autodesk",
    "Capcut Team 1M · 1200 credits": "ai-capcut",
    "Duolingo Super 12M": "ai-duolingo",
    "Elevenlabs Creator 3M": "ai-elevenlabs",
    "Figma Pro Edu 2 Yr": "ai-figma",
    "Framer Basic Plan 12M": "ai-framer",
    "Gemini Plus 12m Links": "ai-gemini-12m",
    "JetBrains Edu Pack 12M": "ai-jetbrains",
    "Miro Edu Panel 100 Invites · Lifetime": "ai-miro",
    "Muse AI stable Account — 1B Tokens": "ai-claude-stable",
    "Notion Business 3M Coupon": "ai-notion-biz",
    "Notion Plus 12M": "ai-notion-plus",
    "Replit Core $40 Credits 1M": "ai-replit",
    "Udemy Personal Plan 1M": "ai-udemy",
    "Wispr Flow Pro 2 Months": "ai-wispr",
    "YouTube Premium 3m": "ai-youtube-premium",
    "Surfshark VPN 2M": "ai-surfshark",
    "ChatGPT Plus 1M": "ai-chatgpt",
    "Canva Pro Edu Panel 500 Invites": "ai-canva",
    "Lovable Pro 10k Credits 2M": "ai-lovable-pro",
    "Lovable Lite 12M": "ai-lovable-lite",
    "Muse AI Account — 30 Billion Tokens": "ai-claude-30b",
    "Gemini Plus 3m Links": "ai-gemini-3m",
    "Amazon Prime Video 1M": "ot-prime-1m",
    "Amazon Prime Video 6M": "ot-prime-6m",
    "Nord VPN 3M Accounts": "ot-nord",
    "Proton VPN 1 Month": "ot-proton",
    "Microsoft Office 365 Plus 12M": "ot-office",
    "Apple Music 5M Redeem Link": "ot-apple-music",
    "iLovePdf Premium 1 Yr": "ot-ilovepdf",
    "LinkedIn Sales Navigator Core 2M": "ot-linkedin-sales",
    "LinkedIn Career 3M": "ot-linkedin-career",
    "Crunchyroll 1 Month Link": "ot-crunchyroll",
    "Outlook Mail": "ot-outlook",
    "YouTube Premium 3-month Coupons": "ot-youtube-premium",
    "Surfshark VPN 2M Private Accounts": "ot-surfshark",
    "Steam Wallet — USA $10": "gc-steam-10",
    "Steam Wallet — USA $25": "gc-steam-25",
    "Steam Wallet — USA $50": "gc-steam-50",
    "Steam Wallet — USA $100": "gc-steam-100",
    "PlayStation Store — USA $25": "gc-psn-25",
    "Xbox Live — USA $25": "gc-xbox-25",
    "PUBG Mobile UC 600": "gc-pubg-600",
}

# Live AI & Tools (22): static names/prices from the live page, with the
# documented live sell-price changes applied (Gemini Plus 12m $0.60,
# Lovable Pro $37.00). Eleven Reader + Gemini AI Pro are gone from Qamify.
AI_TOOLS = [
    ("Adobe Express Premium 12M", "$0.70", "Coupons · Auto delivery"),
    ("Autodesk Admin Panel 3000 Invites 3 Yr", "$12.00", "Auto delivery"),
    ("Capcut Team 1M · 1200 credits", "$2.20", "Auto delivery"),
    ("Duolingo Super 12M", "$0.70", "Coupons · Auto delivery"),
    ("Elevenlabs Creator 3M", "$10.00", "Auto delivery"),
    ("Figma Pro Edu 2 Yr", "$5.30", "Auto delivery"),
    ("Framer Basic Plan 12M", "$9.00", "Auto delivery"),
    ("Gemini Plus 12m Links", "$0.60", "Auto delivery"),
    ("JetBrains Edu Pack 12M", "$4.50", "Auto delivery"),
    ("Miro Edu Panel 100 Invites · Lifetime", "$12.00", "Auto delivery"),
    ("Muse AI stable Account — 1B Tokens", "$0.30", "Auto delivery"),
    ("Notion Business 3M Coupon", "$0.80", "Auto delivery"),
    ("Notion Plus 12M", "$3.00", "Auto delivery"),
    ("Replit Core $40 Credits 1M", "$4.50", "Auto delivery"),
    ("Udemy Personal Plan 1M", "$1.70", "Auto delivery"),
    ("Wispr Flow Pro 2 Months", "$0.30", "Auto delivery"),
]
AI_OUT = ["YouTube Premium 3m", "Surfshark VPN 2M", "ChatGPT Plus 1M", "Canva Pro Edu Panel 500 Invites", "Lovable Pro 10k Credits 2M", "Lovable Lite 12M", "Muse AI Account — 30 Billion Tokens", "Gemini Plus 3m Links"]

# Other Tools (13): live prices with documented changes (Prime 1M $0.60,
# Prime 6M $1.30, Nord $2.90, iLovePdf $1.20 kept).
OTHER_TOOLS = [
    ("Amazon Prime Video 1M", "$0.60", "Auto delivery"),
    ("Amazon Prime Video 6M", "$1.30", "Auto delivery"),
    ("Nord VPN 3M Accounts", "$2.90", "Auto delivery"),
    ("Proton VPN 1 Month", "$2.00", "Auto delivery"),
    ("Microsoft Office 365 Plus 12M", "$0.80", "Auto delivery"),
    ("Apple Music 5M Redeem Link", "$0.80", "Auto delivery"),
    ("iLovePdf Premium 1 Yr", "$1.20", "Auto delivery"),
    ("LinkedIn Sales Navigator Core 2M", "$1.50", "Auto delivery"),
    ("LinkedIn Career 3M", "$1.10", "Auto delivery"),
    ("Crunchyroll 1 Month Link", "$0.80", "Auto delivery"),
    ("Outlook Mail", "$0.10", "Auto delivery"),
]
OTHER_OUT = ["YouTube Premium 3-month Coupons", "Surfshark VPN 2M Private Accounts"]

BRANDS = [
    ("Steam", "🎮", "brand/steam.html", "USA, Europe, KSA, UAE & more", "#1b2838"),
    ("PlayStation", "🎮", "gift-cards.html", "PSN cards · USA, UK, KSA, UAE", "#0070d1"),
    ("Xbox", "🎮", "gift-cards.html", "Xbox Live · USA, UK, Europe", "#107c10"),
    ("Apple", "🍎", "gift-cards.html", "App Store & iTunes · many regions", "#111827"),
    ("Google Play", "▶️", "gift-cards.html", "Play credit · USA, India & more", "#01875f"),
    ("Amazon", "🛒", "gift-cards.html", "Amazon gift cards · USA, UK", "#b45309"),
    ("PUBG Mobile", "🔫", "gift-cards.html", "UC top-up · Global", "#92400e"),
    ("Roblox", "🧱", "gift-cards.html", "Roblox credit · USA", "#b91c1c"),
    ("Netflix", "🎬", "gift-cards.html", "Netflix gift cards · many regions", "#b91c1c"),
    ("Spotify", "🎵", "gift-cards.html", "Premium gift cards", "#15803d"),
    ("Nintendo", "🕹️", "gift-cards.html", "eShop cards · USA, Europe", "#be123c"),
    ("Razer Gold", "⚡", "gift-cards.html", "Razer Gold · Global", "#15803d"),
]

# ---------------- pages ----------------

def product_grid(items, out_items):
    cards = "".join(buy_card(n, p, note) for n, p, note in items)
    cards += "".join(buy_card(n, "", out=True) for n in out_items)
    return f'<div class="grid">{cards}</div>'

def index_page():
    brand_tiles = "".join(
        f'<a class="tile" href="{href}" style="--band:{band}"><span class="tile-icon">{icon}</span>{name}<span class="tile-note">{note}</span></a>'
        for name, icon, href, note, band in BRANDS)
    popular = "".join(buy_card(n, p, note) for n, p, note in [
        ("Steam Wallet — USA $50", "$50.00", "Gift card · Instant delivery"),
        ("PlayStation Store — USA $25", "$25.00", "Gift card · Instant delivery"),
        ("Xbox Live — USA $25", "$25.00", "Gift card · Instant delivery"),
        ("PUBG Mobile UC 600", "$9.99", "Top-up · Instant delivery"),
    ])
    body = f'''
<div class="hero hero-split"><div><span class="eyebrow">Buy Gift Cards with Cryptocurrency | Subvexa</span><h1>Gift cards with crypto.<br>Delivered in seconds.</h1>
<p>Steam, PlayStation, Xbox, PUBG and 500+ brands — pick your region, pay with USDT, and your code appears in your account and email. No waiting, no paperwork.</p>
<div class="cta"><a class="btn btn-green" href="gift-cards.html">Shop gift cards</a><a class="btn btn-white" href="tools.html">Explore Tools</a></div>
<div class="hero-chips"><span>⚡ Instant delivery</span><span>₮ Pay with USDT</span><span>🛡️ Buyer Protection</span><span>🌍 8 Steam regions</span></div></div>
<div class="hero-visual"><div class="showcase"><div class="showcase-top"><span>🎮 Steam · USA</span><span class="pill-instant">⚡ Instant</span></div><h3>Steam Wallet — USA $50</h3><div class="stars">★★★★★ <span>4.8 · 2,300+ bought (demo)</span></div><div class="showcase-price">$50.00</div><div class="tracker"><span class="done">Paid<br><small>14:02:21</small></span><span class="done">Code issued<br><small>14:02:26</small></span><span class="done">Delivered<br><small>~30 sec</small></span></div><div class="codebox"><span>DEMO-7K2Q-9X4M-3P8W</span><button class="copybtn" data-copy="DEMO-7K2Q-9X4M-3P8W">Copy</button></div><p class="tag" style="color:#94a3b8">Sample delivery preview — demo code, not a real code.</p><div class="buy"><button class="btn btn-green" data-add="gc-steam-50">Add to cart</button> <button class="btn btn-ghost" data-buynow="gc-steam-50" style="background:#fff;color:#4f46e5">Buy now</button></div></div></div></div>
{TRUST}
<div class="section-head"><h2>Shop by category</h2><a href="gift-cards.html">All gift cards →</a></div>
<p class="section-sub">Pick a brand, then pick your region.</p>
<div class="tiles">{brand_tiles}</div>
<div class="section-head"><h2>Popular gift cards</h2><a href="gift-cards.html">See all →</a></div>
<p class="section-sub">Most bought this week.</p>
<div class="grid">{popular}</div>
<p style="margin-top:20px"><a class="btn btn-ghost" href="tools.html">Tools — 37 products →</a> <a class="btn btn-ghost" href="how-to-buy.html">How to Buy →</a></p>'''
    write("index.html", page("Buy Gift Cards with Cryptocurrency", "index.html", body))

def gift_cards_page():
    tiles = "".join(
        f'<a class="tile" href="{href}" style="--band:{band}"><span class="tile-icon">{icon}</span>{name}<span class="tile-note">{note}</span></a>'
        for name, icon, href, note, band in BRANDS)
    body = f'''<h1 style="margin-top:0">Gift Cards</h1>
<p class="section-sub">Pick a brand, then pick your region — each region is a separate card with its own denominations. Prices are indicative; the final price is verified before payment.</p>
{TRUST}
{region_warn()}
{PROTECT}
<div class="tiles">{tiles}</div>
<h2>How it works</h2>
<div class="progress"><span>1 · Choose a brand &amp; region</span><span>2 · Pick a value</span><span>3 · Pay with USDT</span><span>4 · Show Code &amp; redeem</span></div>
<p><a class="btn btn-purple" href="how-to-buy.html">Full How-to hub →</a> <a class="btn btn-ghost" href="brand/steam.html">See an example: Steam →</a></p>'''
    write("gift-cards.html", page("Gift Cards", "gift-cards.html", body))

def steam_page():
    regions = [
        ("🇺🇸", "Steam — USA", "$30 / $50 / $100", False),
        ("🇪🇺", "Steam — Europe", "€20 / €50 / €100", False),
        ("🇸🇦", "Steam — KSA", "SAR 100 / 200", False),
        ("🇦🇪", "Steam — UAE", "AED 100 / 200", False),
        ("🇮🇳", "Steam — India", "₹500 / ₹1,000", False),
        ("🇹🇷", "Steam — Turkey", "₺250 / ₺500", True),
        ("🇭🇰", "Steam — Hong Kong", "HKD 200 / 400", False),
        ("🇸🇬", "Steam — Singapore", "SGD 30 / 50", False),
    ]
    cards = ""
    for flag, name, vals, out in regions:
        region = name.split(" — ")[1]
        if out:
            cards += (f'<div class="card out" data-region="{region}"><h3><span class="flag">{flag}</span>{name}</h3>'
                      f'<div class="price">{vals}</div><div class="tag">Currently out of stock</div>'
                      f'<div class="buy"><button class="notify" data-notify="{name}">🔔 Notify me</button></div></div>')
        else:
            cards += (f'<div class="card" data-region="{region}"><h3><span class="flag">{flag}</span>{name}</h3>'
                      f'<div class="price">{vals}</div><div class="tag">In stock · Instant delivery</div>'
                      f'<div class="buy"><a class="btn btn-green" href="#denominations">Choose value →</a></div></div>')
    body = f'''<p class="section-sub"><a href="../gift-cards.html">Gift Cards</a> / <strong>Steam</strong></p>
<h1 style="margin-top:0">🎮 Steam Gift Cards</h1>
<p class="section-sub">One brand, many regions. Pick the region that matches your Steam account — a USA code will not work on a KSA account.</p>
{TRUST}
<div class="box region-helper"><h3 style="margin-top:0">🌍 Region checker (demo)</h3>
<p>Select your Steam account country — the matching region card lights up, the others dim.</p>
<select id="region-select"><option value="">— Select your Steam account country —</option><option>USA</option><option>Europe</option><option>KSA</option><option>UAE</option><option>India</option><option>Turkey</option><option>Hong Kong</option><option>Singapore</option></select>
<p id="region-result" class="tag">Select your Steam account country to highlight the matching region.</p></div>
{region_warn("../")}
{PROTECT}
<h2>Choose your region</h2>
<div class="grid">{cards}</div>
<h2 id="denominations">Denominations — Steam USA</h2>
<p class="section-sub">Example values for the USA variant. Other regions show their own local values.</p>
<div class="grid">
{buy_card("Steam Wallet — USA $10", "$10.00", "Gift card · Instant delivery")}
{buy_card("Steam Wallet — USA $25", "$25.00", "Gift card · Instant delivery")}
{buy_card("Steam Wallet — USA $50", "$50.00", "Gift card · Instant delivery")}
{buy_card("Steam Wallet — USA $100", "$100.00", "Gift card · Instant delivery")}
</div>
{REVIEWS}
<div class="box warn"><h3 style="margin-top:0">⚠️ Redemption requirements</h3>
<p>Use the code on a Steam account from the <strong>same region</strong> as the card. Check the region, currency and expiry before paying. Codes are delivered to your account and email after payment — click <strong>Show Code</strong>, copy and redeem on Steam. Delivered codes cannot be refunded or exchanged.</p></div>
<h2>Steam FAQ</h2><div class="faq">
<details><summary>Which Steam region should I buy?</summary><p>Buy the region that matches your Steam account&apos;s country. A USA code only works on a USA account.</p></details>
<details><summary>How fast is delivery?</summary><p>Instant after payment is confirmed: the code appears in My Orders and in your email. Click Show Code to reveal it.</p></details>
<details><summary>Can I get a refund after delivery?</summary><p>No — once a valid code is delivered it cannot be refunded or exchanged. If you paid but no code was delivered, contact support@subvexa.shop for a refund.</p></details>
<details><summary>What if my code shows as already used or invalid?</summary><p>Contact support with your order number and the exact error message. Do not publish the code anywhere.</p></details>
<details><summary>Can I pay with crypto?</summary><p>Yes — USDT (BEP20). The exact amount and wallet address are shown at checkout. See <a href="../payment-methods.html">Payment Methods</a>.</p></details>
<details><summary>How do I redeem a Steam code?</summary><p>Open Steam → Games → Redeem a Steam Wallet Code, paste the code and confirm. Full steps: <a href="../blog/how-to-redeem-steam-code.html">How to redeem a Steam code</a>.</p></details>
<details><summary>What should I check before buying any gift card?</summary><p>Region, denomination, expiry and fees — the full list is in <a href="../blog/check-before-you-buy.html">What to check before buying a gift card</a>.</p></details>
<details><summary>Do Steam cards expire?</summary><p>Check the expiry on the product page before paying. Some regional cards carry an expiry date.</p></details>
</div>
<div class="shopbox"><strong>Shop from this guide:</strong> <a class="btn btn-green" href="#denominations">Buy Steam USA $50 →</a> <a class="btn btn-ghost" href="../blog/steam-region-guide.html">Read the full region guide →</a></div>'''
    write("brand/steam.html", page("Steam Gift Cards", "gift-cards.html", body, depth=1))

def tools_page():
    body = f'''<h1 style="margin-top:0">Tools</h1>
<p class="section-sub">37 products in one place — 24 AI &amp; Tools + 13 Other Tools &middot; auto delivery &middot; prices indicative, final price verified at checkout. Out-of-stock items show a Notify me button instead of disappearing.</p>
{TRUST}
{REGION_WARN_TOOLS}
{PROTECT}
<div class="filters">
<button class="active" onclick="toolsFilter(this,'all')">All 35</button>
<button onclick="toolsFilter(this,'ai')">AI &amp; Tools (24)</button>
<button onclick="toolsFilter(this,'ot')">Other Tools (13)</button>
</div>
<div id="tools-ai"><h2>AI &amp; Tools</h2><p class="section-sub">24 products &middot; from $0.10 &middot; auto delivery.</p>
{product_grid(AI_TOOLS, AI_OUT)}</div>
<div id="tools-ot"><h2>Other Tools</h2><p class="section-sub">13 products &middot; VPNs, streaming, Office, music &amp; more.</p>
{product_grid(OTHER_TOOLS, OTHER_OUT)}</div>
<div class="box"><h3 style="margin-top:0">Before you buy</h3><p>Check the region, redemption method and expiry for each product — the 2-minute checklist: <a href="blog/check-before-you-buy.html">What to check before buying a gift card</a>. Buyer Protection applies to every order: activation guarantee, unviewed-code refund, escrow-style hold until delivery.</p></div>
{REVIEWS}
<p class="tag" style="margin-top:16px">Note: Eleven Reader Ultra Plan 12M and Gemini AI Pro 18 Month are no longer available from the supplier, so they are not listed. Prices follow the live shop where documented.</p>
<script>
function toolsFilter(btn, which) {{
  document.querySelectorAll('.filters button').forEach(function(b){{ b.classList.remove('active'); }});
  btn.classList.add('active');
  var ai = document.getElementById('tools-ai'), ot = document.getElementById('tools-ot');
  if (ai) ai.style.display = (which === 'ot') ? 'none' : 'block';
  if (ot) ot.style.display = (which === 'ai') ? 'none' : 'block';
}}
</script>'''
    write("tools.html", page("Tools", "tools.html", body))

def ai_tools_page():
    body = f'''<h1 style="margin-top:0">AI &amp; Tools</h1>
<p class="section-sub">AI &amp; Tools is now part of the combined <a href="tools.html">Tools</a> page — 37 products in one place.</p>
<p><a class="btn btn-green" href="tools.html">Go to Tools →</a></p>
<script>window.location.replace("tools.html");</script>'''
    write("ai-tools.html", page("AI & Tools", "tools.html", body))

def other_tools_page():
    body = f'''<h1 style="margin-top:0">Other Tools</h1>
<p class="section-sub">Other Tools is now part of the combined <a href="tools.html">Tools</a> page — 37 products in one place.</p>
<p><a class="btn btn-green" href="tools.html">Go to Tools →</a></p>
<script>window.location.replace("tools.html");</script>'''
    write("other-tools.html", page("Other Tools", "tools.html", body))

def how_to_page():
    body = f'''<h1 style="margin-top:0">How to Buy on Subvexa</h1>
<p class="section-sub">Four short guides. Every order follows the same progress: Validating payment → Cards are being issued → Show Code.</p>
<div class="progress"><span>Validating payment</span><span>Cards are being issued</span><span>Show Code</span></div>
{TRUST}
<div class="steps">
<div class="step"><b>1 · Register</b><h3>Create your account</h3><p>Sign up with your email and verify it. One account per user, one email per account. You need to be 18+.</p></div>
<div class="step"><b>2 · Buy</b><h3>Pick a product &amp; pay</h3><p>Choose a brand and region, pick a value, then pay with USDT (BEP20). The exact amount and wallet are shown at checkout. First, use the region checker on the product page — a wrong region is the #1 reason orders fail. At checkout you confirm the regions match and tick the instant-delivery consent box.</p></div>
<div class="step"><b>3 · Verify</b><h3>Payment check</h3><p>Your payment is verified on-chain. This usually takes under a minute. You can watch the order progress in My Orders.</p></div>
<div class="step"><b>4 · Track order</b><h3>Show Code &amp; redeem</h3><p>When the order is DELIVERED, open My Orders, click Show Code, copy the code and redeem it. A copy is also emailed to you.</p></div>
</div>
<h2>What happens after you pay?</h2>
<div class="box"><ol><li><strong>Validating payment</strong> — we confirm your USDT payment on the blockchain.</li><li><strong>Cards are being issued</strong> — the supplier issues your code or account.</li><li><strong>Show Code</strong> — your code appears in My Orders and in your email. Copy and redeem.</li></ol><p>If delivery fails after payment, you are refunded — see the <a href="returns.html">Return Policy</a>.</p></div>
<h2>Common questions</h2><div class="faq">
<details><summary>Do I need an account to buy?</summary><p>Yes — orders are tied to your account so your codes are always in My Orders, even if the email is lost.</p></details>
<details><summary>How long does delivery take?</summary><p>Usually under a minute after payment is confirmed. If an order is still not delivered after 30 minutes, contact support@subvexa.shop with your order number.</p></details>
<details><summary>What if I pay the wrong amount?</summary><p>Pay the exact amount shown at checkout. If you over- or under-pay, contact support with the transaction hash — do not pay twice.</p></details>
</div>'''
    write("how-to-buy.html", page("How to Buy", "how-to-buy.html", body))

def payment_methods_page():
    rows = [
        ("USDT (BEP20)", "Cryptocurrency", "USD", "Yes — recommended", "Instant after on-chain confirmation"),
        ("USDT (TRC20)", "Cryptocurrency", "USD", "Info only — not live yet", "—"),
        ("Visa / Mastercard", "Card", "USD", "Info only — coming soon", "—"),
        ("Apple Pay / Google Pay", "eWallet", "USD", "Info only — coming soon", "—"),
        ("PayPal", "eWallet", "USD", "Info only — coming soon", "—"),
    ]
    tr = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in rows)
    body = f'''<h1 style="margin-top:0">Payment Methods</h1>
<p class="section-sub">Filter by category. USDT (BEP20) is the live payment method; the others are shown for information.</p>
{TRUST}
<div class="filters">
<button class="active" onclick="filterBy(this,'all')">All</button>
<button onclick="filterBy(this,'crypto')">Cryptocurrency</button>
<button onclick="filterBy(this,'card')">Cards</button>
<button onclick="filterBy(this,'ewallet')">eWallet</button>
</div>
<div class="grid" id="pay-grid">
<div class="card" data-cat="crypto"><h3>₮ USDT (BEP20)</h3><div class="price">Live now</div><div class="tag">Pay the exact USDT amount to the wallet shown at checkout. Verified on-chain (BSC).</div><div class="buy"><a class="btn btn-green" href="how-to-buy.html">How to pay →</a></div></div>
<div class="card" data-cat="crypto"><h3>₮ USDT (TRC20)</h3><div class="price">Info only</div><div class="tag">Not a live checkout option yet. Shown here so you know what is planned.</div></div>
<div class="card" data-cat="card"><h3>💳 Visa / Mastercard</h3><div class="price">Info only</div><div class="tag">Card payments are not live on Subvexa yet.</div></div>
<div class="card" data-cat="ewallet"><h3>📱 Apple Pay / Google Pay</h3><div class="price">Info only</div><div class="tag">Wallet payments are not live on Subvexa yet.</div></div>
<div class="card" data-cat="ewallet"><h3>🅿️ PayPal</h3><div class="price">Info only</div><div class="tag">PayPal is not a live checkout option yet.</div></div>
</div>
<h2>How to pay with USDT (BEP20)</h2>
<div class="box"><ol><li>Create your order and click <strong>Buy now</strong>.</li><li>Copy the <strong>exact USDT amount</strong> and the <strong>wallet address</strong> shown.</li><li>Send from your wallet on the <strong>BEP20 (BSC)</strong> network only.</li><li>Wait for on-chain confirmation — then your code is issued and shown in My Orders.</li></ol></div>
<h2>All methods at a glance</h2>
<table><tr><th>Method</th><th>Category</th><th>Currency</th><th>Status</th><th>Confirmation</th></tr>{tr}</table>'''
    write("payment-methods.html", page("Payment Methods", "payment-methods.html", body))

def my_orders_page():
    body = f'''<h1 style="margin-top:0">My Orders</h1>
<p class="section-sub">All your orders — gift cards and digital goods — in one single section. Orders are rendered live from your demo order history (localStorage), including any order you complete in this demo checkout. Most orders deliver in ~30 seconds after payment is confirmed — each order below shows a delivery timeline with timestamps.</p>
{TRUST}
<div class="filters">
<button class="active" data-order-filter="all">All</button>
<button data-order-filter="DELIVERED">Delivered</button>
<button data-order-filter="AWAITING_PAYMENT">Awaiting payment</button>
<button data-order-filter="FAILED">Failed</button>
</div>
<div id="orders-root"><p class="tag">Loading your demo orders…</p></div>
<p class="tag">Demo data only — in the live shop this page lists your real orders from your account, on any device. Delivered items and Copy buttons appear only when an order is DELIVERED.</p>'''
    write("my-orders.html", page("My Orders", "my-orders.html", body))

def cart_page():
    body = f'''<h1 style="margin-top:0">🛒 Your Cart</h1>
<p class="section-sub"><span id="cart-count-line">0 items</span> · Prices in USD · Demo cart — nothing is charged.</p>
{TRUST}
<div id="cart-root"><p class="tag">Loading your demo cart…</p></div>
<div class="box"><div class="order-head"><strong>Total</strong><strong id="cart-total">$0.00</strong></div>
<p style="margin-top:12px"><a class="btn btn-green" href="checkout.html">Proceed to checkout (demo) →</a> <a class="btn btn-ghost" href="gift-cards.html">Continue shopping</a></p>
<p class="tag">Out-of-stock products can never be added to the cart — they only offer Notify me.</p></div>'''
    write("cart.html", page("Your Cart", "cart.html", body))

def checkout_page():
    body = f'''<h1 style="margin-top:0">Checkout</h1>
<p class="section-sub">Demo checkout — no real payment is taken, no funds move, no data leaves this browser.</p>
{TRUST}
<div class="progress"><span>1 · Account</span><span>2 · Review</span><span>3 · Pay with USDT</span><span>4 · Show Code</span></div>
<div id="checkout-root"><p class="tag">Loading your demo checkout…</p></div>
<p class="tag">Demo payment flow: pay the exact USDT amount to the demo wallet shown, then press “I have paid (demo)” — the order runs through Validating payment → Cards are being issued → Show Code, and the delivered sample code appears here and in My Orders.</p>'''
    write("checkout.html", page("Checkout", "cart.html", body))

def search_page():
    body = f'''<h1 style="margin-top:0" id="search-title">Search the demo catalog</h1>
<p class="section-sub">Searches all demo products: 37 Tools (24 AI &amp; Tools + 13 Other Tools) and the gift-card catalog. Press Enter in the header search on any page to get here.</p>
{TRUST}
<div class="search" style="margin-bottom:16px"><input id="search-page-input" type="search" placeholder="Try Steam, VPN, Gemini, Outlook…"><button onclick="window.location.href='search.html?q='+encodeURIComponent(document.getElementById('search-page-input').value)">Search</button></div>
<div id="search-results"><p class="tag">Type a search above, or open this page with ?q=steam.</p></div>'''
    write("search.html", page("Search", "search.html", body))

def login_page():
    body = f'''<h1 style="margin-top:0">Sign In</h1>
<p class="section-sub">Demo sign-in only — any email works, nothing is verified and nothing leaves this browser.</p>
{TRUST}
<div class="box"><form id="login-form">
<div class="form-row"><label>Your name<br><input id="login-name" value="Demo User"></label></div>
<div class="form-row"><label>Email<br><input id="login-email" type="email" value="demo@subvexa.shop"></label></div>
<div class="form-row"><label>Password (demo — any value works)<br><input type="password" value="demo-only"></label></div>
<button class="btn btn-green" type="submit">Sign in (demo)</button>
</form><p class="tag">Or continue straight to <a href="checkout.html">checkout as the demo user</a> — the checkout offers the same one-click demo sign-in.</p>
<p><a href="account.html">My Account →</a> · <a href="my-orders.html">My Orders →</a></p></div>'''
    write("login.html", page("Sign In", "login.html", body))

def account_page():
    body = f'''<h1 style="margin-top:0">My Account</h1>
<p class="section-sub">Demo profile — saved only in this browser.</p>
{TRUST}
<div id="account-root"><p class="tag">Loading your demo account…</p></div>'''
    write("account.html", page("My Account", "account.html", body))

def support_page():
    body = f'''<h1 style="margin-top:0">Support &amp; FAQ</h1>
<p class="section-sub">Get help with an order, a payment or a code that will not redeem.</p>
{TRUST}
<div class="support-grid">
<div class="support-card"><div class="icon">💬</div><h3>WhatsApp</h3><p class="tag">Fastest for order questions. (Demo link — opens WhatsApp.)</p><a class="btn btn-green" href="https://wa.me/971521705590">Chat on WhatsApp →</a></div>
<div class="support-card"><div class="icon">✈️</div><h3>Telegram</h3><p class="tag">Message support on Telegram. (Demo link.)</p><a class="btn btn-purple" href="https://t.me/subvexa">Message on Telegram →</a></div>
<div class="support-card"><div class="icon">✉️</div><h3>Email</h3><p class="tag">For refunds, failed deliveries and account help.</p><a class="btn btn-ghost" href="mailto:support@subvexa.shop">support@subvexa.shop</a></div>
</div>
<h2>Frequently asked questions</h2><div class="faq">
<details><summary>Where is my code after I pay?</summary><p>In My Orders — click Show Code — and in your email. Both are shown the moment the order is DELIVERED.</p></details>
<details><summary>I paid but nothing was delivered. What now?</summary><p>Check My Orders first — the order may still be validating. If it is still not delivered after 30 minutes, contact support with your order number and transaction hash.</p></details>
<details><summary>Can I get a refund?</summary><p>If you paid but no code was delivered, yes — contact support. After a valid code is delivered, change-of-mind returns are not accepted. See the <a href="returns.html">Return Policy</a>.</p></details>
<details><summary>I bought the wrong region. Can I exchange it?</summary><p>Delivered codes cannot be exchanged. Check the region on the product page before paying — see the <a href="blog/steam-region-guide.html">Steam region guide</a>.</p></details>
<details><summary>Which payment methods do you accept?</summary><p>USDT (BEP20) is live. See the full <a href="payment-methods.html">Payment Methods</a> page.</p></details>
<details><summary>How do I track my order?</summary><p>Every order has a status timeline in <a href="my-orders.html">My Orders</a>: Ordered → Payment → Issuing → Delivered.</p></details>
</div>
<p><a class="btn btn-purple" href="how-to-buy.html">How to Buy hub →</a> <a class="btn btn-ghost" href="my-orders.html">My Orders →</a> <a class="btn btn-ghost" href="help.html">Help Center →</a></p>'''
    write("support.html", page("Support & FAQ", "support.html", body))

def admin_pages():
    admin_nav = '''<div class="admin-nav">
<a href="index.html">Dashboard</a><a href="orders.html">Orders</a><a href="products.html">Products</a><a href="settings.html">Settings</a>
<a href="../index.html">← Back to shop</a></div>
<p class="tag">Demo admin panel — no real password, no real data. Click “Enter demo admin” below; everything here is stored only in this browser.</p>
<p><button class="btn btn-purple" onclick="document.getElementById('admin-body').style.display='block';this.style.display='none'">Enter demo admin →</button></p>
<div id="admin-body" style="display:none">'''
    # Dashboard
    body = f'''<h1 style="margin-top:0">Admin Panel — Dashboard</h1>
<p class="section-sub">Demo admin for the redesigned Subvexa shop.</p>
{admin_nav}
<div class="stats" id="admin-stats"></div>
<h2>Recent orders</h2><div id="orders-root"></div>
</div>'''
    write("admin/index.html", page("Admin — Dashboard", "admin/index.html", body, depth=1))
    # Orders
    body = f'''<h1 style="margin-top:0">Admin — Orders</h1>
<p class="section-sub">All demo orders. Filter by status, or mark an awaiting order delivered (demo).</p>
{admin_nav}
<div class="filters">
<button class="active" data-admin-order-filter="all">All</button>
<button data-admin-order-filter="DELIVERED">Delivered</button>
<button data-admin-order-filter="AWAITING_PAYMENT">Awaiting payment</button>
<button data-admin-order-filter="FAILED">Failed</button>
</div>
<div class="table-wrap" id="admin-orders-root" data-filter="all"><p class="tag">Loading demo orders…</p></div>
</div>'''
    write("admin/orders.html", page("Admin — Orders", "admin/index.html", body, depth=1))
    # Products
    body = f'''<h1 style="margin-top:0">Admin — Products</h1>
<p class="section-sub">24 AI &amp; Tools + 13 Other Tools + gift cards. Edit a price or flip stock — demo only, stored in this browser, picked up by shop pages on next load.</p>
{admin_nav}
<div class="table-wrap" id="admin-products-root"><p class="tag">Loading demo products…</p></div>
</div>'''
    write("admin/products.html", page("Admin — Products", "admin/index.html", body, depth=1))
    # Settings
    body = f'''<h1 style="margin-top:0">Admin — Settings</h1>
<p class="section-sub">Shop settings for the demo. The demo wallet address is what checkout shows — it is fake, never send real funds to it.</p>
{admin_nav}
<div class="box"><form id="settings-form">
<div class="form-row"><label>Shop name<br><input id="set-shop"></label></div>
<div class="form-row"><label>Support email<br><input id="set-email"></label></div>
<div class="form-row"><label>Demo USDT wallet address (BEP20)<br><input id="set-wallet"></label></div>
<p class="tag">Theme note: Subvexa theme is fixed — purple #6D28D9–#7C3AED, hero gradient #5B2BD9 → #3B82F6, mint #5EEAD4, dark navy, emerald #10B981. Do not change the theme for section work.</p>
<button class="btn btn-green" type="submit">Save settings (demo)</button>
</form></div>
<div class="box"><h3 style="margin-top:0">Danger zone (demo)</h3><p class="tag">Clears all demo data in this browser: cart, orders, account, admin edits and settings.</p>
<button class="btn btn-ghost" id="reset-demo">Reset all demo data</button></div>
</div>'''
    write("admin/settings.html", page("Admin — Settings", "admin/index.html", body, depth=1))

def blog_page():
    body = f'''<h1 style="margin-top:0">Blog</h1>
<p class="section-sub">Buyer guides, platform explainers and what to check before you pay.</p>
{TRUST}
<div class="grid">
<div class="card"><h3>Steam region guide: buy the right card first</h3><div class="tag">Region matching, fees and the mistakes to avoid. · Gaming</div><div class="buy"><a class="btn btn-purple" href="blog/steam-region-guide.html">Read →</a></div></div>
<div class="card"><h3>How to buy on Subvexa in under a minute</h3><div class="tag">Register, pick a card, pay with USDT, Show Code. · Guides</div><div class="buy"><a class="btn btn-purple" href="how-to-buy.html">Read →</a></div></div>
<div class="card"><h3>USDT (BEP20) payments, explained simply</h3><div class="tag">What BEP20 is, and why the exact amount matters. · Crypto</div><div class="buy"><a class="btn btn-purple" href="payment-methods.html">Read →</a></div></div>
<div class="card"><h3>PlayStation vs Xbox gift cards: which region?</h3><div class="tag">Same rule as Steam — match the region to your account. · Gaming</div><div class="buy"><a class="btn btn-purple" href="blog/steam-region-guide.html">Read the region guide →</a></div></div>
<div class="card"><h3>How to redeem a Steam code</h3><div class="tag">Client, website and app — step by step, plus what to do if it fails. · Guides</div><div class="buy"><a class="btn btn-purple" href="blog/how-to-redeem-steam-code.html">Read →</a></div></div>
<div class="card"><h3>What to check before buying a gift card</h3><div class="tag">Region, value, expiry, fees — the 2-minute checklist. · Guides</div><div class="buy"><a class="btn btn-purple" href="blog/check-before-you-buy.html">Read →</a></div></div>
</div>
<div class="box" style="margin-top:20px"><h3 style="margin-top:0">📬 Weekly digest</h3><p>One email a week: new products, price drops and guides. (Demo — no signup is stored.)</p><button class="btn btn-purple" data-demo-buy="Weekly digest signup (demo)">Subscribe</button></div>'''
    write("blog.html", page("Blog", "blog.html", body))

def blog_article_page():
    body = f'''<article class="article">
<p class="section-sub"><a href="../blog.html">Blog</a> / Gaming</p>
<h1 style="margin-top:0">Steam region guide: buy the right card first</h1>
<p class="tag">5 Nov 2026 · 4 min read · Buyer guide</p>
{TRUST}
<p>The single most common Steam mistake is buying the wrong region. A USA Steam code only works on a USA Steam account. A KSA code only works on a KSA account. The region is printed on the card — check it before you pay, not after.</p>
<h2>1 · Match the region to your account</h2>
<p>Open Steam, check your account country, then buy the same region: USA, Europe, KSA, UAE, India, Turkey, Hong Kong or Singapore. On Subvexa each region is its own card with a flag badge, so you can see it at a glance.</p>
<h2>2 · Compare the final cost, not just the face value</h2>
<p>Compare the total at checkout — face value plus any fee — in the currency you actually pay. A cheaper-looking card in another currency can cost more after conversion.</p>
<h2>3 · Check expiry and redemption rules</h2>
<p>Some regional cards carry an expiry date. Read the redemption-requirements box on the product page before paying.</p>
<h2>4 · If a code fails, do not buy twice</h2>
<p>Keep your order confirmation and the exact error message, and contact support@subvexa.shop with your order number. Buying a second card will not fix the first one — and delivered codes cannot be refunded.</p>
<div class="shopbox"><strong>Shop from the blog:</strong> Steam USA $50 · Steam Europe €50 · Steam KSA — <a class="btn btn-green" href="../brand/steam.html">See all Steam regions →</a></div>
<p><a href="../blog.html">← Back to the blog</a></p>
</article>'''
    write("blog/steam-region-guide.html", page("Steam region guide", "blog.html", body, depth=1))

def blog_redeem_page():
    body = f'''<article class="article">
<p class="section-sub"><a href="../blog.html">Blog</a> / Guides</p>
<h1 style="margin-top:0">How to redeem a Steam code</h1>
<p class="tag">5 Nov 2026 · 3 min read · Buyer guide</p>
{TRUST}
<p>You have your code — here is how to turn it into Steam Wallet credit. The code works only on a Steam account from the <strong>same region</strong> as the card, so check the region first (see the <a href="steam-region-guide.html">Steam region guide</a>).</p>
<h2>1 · In the Steam client (PC / Mac)</h2>
<p>Open Steam → click <strong>Games</strong> in the top menu → <strong>Redeem a Steam Wallet Code</strong> → paste your code → confirm. The balance appears in your wallet immediately.</p>
<h2>2 · On the Steam website</h2>
<p>Sign in at store.steampowered.com, open your account details, choose <strong>Redeem a Steam Gift Card or Wallet Code</strong>, paste the code and confirm.</p>
<h2>3 · In the Steam mobile app</h2>
<p>Open the app → Store → your account → <strong>Redeem a Steam Gift Card or Wallet Code</strong> → paste and confirm.</p>
<h2>If the code fails</h2>
<p>Read the exact error message and do <strong>not</strong> buy a second card. The usual causes: wrong region, a typo when pasting, or the code was already redeemed. Keep your order confirmation and contact support@subvexa.shop with your order number and the exact error.</p>
<div class="shopbox"><strong>Shop from the blog:</strong> Steam USA $50 · Steam Europe €50 · Steam KSA — <a class="btn btn-green" href="../brand/steam.html">See all Steam regions →</a></div>
<p><a href="../blog.html">← Back to the blog</a></p>
</article>'''
    write("blog/how-to-redeem-steam-code.html", page("How to redeem a Steam code", "blog.html", body, depth=1))

def blog_checklist_page():
    body = f'''<article class="article">
<p class="section-sub"><a href="../blog.html">Blog</a> / Guides</p>
<h1 style="margin-top:0">What to check before buying a gift card</h1>
<p class="tag">5 Nov 2026 · 4 min read · Buyer guide</p>
{TRUST}
<p>Two minutes of checking before you pay saves the most common gift-card headaches. Work through this list every time.</p>
<h2>1 · Region — the big one</h2>
<p>Buy the region that matches your account. A USA code only works on a USA account. Check the flag badge on the product card.</p>
<h2>2 · Denomination &amp; currency</h2>
<p>Check the face value and the currency you pay in. Compare the <strong>final total at checkout</strong>, not just the face value — fees and conversion change the real cost.</p>
<h2>3 · Expiry</h2>
<p>Some regional cards carry an expiry date. Read the redemption-requirements box on the product page before paying.</p>
<h2>4 · Redemption method</h2>
<p>Code, account login, or direct top-up? Know what you will receive and where it appears — on Subvexa, codes appear in My Orders and in your email.</p>
<h2>5 · Buyer protection</h2>
<p>Check the seller&apos;s protection: activation guarantee, unviewed-code refund, and what happens if delivery fails. On Subvexa, Buyer Protection is shown on every product page.</p>
<h2>6 · Delivery email</h2>
<p>Make sure the email on your account is correct — the delivery email goes there. Check spam/promotions if it does not arrive.</p>
<h2>7 · If a code fails, don&apos;t buy twice</h2>
<p>Keep the order confirmation and the exact error message, and contact support with your order number. A second purchase will not fix the first one — and delivered codes cannot be refunded.</p>
<div class="shopbox"><strong>Shop from the blog:</strong> <a class="btn btn-green" href="../gift-cards.html">Browse all gift cards →</a> <a class="btn btn-ghost" href="../brand/steam.html">Steam regions →</a></div>
<p><a href="../blog.html">← Back to the blog</a></p>
</article>'''
    write("blog/check-before-you-buy.html", page("What to check before buying a gift card", "blog.html", body, depth=1))

def help_page():
    body = f'''<h1 style="margin-top:0">Help Center</h1>
<p class="section-sub">Answers grouped by topic. Still stuck? <a href="support.html">Contact support →</a></p>
{TRUST}
<h2>📦 Orders &amp; delivery</h2><div class="faq">
<details><summary>Where is my code after I pay?</summary><p>In My Orders — click Show Code — and in your email. Both appear the moment the order is DELIVERED, usually ~30 seconds after payment is confirmed.</p></details>
<details><summary>How long does delivery take?</summary><p>Usually under a minute after payment is confirmed. If an order is still not delivered after 30 minutes, contact support with your order number.</p></details>
<details><summary>I paid but nothing was delivered. What now?</summary><p>Check My Orders first — the order may still be validating. If it is still not delivered after 30 minutes, contact support@subvexa.shop with your order number and transaction hash. If delivery fails, you are refunded — see the <a href="returns.html">Return Policy</a>.</p></details>
<details><summary>Can I resend my code?</summary><p>Yes — open the order in My Orders and use the Resend code button. The delivery email is re-sent to your account email.</p></details>
</div>
<h2>💳 Payments</h2><div class="faq">
<details><summary>Which payment methods do you accept?</summary><p>USDT (BEP20) is live. See the full <a href="payment-methods.html">Payment Methods</a> page.</p></details>
<details><summary>What if I pay the wrong amount?</summary><p>Pay the exact amount shown at checkout. If you over- or under-pay, contact support with the transaction hash — do not pay twice.</p></details>
<details><summary>Why do I have to tick the consent box at checkout?</summary><p>For digital goods, EU rules require your express consent to instant delivery and your acknowledgement that the withdrawal right ends once the code is revealed. The box is not pre-ticked — you choose.</p></details>
</div>
<h2>🌍 Regions &amp; redemption</h2><div class="faq">
<details><summary>I bought the wrong region. Can I exchange it?</summary><p>Delivered codes cannot be exchanged. Check the region on the product page before paying — see the <a href="blog/steam-region-guide.html">Steam region guide</a>.</p></details>
<details><summary>How do I redeem a Steam code?</summary><p>Steam → Games → Redeem a Steam Wallet Code, paste and confirm. Full steps: <a href="blog/how-to-redeem-steam-code.html">How to redeem a Steam code</a>.</p></details>
<details><summary>My code shows as invalid or already used.</summary><p>Contact support with your order number and the exact error message. Do not publish the code anywhere.</p></details>
</div>
<h2>↩️ Refunds</h2><div class="faq">
<details><summary>Can I get a refund?</summary><p>If you paid but no code was delivered, yes — contact support. After a valid code is delivered, change-of-mind returns are not accepted. Faulty, wrong or undelivered products are replaced or refunded. See the <a href="returns.html">Return Policy</a>.</p></details>
<details><summary>What is Buyer Protection?</summary><p>Every order is covered: activation guarantee (replace or refund if a code won&apos;t activate), unviewed-code refund, and an escrow-style hold — payment is held until delivery is confirmed.</p></details>
</div>
<h2>👤 Account</h2><div class="faq">
<details><summary>Do I need an account to buy?</summary><p>Yes — orders are tied to your account so your codes are always in My Orders, even if the email is lost. You need to be 18+.</p></details>
<details><summary>How do I change my email or password?</summary><p>Go to <a href="account.html">My Account</a> and edit your profile (demo — saved only in this browser).</p></details>
<details><summary>What are Subvexa Rewards points?</summary><p>You earn 5% back in demo points on every delivered order. 100 points = $1 off your next order (demo). Your balance is on the homepage and in <a href="account.html">My Account</a>.</p></details>
</div>
<p><a class="btn btn-purple" href="support.html">Contact support →</a> <a class="btn btn-ghost" href="how-to-buy.html">How to Buy hub →</a></p>'''
    write("help.html", page("Help Center", "help.html", body))

def legal_pages():
    terms = f'''<h1 style="margin-top:0">Terms &amp; Conditions</h1>
<p class="tag">Last updated: 5 November 2026 · Demo version for the redesign preview.</p>
{TRUST}
<div class="box"><h3>1 · Who we are</h3><p>Subvexa (subvexa.shop) is an independent digital marketplace selling digital gift cards and digital goods. All products are delivered electronically — there is no physical shipping.</p>
<h3>2 · Accounts</h3><p>You must be 18 or older. One account per user, one email per account. Only registered users can place orders. Keep your login details safe; you are responsible for activity on your account.</p>
<h3>3 · Orders &amp; delivery</h3><p>Orders are confirmed by email. Codes are delivered in My Orders (click Show Code) and by email, after payment is confirmed. Fees depend on the payment method and are shown at checkout.</p>
<h3>4 · Prices</h3><p>Prices shown are indicative. Availability and the final price are verified before payment. If a product goes out of stock before payment, the order cannot be completed.</p>
<h3>5 · Fair use</h3><p>Accounts may be suspended for violations, false information, fraud or repeat chargebacks. We do not trade with sanctioned countries.</p>
<h3>6 · Contact</h3><p>Support: support@subvexa.shop. Complaints should be sent in writing; we aim to resolve them within 30 days.</p></div>'''
    write("terms.html", page("Terms & Conditions", "terms.html", terms))
    privacy = f'''<h1 style="margin-top:0">Privacy Policy</h1>
<p class="tag">Last updated: 5 November 2026 · Demo version for the redesign preview.</p>
{TRUST}
<div class="box"><h3>What we collect</h3><p>Identity and contact details, transaction and payment data, and technical data (IP address, browser, timezone) needed to run the shop and prevent fraud.</p>
<h3>How we use it</h3><p>To deliver your orders, verify payments, prevent fraud, run support, and — only with your consent — send marketing emails. We never sell your personal data.</p>
<h3>Your rights</h3><p>You can ask for access, correction or deletion of your data, and you can close your account at any time by emailing support@subvexa.shop.</p>
<h3>Cookies</h3><p>Only necessary cookies run without consent; analytics and advertising cookies need your opt-in.</p>
<h3>Under 18s</h3><p>This shop is not for under-18s.</p></div>'''
    write("privacy.html", page("Privacy Policy", "privacy.html", privacy))
    returns = f'''<h1 style="margin-top:0">Return Policy</h1>
<p class="tag">Last updated: 5 November 2026 · Demo version for the redesign preview.</p>
{TRUST}
<div class="box"><h3>Digital delivery, no physical returns</h3><p>All products are delivered electronically. There is no physical shipping and no postal return.</p>
<h3>Paid but not delivered</h3><p>If you paid but no code was delivered, contact support@subvexa.shop promptly with your name and order number. Approved refunds go back to your original payment method.</p>
<h3>After a valid code is delivered</h3><p>Change-of-mind returns are generally not accepted once a valid code or top-up has been delivered, because delivery happens immediately after payment.</p>
<h3>Wrong, defective or invalid product</h3><p>Contact support with your order number and a description of the problem. The remedy is correction, replacement or a refund, as applicable. Never publish your redemption code or share payment passwords.</p>
<h3>Unpaid orders</h3><p>An unpaid order can be cancelled any time before you pay.</p></div>'''
    write("returns.html", page("Return Policy", "returns.html", returns))

if __name__ == "__main__":
    index_page()
    gift_cards_page()
    steam_page()
    tools_page()
    ai_tools_page()
    other_tools_page()
    how_to_page()
    payment_methods_page()
    my_orders_page()
    cart_page()
    checkout_page()
    search_page()
    login_page()
    account_page()
    support_page()
    admin_pages()
    blog_page()
    blog_article_page()
    blog_redeem_page()
    blog_checklist_page()
    help_page()
    legal_pages()
    print("done")
