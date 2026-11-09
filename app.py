import streamlit as st
from pathlib import Path
from urllib.parse import quote
import base64

st.set_page_config(page_title="Spiritus School of Music", page_icon="🎼", layout="wide")
ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
PHONE = "917019586294"
ADDRESS = "Spiritus School of Music, No. 33, Arulappa Road, Near Old Church, Kammanahalli, Bengaluru, Karnataka, India"

st.markdown("""<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,500&display=swap" rel="stylesheet">""", unsafe_allow_html=True)
st.markdown("""
<style>
:root{--navy:#17243d;--gold:#c6a354;--ivory:#f7f5ef;--ink:#1c2942}
.stApp{background:var(--ivory);color:var(--ink);font-family:'DM Sans',sans-serif}
#MainMenu,footer{visibility:hidden} header[data-testid="stHeader"]{background:transparent}
.block-container{max-width:1440px;padding:0 5.5% 2rem}
.brandbar{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:16px 0;border-bottom:1px solid #e4e0d6}
.brand{display:flex;align-items:center;gap:12px;color:var(--navy);text-decoration:none}
.brand img{width:58px;height:58px;object-fit:contain;border:1px solid var(--gold);border-radius:50%;padding:3px}
.brand strong{display:block;font-size:15px;letter-spacing:2px}.brand small{font-size:9px;letter-spacing:3px}
.navlinks{display:flex;gap:20px;align-items:center;flex-wrap:wrap}.navlinks a{font-size:12px;color:var(--ink);text-decoration:none}
.goldbtn{display:inline-block;background:var(--gold);color:#111c30!important;padding:13px 19px;border-radius:4px;text-decoration:none;font-weight:700;font-size:12px}
.hero{margin:0 -6.2%;min-height:570px;padding:75px 10%;display:flex;align-items:center;background:linear-gradient(90deg,rgba(8,16,30,.93),rgba(8,16,30,.76) 52%,rgba(8,16,30,.3)),url('https://images.unsplash.com/photo-1510915361894-db8b60106cb1?auto=format&fit=crop&w=2200&q=85') center/cover;color:white}
.hero-inner{max-width:650px}.eyebrow,.kicker{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:20px}
.hero h1{font:500 clamp(48px,6.4vw,82px)/1.03 'Playfair Display',serif;color:white;margin:0 0 20px}.hero h1 em,.section-title em{color:var(--gold)}
.hero p{font-size:15px;line-height:1.9;color:#e0e3e8;max-width:470px}.hero-actions{display:flex;gap:14px;flex-wrap:wrap;margin-top:28px}
.outlinebtn{display:inline-block;border:1px solid #ddd;color:white!important;padding:12px 19px;text-decoration:none;border-radius:4px;font-size:12px}
.section{padding:82px 0}.section.alt{background:#efede6;margin:0 -6.2%;padding:82px 6.2%}.section.dark{background:var(--navy);color:white;margin:0 -6.2%;padding:78px 6.2%}
.section-title{font:500 clamp(38px,4.7vw,62px)/1.08 'Playfair Display',serif;color:var(--navy);margin:0 0 20px}.dark .section-title{color:white}
.lead{font-size:15px;line-height:1.9;color:#64748b}
.founder-img{display:block;width:100%;height:auto;max-height:560px;aspect-ratio:4/5;object-fit:cover;object-position:center 24%;border-radius:4px;box-shadow:0 16px 38px rgba(23,36,61,.14)}.founder-card{background:var(--navy);color:white;padding:18px 22px;font:19px 'Playfair Display',serif}
.factgrid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:25px}.fact{border-top:1px solid #d8d3c7;padding:13px 0}.fact small{display:block;color:#987a43;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:6px}
.reason{display:grid;grid-template-columns:1fr 1.2fr;gap:9%}.reason-row{display:grid;grid-template-columns:35px 1fr 1.2fr;gap:12px;padding:20px 0;border-top:1px solid #d8d3c7;align-items:center}.reason-row:last-child{border-bottom:1px solid #d8d3c7}.reason-row small{color:#a88336}.reason-row strong{font-size:14px}.reason-row span{font-size:12px;color:#718096;line-height:1.6}
.coursebody{background:#efede6;padding:26px 28px 30px}.coursebody h3{font:500 34px 'Playfair Display',serif;color:var(--navy);margin:8px 0}.coursebody p{font-size:13px;color:#66758a;line-height:1.8}.tags{display:flex;flex-wrap:wrap;gap:10px 16px;margin:18px 0 22px;font-size:12px;color:#52637b}.tags span:before{content:'✓';color:#a88336;margin-right:7px}
.keyboard-feature{background:#17243d;color:white;padding:34px 36px;margin:8px 0 34px;border:1px solid #c6a354;box-shadow:0 18px 45px rgba(23,36,61,.10)}
.keyboard-feature .kicker{color:#d8bd78}.keyboard-feature h3{font:500 clamp(34px,4vw,48px)/1.1 'Playfair Display',serif;color:#fff;margin:8px 0 16px}.keyboard-feature p{color:#d7deea;font-size:14px;line-height:1.9}.keyboard-feature .tags{color:#e4e8ef}.keyboard-feature .tags span:before{color:#d8bd78}
.keyboard-points{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:24px 0}.keyboard-point{border-top:1px solid #46516a;padding:13px 8px 8px 0}.keyboard-point b{display:block;color:#e2c77f;font:20px 'Playfair Display',serif;margin-bottom:5px}.keyboard-point span{font-size:11px;color:#d7deea;line-height:1.6}
.course-label{font-size:10px;letter-spacing:2px;color:#a88336;text-transform:uppercase;font-weight:700}

.visiongrid{display:grid;grid-template-columns:1fr 1fr;gap:7%}.visiongrid article+article{border-left:1px solid #46516a;padding-left:9%}.visiongrid h3{font:500 32px 'Playfair Display',serif;color:white}.visiongrid p{font-size:14px;line-height:1.9;color:#d7dce5}
.admissiongrid{display:grid;grid-template-columns:.8fr 1.2fr;gap:7%;align-items:start}.contactcard{background:#efede6;padding:30px}
.footer{background:#101b2e;color:white;margin:0 -6.2%;padding:42px 6.2% 24px}.footer a{color:#e4c779;text-decoration:none}
@media(max-width:800px){.block-container{padding:0 5% 1rem}.brandbar{align-items:flex-start;flex-direction:column}.navlinks{gap:12px}.hero{margin:0 -5.5%;padding:60px 7%;min-height:500px;background-position:58%}.section{padding:58px 0}.section.alt,.section.dark,.footer{margin-left:-5.5%;margin-right:-5.5%;padding-left:5.5%;padding-right:5.5%}.reason,.admissiongrid,.visiongrid{grid-template-columns:1fr;gap:25px}.visiongrid article+article{border:0;border-top:1px solid #46516a;padding:24px 0 0}.reason-row{grid-template-columns:28px 1fr}.reason-row span{grid-column:2}}
</style>""", unsafe_allow_html=True)

