# Prompt pro Git commit a push do GitHubu

## Pravidla pro commit message

- **Jazyk:** Angličtina
- **Diakritika:** Žádná diakritika (bez háčků, čárek, kroužků)
- **Délka:** Krátká a výstižná
- **Formát:** Konvenční commit style (volitelně, ale preferováno)

## Příklady dobrých commit messages

✅ **DOBRÉ příklady:**
- `Add quality quiz questions for T03-T04, cleanup project structure`
- `Fix responsive design issues in mobile view`
- `Update topic materials with new content`
- `Add audio scripts for T02`
- `Refactor topic loader for better performance`
- `Update CSS styles for compact layout`
- `Create prompts for quiz questions generation`

❌ **ŠPATNÉ příklady (vyvaruj se):**
- `Přidání kvízových otázek pro T03 a T04` (česky)
- `Oprava chyb v responzivním designu` (česky, diakritika)
- `Úprava stylů pro kompaktní layout` (česky, diakritika)
- `Very long commit message that describes every single detail of what was changed and why it was changed and what the implications are` (příliš dlouhé)

## Workflow

1. Zkontrolovat změny:
   ```bash
   git status
   ```

2. Přidat všechny změny:
   ```bash
   git add -A
   ```
   nebo konkrétní soubory:
   ```bash
   git add <file1> <file2>
   ```

3. Zkontrolovat staged změny:
   ```bash
   git status --short
   ```

4. Vytvořit commit s výstižnou zprávou:
   ```bash
   git commit -m "Krátká zpráva v angličtině bez diakritiky"
   ```

5. Pushnout do GitHubu:
   ```bash
   git push
   ```

## Tipy

- Používej slovesa v imperativu (Add, Fix, Update, Create, Remove, Refactor)
- Začni velkým písmenem
- Nepiš tečku na konci
- Pokud je změna komplexní, použij více commitů s jasně definovanými změnami
- Pro větší změny můžeš použít víceřádkový commit message (bez `-m`, editor se otevře)

## Příklady podle typu změny

**Přidání nového obsahu:**
- `Add quiz questions for T03`
- `Add audio scripts for chapter T02`
- `Add new topic template structure`

**Opravy a úpravy:**
- `Fix mobile navigation drawer issue`
- `Fix quiz answer validation logic`
- `Update CSS for better readability`

**Refaktoring:**
- `Refactor topic loader to use dynamic imports`
- `Restructure data folder organization`

**Úklid:**
- `Remove temporary Python scripts`
- `Clean up unused CSS classes`
- `Move documentation to docs folder`

**Dokumentace:**
- `Update README with new features`
- `Add scaling guide documentation`
- `Update time tracker for session 3`

