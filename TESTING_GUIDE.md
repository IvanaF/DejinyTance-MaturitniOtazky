# Testing Guide - Wikipedia Links

## Quick Start
1. Open your browser and go to: **http://localhost:8000**
2. Navigate to topic **T02 - INDIE, ČÍNA, JAPONSKO** (this is where we fixed the Wikipedia links)

## What to Test

### 1. Main Page (Index)
- [ ] Open http://localhost:8000
- [ ] Verify topics list loads correctly
- [ ] Click on "T02 - INDIE, ČÍNA, JAPONSKO"

### 2. Topic Page - Wikipedia Links Testing

#### Test Czech Wikipedia Links (should work):
- [ ] **"Harappská kultura"** - Should link to Czech Wikipedia
- [ ] **"buddhismus"** - Should link to Czech Wikipedia  
- [ ] **"hinduismus"** - Should link to Czech Wikipedia
- [ ] **"Indus"** - Should link to Czech Wikipedia
- [ ] **"Indie"** - Should link to Czech Wikipedia
- [ ] **"Čína"** - Should link to English Wikipedia (was fixed)
- [ ] **"Japonsko"** - Should link to Czech Wikipedia

#### Test English Wikipedia Links (replaced broken Czech links):
- [ ] **"Bharata Natyam"** - Should link to English Wikipedia
- [ ] **"Kathak"** - Should link to English Wikipedia
- [ ] **"Kathakali"** - Should link to English Wikipedia
- [ ] **"Vishnu"** (Višnu) - Should link to English Wikipedia
- [ ] **"Shiva"** (Šiva) - Should link to English Wikipedia
- [ ] **"Kali"** (Kálí) - Should link to English Wikipedia
- [ ] **"Ganesha"** (Ganéša) - Should link to English Wikipedia
- [ ] **"Rigveda"** (Rgvéda) - Should link to English Wikipedia
- [ ] **"Upanishads"** (Upanišady) - Should link to English Wikipedia
- [ ] **"Ramayana"** (Rámajána) - Should link to English Wikipedia
- [ ] **"Sitar"** (sitár) - Should link to English Wikipedia
- [ ] **"Natya Shastra"** (Nátjašastra) - Should link to English Wikipedia

#### Test Common Terms:
- [ ] **"islám"** - Should link to English Wikipedia (was fixed)
- [ ] **"křesťanství"** - Should link to English Wikipedia (was fixed)

### 3. Link Behavior
For each link you test:
- [ ] Click opens in new tab/window
- [ ] Page loads correctly (not 404)
- [ ] Page has actual content (not empty)
- [ ] URL is correct (matches the term)
- [ ] Link is visually distinct (highlighted/underlined)

### 4. Visual Check
- [ ] Terms with links are visually distinct in the text
- [ ] Hover shows the URL in browser status bar
- [ ] Links don't break the text flow
- [ ] Multiple variants of same term work (e.g., "Harappská kultura" vs "Harappské kultury")

## Expected Results

### ✅ Should Work:
- All Czech Wikipedia links that exist (Harappská kultura, buddhismus, hinduismus, etc.)
- All English Wikipedia links we added (Bharata Natyam, Kathak, Vishnu, etc.)
- Common terms (islám, křesťanství) now point to English Wikipedia

### ❌ Should NOT Appear:
- No 404 errors
- No empty Wikipedia pages
- No broken links

## How to Report Issues

If you find a broken link:
1. Note the term name
2. Note the expected URL
3. Note what happens when you click (404, empty page, wrong page, etc.)
4. Check if the page exists manually on Wikipedia

## Quick Test Checklist

**Priority 1 - Most Important:**
- [ ] Harappská kultura (Czech) - **This was the main issue you reported**
- [ ] Bharata Natyam (English) - Should work now
- [ ] islám (English) - Was broken, now fixed
- [ ] křesťanství (English) - Was broken, now fixed

**Priority 2 - Other Fixed Links:**
- [ ] Vishnu, Shiva, Kali, Ganesha (all English)
- [ ] Indian dance forms (Bharata Natyam, Kathak, Kathakali, etc.)
- [ ] Vedic texts (Rigveda, Upanishads, etc.)