logo64 = base64.b64encode((ASSETS/"logo.png").read_bytes()).decode()
st.markdown(f"""<div class="brandbar"><a class="brand" href="#home"><img src="data:image/png;base64,{logo64}"><span><strong>SPIRITUS</strong><small>SCHOOL OF MUSIC</small></span></a>
<nav class="navlinks"><a href="#home">Home</a><a href="#about">About Us</a><a href="#courses">Courses</a><a href="#vision">Vision &amp; Mission</a><a href="#admissions">Admissions</a><a href="#contact">Contact Us</a><a class="goldbtn" href="#admissions">◉ Apply for Admission</a></nav></div>""",unsafe_allow_html=True)
st.markdown("""<div id="home" class="hero"><div class="hero-inner"><div class="eyebrow">— &nbsp; A place to find your sound</div><h1>Let Music Become<br>Your <em>Language.</em></h1><p>Learn Guitar and Keyboard with passion, discipline, and creativity at Spiritus School of Music.</p><div class="hero-actions"><a class="goldbtn" href="#admissions">Join Our Music Family&nbsp; →</a><a class="outlinebtn" href="#courses">Explore Our Courses</a></div></div></div><div style="text-align:center;padding:22px;color:#9a7a3e;font:italic 24px 'Playfair Display',serif">“Discover Your Rhythm. <em>Inspire Your Soul.</em>”</div>""",unsafe_allow_html=True)

