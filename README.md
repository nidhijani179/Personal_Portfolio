<img width="1908" height="832" alt="Screenshot 2025-10-02 235345" src="https://github.com/user-attachments/assets/f61239e4-2a75-40d9-8285-4f71e319dd22" />
<img width="1897" height="860" alt="Screenshot 2025-10-02 235328" src="https://github.com/user-attachments/assets/67a5bb9a-4144-4137-8829-8a11481c3d7e" />
<img width="1869" height="875" alt="Screenshot 2025-10-02 235413" src="https://github.com/user-attachments/assets/693f8a4b-fd4f-479f-a478-498c2c13c2da" />
<img width="1894" height="872" alt="Screenshot 2025-10-02 235355" src="https://github.com/user-attachments/assets/c391e8ed-4d2e-425c-94b5-405f5da5fb86" />

# Nidhi Jani - Personal Portfolio Website

A modern, responsive personal portfolio website built with Flask, featuring AI/ML projects, professional experience, and contact functionality.

## Features

- **Modern Design**: Clean, aesthetic, and professional design with Gen Z-friendly elements
- **Fully Responsive**: Optimized for desktop, tablet, and mobile devices
- **Dark/Light Mode**: Toggle between themes with smooth transitions
- **Smooth Animations**: GSAP and AOS animations for enhanced user experience
- **Contact Form**: Flask backend with SQLite database and email functionality
- **SEO Optimized**: Meta tags and structured content for better search visibility
- **Fast Loading**: Optimized assets and efficient code structure

## Tech Stack

### Backend
- **Flask** - Python web framework
- **SQLite** - Database for contact form submissions
- **Jinja2** - Template engine

### Frontend
- **Bootstrap 5** - CSS framework
- **TailwindCSS** - Utility-first CSS framework
- **GSAP** - Animation library
- **AOS** - Animate on Scroll library
- **Typed.js** - Typing animation effect

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nidhijani179/portfolio-website.git
   cd portfolio-website
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:5000`

## Configuration

### Email Setup (Optional)
To enable email functionality for the contact form:

1. Update the email configuration in `app.py`:
   ```python
   sender_email = "your-email@gmail.com"
   sender_password = "your-app-password"  # Use App Password for Gmail
   ```

2. Enable 2-factor authentication and generate an App Password for Gmail

### Resume File
Place your resume PDF file in `static/files/Nidhi_Jani_Resume.pdf`

### Profile Images
Add your profile images to `static/images/`:
- `profile.jpg` - Main profile image
- `about.jpg` - About section image
- Project images for the portfolio section

## Deployment

### Heroku
1. Create a `Procfile`:
   ```
   web: python app.py
   ```

2. Update `app.py` for production:
   ```python
   if __name__ == '__main__':
       port = int(os.environ.get('PORT', 5000))
       app.run(host='0.0.0.0', port=port)
   ```

### PythonAnywhere
1. Upload files to your PythonAnywhere account
2. Configure WSGI file to point to your Flask app
3. Set up static files mapping

### AWS/DigitalOcean
1. Set up a server with Python 3.8+
2. Install dependencies and configure reverse proxy (Nginx)
3. Use Gunicorn as WSGI server

## Customization

### Colors and Themes
Update CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #6366f1;
    --secondary-color: #8b5cf6;
    --accent-color: #06b6d4;
    /* ... */
}
```

### Content
Update personal information in `templates/index.html`:
- Hero section text and links
- About section content
- Skills, experience, and projects
- Contact information

### Animations
Modify GSAP animations in `static/js/script.js` to customize timing and effects.

## Project Structure

```
portfolio-website/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── portfolio.db          # SQLite database (auto-created)
├── templates/
│   ├── base.html         # Base template
│   └── index.html        # Main page template
└── static/
    ├── css/
    │   └── style.css     # Custom styles
    ├── js/
    │   └── script.js     # JavaScript functionality
    ├── images/           # Profile and project images
    └── files/            # Resume and other files
```

## Features Overview

### Sections
1. **Hero/Home** - Introduction with typing animation
2. **About** - Personal information and skills overview
3. **Skills** - Technical skills with animated tags
4. **Experience** - Professional timeline
5. **Projects** - Portfolio showcase with hover effects
6. **Education** - Academic background and achievements
7. **Contact** - Contact form and social links

### Interactive Elements
- Smooth scrolling navigation
- Hover effects on cards and buttons
- Dark/light mode toggle
- Animated skill tags and project cards
- Responsive mobile menu
- Loading animations

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- Optimized images and assets
- Minified CSS and JavaScript
- Efficient database queries
- Responsive design for all devices
- Fast loading times

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

**Nidhi Jani**
- Email: nidhi.jani03@gmail.com
- LinkedIn: [linkedin.com/in/nidhi-jani-1214b5252](https://linkedin.com/in/nidhi-jani-1214b5252)
- GitHub: [github.com/nidhijani179](https://github.com/nidhijani179)

---

Built with ❤️ using Flask, Bootstrap, and modern web technologies.
