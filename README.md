# Flyer OS (Full BC Template)

静か × 精密 × ミニマルなホーム AI「Flyer」の  
Web プロトタイプ基盤。

- `flyer-core`: FastAPI ベースのコア（Intent / Decision / Action / Knowledge / State）
- `flyer-ui`: Next.js + React ベースの UI（CoreRing / VoiceInput / OutputPanel）

---

## セットアップ

### 1. Core

```bash
cd flyer-core
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