st.markdown('<div id="about" class="section"><div class="kicker">01 — The Spiritus way</div>',unsafe_allow_html=True)
l,r=st.columns([.9,1.1],gap="large")
with l:
    founder64 = base64.b64encode((ASSETS/"founder.jpg").read_bytes()).decode()
    st.markdown(f'<img class="founder-img" src="data:image/jpeg;base64,{founder64}" alt="Founder of Spiritus School of Music" />',unsafe_allow_html=True)
    st.markdown('<div class="founder-card">Meet Our Founder ─────</div>',unsafe_allow_html=True)
with r:
    st.markdown("""<div class="kicker">Music is a language everyone can learn</div><h2 class="section-title">A place to explore.<br>A practice to <em>grow.</em></h2><p class="lead">Spiritus is a place to explore music, develop ability, and grow through structured instrumental learning.</p><p class="lead">We believe a meaningful musical journey is built one curious question, one careful practice, and one small breakthrough at a time. Our learning is grounded in the instrument, shaped around the student, and open to every age and starting point.</p><div class="factgrid"><div class="fact"><small>Founder</small><b>Daniel Prasad J</b></div><div class="fact"><small>Musical background</small><b>Keyboard and Guitar</b></div><div class="fact"><small>Experience</small><b>8 years</b></div><div class="fact"><small>Our approach</small><b>Learn with care</b></div></div>""",unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)

st.markdown("""<div class="section alt"><div class="reason"><div><div class="kicker">02 — Why Spiritus</div><h2 class="section-title">Good music begins<br>with a <em>good fit.</em></h2><p class="lead">Whether you’re discovering an instrument for the first time or building on what you know, your learning should meet you where you are.</p></div><div>
<div class="reason-row"><small>01</small><strong>Personalized learning</strong><span>Learning shaped around each student’s pace and goals.</span></div><div class="reason-row"><small>02</small><strong>Guitar and Keyboard</strong><span>Focused instrumental training across two expressive instruments.</span></div><div class="reason-row"><small>03</small><strong>Supportive by design</strong><span>An encouraging space to ask, practise, try again, and grow.</span></div><div class="reason-row"><small>04</small><strong>Strong foundations</strong><span>Musical fundamentals developed alongside practical skills.</span></div><div class="reason-row"><small>05</small><strong>Every starting point</strong><span>Welcoming beginners and aspiring musicians alike.</span></div></div></div></div>""",unsafe_allow_html=True)

st.markdown('<div id="courses" class="section"><div class="kicker">03 — Find your instrument</div><h2 class="section-title">A world of music.<br><em>Start with a note.</em></h2><p class="lead">Explore our two instrumental programmes, thoughtfully designed to help students build confidence, skill and a lifelong connection with music.</p></div>',unsafe_allow_html=True)

# Featured flagship programme: Keyboard
st.markdown('<div class="keyboard-feature"><div class="kicker">Featured programme · Our flagship learning experience</div><h3>Keyboard — discover the world<br>behind every melody.</h3><p>From your very first notes to expressive playing, our keyboard programme builds a strong musical foundation through guided practice, technique and creativity. Learn to understand music, not just play the keys.</p><div class="keyboard-points"><div class="keyboard-point"><b>01</b><span>Build confident technique and independent finger movement</span></div><div class="keyboard-point"><b>02</b><span>Understand notes, scales, chords and musical patterns</span></div><div class="keyboard-point"><b>03</b><span>Develop rhythm, melody, coordination and musical expression</span></div></div><div class="tags"><span>Keyboard orientation</span><span>Posture & hand position</span><span>Finger exercises</span><span>Notes & notation</span><span>Major and minor scales</span><span>Chords & progressions</span><span>Rhythm & timing</span><span>Sight-reading</span><span>Music theory</span><span>Melody & songs</span><span>Performance confidence</span></div></div>',unsafe_allow_html=True)

