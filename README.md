# 🎮 Laboratorio Pygame su GitHub Codespaces

Ambiente di sviluppo Python con Pygame, pronto all'uso nel browser.

## 🖥️ Accedere al desktop grafico

Pygame ha bisogno di una finestra grafica. Per aprirla:

1. Guarda in basso nella scheda **PORTS** (accanto a TERMINAL)
2. Trova la porta **6080** (noVNC)
3. Clicca sull'icona 🌐 per aprire noVNC nel browser
4. Se richiesta, inserisci la password: **pygame**

Si aprirà un desktop Linux nel browser.

## ▶️ Eseguire un programma Pygame

Nella finestra del desktop remoto (noVNC):

1. Clicca col tasto destro → **Applications → Terminal**
2. Digita:
```bash
cd /workspaces/*
python test_pygame.py
```
Usa le frecce direzionali per muovere il cerchio rosso.

## ⚠️ Note importanti

- **Commit e push** — Per non perdere il lavoro, fai commit su Git

## 🔧 Risoluzione problemi

| Problema | Soluzione |
|----------|-----------|
| Desktop nero o non risponde | Ricarica la pagina noVNC |
| Porta 6080 non visibile | Attendi che il container finisca di avviarsi |

## 📚 Risorse

- [Documentazione Pygame](https://www.pygame.org/docs/)
- [Documentazione Pymunk](https://www.pymunk.org/en/latest/)
