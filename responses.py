"""
responses.py
------------
This module is the "knowledge base" of the Smart Career Assistant.

Design note (important for interviews):
    A naive rule-based bot is often written as a long if/elif/elif
    ladder. That works, but it doesn't scale — every new rule makes
    the chain longer and slower to search (O(n) in the worst case).

    Instead, this project stores all knowledge as DICTIONARIES
    (hash maps). Looking a keyword up in a dictionary is a near
    constant-time O(1) operation on average, and it keeps the data
    (the rules) separate from the logic (the matching engine).

    Each category below maps a KEYWORD -> a professional response.
    The matching engine (`get_response`) then scans the user's
    sanitized input for any of these keywords.
"""

# ---------------------------------------------------------------
# 1. GREETINGS
# ---------------------------------------------------------------
GREETINGS = {
    "hello": "Hello! 👋 I'm your Smart Career Assistant. How can I help your career journey today?",
    "hi": "Hi there! 😊 Ready to talk about careers, code, or interviews?",
    "hey": "Hey! Good to see you. What's on your mind today?",
    "good morning": "Good morning! 🌅 Let's make today productive — ask me anything career-related.",
    "good evening": "Good evening! 🌆 Winding down or just getting started? I'm here either way.",
    "good afternoon": "Good afternoon! ☀️ How can I assist you with your career today?",
}

# ---------------------------------------------------------------
# 2. FAREWELLS
# ---------------------------------------------------------------
FAREWELLS = {
    "exit": "Goodbye! 👋 Wishing you success in your career journey. Come back anytime!",
    "quit": "Session ended. Take care, and keep learning! 🚀",
    "bye": "Bye! 🙌 Remember — consistency beats motivation. See you soon!",
}

# ---------------------------------------------------------------
# 3. IDENTITY
# ---------------------------------------------------------------
IDENTITY = {
    "who are you": "I'm the Smart Career Assistant 🤖 — a rule-based chatbot built to guide you "
                    "on careers, interviews, resumes, and learning roadmaps.",
    "what can you do": "I can guide you on career paths, programming roadmaps, interview prep, "
                        "resume building, and even motivate you when you need it! Type 'help' for details.",
    "help": None,  # handled specially in chatbot.py (prints the help menu)
}

# ---------------------------------------------------------------
# 4. CAREER GUIDANCE
# ---------------------------------------------------------------
CAREER_GUIDANCE = {
    "software engineer": "A Software Engineer designs, builds, and maintains software systems. "
                          "Focus on DSA, one strong language (Python/Java/C++), and system design basics.",
    "data scientist": "A Data Scientist extracts insights from data using statistics, Python, "
                       "and ML. Start with Python, SQL, statistics, and pandas/numpy.",
    "ai engineer": "An AI Engineer builds intelligent systems — from rule-based logic (like this "
                   "project!) to ML and LLM-based applications. Learn Python, ML basics, and one "
                   "framework like PyTorch or TensorFlow.",
    "web developer": "A Web Developer builds websites and web apps. Learn HTML, CSS, JavaScript, "
                      "then a framework — React for frontend, Node/Express for backend.",
    "cloud engineer": "A Cloud Engineer manages cloud infrastructure (AWS/Azure/GCP). Learn Linux, "
                       "networking basics, and one cloud provider's core services (EC2, S3, IAM, etc.).",
    "cybersecurity": "Cybersecurity professionals protect systems from threats. Start with networking "
                      "fundamentals, Linux, and certifications like CompTIA Security+ or CEH.",
}

# ---------------------------------------------------------------
# 5. PROGRAMMING LANGUAGES
# ---------------------------------------------------------------
LANGUAGES = {
    "python": "Python is beginner-friendly and versatile — great for AI, web dev, automation, "
              "and data science. Master syntax, OOP, and libraries like pandas/numpy.",
    "java": "Java is widely used in enterprise systems and Android apps. Focus on OOP concepts, "
            "collections framework, and Spring Boot for backend roles.",
    "c++": "C++ gives you fine control over memory and performance — ideal for competitive "
           "programming, game dev, and systems programming. Master pointers and STL.",
    "javascript": "JavaScript powers the web. Learn the fundamentals, then explore frameworks "
                  "like React (frontend) and Node.js (backend) for full-stack development.",
}

# ---------------------------------------------------------------
# 6. INTERVIEW PREPARATION
# ---------------------------------------------------------------
INTERVIEW_PREP = {
    "hr interview": "For HR interviews, prepare your 'Tell me about yourself' pitch, know the "
                    "company, and be ready to discuss strengths, weaknesses, and salary expectations.",
    "technical interview": "For technical interviews, revise DSA, practice explaining your thought "
                            "process out loud, and be ready to write clean, working code on a whiteboard/editor.",
    "aptitude": "Aptitude rounds test quantitative, logical, and verbal reasoning. Practice daily "
                "on platforms like IndiaBix or PrepInsta, and focus on speed + accuracy.",
    "coding interview": "Coding interviews assess problem-solving. Practice on LeetCode/HackerRank, "
                         "master arrays, strings, recursion, and time/space complexity analysis.",
}

