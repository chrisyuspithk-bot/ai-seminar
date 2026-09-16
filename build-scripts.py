#!/usr/bin/env python3
"""Render the Cantonese lecture scripts into styled HTML pages.

Reads  *-script-cantonese.md  and writes  *-script.html  using the same
design tokens as the outline pages, so the scripts read as part of the site
rather than as raw Markdown downloads.
"""
import html
import os
import re

REPO = os.path.dirname(os.path.abspath(__file__))

COURSES = [
    {
        "md": "ai-lecture-script-cantonese.md",
        "out": "ai-lecture-script.html",
        "deck": "ai-lecture-deck.html",
        "outline": "ai-lecture-outline.html",
        "accent": "l1",
        "nav": "從圖靈到代理人",
        "chapters": ("Part 1", "Part 2", "Part 3"),
        "label": "第一課",
    },
    {
        "md": "ai-llm-lmstudio-script-cantonese.md",
        "out": "ai-llm-lmstudio-script.html",
        "deck": "ai-llm-lmstudio-deck.html",
        "outline": "ai-llm-lmstudio-outline.html",
        "accent": "l2",
        "nav": "LLM 基礎與 LM Studio",
        "chapters": tuple(f"Part {i}" for i in range(1, 9)),
        "label": "第二課",
    },
    {
        "md": "agentic-ai-script-cantonese.md",
        "out": "agentic-ai-script.html",
        "deck": "agentic-ai-deck.html",
        "outline": "agentic-ai-outline.html",
        "accent": "l3",
        "nav": "Agentic AI",
        "chapters": tuple(f"Part {i}" for i in range(1, 8)) + ("BREAK",),
        "label": "第三課",
    },
    {
        "md": "ml-titanic-script-cantonese.md",
        "out": "ml-titanic-script.html",
        "deck": "ml-titanic-deck.html",
        "outline": "ml-titanic-outline.html",
        "accent": "l4",
        "nav": "機器學習與鐵達尼號",
        "chapters": tuple(f"Part {i}" for i in range(1, 7)) + ("開場",),
        "label": "第四課",
    },
    {
        "md": "deepfake-script-cantonese.md",
        "out": "deepfake-script.html",
        "deck": "deepfake-deck.html",
        "outline": "deepfake-outline.html",
        "accent": "l5",
        "nav": "深偽辨識與倫理",
        "chapters": ("第一節", "第二節", "第三節", "第四節", "小休"),
        "label": "第五課",
    },
]

NOTE_KINDS = {
    "操作提示": "ops",
    "補充": "aside",
    "學員可能問": "ask",
    "教學提示": "teach",
    "講者提示": "ops",
}

