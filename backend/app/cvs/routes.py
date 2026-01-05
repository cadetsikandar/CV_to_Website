# app/cvs/routes.py
import os
import re
import uuid
from datetime import datetime
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from PyPDF2 import PdfReader
from docx import Document
import requests
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

UPLOAD_DIR = "uploads"
GENERATED_DIR = "generated_portfolios"
HOSTED_DIR = "hosted_portfolios"

# Create necessary directories
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(GENERATED_DIR, exist_ok=True)
os.makedirs(HOSTED_DIR, exist_ok=True)

# Configure Grok API
GROK_API_KEY = os.getenv("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY not found in environment variables")

GROK_API_URL = "https://api.x.ai/v1/chat/completions"

# Store generated portfolios metadata
portfolios_db = {}


def extract_text(file_path: str):
    """Extract text from PDF or DOCX file"""
    paragraphs = []

    try:
        if file_path.endswith(".pdf"):
            with open(file_path, 'rb') as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    text = page.extract_text() or ""
                    for para in text.split("\n\n"):
                        clean_para = " ".join(para.split())
                        if clean_para:
                            paragraphs.append(clean_para)

        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            for para in doc.paragraphs:
                clean_para = " ".join(para.text.split())
                if clean_para:
                    paragraphs.append(clean_para)
        else:
            raise ValueError("Unsupported file type")

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error extracting text: {str(e)}")

    readable_text = "\n\n".join(paragraphs)
    flat_text = " ".join(paragraphs)

    return {
        "paragraphs": paragraphs,
        "readable_text": readable_text,
        "flat_text": flat_text
    }


def clean_html_code(html_code: str) -> str:
    """Clean and format HTML code properly"""
    
    # Remove markdown code blocks
    if '```html' in html_code:
        html_code = html_code.split('```html')[1].split('```')[0]
    elif '```' in html_code:
        parts = html_code.split('```')
        if len(parts) >= 3:
            html_code = parts[1]
    
    # Replace literal \n with actual newlines
    html_code = html_code.replace('\\n', '\n')
    
    # Remove excessive newlines (more than 2 consecutive)
    html_code = re.sub(r'\n{3,}', '\n\n', html_code)
    
    # Remove leading/trailing whitespace
    html_code = html_code.strip()
    
    # Ensure proper HTML structure
    if not html_code.startswith('<!DOCTYPE html>') and not html_code.startswith('<html'):
        html_match = re.search(r'<!DOCTYPE html>|<html', html_code, re.IGNORECASE)
        if html_match:
            html_code = html_code[html_match.start():]
    
    return html_code