st.markdown('<div class="course-label">A learning journey that grows with you</div>',unsafe_allow_html=True)
p1,p2,p3=st.columns(3,gap="medium")
with p1:
    st.markdown('<div class="coursebody"><div class="kicker">Stage 01</div><h3>Foundations</h3><p>Get comfortable with the keyboard, learn note names, hand position, posture, finger numbers and simple melodies.</p></div>',unsafe_allow_html=True)
with p2:
    st.markdown('<div class="coursebody"><div class="kicker">Stage 02</div><h3>Skill building</h3><p>Develop scales, chords, rhythm, two-hand coordination, reading skills and a deeper understanding of music.</p></div>',unsafe_allow_html=True)
with p3:
    st.markdown('<div class="coursebody"><div class="kicker">Stage 03</div><h3>Musical expression</h3><p>Bring songs to life with dynamics, expression, accompaniment patterns and confident performance.</p></div>',unsafe_allow_html=True)

kb1,kb2=st.columns([1.05,.95],gap="large")
with kb1:
    st.image("https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?auto=format&fit=crop&w=1400&q=90",use_container_width=True)
with kb2:
    st.markdown('<div class="coursebody" style="height:100%"><div class="kicker">Keyboard classes</div><h3>Your first note can become a lifelong skill.</h3><p>Whether you are a complete beginner or already familiar with the instrument, lessons are shaped around your pace, age and musical goals.</p><div class="tags"><span>Beginner friendly</span><span>Structured practice</span><span>Individual progress</span><span>Practical learning</span></div></div>',unsafe_allow_html=True)
st.markdown(f'<a class="goldbtn" href="https://wa.me/{PHONE}?text={quote("Hello Spiritus School of Music, I would like to enquire about Keyboard classes. Please share the syllabus, class timings and fees.")}" target="_blank">Enquire About Keyboard Classes&nbsp; →</a>',unsafe_allow_html=True)

st.markdown('<div style="height:58px"></div><div class="course-label">Also available at Spiritus</div><h2 class="section-title" style="font-size:42px">Guitar</h2>',unsafe_allow_html=True)
g1,g2=st.columns([.9,1.1],gap="large")
with g1:
    st.image("https://images.unsplash.com/photo-1510915361894-db8b60106cb1?auto=format&fit=crop&w=1200&q=85",use_container_width=True)
with g2:
    st.markdown('<div class="coursebody"><div class="kicker">Instrumental learning</div><h3>Find your rhythm on guitar.</h3><p>Learn guitar from the fundamentals to more advanced playing skills through structured, practical lessons.</p><div class="tags"><span>Basic chords</span><span>Strumming patterns</span><span>Rhythm</span><span>Scales</span><span>Music theory</span><span>Songs</span></div></div>',unsafe_allow_html=True)
    st.markdown(f'<a class="goldbtn" href="https://wa.me/{PHONE}?text={quote("Hello Spiritus School of Music, I would like to enquire about Guitar classes.")}" target="_blank">Enquire About Guitar Classes&nbsp; →</a>',unsafe_allow_html=True)

st.markdown("""<div id="vision" class="section dark"><div class="kicker">04 — What we believe</div><hr style="border-color:#46516a;margin:20px 0 42px"><div class="visiongrid"><article><div class="kicker">V.</div><h3>Our Vision</h3><p>Our vision is to inspire a love for music, nurture creativity, and empower every student to discover their musical potential through quality instrumental education.</p></article><article><div class="kicker">M.</div><h3>Our Mission</h3><p>Our mission is to provide an encouraging and disciplined learning environment where students develop musical skills, confidence, creativity, and a lifelong appreciation for music.</p></article></div><hr style="border-color:#46516a;margin:45px 0 20px"><p style="text-align:center;color:#d8bd78;font-size:10px;letter-spacing:2px">LEARN WITH CARE　 —　 PLAY WITH CONFIDENCE　 —　 KEEP LISTENING</p></div>""",unsafe_allow_html=True)

