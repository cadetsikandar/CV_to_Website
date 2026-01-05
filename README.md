<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Portfolio of Sikandar Ali, Deep Learning Engineer">
    <meta name="keywords" content="Sikandar Ali, Deep Learning, Python Developer, Portfolio">
    <meta name="author" content="Sikandar Ali">
    <title>Sikandar Ali - Deep Learning Engineer</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&family=Roboto:wght@400;700&family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #667eea;
            --secondary-color: #764ba2;
            --accent-color: #4facfe;
            --text-color: #333;
            --bg-color: #f9f9f9;
            --card-bg: rgba(255, 255, 255, 0.8);
            --box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            --border-radius: 12px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background: var(--bg-color);
            overflow-x: hidden;
        }

        h1, h2, h3 {
            font-family: 'Space Grotesk', sans-serif;
            margin-bottom: 20px;
        }

        h1 {
            font-size: 48px;
            line-height: 1.2;
        }

        h2 {
            font-size: 36px;
        }

        h3 {
            font-size: 24px;
        }

        p {
            font-size: 18px;
            margin-bottom: 20px;
        }

        a {
            color: var(--accent-color);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        a:hover {
            color: var(--primary-color);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            z-index: 1000;
            transition: all 0.3s ease;
        }

        nav.scrolled {
            background: rgba(255, 255, 255, 0.95);
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }

        .logo {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 24px;
            color: var(--primary-color);
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 30px;
        }

        .nav-links a {
            font-weight: 700;
            transition: transform 0.3s ease, color 0.3s ease;
        }

        .nav-links a:hover {
            transform: translateY(-2px);
            color: var(--secondary-color);
        }

        .nav-links a.active {
            color: var(--secondary-color);
        }

        .hamburger {
            display: none;
            cursor: pointer;
        }

        .hamburger div {
            width: 30px;
            height: 3px;
            background-color: var(--text-color);
            margin: 6px 0;
            transition: 0.4s;
        }

        /* Hero Section */
        .hero {
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
        }

        .hero-content {
            text-align: center;
            z-index: 2;
        }

        .hero h1 {
            font-size: 80px;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            animation: fadeInUp 1s ease forwards;
        }

        .hero p {
            font-size: 24px;
            font-weight: 400;
            margin-bottom: 40px;
            animation: fadeInUp 1s ease 0.5s forwards;
            opacity: 0;
        }

        .hero .cta-button {
            display: inline-block;
            padding: 15px 30px;
            background: var(--accent-color);
            color: white;
            font-weight: 700;
            border-radius: var(--border-radius);
            transition: all 0.3s ease;
            box-shadow: var(--box-shadow);
            animation: fadeInUp 1s ease 1s forwards;
            opacity: 0;
        }

        .hero .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .particles {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }

        /* About Section */
        .about {
            padding: 100px 0;
            background: var(--bg-color);
        }

        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            align-items: center;
        }

        .about-image {
            width: 100%;
            max-width: 400px;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            transform: rotate(-5deg);
            transition: transform 0.3s ease;
        }

        .about-image:hover {
            transform: rotate(0deg) scale(1.05);
        }

        .about-text h2 {
            font-size: 48px;
            margin-bottom: 20px;
            color: var(--primary-color);
        }

        .about-text p {
            font-size: 18px;
            line-height: 1.8;
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 40px;
        }

        .skill {
            background: var(--card-bg);
            padding: 20px;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            width: calc(50% - 20px);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .skill:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .skill h3 {
            font-size: 20px;
            margin-bottom: 10px;
            color: var(--secondary-color);
        }

        .skill-progress {
            height: 8px;
            background: #e0e0e0;
            border-radius: 4px;
            overflow: hidden;
        }

        .skill-bar {
            height: 100%;
            background: var(--accent-color);
            transition: width 1s ease;
        }

        /* Experience Section */
        .experience {
            padding: 100px 0;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
        }

        .experience-content {
            position: relative;
        }

        .timeline {
            position: relative;
            padding-left: 30px;
        }

        .timeline::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 2px;
            height: 100%;
            background: rgba(255, 255, 255, 0.2);
        }

        .timeline-item {
            position: relative;
            margin-bottom: 40px;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            top: 8px;
            left: -10px;
            width: 20px;
            height: 20px;
            background: var(--accent-color);
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        .timeline-item:last-child {
            margin-bottom: 0;
        }

        .timeline-item h3 {
            font-size: 24px;
            margin-bottom: 10px;
        }

        .timeline-item p {
            font-size: 18px;
            line-height: 1.6;
        }

        .job-card {
            background: var(--card-bg);
            padding: 30px;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .job-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        /* Education Section */
        .education {
            padding: 100px 0;
            background: var(--bg-color);
        }

        .education-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px;
        }

        .education-card {
            background: var(--card-bg);
            padding: 30px;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .education-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .education-card img {
            max-width: 100px;
            margin-bottom: 20px;
        }

        .education-card h3 {
            font-size: 24px;
            margin-bottom: 10px;
            color: var(--primary-color);
        }

        .education-card p {
            font-size: 16px;
            line-height: 1.6;
        }

        /* Projects Section */
        .projects {
            padding: 100px 0;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
        }

        .projects-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
        }

        .project-card {
            position: relative;
            overflow: hidden;
            border-radius: var(--border-radius);
            transition: transform 0.3s ease;
        }

        .project-card:hover {
            transform: scale(1.05);
        }

        .project-image {
            width: 100%;
            height: 300px;
            object-fit: cover;
            transition: transform 0.3s ease;
        }

        .project-card:hover .project-image {
            transform: scale(1.1);
        }

        .project-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6));
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .project-card:hover .project-overlay {
            opacity: 1;
        }

        .project-overlay h3 {
            font-size: 24px;
            margin-bottom: 20px;
        }

        .project-overlay .view-button {
            padding: 10px 20px;
            background: var(--accent-color);
            color: white;
            font-weight: 700;
            border-radius: var(--border-radius);
            transition: all 0.3s ease;
        }

        .project-overlay .view-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 20px;
        }

        .tech-stack span {
            background: rgba(255, 255, 255, 0.2);
            padding: 5px 10px;
            border-radius: var(--border-radius);
            font-size: 14px;
        }

        /* Contact Section */
        .contact {
            padding: 100px 0;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
        }

        .contact-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
        }

        .contact-form {
            background: var(--card-bg);
            padding: 40px;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
        }

        .contact-form h2 {
            font-size: 36px;
            margin-bottom: 30px;
            color: var(--primary-color);
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 700;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: var(--border-radius);
            font-size: 16px;
            transition: border-color 0.3s ease;
        }

        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: var(--accent-color);
        }

        .form-group textarea {
            resize: vertical;
            min-height: 150px;
        }

        .contact-form button {
            background: var(--accent-color);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: var(--border-radius);
            font-size: 18px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: var(--box-shadow);
        }

        .contact-form button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .contact-details {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .contact-details h2 {
            font-size: 36px;
            margin-bottom: 30px;
            color: var(--primary-color);
        }

        .contact-item {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }

        .contact-item i {
            font-size: 24px;
            margin-right: 20px;
            color: var(--accent-color);
        }

        .social-icons {
            display: flex;
            gap: 20px;
            margin-top: 40px;
        }

        .social-icons a {
            font-size: 24px;
            color: white;
            transition: transform 0.3s ease, color 0.3s ease;
        }

        .social-icons a:hover {
            transform: translateY(-3px);
            color: var(--accent-color);
        }

        /* Footer */
        footer {
            background: var(--primary-color);
            color: white;
            padding: 20px 0;
            text-align: center;
        }

        footer p {
            font-size: 16px;
        }

        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes pulse {
            0% {
                transform: scale(0.95);
                box-shadow: 0 0 0 0 rgba(79, 172, 254, 0.7);
            }
            
            70% {
                transform: scale(1);
                box-shadow: 0 0 0 10px rgba(79, 172, 254, 0);
            }
            
            100% {
                transform: scale(0.95);
                box-shadow: 0 0 0 0 rgba(79, 172, 254, 0);
            }
        }

        /* Responsive Design */
        @media screen and (max-width: 1024px) {
            .container {
                max-width: 960px;
            }

            .about-content,
            .contact-content {
                grid-template-columns: 1fr;
            }

            .about-image {
                margin: 0 auto 40px;
            }

            .skill {
                width: 100%;
            }
        }

        @media screen and (max-width: 768px) {
            .container {
                max-width: 720px;
            }

            .nav-links {
                display: none;
                flex-direction: column;
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                padding: 20px;
                text-align: center;
            }

            .nav-links.active {
                display: flex;
            }

            .nav-links li {
                margin: 10px 0;
            }

            .hamburger {
                display: block;
            }

            .hero h1 {
                font-size: 60px;
            }

            .hero p {
                font-size: 20px;
            }

            .about-text h2 {
                font-size: 36px;
            }

            .education-content {
                grid-template-columns: 1fr;
            }

            .projects-content {
                grid-template-columns: 1fr;
            }
        }

        @media screen and (max-width: 480px) {
            .container {
                padding: 0 10px;
            }

            .hero h1 {
                font-size: 48px;
            }

            .hero p {
                font-size: 18px;
            }

            .about-text h2 {
                font-size: 28px;
            }

            .contact-form {
                padding: 20px;
            }

            .contact-form h2 {
                font-size: 28px;
            }

            .contact-details h2 {
                font-size: 28px;
            }
        }
    </style>
</head>
<body>
    <nav id="navbar">
        <div class="nav-container container">
            <div class="logo">Sikandar Ali</div>
            <ul class="nav-links">
                <li><a href="#hero" class="nav-link">Home</a></li>
                <li><a href="#about" class="nav-link">About</a></li>
                <li><a href="#experience" class="nav-link">Experience</a></li>
                <li><a href="#education" class="nav-link">Education</a></li>
                <li><a href="#projects" class="nav-link">Projects</a></li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
            <div class="hamburger">
                <div class="line1"></div>
                <div class="line2"></div>
                <div class="line3"></div>
            </div>
        </div>
    </nav>

    <section id="hero" class="hero">
        <div class="hero-content">
            <h1>Sikandar Ali</h1>
            <p id="hero-text">Deep Learning Engineer | Python Developer</p>
            <a href="#contact" class="cta-button">Get in Touch</a>
        </div>
        <div class="particles" id="particles-js"></div>
    </section>

    <section id="about" class="about">
        <div class="container">
            <div class="about-content">
                <div class="about-image">
                    <img src="https://via.placeholder.com/400x400" alt="Sikandar Ali">
                </div>
                <div class="about-text">
                    <h2>About Me</h2>
                    <p>Passionate and solution-driven Python developer with a strong foundation in deep learning, data science, and AI. Experienced in designing machine learning models, analyzing complex datasets, and automating tasks using Python-based tools. Known for fast learning, clean coding practices, and collaborative development.</p>
                    <div class="skills">
                        <div class="skill">
                            <h3>Python</h3>
                            <div class="skill-progress">
                                <div class="skill-bar" style="width: 90%"></div>
                            </div>
                        </div>
                        <div class="skill">
                            <h3>Deep Learning</h3>
                            <div class="skill-progress">
                                <div class="skill-bar" style="width: 85%"></div>
                            </div>
                        </div>
                        <div class="skill">
                            <h3>Data Science</h3>
                            <div class="skill-progress">
                                <div class="skill-bar" style="width: 80%"></div>
                            </div>
                        </div>
                        <div class="skill">
                            <h3>Machine Learning</h3>
                            <div class="skill-progress">
                                <div class="skill-bar" style="width: 85%"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="experience" class="experience">
        <div class="container">
            <h2>Experience</h2>
            <div class="experience-content">
                <div class="timeline">
                    <div class="timeline-item">
                        <div class="job-card">
                            <h3>Python Developer</h3>
                            <p>Freelance | Jan '23 — Jan '24 | Remote</p>
                            <p>Built Python-based data analysis pipelines using pandas and matplotlib. Developed and deployed Streamlit web apps for real-time data dashboards.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="education" class="education">
        <div class="container">
            <h2>Education</h2>
            <div class="education-content">
                <div class="education-card">
                    <img src="https://via.placeholder.com/100x100" alt="Riphah International University">
                    <h3>BS Computer Science</h3>
                    <p>Riphah International University | Jan '20 — Dec '24 | GPA: 3.07</p>
                    <p>Relevant Coursework: Deep Learning, Machine Learning, Operating Systems, Software Engineering</p>
                    <p>Final Year Project: UML Diagram Recognition and Conversion System</p>
                </div>
                <div class="education-card">
                    <img src="https://via.placeholder.com/100x100" alt="Cadet College Petaro">
                    <h3>Intermediate</h3>
                    <p>Cadet College Petaro | Mar '18 — Feb '20</p>
                    <p>Trained athlete and gymnast with active participation in college sports and physical disciplines.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="projects" class="projects">
        <div class="container">
            <h2>Projects</h2>
            <div class="projects-content">
                <div class="project-card">
                    <img src="https://via.placeholder.com/600x400" alt="UML Recognition and Conversion System" class="project-image">
                    <div class="project-overlay">
                        <h3>UML Recognition and Conversion System</h3>
                        <a href="#" class="view-button">View Project</a>
                        <div class="tech-stack">
                            <span>Python</span>
                            <span>OpenCV</span>
                            <span>Tesseract OCR</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="contact" class="contact">
        <div class="container">
            <div class="contact-content">
                <div class="contact-form">
                    <h2>Get in Touch</h2>
                    <form id="contact-form">
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input type="text" id="name" name="name" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" required>
                        </div>
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea id="message" name="message" required></textarea>
                        </div>
                        <button type="submit">Send Message</button>
                    </form>
                </div>
                <div class="contact-details">
                    <h2>Contact Details</h2>
                    <div class="contact-item">
                        <i class="fas fa-map-marker-alt"></i>
                        <p>Islamabad, Islamabad, Pakistan</p>
                    </div>
                    <div class="contact-item">
                        <i class="fas fa-phone"></i>
                        <p>+923102660600</p>
                    </div>
                    <div class="contact-item">
                        <i class="fas fa-envelope"></i>
                        <p>sikandar.umrani.5@gmail.com</p>
                    </div>
                    <div class="social-icons">
                        <a href="#" target="_blank"><i class="fab fa-linkedin"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 Sikandar Ali. All rights reserved.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script src="https://kit.fontawesome.com/your-fontawesome-kit.js" crossorigin="anonymous"></script>
    <script>
        // Navbar scroll effect
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - navbar.offsetHeight,
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Active navigation link
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('.nav-link');

        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop - navbar.offsetHeight;
                const sectionHeight = section.clientHeight;
                if (window.scrollY >= sectionTop - 50 && window.scrollY < sectionTop + sectionHeight - 50) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href').substring(1) === current) {
                    link.classList.add('active');
                }
            });
        });

        // Mobile menu toggle
        const hamburger = document.querySelector('.hamburger');
        const navLinksMobile = document.querySelector('.nav-links');

        hamburger.addEventListener('click', () => {
            navLinksMobile.classList.toggle('active');
            hamburger.classList.toggle('active');
        });

        // Typewriter effect
        const heroText = document.getElementById('hero-text');
        const text = heroText.textContent;
        heroText.textContent = '';

        let i = 0;
        function typeWriter() {
            if (i < text.length) {
                heroText.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }

        typeWriter();

        // Intersection Observer for animations
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate');
                }
            });
        });

        document.querySelectorAll('.skill, .timeline-item, .education-card, .project-card').forEach(el => {
            observer.observe(el);
        });

        // Particles.js
        particlesJS('particles-js', {
            "particles": {
                "number": {
                    "value": 80,
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                    "value": "#ffffff"
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 0,
                        "color": "#000000"
                    },
                    "polygon": {
                        "nb_sides": 5
                    },
                    "image": {
                        "src": "img/github.svg",
                        "width": 100,
                        "height": 100
                    }
                },
                "opacity": {
                    "value": 0.5,
                    "random": false,
                    "anim": {
                        "enable": false,
                        "speed": 1,
                        "opacity_min": 0.1,
                        "sync": false
                    }
                },
                "size": {
                    "value": 3,
                    "random": true,
                    "anim": {
                        "enable": false,
                        "speed": 40,
                        "size_min": 0.1,
                        "sync": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#ffffff",
                    "opacity": 0.4,
                    "width": 1
                },
                "move": {
                    "enable": true,
                    "speed": 6,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false,
                    "attract": {
                        "enable": false,
                        "rotateX": 600,
                        "rotateY": 1200
                    }
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "repulse"
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"
                    },
                    "resize": true
                },
                "modes": {
                    "grab": {
                        "distance": 400,
                        "line_linked": {
                            "opacity": 1
                        }
                    },
                    "bubble": {
                        "distance": 400,
                        "size": 40,
                        "duration": 2,
                        "opacity": 8,
                        "speed": 3
                    },
                    "repulse": {
                        "distance": 200,
                        "duration": 0.4
                    },
                    "push": {
                        "particles_nb": 4
                    },
                    "remove": {
                        "particles_nb": 2
                    }
                }
            },
            "retina_detect": true
        });

        // Form validation
        const contactForm = document.getElementById('contact-form');
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            if (name === '' || email === '' || message === '') {
                alert('Please fill in all fields.');
                return;
            }

            if (!validateEmail(email)) {
                alert('Please enter a valid email address.');
                return;
            }

            alert('Thank you for your message! I will get back to you soon.');
            contactForm.reset();
        });

        function validateEmail(email) {
            const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(String(email).toLowerCase());
        }

        // Back to top button
        const backToTopButton = document.createElement('button');
        backToTopButton.id = 'back-to-top';
        backToTopButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
        backToTopButton.style.display = 'none';
        backToTopButton.style.position = 'fixed';
        backToTopButton.style.bottom = '20px';
        backToTopButton.style.right = '20px';
        backToTopButton.style.zIndex = '1000';
        backToTopButton.style.padding = '10px';
        backToTopButton.style.backgroundColor = 'var(--accent-color)';
        backToTopButton.style.color = 'white';
        backToTopButton.style.border = 'none';
        backToTopButton.style.borderRadius = 'var(--border-radius)';
        backToTopButton.style.cursor = 'pointer';
        backToTopButton.style.transition = 'opacity 0.3s ease';
        backToTopButton.style.opacity = '0.7';

        backToTopButton.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });

        backToTopButton.addEventListener('mouseenter', () => {
            backToTopButton.style.opacity = '1';
        });

        backToTopButton.addEventListener('mouseleave', () => {
            backToTopButton.style.opacity = '0.7';
        });

        document.body.appendChild(backToTopButton);

        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopButton.style.display = 'block';
            } else {
                backToTopButton.style.display = 'none';
            }
        });
    </script>
</body>
</html>