@router.post("/generate-portfolio")
async def generate_portfolio(file: UploadFile = File(...)):
    """
    Upload a CV and generate a portfolio website
    Returns: portfolio_id, download_url, preview_url
    """
    # Validate file type
    if not (file.filename.endswith(".pdf") or file.filename.endswith(".docx")):
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported")

    file_path = None
    try:
        # Save uploaded file temporarily
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        contents = await file.read()
        
        # Validate file size (10MB max)
        MAX_FILE_SIZE = 10 * 1024 * 1024
        if len(contents) > MAX_FILE_SIZE:
            raise HTTPException(status_code=413, detail="File too large. Maximum size is 10MB")
        
        with open(file_path, "wb") as f:
            f.write(contents)

        # Extract text
        data = extract_text(file_path)

        # Enhanced prompt for Grok with MAXIMUM styling and uniqueness
        prompt = f"""
You are an elite web designer who creates award-winning, breathtaking portfolio websites. Each website must be a UNIQUE MASTERPIECE tailored to the person's profession.

🎯 ANALYZE THE PROFESSION FIRST:
Read the CV carefully and identify the person's primary profession/role (e.g., Computer Vision Engineer, Doctor, Lawyer, Designer, Developer, Data Scientist, Marketing Professional, etc.)

📊 PROFESSION-SPECIFIC DESIGN SYSTEMS:

**TECH/ENGINEERING (Computer Vision Engineer, Software Developer, Data Scientist, AI/ML Engineer):**
- Color Scheme: Choose randomly from:
  * Option 1: Electric Blue (#00D9FF), Cyber Purple (#9D4EDD), Neon Green (#39FF14), Dark Navy (#0A0E27)
  * Option 2: Matrix Green (#00FF41), Deep Purple (#6B00B6), Dark Gray (#1A1A1D), Neon Yellow (#FFF01F)
  * Option 3: Cyberpunk Pink (#FF006E), Electric Cyan (#00F5FF), Dark Slate (#0F0F1E), Hot Orange (#FF4500)
- Aesthetic: Sleek, modern, minimalist, high-tech, digital, futuristic
- Visual Elements: Circuit patterns, code snippets as background, hexagonal grids, glowing effects, matrix-style animations, binary code patterns
- Fonts: Monospace for code elements (JetBrains Mono, Fira Code, Source Code Pro) + Modern sans-serif (Inter, Space Grotesk, Poppins)
- Icons: Tech symbols, chip designs, neural network diagrams, terminal icons, brackets
- Animations: Digital glitch effects, typing animations, particle systems, holographic effects, scanning lines
- Header Style: Glowing neon text, tech grid background, animated code rain, holographic effects

**MEDICAL (Doctor, Surgeon, Nurse, Healthcare Professional):**
- Color Scheme: Choose randomly from:
  * Option 1: Medical Blue (#0077BE), Clean White (#FFFFFF), Healing Green (#00A86B), Navy (#003366)
  * Option 2: Hospital Teal (#008B8B), Soft Cream (#FFF8DC), Mint Green (#98FB98), Deep Blue (#000080)
  * Option 3: Healthcare Purple (#6A0DAD), Pearl White (#F8F8FF), Fresh Green (#32CD32), Dark Teal (#008080)
- Aesthetic: Clean, trustworthy, professional, calming, sterile yet warm, compassionate
- Visual Elements: Medical cross symbols, heartbeat lines (EKG), stethoscope icons, DNA helixes, subtle pulse animations, caduceus
- Fonts: Professional serif (Crimson Text, Merriweather, Lora) mixed with clean sans-serif (Raleway, Nunito)
- Icons: Medical symbols, caduceus, health icons, heart, pulse, medical equipment
- Animations: Smooth, calming transitions, heartbeat pulse effects, gentle fades, breathing animations
- Header Style: Clean professional layout, subtle pulse animations, medical symbol watermarks, calming gradient

**LEGAL (Lawyer, Advocate, Attorney, Judge):**
- Color Scheme: Choose randomly from:
  * Option 1: Professional Navy (#1A1A2E), Gold Accents (#D4AF37), Burgundy (#800020), Cream (#F5F5DC)
  * Option 2: Dark Charcoal (#36454F), Bronze (#CD7F32), Wine Red (#722F37), Beige (#F5DEB3)
  * Option 3: Midnight Blue (#191970), Silver (#C0C0C0), Mahogany (#C04000), Ivory (#FFFFF0)
- Aesthetic: Authoritative, prestigious, traditional yet modern, sophisticated, dignified
- Visual Elements: Scales of justice, law book symbols, pillar designs, subtle marble textures, gavel icons, classical columns
- Fonts: Elegant serif fonts (Playfair Display, Cormorant Garamond, Libre Baskerville), professional spacing
- Icons: Gavel, scales, legal documents, courthouse pillars, law books, certificates
- Animations: Elegant, dignified transitions, subtle gold shimmer effects, page turn effects, classic fades
- Header Style: Prestigious banner with columns, embossed text effect, gold accents, classical elegance

**CREATIVE (Designer, Artist, Photographer, Creative Director):**
- Color Scheme: Choose randomly from bold, vibrant, unexpected combinations:
  * Option 1: Magenta (#FF006E), Electric Yellow (#FFBE0B), Turquoise (#06FFA5), Deep Purple (#3A0CA3)
  * Option 2: Hot Pink (#FF1493), Lime Green (#32CD32), Bright Orange (#FF8C00), Royal Blue (#4169E1)
  * Option 3: Coral (#FF7F50), Aqua (#00FFFF), Violet (#8F00FF), Sunshine Yellow (#FFD700)
- Aesthetic: Artistic, bold, expressive, unconventional layouts, experimental, vibrant
- Visual Elements: Geometric shapes, abstract patterns, paintbrush strokes, gallery-style layouts, color splashes, artistic frames
- Fonts: Artistic, expressive fonts (Bebas Neue, Oswald, Righteous, Archivo Black)
- Icons: Palette, brush, camera, creative tools, paint splatters, design elements
- Animations: Dynamic, playful, morphing shapes, color transitions, paint drip effects, creative reveals
- Header Style: Bold artistic typography, abstract background shapes, vibrant gradients, creative asymmetry

**BUSINESS (MBA, Manager, Consultant, Entrepreneur, Finance):**
- Color Scheme: Choose randomly from:
  * Option 1: Corporate Blue (#0A2463), Professional Gray (#6C757D), Success Green (#28A745), Confidence Red (#DC3545)
  * Option 2: Executive Navy (#001F3F), Slate Gray (#708090), Growth Green (#2ECC71), Burgundy (#8B0000)
  * Option 3: Business Teal (#008080), Charcoal (#36454F), Emerald (#50C878), Crimson (#DC143C)
- Aesthetic: Professional, polished, executive, results-driven, corporate, sophisticated
- Visual Elements: Charts, graphs, growth arrows, building silhouettes, briefcase icons, data visualizations
- Fonts: Corporate sans-serif (Roboto, Open Sans, Lato, Montserrat)
- Icons: Briefcase, graph trends, handshake, buildings, money symbols, upward arrows
- Animations: Professional slides, chart animations, growth indicators, smooth fades
- Header Style: Executive banner, clean corporate layout, professional gradient, business iconography

**ACADEMIC/RESEARCH (Professor, Researcher, Scientist, PhD):**
- Color Scheme: Choose randomly from:
  * Option 1: Academic Blue (#003366), Scholarly Brown (#8B4513), Ivory (#FFFFF0), Forest Green (#228B22)
  * Option 2: Oxford Blue (#002147), Burgundy (#800020), Parchment (#F1E9D2), Olive (#808000)
  * Option 3: Cambridge Blue (#A3C1AD), Maroon (#800000), Cream (#FFFDD0), Dark Green (#013220)
- Aesthetic: Scholarly, intellectual, authoritative, traditional academia meets modern
- Visual Elements: Books, graduation caps, academic laurels, research icons, publications, citations
- Fonts: Academic serif (EB Garamond, Libre Baskerville, Merriweather)
- Icons: Books, microscope, graduation cap, research papers, academic awards
- Animations: Page turns, scholarly reveals, dignified fades
- Header Style: Academic crest style, traditional banner, intellectual elegance

🎨 CRITICAL: CREATE UNIQUENESS EVERY TIME:

Even for the same profession, make each website COMPLETELY DIFFERENT by:

1. **Randomize Layout Patterns:**
   - Vary section orders (after hero, mix up About/Skills/Experience)
   - Alternate between left/right image placements
   - Use different grid patterns (2-col, 3-col, masonry, asymmetric)
   - Change card vs. timeline vs. list layouts

2. **Vary Visual Styles:**
   - Rotate through different color palettes (provide 3+ per profession)
   - Change border-radius (sharp, rounded, pill-shaped)
   - Alternate shadow intensities (subtle to dramatic)
   - Mix flat design vs. depth/3D effects

3. **Diverse Animation Approaches:**
   - Rotate animation types: fade-in, slide-up, scale, rotate, flip
   - Vary animation timing and easing functions
   - Different hover effects each time: lift, glow, scale, tilt, shimmer
   - Change transition speeds (fast, medium, slow)

4. **Typography Variations:**
   - Use different Google Font combinations each time
   - Vary heading sizes and weights
   - Change letter-spacing and line-heights
   - Alternate between uppercase, sentence case, title case

5. **Background Diversity:**
   - Option 1: Solid gradient
   - Option 2: Animated gradient mesh
   - Option 3: Geometric patterns
   - Option 4: Particle effects
   - Option 5: Wave animations
   - Option 6: Abstract shapes
   - Option 7: Grid patterns with parallax

6. **Navigation Styles:**
   - Option 1: Top centered
   - Option 2: Top split (logo left, menu right)
   - Option 3: Side navigation
   - Option 4: Hamburger full-screen overlay
   - Vary glassmorphism intensity

7. **Section Layout Variations:**
   - Skills: Grid cards / Circular progress / Linear bars / Tag cloud
   - Experience: Vertical timeline / Horizontal timeline / Card grid / List with icons
   - Projects: Masonry / Equal grid / Carousel / Tabs
   - Contact: Form + info side-by-side / Form centered / Split screen

🎨 SPECTACULAR HEADER DESIGN (CRITICAL - 40% OF EFFORT HERE):

The header is the HERO - make it absolutely stunning:

1. **Full Viewport Hero (100vh minimum)**
   
2. **Background Effects (Choose 1-2 randomly):**
   - Animated gradient that shifts colors smoothly (background-size: 400% 400%)
   - Floating particle system (CSS-only using ::before/::after with animations)
   - Geometric shapes rotating/moving on scroll
   - Wave animations at bottom using SVG or CSS
   - 3D perspective text effects with transforms
   - Parallax layers with different scroll speeds
   - Mesh gradient with multiple colors
   - Abstract animated shapes
   - Code rain (for tech)
   - Pulse/heartbeat effects (for medical)

3. **Name Display - Make it ICONIC (HUGE):**
   - Font size: 80-120px on desktop, 48-64px on mobile
   - Profession-specific styling:
     * **Tech:** text-shadow: 0 0 20px #00D9FF, 0 0 40px #9D4EDD; letter-spacing: 8px; glowing effect
     * **Medical:** Clean bold with text-shadow: 0 2px 4px rgba(0,0,0,0.1); trustworthy weight
     * **Legal:** Elegant serif with gold underline or gradient background
     * **Creative:** Gradient text fill with -webkit-background-clip: text;
     * **Business:** Bold sans-serif with professional shadow

   - Text Animations (Choose 1):
     * Fade in + slide up
     * Typewriter effect
     * Glitch effect (for tech)
     * Letter-by-letter reveal
     * Gradient animation
     * 3D flip reveal

4. **Professional Title/Tagline:**
   - Below name, 24-32px
   - Animated separately (delay 0.5s after name)
   - Add animated underline that draws in
   - Or rotating text showing multiple skills

5. **Navigation Bar - PREMIUM QUALITY:**
   - Position: fixed top with glassmorphism
   - backdrop-filter: blur(10px)
   - Smooth transitions on all elements
   - Active section highlighted
   - Hover effects with animations
   - Mobile: Animated hamburger menu

6. **Hero Interactive Elements:**
   - Large CTA buttons with animations
   - Social media icons with hover effects
   - Scroll indicator animation
   - Optional custom cursor trail

7. **Advanced CSS Animations:**

@keyframes gradientShift {{
  0%, 100% {{ background-position: 0% 50%; }}
  50% {{ background-position: 100% 50%; }}
}}

@keyframes float {{
  0%, 100% {{ transform: translateY(0); }}
  50% {{ transform: translateY(-20px); }}
}}

@keyframes glow {{
  0%, 100% {{ box-shadow: 0 0 5px currentColor; }}
  50% {{ box-shadow: 0 0 20px currentColor; }}
}}

🏆 PREMIUM FOOTER DESIGN (EQUALLY IMPORTANT):

1. **Multi-Column Layout:**
   Desktop: [About | Quick Links | Social Media | Contact]
   Mobile: Stack vertically

2. **Styling:**
   - Dark background with gradient
   - Perfect typography and spacing
   - Beautiful hover effects

3. **Footer Sections:**
   - About: Mini bio, availability badge
   - Quick Links: All sections with hover effects
   - Social: Large icons with animations
   - Contact: Email, phone, location with icons

4. **Footer Bottom:**
   - Copyright notice
   - "Made with ❤️ and Code"
   - Back to top button

5. **Animations:**
   - Fade in on scroll
   - Hover effects on all elements
   - Social icons lift and glow

💫 ADVANCED ANIMATIONS TO IMPLEMENT:

**Scroll-Based:**
- Intersection Observer for reveals
- Fade in from bottom
- Scale up for cards
- Counter animations
- Progress bars
- Timeline sequence

**Hover Effects:**
- Cards: translateY(-10px) + shadow
- Buttons: scale(1.05) + glow
- Images: zoom in
- Links: underline expand
- Icons: rotate or bounce

**JavaScript Features:**
- Smooth scroll
- Active nav highlighting
- Typing effect
- Counter animation
- Mobile menu toggle
- Back to top button
- Form validation

🎯 SECTION SPECIFICATIONS:

**ABOUT:** Two-column, image with creative border, stats counter, download CV button

**SKILLS:** Grid layout, cards with icons, skill level indicators, color-coded, stagger animation

**EXPERIENCE:** Vertical timeline, cards with hover, duration badges, tech tags

**EDUCATION:** Cards or timeline, institution names, GPA/honors, achievements

**PROJECTS:** Grid of cards, image with overlay, tech stack badges, view buttons

**CONTACT:** Form with floating labels, validation, contact info with icons

📱 RESPONSIVE DESIGN:

/* Mobile First */
@media (min-width: 768px) {{ /* Tablet 2-col */ }}
@media (min-width: 1024px) {{ /* Desktop 3-col */ }}
@media (min-width: 1440px) {{ /* Large Desktop */ }}

🎨 CSS CUSTOM PROPERTIES:

:root {{
  --primary-color: #color;
  --secondary-color: #color;
  --spacing-sm: 16px;
  --spacing-lg: 48px;
  --radius-md: 8px;
  --shadow-lg: 0 10px 40px rgba(0,0,0,0.15);
  --transition-base: 0.3s ease;
}}

📋 HTML STRUCTURE:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Name] - [Title] | Portfolio</title>
    <link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* ALL CSS HERE */
    </style>
</head>
<body>
    <nav class="navbar">...</nav>
    <header id="home" class="hero">...</header>
    <section id="about" class="about">...</section>
    <section id="skills" class="skills">...</section>
    <section id="experience" class="experience">...</section>
    <section id="education" class="education">...</section>
    <section id="projects" class="projects">...</section>
    <section id="contact" class="contact">...</section>
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-about">...</div>
            <div class="footer-links">...</div>
            <div class="footer-social">...</div>
            <div class="footer-contact">...</div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 [Name]. All Rights Reserved.</p>
            <button id="backToTop"><i class="fas fa-arrow-up"></i></button>
        </div>
    </footer>
    <script>
        /* ALL JAVASCRIPT HERE */
    </script>
</body>
</html>

📝 CV DATA:
{data['flat_text']}

✅ CHECKLIST:
✅ Analyze profession and use appropriate design
✅ Use profession-specific colors and fonts
✅ 80-120px name in header
✅ Animated background effects
✅ Glassmorphism navigation
✅ Premium multi-column footer
✅ Back-to-top button
✅ 10+ animation types
✅ Intersection Observer
✅ Hover effects everywhere
✅ Smooth scroll
✅ Active nav highlighting
✅ Mobile hamburger menu
✅ CSS Custom Properties
✅ Fully responsive
✅ Typing/animated text
✅ Counter animations
✅ Floating labels
✅ Social icons with animations
✅ All sections included
✅ Production-ready
✅ Semantic HTML5
✅ Proper meta tags

🚀 RANDOMIZE FOR UNIQUENESS:
- Color palette
- Layout patterns
- Animation types
- Typography
- Background effects
- Section layouts
- Border styles
- Shadows
- Hover effects

CREATE A $10,000+ MASTERPIECE!

Return ONLY HTML code starting with <!DOCTYPE html>.
"""

        # Call Grok API
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GROK_API_KEY}"
            }
            
            payload = {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an award-winning web designer and frontend developer who creates stunning, unique, modern portfolio websites. Every website you create is a masterpiece with beautiful animations, perfect typography, and professional styling. You always include complete, production-ready code with all CSS and JavaScript embedded."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "model": "grok-2-latest",
                "stream": False,
                "temperature": 0.9,  # Higher for more creativity
                "max_tokens": 25000  # Increased for more detailed code
            }
            
            response = requests.post(
                GROK_API_URL,
                headers=headers,
                json=payload,
                timeout=180  # Increased timeout
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Grok API error: {response.status_code}: {response.text}"
                )
            
            response_data = response.json()
            website_code = response_data['choices'][0]['message']['content']
            
            # Clean the HTML code
            website_code = clean_html_code(website_code)
            
            # Verify the HTML contains styling
            if '<style>' not in website_code.lower():
                raise HTTPException(
                    status_code=500,
                    detail="Generated HTML is missing CSS styling. Please try again."
                )
            
        except requests.exceptions.Timeout:
            raise HTTPException(status_code=504, detail="Grok API request timed out. The portfolio is being generated, please try again.")
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Grok API request error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Grok API error: {str(e)}")

        # Generate unique portfolio ID
        portfolio_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portfolio_{timestamp}.html"
        
        # Save the generated HTML file
        output_path = os.path.join(GENERATED_DIR, filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(website_code)
        
        # Store metadata
        portfolios_db[portfolio_id] = {
            "filename": filename,
            "filepath": output_path,
            "created_at": timestamp,
            "original_cv": file.filename,
            "is_published": False,
            "hosted_url": None
        }
        
        # Get base URL (you should set this in .env for production)
        base_url = os.getenv("BASE_URL", "http://localhost:8000")
        
        return {
            "portfolio_id": portfolio_id,
            "filename": filename,
            "download_url": f"{base_url}/portfolio/download/{portfolio_id}",
            "preview_url": f"{base_url}/portfolio/preview/{portfolio_id}",
            "message": "✨ Stunning portfolio generated successfully! Preview it now!"
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating portfolio: {str(e)}")
    
    finally:
        # Cleanup: remove uploaded file
        if file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass


@router.get("/portfolio/preview/{portfolio_id}")
async def preview_portfolio(portfolio_id: str):
    """
    Preview the generated portfolio website
    """
    if portfolio_id not in portfolios_db:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    
    portfolio = portfolios_db[portfolio_id]
    filepath = portfolio["filepath"]
    
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Portfolio file not found")
    
    with open(filepath, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    return HTMLResponse(content=html_content)


@router.get("/portfolio/download/{portfolio_id}")
async def download_portfolio(portfolio_id: str):
    """
    Download the generated portfolio HTML file
    """
    if portfolio_id not in portfolios_db:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    
    portfolio = portfolios_db[portfolio_id]
    filepath = portfolio["filepath"]
    filename = portfolio["filename"]
    
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Portfolio file not found")
    
    return FileResponse(
        path=filepath,
        filename=filename,
        media_type="text/html"
    )


@router.post("/portfolio/publish/{portfolio_id}")
async def publish_portfolio(portfolio_id: str):
    """
    Publish/host the portfolio and get a public URL
    """
    if portfolio_id not in portfolios_db:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    
    portfolio = portfolios_db[portfolio_id]
    
    if portfolio["is_published"]:
        return {
            "message": "Portfolio already published",
            "hosted_url": portfolio["hosted_url"],
            "portfolio_id": portfolio_id
        }
    
    # Copy file to hosted directory
    source_path = portfolio["filepath"]
    hosted_filename = f"{portfolio_id}.html"
    hosted_path = os.path.join(HOSTED_DIR, hosted_filename)
    
    with open(source_path, "r", encoding="utf-8") as src:
        with open(hosted_path, "w", encoding="utf-8") as dst:
            dst.write(src.read())
    
    # Update metadata
    base_url = os.getenv("BASE_URL", "http://localhost:8000")
    hosted_url = f"{base_url}/portfolio/{portfolio_id}"
    
    portfolios_db[portfolio_id]["is_published"] = True
    portfolios_db[portfolio_id]["hosted_url"] = hosted_url
    portfolios_db[portfolio_id]["hosted_path"] = hosted_path
    
    return {
        "message": "🚀 Portfolio published successfully!",
        "hosted_url": hosted_url,
        "portfolio_id": portfolio_id
    }


@router.get("/portfolio/{portfolio_id}")
async def view_hosted_portfolio(portfolio_id: str):
    """
    View the published portfolio at its public URL
    """
    if portfolio_id not in portfolios_db:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    
    portfolio = portfolios_db[portfolio_id]
    
    if not portfolio["is_published"]:
        raise HTTPException(status_code=404, detail="Portfolio not published yet")
    
    hosted_path = portfolio.get("hosted_path")
    
    if not hosted_path or not os.path.exists(hosted_path):
        raise HTTPException(status_code=404, detail="Hosted portfolio file not found")
    
    with open(hosted_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    return HTMLResponse(content=html_content)


@router.get("/portfolio/list")
async def list_portfolios():
    """
    List all generated portfolios
    """
    portfolios = []
    base_url = os.getenv("BASE_URL", "http://localhost:8000")
    
    for portfolio_id, data in portfolios_db.items():
        portfolios.append({
            "portfolio_id": portfolio_id,
            "filename": data["filename"],
            "created_at": data["created_at"],
            "original_cv": data["original_cv"],
            "is_published": data["is_published"],
            "preview_url": f"{base_url}/portfolio/preview/{portfolio_id}",
            "download_url": f"{base_url}/portfolio/download/{portfolio_id}",
            "hosted_url": data["hosted_url"] if data["is_published"] else None
        })
    
    return {
        "total": len(portfolios),
        "portfolios": portfolios
    }


@router.delete("/portfolio/{portfolio_id}")
async def delete_portfolio(portfolio_id: str):
    """
    Delete a generated portfolio
    """
    if portfolio_id not in portfolios_db:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    
    portfolio = portfolios_db[portfolio_id]
    
    # Delete files
    try:
        if os.path.exists(portfolio["filepath"]):
            os.remove(portfolio["filepath"])
        
        if portfolio["is_published"] and "hosted_path" in portfolio:
            if os.path.exists(portfolio["hosted_path"]):
                os.remove(portfolio["hosted_path"])
    except Exception as e:
        print(f"Error deleting files: {e}")
    
    # Remove from database
    del portfolios_db[portfolio_id]
    
    return {
        "message": "Portfolio deleted successfully",
        "portfolio_id": portfolio_id
    }