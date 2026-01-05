# CV to Website Generator 🚀

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Transform your CV/Resume into a stunning, professional portfolio website in seconds using AI!

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🌟 Overview

**CV to Website Generator** is an AI-powered application that automatically converts your CV (PDF/DOCX) into a beautiful, responsive portfolio website. Upload your resume, and get a profession-tailored, animated, production-ready portfolio in minutes!

### Why Use This?

- ⚡ **Instant Generation**: Get your portfolio website in under 2 minutes
- 🎨 **Profession-Specific Design**: Automatically adapts design based on your career (Tech, Medical, Legal, Creative, Business, Academic)
- 🎭 **Unique Every Time**: Each generated website is unique, even for the same profession
- 📱 **Fully Responsive**: Works perfectly on desktop, tablet, and mobile
- 🚀 **Production-Ready**: Download and host anywhere immediately
- 💫 **Advanced Animations**: Smooth transitions, hover effects, and scroll animations
- 🎯 **No Coding Required**: Just upload your CV!

## ✨ Features

### Core Features

- 📄 **Multi-Format Support**: Upload PDF or DOCX files
- 🤖 **AI-Powered Design**: Uses Grok AI to generate beautiful, tailored websites
- 🎨 **6+ Profession Templates**: Tech, Medical, Legal, Creative, Business, Academic
- 🌈 **Dynamic Color Schemes**: 3+ color palettes per profession
- ✨ **Advanced Animations**: 15+ animation types including:
  - Fade-in effects
  - Scroll-based reveals
  - Hover transformations
  - Particle systems
  - Gradient animations
  - Typing effects
  - Counter animations

### Design Features

- 🎭 **Spectacular Header**: 
  - Full viewport hero section
  - Animated gradient backgrounds
  - 80-120px name display
  - Glassmorphism navigation
  - Floating particles

- 🏆 **Premium Footer**:
  - Multi-column layout
  - Social media links
  - Contact information
  - Back-to-top button
  - Smooth animations

- 📱 **Responsive Design**:
  - Mobile-first approach
  - Breakpoints: 768px, 1024px, 1440px
  - Touch-friendly interactions
  - Hamburger menu on mobile

### Portfolio Sections

- 🏠 **Hero Section**: Eye-catching introduction with animated background
- 👤 **About**: Professional bio with stats and profile image
- 💼 **Skills**: Visual skill indicators with progress bars
- 📊 **Experience**: Timeline-style work history
- 🎓 **Education**: Academic achievements and certifications
- 🚀 **Projects**: Portfolio showcase with hover effects
- 📧 **Contact**: Interactive form with validation

### Management Features

- 👁️ **Preview**: View your portfolio before publishing
- ⬇️ **Download**: Get HTML file for self-hosting
- 🌐 **Publish**: Host on the platform and get shareable URL
- 📋 **List All**: View all generated portfolios
- 🗑️ **Delete**: Remove unwanted portfolios

## 🎬 Demo

### Input
Upload your CV (PDF or DOCX format)

### Output
A stunning portfolio website with:
- Modern, profession-specific design
- Smooth animations and transitions
- Fully responsive layout
- Interactive elements
- Social media integration
- Contact form

