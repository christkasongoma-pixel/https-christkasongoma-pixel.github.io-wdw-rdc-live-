# WDW News Today – RDC en direct

Page d'actualités sur la RDC avec badges de vérification par sources, plus une version « complète » avec modules tiers et modèle de sécurité.

## Contenu
- `index.html` : page « RDC en direct » (actualités recoupées + onglet Connexions).
- `full.html` : page complète avec scripts tiers chargés après consentement et CSP.
- `security-headers.conf` : en-têtes de sécurité nginx (CSP, HSTS, etc.).
- `data/feed-latest.json` : flux d'actualités vérifié au 11 octobre 2026.
- `archive/` : versions intermédiaires (`head-clean.html`, `page.html`).

## À savoir
- `index.html` a été conçue pour l'hébergement Claude. Hors de cet hébergement, la base partagée n'existe pas : la page affiche l'instantané intégré et le compteur de connexions reste à zéro.
- Dans `full.html`, remplacez `PIXEL_ID`, `CONFIG_ID`, `WRITE_KEY`, `SITE_ID` et `REPLACE_ME`.
- Si vous modifiez le script inline de `full.html`, recalculez l'empreinte sha256 du CSP.
