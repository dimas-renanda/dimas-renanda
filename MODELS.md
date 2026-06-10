# MODELS.md — GitHub Copilot Model Reference

> Gunakan `/model <alias>` untuk ganti model di session.
> Alias pendek = shortcut; nama lengkap juga tetap bisa dipakai.

---

## 🟢 FREE (0x) — Unlimited, tidak makan quota

| Alias | Model | Terbaik untuk |
|-------|-------|---------------|
| `gpt4o` | github-copilot/gpt-4o | Chat umum, tanya-jawab, draft teks, summarize |
| `gpt4.1` | github-copilot/gpt-4.1 | Coding sehari-hari, debug ringan, Q&A teknis |
| `gpt5-mini` | github-copilot/gpt-5-mini | Chat cepat, tugas ringan, hemat token |

---

## 🟢 SANGAT MURAH (0.25x–0.33x) — Hampir gratis

| Alias | Model | Multiplier | Terbaik untuk |
|-------|-------|-----------|---------------|
| `haiku` / `haiku4.5` | claude-haiku-4.5 | 0.33x | Coding ringan, format teks, klasifikasi cepat |
| `gemini3-flash` | gemini-3-flash-preview | 0.33x | Summarize panjang, dokumen, multimodal ringan |
| `gpt5.4-mini` | gpt-5.4-mini | 0.33x | Coding cepat, autocomplete, tugas repetitif |

---

## 🟡 NORMAL (1x) — Standar premium

| Alias | Model | Multiplier | Terbaik untuk |
|-------|-------|-----------|---------------|
| `sonnet` / `sonnet4.5` | claude-sonnet-4.5 | 1x | Coding medium, refactor, review code |
| `sonnet4.6` / `sonnet` (default) | claude-sonnet-4.6 | 1x | Coding kompleks, nulis panjang, analisis |
| `gemini-pro` / `gemini2.5` | gemini-2.5-pro | 1x | Riset, long context, dokumen panjang, math |
| `gemini3.1` | gemini-3.1-pro-preview | 1x | Riset terbaru, long context, multimodal |
| `gemini3pro` | gemini-3-pro-preview | 1x | Alternatif Gemini 3, tugas analitis |
| `gpt5.1` | gpt-5.1 | 1x | Coding advanced, agentic tasks |
| `gpt5.2` | gpt-5.2 | 1x | General advanced, reasoning medium |
| `gpt5.3` | gpt-5.3-codex | 1x | Coding intensif, code generation |
| `gpt5.4` | gpt-5.4 | 1x | Reasoning + coding balanced |
| `codex` | gpt-5.1-codex | 1x | Code generation, autocomplete canggih |
| `codex-mini` | gpt-5.1-codex-mini | 1x | Coding ringan-medium, lebih hemat dari codex |
| `codex5.2` | gpt-5.2-codex | 1x | Coding kompleks generasi terbaru |
| `grok` | grok-code-fast-1 | ~1x | Coding cepat, alternatif GPT untuk dev |

---

## 🟠 MAHAL (3x) — Gunakan kalau benar-benar butuh

| Alias | Model | Multiplier | Terbaik untuk |
|-------|-------|-----------|---------------|
| `opus4.5` | claude-opus-4.5 | 3x | Tugas sangat kompleks, deep reasoning, arsitektur |
| `opus` / `opus4.6` | claude-opus-4.6 | 3x | Tugas berat, nulis panjang berkualitas tinggi |

---

## 🔴 SANGAT MAHAL — Hanya untuk keperluan kritis

| Alias | Model | Multiplier | Terbaik untuk |
|-------|-------|-----------|---------------|
| `gpt5` | gpt-5 | ~5x | Reasoning paling canggih OpenAI |
| `gpt5.5` | gpt-5.5 | 7.5x | Frontier task, research-grade |
| `codex-max` | gpt-5.1-codex-max | ~7.5x | Coding project besar, agentic coding |
| `opus4.7` | claude-opus-4.7 | 15x | ⚠️ Paling canggih Claude, gunakan hemat-hemat |

---

## 💡 Rekomendasi Penggunaan Harian

```
Tanya cepat / chat biasa    → /model gpt4o       (0x, gratis)
Coding sehari-hari          → /model gpt4.1      (0x, gratis)
Summarize / dokumen panjang → /model gemini3-flash (0.33x, murah)
Coding serius / review      → /model sonnet4.6   (1x, standar)
Riset panjang / analisis    → /model gemini2.5   (1x, standar)
Tugas berat / deep thinking → /model opus4.6     (3x, hemat-hemat)
```

---

## 📌 Default saat ini
Model default: `github-copilot/claude-sonnet-4.6` (1x)

Ganti default permanen: `openclaw models set <model-id>`