CSS = """
    :root {
      --bg:#fff; --surface:#f4f7fd; --fg:#0b1220; --muted:#5b6675;
      --border:#e2e8f2; --accent:#116dff; --accent-ink:#0a4ec2;
      --accent-soft: color-mix(in oklch, var(--accent) 12%, transparent);
      --cc: var(--accent);
      --font-display:'Poppins','PingFang TC','Noto Sans TC','Microsoft JhengHei',system-ui,sans-serif;
      --font-body:'Noto Sans TC','PingFang TC','Microsoft JhengHei',-apple-system,system-ui,sans-serif;
      --font-mono:ui-monospace,'SF Mono','JetBrains Mono',Menlo,monospace;
      --container:1080px; --gutter:28px; --radius:8px; --radius-lg:16px;
    }
    *,*::before,*::after{box-sizing:border-box}
    html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
    body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--font-body);font-size:16px;line-height:1.75;-webkit-font-smoothing:antialiased}
    a{color:inherit;text-decoration:none}
    .container{max-width:var(--container);margin-inline:auto;padding-inline:var(--gutter)}
    .section{padding-block:clamp(40px,6vw,80px)}
    .h1,h1{font-family:var(--font-display);font-size:clamp(30px,4.4vw,54px);font-weight:800;line-height:1.1;letter-spacing:-.028em;margin:0}
    .h2,h2{font-family:var(--font-display);font-size:clamp(22px,2.6vw,32px);font-weight:700;line-height:1.25;letter-spacing:-.018em;margin:0}
    .eyebrow{font-family:var(--font-mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent-ink);font-weight:600;margin:0 0 12px}
    .lead{font-size:clamp(16px,1.4vw,19px);line-height:1.75;color:var(--muted);max-width:62ch;margin:0}
    .topnav{position:sticky;top:0;z-index:20;background:color-mix(in oklch,var(--bg) 92%,transparent);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}
    .topnav-inner{display:flex;align-items:center;justify-content:space-between;gap:18px;padding-block:12px}
    .topnav .logo{font-family:var(--font-display);font-size:15px;font-weight:700}
    .topnav .logo span{color:var(--muted);font-weight:500}
    .topnav nav{display:flex;gap:18px;overflow-x:auto;scrollbar-width:none}
    .topnav nav::-webkit-scrollbar{display:none}
    .topnav nav a{font-size:13px;color:var(--muted);white-space:nowrap;padding:4px 0;border-bottom:2px solid transparent;transition:color .15s,border-color .15s}
    .topnav nav a:hover{color:var(--fg)}
    .topnav nav a.on{color:var(--cc);border-bottom-color:var(--cc);font-weight:600}
    .topnav nav a.sub{font-size:12.5px;padding-left:10px}
    @media(max-width:820px){.topnav nav{display:none}}
    .btn{display:inline-flex;align-items:center;gap:8px;padding:10px 18px;min-height:42px;border-radius:var(--radius);border:1px solid var(--border);font-size:14px;font-weight:600}
    .btn:hover{border-color:var(--fg)}
    .hero{padding-block:clamp(44px,7vw,96px) clamp(32px,4vw,56px)}
    .hero .h1{max-width:24ch;margin-bottom:18px}
    .hero-meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
    .chip{display:inline-flex;align-items:baseline;gap:8px;padding:7px 13px;border:1px solid var(--border);border-radius:999px;background:var(--surface);font-size:13px;color:var(--muted)}
    .chip b{font-family:var(--font-mono);font-weight:600;font-size:11.5px;color:var(--fg)}

    .layout{display:grid;grid-template-columns:236px 1fr;gap:clamp(28px,4vw,60px);align-items:start}
    @media(max-width:960px){.layout{grid-template-columns:1fr}.toc{display:none}}
    .toc{position:sticky;top:72px;max-height:calc(100vh - 96px);overflow-y:auto;padding-right:8px}
    .toc p{font-family:var(--font-mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 12px}
    .toc ol{list-style:none;margin:0;padding:0;display:grid;gap:2px;counter-reset:s}
    .toc a{display:block;font-size:13.5px;color:var(--muted);padding:6px 10px;border-radius:6px;border-left:2px solid transparent;line-height:1.45}
    .toc a:hover{background:var(--surface);color:var(--fg)}
    .toc a.on{background:var(--accent-soft);color:var(--fg);border-left-color:var(--cc);font-weight:600}

    .part{margin-top:clamp(40px,6vw,72px)}
    .part-head{display:grid;grid-template-columns:auto 1fr;gap:22px;align-items:end;padding-bottom:18px;border-bottom:2px solid var(--border);margin-bottom:28px;scroll-margin-top:80px}
    .part-head .pn{font-family:var(--font-display);font-weight:800;font-size:clamp(40px,5vw,62px);line-height:.8;letter-spacing:-.05em;color:var(--cc)}
    .part-head h2{font-size:clamp(20px,2.4vw,28px)}

    .slide{padding-block:26px;border-top:1px solid var(--border);scroll-margin-top:76px}
    .slide:first-of-type{border-top:0}
    .slide-head{display:flex;align-items:baseline;gap:14px;margin-bottom:14px;flex-wrap:wrap}
    .slide-head .pg{display:inline-flex;align-items:center;justify-content:center;min-width:46px;padding:3px 10px;background:var(--surface);border:1px solid var(--border);border-radius:999px;font-family:var(--font-mono);font-size:12px;font-weight:700;color:var(--cc);font-variant-numeric:tabular-nums}
    .slide-head h3{font-family:var(--font-display);font-size:clamp(17px,1.8vw,21px);font-weight:700;margin:0;line-height:1.35}
    .say{font-size:16.5px;line-height:1.85}
    .say p{margin:0 0 14px}
    .say p:last-child{margin-bottom:0}
    .say strong{font-weight:700;background:linear-gradient(transparent 62%,color-mix(in oklch,var(--cc) 22%,transparent) 62%)}

    .notes{margin-top:20px;display:grid;gap:10px}
    .note{border-left:3px solid var(--border);background:var(--surface);border-radius:0 var(--radius) var(--radius) 0;padding:12px 16px;font-size:14.5px;line-height:1.72;color:var(--muted)}
    .note-tag{display:inline-block;font-family:var(--font-mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:700;margin-right:8px;padding:2px 7px;border-radius:4px;background:var(--border);color:var(--fg);vertical-align:1px}
    .note p{margin:0}
    .note strong{font-weight:700;color:var(--fg)}
    .note.ops{border-left-color:#0aa06e}.note.ops .note-tag{background:#0aa06e;color:#fff}
    .note.ask{border-left-color:#d98200}.note.ask .note-tag{background:#d98200;color:#fff}
    .note.teach{border-left-color:#116dff}.note.teach .note-tag{background:#116dff;color:#fff}
    .note.aside{border-left-color:#8b93a3}
    .note.aside .note-tag{background:#8b93a3;color:#fff}

    .plain p{margin:0 0 14px;font-size:16px;line-height:1.78}
    .plain ul,.plain ol{margin:0 0 14px;padding-left:24px}
    .plain li{margin-bottom:7px;line-height:1.75}
    .plain blockquote{margin:0 0 16px;padding:14px 18px;background:var(--surface);border-left:3px solid var(--cc);border-radius:0 var(--radius) var(--radius) 0;color:var(--muted);font-size:15px}
    .plain blockquote p{margin:0 0 8px}
    .plain blockquote p:last-child{margin:0}
    .plain h3{font-family:var(--font-display);font-size:19px;margin:26px 0 12px}
    .plain hr{border:0;border-top:1px solid var(--border);margin:28px 0}
    .plain code{font-family:var(--font-mono);font-size:.9em;background:var(--surface);padding:2px 6px;border-radius:4px}
    .plain table{width:100%;border-collapse:collapse;font-size:14.5px;margin:0 0 18px}
    .plain th,.plain td{padding:10px 14px;text-align:left;border-bottom:1px solid var(--border);vertical-align:top}
    .plain th{font-family:var(--font-mono);font-size:11.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:600}
    .plain .tw{overflow-x:auto}
    .plain .closing{margin-top:34px;padding-top:22px;border-top:1px solid var(--border);font-size:14px;color:var(--muted);font-style:normal}
    .plain .lead-line{font-size:17px;font-weight:700;line-height:1.75;padding:16px 20px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);margin:0 0 18px}

    .pagefoot{padding-block:38px;border-top:1px solid var(--border);color:var(--muted);font-size:13px;margin-top:56px}
    .pagefoot .row{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
    .toplink{font-family:var(--font-mono);font-size:12px;color:var(--muted)}
    .toplink:hover{color:var(--fg)}
    @media print{
      .topnav,.toc,.pagefoot{display:none}
      .layout{grid-template-columns:1fr}
      .slide{break-inside:avoid}
      body{font-size:11.5pt}
    }
"""


