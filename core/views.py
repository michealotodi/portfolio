from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['profile'] = {
            'name': 'Micheal Otodi',
            'phone': '(+256) 743099500',
            'email': 'michealotodi81@gmail.com',
            'github': 'https://github.com/michealotodi',
            'about_me': """I am an experienced software engineer with a strong foundation in software development, acquired through hands-on experience gained from the Refactory. I am enthusiastic about exploring opportunities across a wide spectrum of software development domains. I thrive on learning and adapting to new challenges in the dynamic field of software engineering.

With an open mindset and eagerness to embrace diverse projects, I am committed to continuously expanding my skills and expertise. This proactive approach enables me to excel in various software development environments, contributing effectively to innovative solutions and driving impactful results."""
        }

        context['educations'] = [
            {
                'year': '2025',
                'institution': 'Refactory Academy',
                'degree': 'Certificate in Software Engineering with Python',
                'location': 'Kampala - Uganda',
            },
            {
                'year': '2022',
                'institution': 'Onono Memorial College',
                'degree': 'Uganda Certificate of Education',
                'location': 'Omoro District',
            },
        ]

        context['technical_skills'] = [
            {'name': 'Python'},
            {'name': 'Django'},
            {'name': 'HTML/CSS'},
            {'name': 'Django Rest Framework'},
            {'name': 'SQLite'},
            {'name': 'PostgreSQL'},
            {'name': 'MySQL'},
            {'name': 'Git'},
            {'name': 'GitHub'},
            {'name': 'GitLab'},
            {'name': 'VS Code'},
        ]

        context['soft_skills'] = [
            {'name': 'Communication skills'},
            {'name': 'Leadership skills'},
            {'name': 'Creativity and innovation'},
            {'name': 'Paying attention to details'},
            {'name': 'Time management and prioritization'},
            {'name': 'Problem solving skills'},
            {'name': 'Teamwork and collaboration'},
        ]

        context['experiences'] = [
            {
                'title': 'Software Developer',
                'company': 'Happy Hoe Grocery Ltd (KGL)',
                'period': 'Feb 2025 – Apr 2025',
                'roles': """Led the design and development of a full-featured inventory and sales management system for a multi-branch wholesale produce distributor.
Implemented role-based dashboards for directors, managers, and sales agents to manage procurement, sales, stock levels, and credit transactions.
Built modules for recording produce entries, tracking stock in real time, managing cash and credit sales, and generating digital receipts.
Applied strict data validation rules to ensure accuracy and integrity in procurement and sales records (e.g., tonnage, pricing, buyer info).
Enabled editable stock and sales records, automated stock deductions on sales, and integrated low-stock alerts for proactive restocking.
Collaborated with end users to gather requirements, conduct usability testing, and refine features to suit real business workflows.
Delivered regular feature updates and system demonstrations to stakeholders for continuous feedback and improvement.""",
                'achievements': """Successfully digitized operations for a multi-branch produce distributor, reducing manual entry errors.
Enabled real-time stock tracking and low-stock alerts, improving restocking efficiency across both branches.
Streamlined the procurement and sales process, cutting down transaction recording time.
Designed a credit sales tracking system that enhanced visibility on deferred payments and due dates.
Developed a robust role-based access control system that improved operational transparency and accountability.""",
            },
            {
                'title': 'Software Developer',
                'company': 'RIM Aviation Group',
                'period': 'Apr 2025 – May 2025',
                'roles': """Developed a responsive online flight booking system to streamline and secure client flight requests, replacing a manual paper-based workflow.
Created a form-driven interface for capturing passenger, contact, and travel details with built-in validations and file upload support.
Ensured high usability with real-time feedback, error messaging, and form reset capabilities after successful submission.
Improved data quality and submission speed while laying the foundation for full automation of RIM Aviation’s booking process.
Followed sprint-based development, prioritizing features for efficient delivery and alignment with operational goals.""",
                'achievements': """Built and deployed a flight reservation system that replaced inefficient paper-based booking, reducing booking errors and delays.
Improved data validation and security, ensuring accurate submissions for all client bookings.
Enhanced user experience through real-time feedback and submission confirmation, improving client satisfaction.
Delivered the core booking module ahead of schedule, laying a foundation for future system-wide automation.
Enabled scalable digital bookings, supporting the company’s transition into a more tech-driven operation.""",
            },
        ]

        context['references'] = [
            {
                'name': 'Dorothy Oyella',
                'title': 'Placement and mentorship lead at the Refactory',
                'email': 'doyella@refactory.academy',
                'phone': '0772122523',
            },
            {
                'name': 'Joan Twinomugyisha',
                'title': 'Technical facilitator at the Refactory',
                'email': 'jtwinomugyisha@refactory.academy',
                'phone': '0705959119',
            },
            {
                'name': 'Mark Latim',
                'title': 'Technical coach at the Refactory',
                'email': 'latimmark@gmail.com',
                'phone': '078301357',
            },
        ]

        return context


# views.py

from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Profile, Education, Experience, Skill, Reference

class ContactView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            profile = Profile.objects.first()
            context['profile'] = profile
            context['educations'] = profile.educations.all() if profile else []
            context['experiences'] = profile.experiences.all() if profile else []
            context['technical_skills'] = profile.skills.filter(skill_type='technical') if profile else []
            context['soft_skills'] = profile.skills.filter(skill_type='soft') if profile else []
            context['references'] = profile.references.all() if profile else []
        except Profile.DoesNotExist:
            pass
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New message from {name} via portfolio site"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(subject, full_message, email, ['michealotodi81email@gmail.com'])  # Your receiving email
            messages.success(request, 'Message sent successfully!')
        except Exception as e:
            messages.error(request, f'Error sending message: {str(e)}')

        return redirect(f"{request.path}#contact")
