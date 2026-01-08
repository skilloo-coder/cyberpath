import streamlit as st
import time

# --- 1. CONFIGURATION & SECURITY HEADERS ---
st.set_page_config(
    page_title="CyberPath Pro",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS for a professional "Dark Mode" Security UI
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .roadmap-card { padding: 20px; border-radius: 10px; border-left: 5px solid #007bff; background-color: #1e2130; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE ROADMAP DATA ---
ROADMAPS = {
    "Red": {
        "title": "Red Team (Offensive Operations)",
        "desc": "You are a digital pathfinder, finding vulnerabilities to help organizations stay ahead of attackers.",
        "steps": [
            "1. Foundational Systems: Master Linux (Kali/Parrot) and Networking (TCP/IP, OSI Model).",
            "2. Web Security: Learn the OWASP Top 10 (Injection, Broken Access Control, etc.).",
            "3. Exploit Development: Practice with Metasploit and basic Python/C scripting.",
            "4. Active Labbing: Grind HackTheBox or TryHackMe (Offensive paths).",
            "5. Advanced Tactics: Study Active Directory exploitation and Cloud-Native security (AWS/Azure)."
        ],
        "tools": ["Burp Suite", "Nmap", "Metasploit", "Kali Linux"],
        "color": "#ff4b4b"
    },
    "Blue": {
        "title": "Blue Team (Defensive Operations)",
        "desc": "You are the guardian, building shields and monitoring networks to detect and neutralize threats.",
        "steps": [
            "1. Security Foundations: Understand the CIA Triad, Risk Management, and Zero Trust.",
            "2. Log Analysis: Master SIEM tools like Splunk or Elastic Security.",
            "3. Network Monitoring: Learn packet analysis using Wireshark and Zeek.",
            "4. Incident Response: Learn how to perform Digital Forensics and Incident Response (DFIR).",
            "5. Defense Engineering: Configure Firewalls (Palo Alto) and Endpoint Security (EDR)."
        ],
        "tools": ["Splunk", "Wireshark", "SentinelOne", "Suricata"],
        "color": "#1c83e1"
    },
    "Purple": {
        "title": "Purple Team (Integration & Strategy)",
        "desc": "You are the bridge, using attack data to sharpen defenses and improve overall security posture.",
        "steps": [
            "1. Dual Mastery: Gain basic experience in both Red (attacking) and Blue (defending).",
            "2. Framework Knowledge: Master the MITRE ATT&CK and D3F3ND frameworks.",
            "3. Adversary Emulation: Use tools like Atomic Red Team to simulate specific threats.",
            "4. Detection Engineering: Write custom detection rules (YARA, Sigma) based on attack logs.",
            "5. Continuous Improvement: Lead collaborative workshops to fix gaps identified in tests."
        ],
        "tools": ["MITRE ATT&CK", "Atomic Red Team", "Caldera", "Vector"],
        "color": "#7d31ff"
    }
}

# --- 3. SESSION STATE ---
if 'app_state' not in st.session_state:
    st.session_state.app_state = 'quiz'
if 'scores' not in st.session_state:
    st.session_state.scores = {"Red": 0, "Blue": 0, "Purple": 0}

# --- 4. NAVIGATION & SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Controls")
    if st.button("Reset Assessment"):
        st.session_state.app_state = 'quiz'
        st.session_state.scores = {"Red": 0, "Blue": 0, "Purple": 0}
        st.rerun()
    st.divider()
    st.caption("Secure decision-support engine v2.0")

# --- 5. APP PAGES ---
if st.session_state.app_state == 'quiz':
    st.title("CyberPath Career Assessment")
    st.write("Complete all 20 questions to determine your ideal cybersecurity path.")

    with st.form("assessment_form"):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Mindset & Logic")
            q1 = st.slider("1. Enjoy 'breaking' things to see how they work?", 1, 5, 3)
            q2 = st.slider("2. Satisfaction from building a perfect defense?", 1, 5, 3)
            q3 = st.slider("3. Curiosity about 'the why' behind a failure?", 1, 5, 3)
            q4 = st.slider("4. Do you enjoy finding 'shortcuts' or loopholes?", 1, 5, 3)
            q5 = st.slider("5. Solving multi-layered, complex puzzles?", 1, 5, 3)

            st.subheader("Technical Preferences")
            q6 = st.slider("6. Writing scripts to automate boring tasks?", 1, 5, 3)
            q7 = st.slider("7. Interest in learning how malware functions?", 1, 5, 3)
            q8 = st.slider("8. Analyzing network traffic and logs?", 1, 5, 3)
            q9 = st.slider("9. Interest in 'social engineering' (psychology)?", 1, 5, 3)
            q10 = st.slider("10. Setting up and configuring firewalls?", 1, 5, 3)

        with col2:
            st.subheader("Work Style & Ethics")
            q11 = st.slider("11. Prefer working alone for long hours?", 1, 5, 3)
            q12 = st.slider("12. Explaining technical risks to non-techies?", 1, 5, 3)
            q13 = st.slider("13. Following strict legal/ethical protocols?", 1, 5, 3)
            q14 = st.slider("14. Prefer high-intensity 'bursts' over routine?", 1, 5, 3)
            q15 = st.slider("15. Teaching others security best practices?", 1, 5, 3)

            st.subheader("Situational Response")
            q16 = st.slider("16. Staying calm when a system is 'under alarm'?", 1, 5, 3)
            q17 = st.slider("17. 'Hunting' for something hidden in massive data?", 1, 5, 3)
            q18 = st.slider("18. Prefer 'winning' vs 'preventing loss'?", 1, 5, 3)
            q19 = st.slider("19. Valuing a broad view of company security?", 1, 5, 3)
            q20 = st.slider("20. Thinking like a thief to prevent a crime?", 1, 5, 3)

        submit = st.form_submit_button("Analyze My Path")

        if submit:
            # RED SCORE: Focus on Offense, Breaking, Stealth, and Winning
            st.session_state.scores["Red"] = (q1 + q4 + q7 + q9 + q11 + q14 + q18 + q20)

            # BLUE SCORE: Focus on Defense, Logs, Protocols, and Prevention
            st.session_state.scores["Blue"] = (q2 + q8 + q10 + q13 + q16 + q17 + (6 - q18))

            # PURPLE SCORE: Focus on Coordination, Why, Automation, and Strategy
            st.session_state.scores["Purple"] = (q3 + q5 + q6 + q12 + q15 + q19)

            with st.spinner("Calculating Career Trajectory..."):
                time.sleep(1.5)
            st.session_state.app_state = 'result'
            st.rerun()

elif st.session_state.app_state == 'result':
    winner = max(st.session_state.scores, key=st.session_state.scores.get)
    res = ROADMAPS[winner]

    st.title(f"Target Path Identified: {res['title']}")
    st.markdown(f"<div style='border-bottom: 5px solid {res['color']}; margin-bottom: 20px;'></div>",
                unsafe_allow_html=True)

    st.info(f"**Description:** {res['desc']}")

    col_a, col_b = st.columns([2, 1])

    with col_a:
        st.subheader("🚀 Your Success Roadmap")
        for step in res['steps']:
            st.markdown(f"""<div class='roadmap-card' style='border-left-color: {res['color']}'>{step}</div>""",
                        unsafe_allow_html=True)

    with col_b:
        st.subheader("🛠️ Core Tech Stack")
        for tool in res['tools']:
            st.button(tool, disabled=True, key=tool)

        st.divider()
        if winner == "Blue":
            st.success("Analysis Complete: Guardian Mindset Detected.")
        elif winner == "Red":
            st.warning("Analysis Complete: Pathfinder Mindset Detected.")
        else:
            st.info("Analysis Complete: Strategist Mindset Detected.")

    if st.button("Retake Assessment"):
        st.session_state.app_state = 'quiz'
        st.rerun()