def esc(t):
    return html.escape(t, quote=False)


def inline(t):
    """Convert inline markdown to HTML (already-escaped input expected)."""
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t


def parse_table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    if len(cells) > 1 and all(re.fullmatch(r":?-{2,}:?", c) for c in cells[1]):
        head, body = cells[0], cells[2:]
    else:
        head, body = None, cells
    out = ['<div class="tw"><table>']
    if head:
        out.append("<thead><tr>" + "".join(f"<th>{inline(esc(c))}</th>" for c in head) + "</tr></thead>")
    out.append("<tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(esc(c))}</td>" for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def blocks(lines):
    """Render a list of markdown lines into HTML blocks."""
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1
            continue
        if s == "---":
            i += 1
            continue
        if s.startswith("|"):
            j = i
            while j < len(lines) and lines[j].strip().startswith("|"):
                j += 1
            out.append(parse_table(lines[i:j]))
            i = j
            continue
        m = re.match(r"^(#{2,4})\s+(.*)$", s)
        if m:
            lvl = min(len(m.group(1)), 4)
            out.append(f"<h{lvl}>{inline(esc(m.group(2)))}</h{lvl}>")
            i += 1
            continue
        if re.match(r"^[-*]\s+", s):
            items = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[i].strip()))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(esc(x))}</li>" for x in items) + "</ul>")
            continue
        if re.match(r"^\d+\.\s+", s):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(esc(x))}</li>" for x in items) + "</ol>")
            continue
        if s.startswith(">"):
            q = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            out.append("<blockquote>" + "".join(f"<p>{inline(esc(x))}</p>" for x in q if x) + "</blockquote>")
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^(#{2,4}\s|[-*]\s|\d+\.\s|>|\||---$)", lines[i].strip()
        ):
            para.append(lines[i].strip())
            i += 1
        if para:
            out.append("<p>" + inline(esc(" ".join(para))) + "</p>")
        else:
            i += 1
    return "".join(out)


