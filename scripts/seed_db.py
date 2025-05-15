#!/usr/bin/env python
"""
Script to populate the database with sample data for Micheal Otodi's portfolio.
"""
import os
import sys
import django

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from core.models import Profile, Education, Experience, Skill, Reference

def seed_database():
    # Clear existing data
    Profile.objects.all().delete()
    
    # Create profile
    profile = Profile.objects.create(
        name="Micheal Otodi",
        phone="(+256) 743099500",
        email="michealotodi81@gmail.com",
        github="https://github.com/michealotodi",
        about_me=(
            "I am an experienced software engineer with a strong foundation in "
            "software development, acquired through hands on experience gained "
            "from the Refactory. I am enthusiastic about exploring opportunities "
            "across a wide spectrum of software development domains. I thrive on "
            "learning and adapting to new challenges in the dynamic field of software "
            "engineering.\n\n"
            "With an open mindset and eagerness to embrace diverse "
            "projects, I am committed to continuously expanding my skills and "
            "expertise. This proactive approach enables me to excel in various "
            "software development environments, contributing effectively to "
            "innovative solutions and driving impactful results."
        )
    )
    
    # Create education
    Education.objects.create(
        profile=profile,
        institution="REFACTORY ACADEMY",
        degree="Certificate in software engineering with python",
        year="2025",
        location="Kampala - Uganda"
    )
    
    Education.objects.create(
        profile=profile,
        institution="ONONO MEMORIAL COLLEGE",
        degree="Uganda Certificate of Education",
        year="2022",
        location="Omoro District"
    )
    
    # Create experiences
    experience1 = Experience.objects.create(
        profile=profile,
        title="Software Developer",
        company="Happy Hoe Grocery Ltd (KGL)",
        period="February 2025 – April 2025",
        roles=(
            "Led the design and development of a full-featured inventory and sales "
            "management system for a multi-branch wholesale produce distributor.\n"
            "Implemented role-based dashboards for directors, managers, and sales "
            "agents to manage procurement, sales, stock levels, and credit transactions.\n"
            "Built modules for recording produce entries, tracking stock in real time, "
            "managing cash and credit sales, and generating digital receipts.\n"
            "Applied strict data validation rules to ensure accuracy and integrity in "
            "procurement and sales records (e.g., tonnage, pricing, buyer info).\n"
            "Enabled editable stock and sales records, automated stock deductions on "
            "sales, and integrated low-stock alerts for proactive restocking.\n"
            "Collaborated with end users to gather requirements, conduct usability "
            "testing, and refine features to suit real business workflows.\n"
            "Delivered regular feature updates and system demonstrations to "
            "stakeholders for continuous feedback and improvement."
        ),
        achievements=(
            "Successfully digitized operations for a multi-branch produce distributor, "
            "reducing manual entry errors.\n"
            "Enabled real-time stock tracking and low-stock alerts, improving "
            "restocking efficiency across both branches.\n"
            "Streamlined the procurement and sales process, cutting down transaction "
            "recording time.\n"
            "Designed a credit sales tracking system that enhanced visibility on "
            "deferred payments and due dates.\n"
            "Developed a robust role-based access control system that improved "
            "operational transparency and accountability."
        )
    )
    
    experience2 = Experience.objects.create(
        profile=profile,
        title="Software Developer",
        company="RIM Aviation Group",
        period="April 2025 – May 2025",
        roles=(
            "Developed a responsive online flight booking system to streamline and "
            "secure client flight requests, replacing a manual paper-based workflow.\n"
            "Created a form-driven interface for capturing passenger, contact, and "
            "travel details with built-in validations and file upload support.\n"
            "Ensured high usability with real-time feedback, error messaging, and form "
            "reset capabilities after successful submission.\n"
            "Improved data quality and submission speed while laying the foundation "
            "for full automation of RIM Aviation's booking process.\n"
            "Followed sprint-based development, prioritizing features for efficient "
            "delivery and alignment with operational goals."
        ),
        achievements=(
            "Built and deployed a flight reservation system that replaced inefficient "
            "paper-based booking, reducing booking errors and delays.\n"
            "Improved data validation and security, ensuring accurate submissions for all "
            "client bookings.\n"
            "Enhanced user experience through real-time feedback and submission "
            "confirmation, improving client satisfaction.\n"
            "Delivered the core booking module ahead of schedule, laying a foundation "
            "for future system-wide automation.\n"
            "Enabled scalable digital bookings, supporting the company's transition into "
            "a more tech-driven operation."
        )
    )
    
    # Create skills - Technical
    technical_skills = [
        "Python",
        "Django",
        "HTML/CSS",
        "Django Rest Framework",
        "SQLite",
        "PostgreSQL",
        "MySQL",
        "Git",
        "GitHub",
        "GitLab",
        "VS Code"
    ]
    
    for skill in technical_skills:
        Skill.objects.create(
            profile=profile,
            name=skill,
            skill_type="technical"
        )
    
    # Create skills - Soft
    soft_skills = [
        "Communication skills",
        "Leadership skills",
        "Creativity and innovation",
        "Paying attention to details",
        "Time management and prioritization",
        "Problem solving skills",
        "Teamwork and collaboration"
    ]
    
    for skill in soft_skills:
        Skill.objects.create(
            profile=profile,
            name=skill,
            skill_type="soft"
        )
    
    # Create references
    Reference.objects.create(
        profile=profile,
        name="Dorothy Oyella",
        title="Placement and mentorship lead at the Refactory",
        email="doyella@refactory.academy",
        phone="0772122523"
    )
    
    Reference.objects.create(
        profile=profile,
        name="Joan Twinomugyisha",
        title="Technical facilitator at the Refactory",
        email="jtwinomugyisha@refactory.academy",
        phone="0705959119"
    )
    
    Reference.objects.create(
        profile=profile,
        name="Mark Latim",
        title="Technical coach at the Refactory",
        email="latimmark@gmail.com",
        phone="078301357"
    )
    
    print("Database successfully seeded with Micheal Otodi's portfolio data!")

if __name__ == "__main__":
    seed_database()