# ---------------------------------------------------------------
# 7. RESUME TIPS
# ---------------------------------------------------------------
RESUME_TIPS = {
    "resume": "Keep your resume to 1 page, use action verbs, quantify achievements, and tailor it "
              "to each job description. Avoid generic objective statements.",
    "projects": "Showcase 2-3 solid projects with clear problem statements, your role, tech stack, "
                "and measurable outcomes. Link GitHub/live demos if possible.",
    "skills": "List skills relevant to the job — group them as Languages, Frameworks, Tools, and "
              "Soft Skills. Avoid listing skills you can't defend in an interview.",
    "internships": "Internships are proof of real-world experience. Highlight what you built, "
                   "learned, and the impact you made — not just your job title.",
}

# ---------------------------------------------------------------
# 8. LEARNING ROADMAPS
# ---------------------------------------------------------------
ROADMAPS = {
    "ai roadmap": "AI Roadmap: Python -> Math (Linear Algebra, Probability) -> ML Algorithms -> "
                  "Deep Learning (Neural Nets) -> Frameworks (PyTorch/TensorFlow) -> Projects.",
    "data science roadmap": "Data Science Roadmap: Python/R -> SQL -> Statistics -> Pandas/Numpy -> "
                             "Data Visualization -> Machine Learning -> Real-world Projects.",
    "mern roadmap": "MERN Roadmap: HTML/CSS/JS -> React -> Node.js -> Express.js -> MongoDB -> "
                    "Build full-stack projects -> Deployment (Vercel/Render).",
    "python roadmap": "Python Roadmap: Syntax & Basics -> OOP -> File Handling -> Libraries "
                       "(NumPy, Pandas) -> Mini Projects -> Frameworks (Flask/Django) -> Portfolio Projects.",
}

# ---------------------------------------------------------------
# 9. MOTIVATION
# ---------------------------------------------------------------
MOTIVATION = {
    "motivate me": "Every expert was once a beginner. 💪 Keep showing up — small consistent effort "
                   "beats occasional bursts of motivation every time.",
    "confidence": "Confidence comes from preparation. The more problems you solve and projects you "
                  "build, the more naturally your confidence will grow.",
    "study tips": "Use active recall, spaced repetition, and the Pomodoro technique (25 min focus, "
                  "5 min break). Teach concepts to someone else to test real understanding.",
}

# ---------------------------------------------------------------
# 10. COLLEGE & PLACEMENT HELP
# ---------------------------------------------------------------
COLLEGE_HELP = {
    "placement": "Start placement prep early: strengthen DSA, build 2-3 solid projects, and "
                 "practice mock interviews at least 3 months before placement season.",
    "cgpa": "CGPA matters for initial shortlisting at some companies, but skills and projects "
            "carry more weight in interviews. Aim for a healthy balance, don't obsess over it.",
    "internship": "Apply early, tailor your resume per role, and don't hesitate to reach out to "
                  "recruiters directly on LinkedIn with a short, genuine message.",
}

# ---------------------------------------------------------------
# MASTER KNOWLEDGE BASE
# ---------------------------------------------------------------
# Combining every category into one master dictionary makes the
# matching engine in get_response() simple to maintain and extend.
# Order matters only in the sense that more specific multi-word
# keywords should be checked before shorter/generic ones — this is
# handled by sorting keywords by length in get_response().
KNOWLEDGE_BASE = {
    **GREETINGS,
    **IDENTITY,
    **CAREER_GUIDANCE,
    **LANGUAGES,
    **INTERVIEW_PREP,
    **RESUME_TIPS,
    **ROADMAPS,
    **MOTIVATION,
    **COLLEGE_HELP,
}

DEFAULT_RESPONSE = (
    "🤔 I don't have a specific rule for that yet. Try asking about a career role, "
    "programming language, interview type, resume tips, or type 'menu' to see topics I know."
)


def get_response(user_input):
    """
    Core matching engine of the rule-based chatbot.

    Scans the sanitized user input for any known keyword and returns
    the associated response. Longer (more specific) keywords are
    checked first so that, for example, "technical interview" matches
    before a shorter overlapping keyword would.

    Args:
        user_input (str): Already lower-cased & stripped user input.

    Returns:
        str or None: The matched response, DEFAULT_RESPONSE if no
                      keyword matched, or None for special commands
                      (like 'help') that are handled elsewhere.
    """
    # Sort keywords by length (longest first) to prioritize specific phrases
    sorted_keywords = sorted(KNOWLEDGE_BASE.keys(), key=len, reverse=True)

    for keyword in sorted_keywords:
        if keyword in user_input:
            return KNOWLEDGE_BASE[keyword]

    return DEFAULT_RESPONSE