def section_body(lines):
    """Split a slide into the read-aloud script and the speaker notes."""
    say, notes = [], []
    for ln in lines:
        s = ln.strip()
        m = re.match(r"^>\s*\*\*(.+?)\*\*\s*(.*)$", s)
        if m and m.group(1) in NOTE_KINDS:
            notes.append((NOTE_KINDS[m.group(1)], m.group(1), m.group(2)))
            continue
        if s.startswith(">") and notes and notes[-1][2] == "":
            notes[-1] = (notes[-1][0], notes[-1][1], re.sub(r"^>\s?", "", s))
            continue
        if s.startswith(">"):
            m2 = re.match(r"^>\s*\*\*(.+?)\*\*(.*)$", s)
            if m2:
                notes.append(("aside", m2.group(1), m2.group(2)))
            continue
        if notes and s and not s.startswith(">"):
            kind, tag, txt = notes[-1]
            notes[-1] = (kind, tag, (txt + " " + s).strip())
            continue
        say.append(ln)

    html_say = f'<div class="say">{blocks(say)}</div>'
    if not notes:
        return html_say
    nhtml = []
    for kind, tag, txt in notes:
        nhtml.append(
            f'<div class="note {kind}"><p><span class="note-tag">{esc(tag)}</span>'
            f"{inline(esc(txt.strip()))}</p></div>"
        )
    return html_say + '<div class="notes">' + "".join(nhtml) + "</div>"