### Live Example
Check out a generated portfolio: [Example Portfolio](#)

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework
- **Python 3.8+**: Core programming language
- **Grok AI API**: AI-powered code generation
- **PyPDF2**: PDF text extraction
- **python-docx**: DOCX processing
- **SQLAlchemy**: Database ORM
- **Uvicorn**: ASGI server

### Frontend (Generated)
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with animations
- **JavaScript (Vanilla)**: Interactive features
- **Google Fonts**: Professional typography
- **Font Awesome**: Icon library

### Features in Generated Sites
- CSS Custom Properties (Variables)
- CSS Grid & Flexbox
- Intersection Observer API
- Smooth Scroll
- Form Validation
- Responsive Design
- Glassmorphism Effects
- Gradient Animations

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Grok API Key ([Get one here](https://console.x.ai/))

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/cv-to-website.git
cd cv-to-website
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory:

```env
# Grok API Configuration
GROK_API_KEY=your_grok_api_key_here

# Server Configuration
BASE_URL=http://localhost:8000
DEBUG=True

# Database Configuration (optional)
DATABASE_URL=sqlite:///./cv_to_website.db

# File Upload Settings
MAX_FILE_SIZE=10485760  # 10MB in bytes
ALLOWED_EXTENSIONS=pdf,docx
```

### Step 5: Create Required Directories

```bash
mkdir uploads generated_portfolios hosted_portfolios
```

### Step 6: Run the Application

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `GROK_API_KEY` | Your Grok AI API key | - | ✅ Yes |
| `BASE_URL` | Base URL for the application | `http://localhost:8000` | ❌ No |
| `DEBUG` | Enable debug mode | `True` | ❌ No |
| `DATABASE_URL` | Database connection string | `sqlite:///./cv_to_website.db` | ❌ No |
| `MAX_FILE_SIZE` | Maximum upload file size (bytes) | `10485760` (10MB) | ❌ No |

### API Rate Limits

- Grok API: Varies by plan
- File Upload: 10MB maximum
- Timeout: 200 seconds per generation

## 🚀 Usage

### Method 1: Using the API

#### 1. Generate Portfolio

```bash
curl -X POST "http://localhost:8000/generate-portfolio" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/your/resume.pdf"
```

**Response:**
```json
{
  "portfolio_id": "abc-123-def-456",
  "filename": "portfolio_20240103_120000.html",
  "download_url": "http://localhost:8000/portfolio/download/abc-123-def-456",
  "preview_url": "http://localhost:8000/portfolio/preview/abc-123-def-456",
  "message": "✨ SPECTACULAR profession-tailored portfolio generated!"
}
```

#### 2. Preview Portfolio

Open in browser:
```
http://localhost:8000/portfolio/preview/{portfolio_id}
```

#### 3. Download Portfolio

```
http://localhost:8000/portfolio/download/{portfolio_id}
```

#### 4. Publish Portfolio

```bash
curl -X POST "http://localhost:8000/portfolio/publish/{portfolio_id}"
```

**Response:**
```json
{
  "message": "🚀 Portfolio published successfully!",
  "hosted_url": "http://localhost:8000/portfolio/abc-123-def-456",
  "portfolio_id": "abc-123-def-456"
}
```

#### 5. List All Portfolios

```bash
curl "http://localhost:8000/portfolio/list"
```

#### 6. Delete Portfolio

```bash
curl -X DELETE "http://localhost:8000/portfolio/{portfolio_id}"
```

### Method 2: Using Swagger UI

1. Open your browser and navigate to: `http://localhost:8000/docs`
2. You'll see the interactive API documentation
3. Try out endpoints directly from the browser
4. Upload files and test responses

### Method 3: Using Python Requests

```python
import requests

# Upload CV and generate portfolio
url = "http://localhost:8000/generate-portfolio"
files = {"file": open("resume.pdf", "rb")}
response = requests.post(url, files=files)
data = response.json()

portfolio_id = data["portfolio_id"]
preview_url = data["preview_url"]

print(f"Portfolio generated! Preview at: {preview_url}")

# Publish portfolio
publish_url = f"http://localhost:8000/portfolio/publish/{portfolio_id}"
publish_response = requests.post(publish_url)
hosted_url = publish_response.json()["hosted_url"]

print(f"Portfolio published at: {hosted_url}")
```

## 🔌 API Endpoints

### Portfolio Generation

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/generate-portfolio` | Upload CV and generate portfolio |
| `GET` | `/portfolio/preview/{id}` | Preview generated portfolio |
| `GET` | `/portfolio/download/{id}` | Download portfolio HTML file |
| `POST` | `/portfolio/publish/{id}` | Publish portfolio and get URL |
| `GET` | `/portfolio/{id}` | View published portfolio |
| `GET` | `/portfolio/list` | List all portfolios |
| `DELETE` | `/portfolio/{id}` | Delete a portfolio |

### System

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check and API info |
| `GET` | `/db-test` | Test database connection |
| `GET` | `/info` | Get API information |

### Detailed Endpoint Documentation

#### POST /generate-portfolio

**Request:**
- **Content-Type**: `multipart/form-data`
- **Body**: 
  - `file`: CV file (PDF or DOCX, max 10MB)

**Response:**
```json
{
  "portfolio_id": "string",
  "filename": "string",
  "download_url": "string",
  "preview_url": "string",
  "message": "string"
}
```

**Status Codes:**
- `200`: Portfolio generated successfully
- `400`: Invalid file type or format
- `413`: File too large
- `500`: Generation error
- `504`: Timeout error

## 📁 Project Structure

```
cv-to-website/
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   └── database.py          # Database configuration
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py            # User models
│   │   └── routes.py            # User routes
│   ├── cvs/
│   │   ├── __init__.py
│   │   ├── models.py            # CV models
│   │   └── routes.py            # Portfolio generation routes
│   └── __init__.py
├── uploads/                      # Temporary CV uploads
├── generated_portfolios/         # Generated HTML files
├── hosted_portfolios/            # Published portfolios
├── main.py                       # FastAPI application entry point
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (create this)
├── .gitignore                    # Git ignore file
└── README.md                     # This file
```

## 🔧 How It Works

### 1. Upload & Extract
```python
# User uploads CV (PDF/DOCX)
file = request.files['cv']

# Extract text from document
if file.endswith('.pdf'):
    text = extract_pdf_text(file)
elif file.endswith('.docx'):
    text = extract_docx_text(file)
```

### 2. AI Analysis
```python
# Grok AI analyzes CV and identifies:
- Profession (Tech, Medical, Legal, etc.)
- Skills and technologies
- Experience level
- Projects and achievements
- Contact information
```

### 3. Design Generation
```python
# AI generates profession-specific design:
- Color scheme (3+ palettes per profession)
- Typography (2-3 complementary fonts)
- Layout structure (unique each time)
- Animation styles (15+ types)
- Visual elements (icons, patterns, effects)
```

### 4. Code Creation
```python
# Complete HTML/CSS/JS generated:
- Semantic HTML5 structure
- Embedded CSS (3000-5000 lines)
- Vanilla JavaScript for interactions
- Responsive breakpoints
- Accessibility features
```

### 5. Output & Hosting
```python
# Three options:
1. Preview in browser
2. Download HTML file
3. Publish and get shareable URL
```

## 🎨 Customization

### Profession-Specific Styling

The generator automatically detects your profession and applies appropriate styling:

#### Tech/Engineering
- **Colors**: Electric Blue, Cyber Purple, Neon Green
- **Elements**: Code snippets, circuit patterns, tech icons
- **Animations**: Glitch effects, typing animations, particles

#### Medical
- **Colors**: Medical Blue, Healing Green, Navy
- **Elements**: Medical symbols, heartbeat lines, health icons
- **Animations**: Pulse effects, calm transitions

#### Legal
- **Colors**: Navy, Gold, Burgundy
- **Elements**: Scales of justice, pillars, law books
- **Animations**: Elegant transitions, gold shimmer

#### Creative
- **Colors**: Vibrant, bold combinations
- **Elements**: Abstract shapes, artistic patterns
- **Animations**: Dynamic morphing, color transitions

#### Business
- **Colors**: Corporate Blue, Professional Gray, Success Green
- **Elements**: Charts, graphs, growth arrows
- **Animations**: Professional slides, chart animations

#### Academic
- **Colors**: Academic Blue, Scholarly Brown, Forest Green
- **Elements**: Books, graduation caps, research icons
- **Animations**: Page turns, scholarly reveals

### Manual Customization

After downloading the HTML file, you can customize:

1. **Colors**: Edit CSS variables in `:root`
```css
:root {
  --primary-color: #your-color;
  --secondary-color: #your-color;
}
```

2. **Fonts**: Change Google Fonts link
```html
<link href="https://fonts.googleapis.com/css2?family=YourFont" rel="stylesheet">
```

3. **Content**: Edit HTML sections directly

4. **Images**: Replace placeholder images with your own

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Bugs

1. Check if the bug is already reported in [Issues](https://github.com/cadetsikandar/CV-to-Website/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Your environment details

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and its benefits
3. Provide examples or mockups if possible

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/cadetsikandar/CV-to-Website.git

# Create a branch
git checkout -b feature/your-feature

# Make changes and test
pytest tests/

# Commit and push
git add .
git commit -m "Your descriptive commit message"
git push origin feature/your-feature
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Sikandar ALi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 📧 Contact

### Project Maintainer
- **Name**: Sikandar Ali
- **Email**: sikandar.umrani.5@gmail.com.com
- **GitHub**: [@cadetsikandar](https://github.com/cadetsikandar)
- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/sikandar-ali-sk)

### Project Links
- **Repository**: [https://github.com/cadetsikandar/CV-to-Website](https://github.com/cadetsikandar/CV-to-Website)
- **Issues**: [https://github.com/cadetsikandar/CV-to-Website/issues](https://github.com/cadetsikandar/CV-to-Website/issues)
- **Discussions**: [https://github.com/cadetsikandar/CV-to-Website/discussions](https://github.com/cadetsikandar/CV-to-Website/discussions)

### Get Help
- 📚 [Documentation](https://github.com/cadetsikandar/CV-to-Website)

## 🙏 Acknowledgments

- **Grok AI** for powering the intelligent code generation
- **FastAPI** for the amazing web framework
- **Google Fonts** for beautiful typography
- **Font Awesome** for the icon library
- All contributors who helped improve this project

## 🗺️ Roadmap

### Version 2.0 (Planned)
- [ ] Multi-language support
- [ ] Custom theme builder
- [ ] Real-time editing
- [ ] Template marketplace
- [ ] Integration with GitHub Pages
- [ ] SEO optimization tools
- [ ] Analytics dashboard
- [ ] Team collaboration features

### Version 1.1 (In Progress)
- [x] Profession-specific designs
- [x] Advanced animations
- [x] Mobile responsiveness
- [ ] Dark mode support
- [ ] Export to multiple formats
- [ ] Custom domain support

## 📊 Statistics

- 🎨 **6+ Profession Templates**
- 🌈 **18+ Color Schemes**
- ✨ **15+ Animation Types**
- 📱 **100% Responsive**
- ⚡ **<2 Min Generation Time**
- 🎯 **0 Coding Required**

---

<div align="center">

### Made with ❤️ and Code

**If this project helped you, please give it a ⭐️!**

[Report Bug](https://github.com//cv-to-website/issues) · [Request Feature](https://github.com/yourusername/cv-to-website/issues)

</div>