st.markdown('<div id="admissions" class="section"><div class="admissiongrid"><div><div class="kicker">05 — Your next chapter</div><h2 class="section-title">Make room<br>for <em>music.</em></h2><p class="lead">Curiosity is a wonderful place to begin.</p><p class="lead">Tell us a little about the student and the instrument they’re drawn to. We’ll help you understand the admission procedure, class timings, and fee details.</p><p style="margin-top:28px;font-size:11px;letter-spacing:2px;color:#8b7851">RATHER TALK FIRST?</p><h3>+91 70195 86294</h3><p class="lead"><i>“Every musical journey begins with a first note.”</i></p></div>',unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="contactcard"><div class="kicker">Your first note</div><h2 class="section-title" style="font-size:38px">Tell us what you’d love to learn.</h2><p class="lead">Share a few details. We’ll open a WhatsApp message for you to review and send.</p>',unsafe_allow_html=True)
    with st.form("admission_form"):
        a,b=st.columns(2)
        with a:
            student=st.text_input("Student Full Name *",placeholder="Your name")
            age=st.text_input("Age *",placeholder="Age")
            instrument=st.selectbox("Instrument *",["Choose an instrument","Guitar","Keyboard","Both Guitar and Keyboard"])
        with b:
            guardian=st.text_input("Parent/Guardian Name",placeholder="Optional")
            mobile=st.text_input("WhatsApp / Mobile Number *",placeholder="+91")
            experience=st.selectbox("Previous Musical Experience",["Beginner","Some experience","Intermediate","Advanced"])
        timing=st.text_input("Preferred Class Timing",placeholder="Optional — let us know what works for you")
        message=st.text_area("Additional Message",placeholder="Anything else you’d like us to know?")
        submitted=st.form_submit_button("Continue to WhatsApp →",use_container_width=True)
        if submitted:
            if not student.strip() or not age.strip() or not mobile.strip() or instrument=="Choose an instrument":
                st.error("Please complete the required fields marked with *.")
            else:
                msg=f"""Hello Spiritus School of Music,\n\nI would like to enquire about admission.\nStudent name: {student}\nAge: {age}\nParent/Guardian: {guardian or 'Not provided'}\nMobile: {mobile}\nInstrument: {instrument}\nPrevious experience: {experience}\nPreferred timing: {timing or 'Not specified'}\nAdditional message: {message or 'None'}\n\nPlease share the admission procedure, class timings and fee details. Thank you."""
                st.link_button("Open WhatsApp to review and send",f"https://wa.me/{PHONE}?text={quote(msg)}",use_container_width=True)
                st.caption("Your message is not sent automatically. You can review it before sending.")
    st.markdown('</div>',unsafe_allow_html=True)
st.markdown('</div></div>',unsafe_allow_html=True)

st.markdown(f"""<div id="contact" class="section dark"><div class="admissiongrid"><div style="display:flex;align-items:center;justify-content:center;border-right:1px solid #46516a;min-height:250px"><div style="font:italic 180px 'Playfair Display',serif;color:#c6a354">S</div></div><div><div class="kicker">A place for every note</div><h2 class="section-title">Your music<br>starts <em>here.</em></h2><p class="lead" style="color:#d5dce7">We’d love to hear what you’re hoping to learn.</p><hr style="border-color:#46516a"><div class="kicker">Visit us</div><p>{ADDRESS}</p><a href="https://maps.app.goo.gl/MN6W9uuuRen73P7S7" target="_blank">Get Directions ↗</a><br><br><div class="kicker">Call or WhatsApp</div><p>+91 70195 86294</p><a href="https://wa.me/{PHONE}" target="_blank">WhatsApp enquiry ↗</a></div></div></div><div class="footer"><strong style="font:22px 'Playfair Display',serif">Spiritus School of Music</strong><p>Discover Your Rhythm. Inspire Your Soul.</p><p><a href="#home">Home</a>　<a href="#about">About</a>　<a href="#courses">Courses</a>　<a href="#admissions">Admissions</a></p><hr style="border-color:#344056">© 2026 Spiritus School of Music. All rights reserved.</div>""",unsafe_allow_html=True)