def render(course):
    src = os.path.join(REPO, course["md"])
    with open(src, encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")

    title = ""
    intro = []
    chapters = []          # (id, label, [ (num, name, html) ])
    cur_part = None
    cur_slide = None

    def flush_slide():
        if cur_slide and cur_part is not None:
            cur_part[2].append(cur_slide)

    for idx, ln in enumerate(lines):
        s = ln.strip()
        m = re.match(r"^#\s+(.+)$", s)
        if m and not s.startswith("## "):
            head = m.group(1)
            if not title:
                title = head
                continue
            for key in course["chapters"]:
                if head.startswith(key):
                    flush_slide()
                    cur_slide = None
                    pid = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-") or f"ch{len(chapters)}"
                    cur_part = [pid, head, []]
                    chapters.append(cur_part)
                    break
            else:
                flush_slide()
                cur_slide = None
                pid = "app-" + str(len(chapters))
                cur_part = [pid, head, []]
                chapters.append(cur_part)
            continue
        m = re.match(r"^##\s+第\s*(\d+)\s*頁\s*[·:：]?\s*(.*)$", s)
        if m and cur_part is not None:
            flush_slide()
            cur_slide = [m.group(1), m.group(2) or "", []]
            continue
        m = re.match(r"^##\s+(.+)$", s)
        if m and cur_part is not None:
            flush_slide()
            cur_slide = [None, m.group(1), []]
            continue
        if cur_part is None:
            intro.append(ln)
        elif cur_slide is not None:
            cur_slide[2].append(ln)
        else:
            cur_part[2].append(("__prose__", "", [ln]))
    flush_slide()

    body, toc = [], []
    for pid, pname, items in chapters:
        plain = re.match(r"^#\s*(Part\s*\d+|BREAK|開場|小休)?", pname)
        pn = ""
        m = re.match(r"^(Part\s*\d+|BREAK|第[一二三四]節|開場|小休)\s*[·:：]?\s*(.*)$", pname)
        if m:
            pn, rest = m.group(1), m.group(2)
        else:
            rest = pname
        toc.append((pid, pname, pn))
        head = (
            f'<div class="part-head" id="{pid}">'
            f'<span class="pn">{esc(pn or "·")}</span>'
            f"<h2>{esc(rest or pname)}</h2></div>"
        )
        body.append(f'<section class="part">{head}')
        for it in items:
            if it[0] == "__prose__":
                body.append(f'<div class="plain">{blocks(it[2])}</div>')
                continue
            num, name, sl = it
            if num is None:
                body.append(f'<div class="slide"><header class="slide-head"><h3>{esc(name)}</h3></header>{section_body(sl)}</div>')
            else:
                sid = f"s{num}"
                body.append(
                    f'<article class="slide" id="{sid}"><header class="slide-head">'
                    f'<span class="pg">{int(num):02d}</span><h3>{esc(name)}</h3></header>'
                    f"{section_body(sl)}</article>"
                )
        body.append("</section>")

    intro_html = f'<div class="plain">{blocks(intro)}</div>'

    # TOC: list each chapter, and its slides when there are many
    toc_items = []
    for pid, pname, pn in toc:
        label = pname.replace("# ", "")
        toc_items.append(f'<li><a href="#{pid}">{esc(label)}</a></li>')
        chap = next(c for c in chapters if c[0] == pid)
        nums = [it for it in chap[2] if it[0] != "__prose__" and it[0] is not None]
        if 0 < len(nums) <= 40 and pn:
            for it in nums:
                toc_items.append(
                    f'<li><a class="sub" href="#s{it[0]}">{int(it[0]):02d} · {esc(it[1][:26])}</a></li>'
                )

    nav_links = "".join(
        f'<a href="#{pid}">{esc(pn or pname[:14])}</a>' for pid, pname, pn in toc if pn
    )
    has_app = any(not pn for _, _, pn in toc)
    if has_app:
        nav_links += f'<a href="#{toc[-1][0]}">附錄</a>'

    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · 粵語講稿</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
{CSS}
    :root {{ --cc: var(--{course['accent']}); }}
</style>
</head>
<body>
<header class="topnav" id="top">
  <div class="container topnav-inner">
    <span class="logo">{esc(title.split("粵語")[0])}<span> · 粵語講稿</span></span>
    <nav>{nav_links}</nav>
    <a class="btn" href="{course['deck']}">看簡報</a>
  </div>
</header>
<main class="container">
  <section class="hero">
    <p class="eyebrow">{esc(course['label'])} · 逐頁講稿</p>
    <h1 class="h1">{esc(title)}</h1>
    <p class="lead">每頁一節。每節第一段係可以照讀嘅講稿，其後「操作提示」「補充」「學員可能問」係唔讀出嚟嘅備忘。</p>
    <div class="hero-meta">
      <span class="chip"><b>語言</b> 粵語口語（香港）</span>
      <span class="chip"><b>簡報</b> {esc(course['deck'])}</span>
      <span class="chip"><b>大綱</b> <a href="{course['outline']}">課程大綱</a></span>
    </div>
  </section>
  <div class="layout">
    <aside class="toc">
      <p>目錄</p>
      <ol>{''.join(toc_items)}</ol>
    </aside>
    <div>
      {intro_html}
      {''.join(body)}
      <footer class="pagefoot">
        <div class="row">
          <span>本講稿對應簡報 <code>{esc(course['deck'])}</code></span>
          <a class="toplink" href="#top">返回頂部 ↑</a>
        </div>
      </footer>
    </div>
  </div>
</main>
<script>
(function(){{
  var links=[].slice.call(document.querySelectorAll('.toc a'));
  var targets=links.map(function(a){{return document.querySelector(a.getAttribute('href'));}});
  var nav=[].slice.call(document.querySelectorAll('.topnav nav a'));
  function upd(){{
    var y=window.scrollY+120,best=-1;
    targets.forEach(function(t,i){{if(t&&t.offsetTop<=y)best=i;}});
    links.forEach(function(a,i){{a.classList.toggle('on',i===best);}});
    var top=0;
    var parts=[].slice.call(document.querySelectorAll('.part-head'));
    parts.forEach(function(p,i){{if(p.offsetTop<=y)top=i;}});
    nav.forEach(function(a,i){{a.classList.toggle('on',i===top);}});
  }}
  window.addEventListener('scroll',upd,{{passive:true}});
  upd();
}})();
</script>
</body>
</html>
"""


def main():
    for c in COURSES:
        out = render(c)
        with open(os.path.join(REPO, c["out"]), "w", encoding="utf-8") as f:
            f.write(out)
        print(f"wrote {c['out']:42s} {len(out):8,d} bytes")


if __name__ == "__main__":
    main()
