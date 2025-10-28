# AI Task Planning Template - Starter Framework

---

## 1. Task Overview

### Task Title
**Title:** Améliorer le prompt système Perplexity pour obtenir des résultats plus fiables et structurés

### Goal Statement
**Goal:** Optimiser le prompt système et utilisateur envoyé à l'API Perplexity pour maximiser la qualité, la fiabilité et la structure des réponses (titres, snippets, URLs valides).

---

## 2. Project Analysis & Current State

### Technology & Architecture
- **Frameworks & Versions:** FastAPI, Perplexity API (sonar model)
- **Language:** Python 3.11+
- **Database & ORM:** None

### Current State
Le service `perplexity_client.py` envoie un prompt système et utilisateur basique. Les résultats sont inconstants : parfois bien structurés (TITLE/SNIPPET/URL), parfois incomplets ou mal formatés, nécessitant le fallback d'extraction d'URLs.

---

## 3. Context & Problem Definition

### Problem Statement
Le prompt actuel ne garantit pas une réponse structurée fiable. L'API Perplexity peut retourner du texte non formaté, des URLs manquantes, ou des snippets trop longs/courts. Le taux de recours au fallback d'extraction d'URLs est élevé.

### Success Criteria
- [ ] Prompt système et utilisateur optimisés avec instructions claires et exemples
- [ ] Taux de parsing structuré (regex TITLE/SNIPPET/URL) > 80% sur tests réels
- [ ] Réduction des appels au fallback d'extraction d'URLs
- [ ] Snippets concis (1-2 phrases) et URLs toujours présentes
- [ ] Validation et logs détaillés sur la qualité des réponses

---

## 4. Development Mode Context
Local-only ; priorité à la qualité des résultats pour améliorer l'UX.

---

## 5. Technical Requirements

### Functional Requirements
- Améliorer le prompt système avec :
  - Instructions explicites sur le format de sortie
  - Exemples concrets de format attendu (few-shot)
  - Contraintes claires (URLs obligatoires, snippets brefs)
- Ajuster le prompt utilisateur pour spécifier le délai (24h ou 7 jours) et le nombre exact de résultats
- Ajouter validation côté parsing : log des réponses mal structurées pour analyse

### Non-Functional Requirements
- **Fiabilité:** Réduire la variabilité des formats de réponse
- **Performance:** Maintenir le timeout actuel (30s)
- **Observabilité:** Logger les réponses brutes pour debug et itération

### Technical Constraints
- Pas de changement au modèle Perplexity (sonar)
- Conserver le parsing existant (regex + fallback) comme filet de sécurité

---

## 6. Data & Database Changes
None.

---

## 7. API & Backend Changes
- Modifier `server/services/perplexity_client.py` :
  - Améliorer le prompt système (`system` role)
  - Améliorer le prompt utilisateur (`user` role)
  - Optionnel : ajouter des paramètres API (température, etc.) pour stabilité

---

## 8. Frontend Changes
None. Impact transparent pour l'utilisateur final (meilleure qualité des résultats affichés).

---

## 9. Implementation Plan
1. **Recherche & benchmark:** Tester différentes variantes de prompts avec l'API Perplexity
2. **Prompt système:** Ajouter exemples few-shot, renforcer contraintes de format
3. **Prompt utilisateur:** Clarifier délai et nombre de résultats
4. **Validation:** Tester sur plusieurs topics (technologie, politique, sport, etc.)
5. **Logging:** Logger réponses brutes pour analyse post-déploiement
6. **Itération:** Ajuster en fonction des logs et taux de parsing

---

## 10. Task Completion Tracking
- Tests manuels sur 5+ topics différents
- Vérifier logs : taux de matches regex vs fallback
- Comparer avant/après : qualité des snippets et présence d'URLs

### Documentation Updates
- Update `README.md` only for user-facing changes (features, installation, run instructions)
- Update `ARCHITECTURE.md` for technical changes (data models, services, API endpoints, architecture)

---

## 11. File Structure & Organization
- `server/services/perplexity_client.py` (méthode `search_latest` et `_parse_response`)

---

## 12. AI Agent Instructions
1) Analyser le prompt actuel et identifier faiblesses (manque d'exemples, instructions vagues)
2) Proposer 2-3 variantes de prompts améliorés (avec few-shot examples)
3) Implémenter la meilleure variante
4) Tester sur plusieurs topics et logger les résultats
5) Ajuster si nécessaire en fonction des logs

### Testing Procedure
**🚨 CRITICAL:** Before testing any changes, always follow the complete testing sequence defined in `.cursor/local-testing-procedure.mdc`:

1. **Clean port 8000**: Kill any existing process
2. **Setup venv**: Create/activate virtual environment and install dependencies
3. **Launch server**: `venv\Scripts\Activate.ps1; uvicorn server.main:app --reload`
4. **Verify health**: Test `http://127.0.0.1:8000/api/health` returns `{"status":"ok"}`
5. **Test topics:** Call `/api/get_news` with various topics and verify response quality

⚠️ **Never skip venv activation before running uvicorn** - it will fail with "command not found"

### Communication Preferences
Proposer plusieurs variantes de prompt avant implémentation ; expliquer rationale des choix.

### Code Quality Standards
Maintenir types explicites ; commenter les changements significatifs au prompt ; logger réponses brutes pour debug.

---

## 13. Second-Order Impact Analysis

### Impact Assessment
**Risques:**
- Un prompt trop contraignant pourrait réduire la richesse des réponses
- Coût API inchangé mais meilleur ROI par requête
- Nécessite validation continue (LLMs peuvent changer de comportement)

**Bénéfices:**
- UX améliorée : résultats plus fiables et présentables
- Moins de cas edge à gérer côté parsing
- Base pour futures améliorations (filtres, classement, etc.)


