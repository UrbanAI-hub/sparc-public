const translations = {
    en: {
        nav_home: "Home",
        nav_about: "About SPARC",
        nav_projects: "Projects",
        nav_people: "People",
        nav_contact: "Contact Us",
        hero_title: "SPARC",
        hero_subtitle: "Strategic Partnership for AI and Rotterdam's Challenges",
        about_title: "About SPARC",
        about_desc_1: "SPARC is a collaborative initiative between Delft University of Technology, Erasmus University, and the municipality of Rotterdam focusing on the integration of AI solutions within the municipality.",
        about_desc_2: "Designed as a dynamic operational framework, SPARC bridges the gap between innovation and public service, serving as relevant launchpad for data-driven projects within the municipality.",
        vision_title: "Our Vision",
        vision_desc: "Establish an Urban AI Innovation Hub at the Municipality of Rotterdam that provides a dedicated space for developing scientific, data-driven solutions. The focus is on connecting other municipalities, universities, industry partners, and other urban stakeholders to advance sustainable, safe, and inclusive cities, while fostering collaboration, knowledge exchange, and talent development.",
        mission_title: "Our Mission",
        mission_desc: "To empower urban innovation through AI-driven collaboration between universities, industry, and the public sector.",
        projects_title: "Projects",
        people_title: "Our Team",
        contact_title: "Contact Us",
        footer_partners: "Partners"
    },
    nl: {
        nav_home: "Home",
        nav_about: "Over SPARC",
        nav_projects: "Projecten",
        nav_people: "Mensen",
        nav_contact: "Contact",
        hero_title: "SPARC",
        hero_subtitle: "Strategisch Partnerschap voor AI en Rotterdamse Uitdagingen",
        about_title: "Over SPARC",
        about_desc_1: "SPARC is een samenwerkingsinitiatief tussen de Technische Universiteit Delft, de Erasmus Universiteit en de gemeente Rotterdam, gericht op de integratie van AI-oplossingen binnen de gemeente.",
        about_desc_2: "Ontworpen als een dynamisch operationeel kader, overbrugt SPARC de kloof tussen innovatie en publieke dienstverlening, en dient het als een relevante springplank voor datagestuurde projecten binnen de gemeente.",
        vision_title: "Onze Visie",
        vision_desc: "Het vestigen van een Urban AI Innovation Hub bij de Gemeente Rotterdam die een speciale ruimte biedt voor het ontwikkelen van wetenschappelijke, datagestuurde oplossingen. De focus ligt op het verbinden van andere gemeenten, universiteiten, industriële partners en andere stedelijke belanghebbenden om duurzame, veilige en inclusieve steden te bevorderen, terwijl samenwerking, kennisuitwisseling en talentontwikkeling worden gestimuleerd.",
        mission_title: "Onze Missie",
        mission_desc: "Stedelijke innovatie versterken door AI-gestuurde samenwerking tussen universiteiten, de industrie en de publieke sector.",
        projects_title: "Projecten",
        people_title: "Ons Team",
        contact_title: "Neem contact op",
        footer_partners: "Partners"
    }
};

// Use localStorage to persist language across pages
let currentLang = localStorage.getItem('sparc_lang') || 'en';

function updateContent() {
    const elements = document.querySelectorAll('[data-key]');
    elements.forEach(el => {
        const key = el.getAttribute('data-key');
        if (translations[currentLang] && translations[currentLang][key]) {
            el.textContent = translations[currentLang][key];
        }
    });

    // Update active button state
    document.querySelectorAll('.lang-btn').forEach(btn => {
        const lang = btn.getAttribute('data-lang');
        btn.classList.toggle('active', lang === currentLang);
    });
}

window.switchLang = (lang) => {
    currentLang = lang;
    localStorage.setItem('sparc_lang', lang);
    updateContent();
};

document.addEventListener('DOMContentLoaded', () => {
    updateContent();

    // Smooth scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href.startsWith('#')) {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
});