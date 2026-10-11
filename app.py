import streamlit as st
import html
import base64
from datetime import datetime

# =========================================================
# CẤU HÌNH
# =========================================================
st.set_page_config(
    page_title="JOBMATE - Hồ sơ xin việc",
    page_icon="💼",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#f5f7fb,#edf2ff);}
.block-container {max-width:1200px;padding-top:1.5rem;padding-bottom:3rem;}
.hero {background:linear-gradient(135deg,#111827,#374151);padding:30px;border-radius:22px;color:white;margin-bottom:22px;}
.hero-title {font-size:42px;font-weight:800;margin-bottom:5px;}
.hero-subtitle {font-size:18px;}
.cv-section {font-size:19px;font-weight:800;border-bottom:2px solid #334155;padding-bottom:7px;margin:18px 0 10px;}
.score-box {background:white;padding:25px;border-radius:18px;text-align:center;border:1px solid #ddd;}
.score-number {font-size:48px;font-weight:800;}
</style>
""", unsafe_allow_html=True)

# =========================================================
# DỮ LIỆU LƯU TRONG SESSION
# =========================================================
DEFAULTS = {
    "full_name": "", "birthday": "", "gender": "Chưa chọn",
    "phone": "", "email": "", "address": "", "job": "",
    "career_goal": "", "about": "", "school": "", "major": "",
    "education_time": "", "gpa": 0.0, "experience": "",
    "skills": "", "languages": "", "certificates": "",
    "achievements": "", "salary": 0, "photo_bytes": None,
    "interview_index": 0, "interview_started": False,
    "interview_history": []
}
for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value

def esc(value):
    """Escape dữ liệu người dùng trước khi đưa vào HTML."""
    return html.escape(str(value or "")).replace("\n", "<br>")

def section_html(title, content):
    return f'<section><h2>{title}</h2><div>{content or "<p>Chưa cập nhật</p>"}</div></section>'

def build_cv_html():
    """Tạo bản CV HTML độc lập để tải xuống, in hoặc lưu PDF."""
    s = st.session_state
    name = esc(s.full_name or "HỌ VÀ TÊN")
    job = esc(s.job or "VỊ TRÍ ỨNG TUYỂN")
    photo_html = ""
    if s.photo_bytes:
        photo_b64 = base64.b64encode(s.photo_bytes).decode("utf-8")
        photo_html = f'<img class="photo" src="data:image/jpeg;base64,{photo_b64}" alt="Ảnh hồ sơ">'

    contact = [
        ("Điện thoại", s.phone), ("Email", s.email),
        ("Địa chỉ", s.address), ("Ngày sinh", s.birthday),
        ("Giới tính", s.gender)
    ]
    contact_html = "".join(
        f"<p><b>{html.escape(label)}:</b> {esc(value or 'Chưa cập nhật')}</p>"
        for label, value in contact
    )

    sections = [
        ("MỤC TIÊU NGHỀ NGHIỆP", s.career_goal),
        ("GIỚI THIỆU BẢN THÂN", s.about),
        ("HỌC VẤN", f"<p><b>{esc(s.school or 'Chưa cập nhật')}</b></p>"
         f"<p>Chuyên ngành: {esc(s.major or 'Chưa cập nhật')}</p>"
         f"<p>Thời gian: {esc(s.education_time or 'Chưa cập nhật')}</p>"
         f"<p>GPA: {s.gpa:.1f}/4.0</p>"),
        ("KINH NGHIỆM LÀM VIỆC", s.experience),
        ("KỸ NĂNG", s.skills),
        ("NGOẠI NGỮ", s.languages),
        ("CHỨNG CHỈ", s.certificates),
        ("THÀNH TÍCH", s.achievements),
        ("MỨC LƯƠNG MONG MUỐN",
         f"<p>{s.salary:,.0f} VNĐ/tháng</p>" if s.salary else "Chưa cập nhật")
    ]
    sections_html = "".join(
        f'<section><h2>{title}</h2><div>{esc(content) if isinstance(content, str) else content}</div></section>'
        for title, content in sections
    )
    return f"""<!doctype html>
<html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CV - {name}</title>
<style>
*{{box-sizing:border-box}} body{{font-family:Arial,Helvetica,sans-serif;background:#eef2f7;color:#1f2937;margin:0;padding:24px;line-height:1.55}}
.toolbar{{max-width:850px;margin:0 auto 16px;text-align:right}}
button{{background:#1d4ed8;color:#fff;border:0;border-radius:8px;padding:12px 18px;font-size:15px;cursor:pointer}}
.cv{{max-width:850px;margin:auto;background:#fff;padding:42px;border-radius:12px;box-shadow:0 4px 22px #0001}}
.top{{display:flex;gap:24px;align-items:center;border-bottom:3px solid #1d4ed8;padding-bottom:22px}}
.photo{{width:135px;height:160px;object-fit:cover;border-radius:8px}}
h1{{font-size:30px;margin:0 0 5px;color:#111827}} .job{{font-size:18px;color:#1d4ed8;font-weight:bold;margin-bottom:12px}}
.contact p{{margin:3px 0;font-size:14px}} section{{margin-top:20px;break-inside:avoid}}
h2{{font-size:16px;color:#1d4ed8;border-bottom:1px solid #cbd5e1;padding-bottom:6px}}
section div{{white-space:normal;overflow-wrap:anywhere}}
@media(max-width:600px){{body{{padding:8px}}.cv{{padding:20px}}.top{{align-items:flex-start;flex-direction:column}}}}
@media print{{body{{background:white;padding:0}}.toolbar{{display:none}}.cv{{box-shadow:none;border-radius:0;padding:12mm;max-width:none}}@page{{size:A4;margin:10mm}}}}
</style></head><body>
<div class="toolbar"><button onclick="window.print()">🖨️ In / Lưu thành PDF</button></div>
<main class="cv">
<div class="top">{photo_html}<div><h1>{name}</h1><div class="job">{job}</div><div class="contact">{contact_html}</div></div></div>
{sections_html}
</main></body></html>"""

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="hero">
  <div class="hero-title">💼 JOBMATE</div>
  <div class="hero-subtitle">HỒ SƠ XIN VIỆC THÔNG MINH</div>
  <p>Tạo CV chuyên nghiệp • Đánh giá hồ sơ • Luyện phỏng vấn</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("💼 JOBMATE")
st.sidebar.caption("HỒ SƠ XIN VIỆC THÔNG MINH")
pages = [
    "👤 Thông tin cá nhân", "🎓 Học vấn",
    "💼 Kinh nghiệm & kỹ năng", "💰 Mức lương mong muốn",
    "📊 Đánh giá hồ sơ", "🤖 AI Phỏng vấn", "📄 Xem hồ sơ"
]
page = st.sidebar.radio("📌 CHỨC NĂNG", pages)
st.sidebar.info("Điền thông tin rồi bấm nút Lưu ở cuối mỗi mục. Dữ liệu được giữ khi chuyển trang trong phiên làm việc này.")

# =========================================================
# 1. THÔNG TIN CÁ NHÂN
# =========================================================
if page == "👤 Thông tin cá nhân":
    st.header("👤 THÔNG TIN CÁ NHÂN")
    col_photo, col_info = st.columns([1, 2])
    with col_photo:
        st.subheader("📷 Ảnh hồ sơ")
        photo = st.file_uploader("Tải ảnh chân dung", type=["jpg", "jpeg", "png"], key="photo_upload")
        if photo is not None:
            st.session_state.photo_bytes = photo.getvalue()
        if st.session_state.photo_bytes:
            st.image(st.session_state.photo_bytes, width=200)
        st.caption("Nên dùng ảnh rõ mặt, nền đơn giản.")
    with col_info:
        full_name = st.text_input("Họ và tên *", value=st.session_state.full_name)
        birthday = st.text_input("Ngày sinh", value=st.session_state.birthday, placeholder="09/06/2006")
        gender = st.selectbox("Giới tính", ["Chưa chọn", "Nam", "Nữ", "Khác"],
                              index=["Chưa chọn", "Nam", "Nữ", "Khác"].index(
                                  st.session_state.gender if st.session_state.gender in ["Chưa chọn", "Nam", "Nữ", "Khác"] else "Chưa chọn"))
        phone = st.text_input("Số điện thoại *", value=st.session_state.phone)
        email = st.text_input("Email *", value=st.session_state.email)
        address = st.text_input("Địa chỉ", value=st.session_state.address)
    job = st.text_input("🎯 Vị trí muốn ứng tuyển *", value=st.session_state.job, placeholder="Ví dụ: Nhân viên ngân hàng")
    career_goal = st.text_area("🎯 Mục tiêu nghề nghiệp", value=st.session_state.career_goal, height=100)
    about = st.text_area("✨ Giới thiệu bản thân", value=st.session_state.about, height=120)
    if st.button("💾 LƯU THÔNG TIN CÁ NHÂN", type="primary", use_container_width=True):
        st.session_state.update({
            "full_name": full_name.strip(), "birthday": birthday.strip(),
            "gender": gender, "phone": phone.strip(), "email": email.strip(),
            "address": address.strip(), "job": job.strip(),
            "career_goal": career_goal.strip(), "about": about.strip()
        })
        st.success("Đã lưu thông tin cá nhân!")

# =========================================================
# 2. HỌC VẤN
# =========================================================
elif page == "🎓 Học vấn":
    st.header("🎓 HỌC VẤN")
    school = st.text_input("🏫 Tên trường", value=st.session_state.school)
    major = st.text_input("📚 Chuyên ngành", value=st.session_state.major)
    education_time = st.text_input("📅 Thời gian học", value=st.session_state.education_time, placeholder="2024 - 2028")
    gpa = st.number_input("📊 GPA (thang điểm 4)", min_value=0.0, max_value=4.0, value=float(st.session_state.gpa), step=0.1)
    if st.button("💾 LƯU HỌC VẤN", type="primary", use_container_width=True):
        st.session_state.update({"school": school.strip(), "major": major.strip(),
                                 "education_time": education_time.strip(), "gpa": gpa})
        st.success("Đã lưu học vấn!")

# =========================================================
# 3. KINH NGHIỆM & KỸ NĂNG
# =========================================================
elif page == "💼 Kinh nghiệm & kỹ năng":
    st.header("💼 KINH NGHIỆM & KỸ NĂNG")
    experience = st.text_area("💼 Kinh nghiệm làm việc", value=st.session_state.experience, height=180,
        placeholder="Công ty ABC\nVị trí: Nhân viên bán hàng\nThời gian: 06/2025 - 08/2026\n- Tư vấn khách hàng\n- Quản lý hàng hóa")
    skills = st.text_area("🛠️ Kỹ năng", value=st.session_state.skills, height=120, placeholder="Giao tiếp\nLàm việc nhóm\nExcel\nChăm sóc khách hàng")
    languages = st.text_area("🌐 Ngoại ngữ", value=st.session_state.languages, height=90, placeholder="Tiếng Anh..., Tiếng Trung...")
    certificates = st.text_area("📜 Chứng chỉ", value=st.session_state.certificates, height=90)
    achievements = st.text_area("🏆 Thành tích", value=st.session_state.achievements, height=90)
    if st.button("💾 LƯU KINH NGHIỆM & KỸ NĂNG", type="primary", use_container_width=True):
        st.session_state.update({"experience": experience.strip(), "skills": skills.strip(),
                                 "languages": languages.strip(), "certificates": certificates.strip(),
                                 "achievements": achievements.strip()})
        st.success("Đã lưu kinh nghiệm và kỹ năng!")

# =========================================================
# 4. LƯƠNG
# =========================================================
elif page == "💰 Mức lương mong muốn":
    st.header("💰 MỨC LƯƠNG MONG MUỐN")
    salary = st.number_input("Mức lương mong muốn (VNĐ/tháng)", min_value=0,
                              value=int(st.session_state.salary), step=100000)
    if salary:
        st.success(f"Mức lương: {salary:,.0f} VNĐ/tháng")
    if st.button("💾 LƯU MỨC LƯƠNG", type="primary", use_container_width=True):
        st.session_state.salary = int(salary)
        st.success("Đã lưu mức lương!")

# =========================================================
# 5. ĐÁNH GIÁ HỒ SƠ
# =========================================================
elif page == "📊 Đánh giá hồ sơ":
    st.header("📊 ĐÁNH GIÁ HỒ SƠ")
    s = st.session_state
    personal = sum([5 if s.full_name else 0, 5 if s.phone else 0,
                    5 if s.email else 0, 5 if s.photo_bytes else 0])
    education = sum([7 if s.school else 0, 7 if s.major else 0, 6 if s.gpa > 0 else 0])
    experience_score = 20 if s.experience else 0
    skills_score = (12 if s.skills else 0) + (8 if s.languages else 0)
    extras = (10 if s.certificates else 0) + (10 if s.achievements else 0)
    score = personal + education + experience_score + skills_score + extras
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown(f'<div class="score-box"><div>ĐIỂM HỒ SƠ</div><div class="score-number">{score}/100</div></div>', unsafe_allow_html=True)
    with c2:
        if score >= 85:
            st.success("🌟 Hồ sơ rất tốt. Hãy kiểm tra chính tả trước khi ứng tuyển.")
        elif score >= 70:
            st.info("👍 Hồ sơ khá tốt. Bạn có thể bổ sung thêm thành tích hoặc chứng chỉ.")
        elif score >= 50:
            st.warning("⚠️ Hồ sơ cần bổ sung một số nội dung.")
        else:
            st.error("❗ Hồ sơ còn thiếu nhiều thông tin.")
    st.divider()
    for label, got in [
        ("Thông tin cá nhân", personal), ("Học vấn", education),
        ("Kinh nghiệm", experience_score), ("Kỹ năng & ngoại ngữ", skills_score),
        ("Chứng chỉ & thành tích", extras)
    ]:
        st.write(f"**{label}: {got}/20 điểm**")
        st.progress(got / 20)
    tips = []
    if not s.full_name or not s.phone or not s.email: tips.append("Điền họ tên, số điện thoại và email.")
    if not s.photo_bytes: tips.append("Thêm ảnh hồ sơ rõ nét.")
    if not s.school or not s.major: tips.append("Bổ sung thông tin học vấn.")
    if not s.experience: tips.append("Bổ sung kinh nghiệm hoặc hoạt động thực tế liên quan.")
    if not s.skills: tips.append("Nêu các kỹ năng phù hợp với vị trí.")
    if not s.languages: tips.append("Bổ sung ngoại ngữ nếu có.")
    if not s.certificates: tips.append("Thêm chứng chỉ liên quan nếu có.")
    st.subheader("💡 Gợi ý cải thiện")
    if tips:
        for tip in tips: st.write("• " + tip)
    else:
        st.success("Hồ sơ đã có đầy đủ các mục quan trọng!")
    st.caption("Điểm số chỉ đánh giá mức độ đầy đủ của thông tin, không bảo đảm kết quả tuyển dụng.")

# =========================================================
# 6. LUYỆN PHỎNG VẤN
# =========================================================
elif page == "🤖 AI Phỏng vấn":
    st.header("🤖 JOBMATE INTERVIEW COACH")
    st.info("Đây là công cụ luyện tập theo ngân hàng câu hỏi có sẵn; chưa kết nối mô hình AI trực tuyến.")
    question_bank = {
        "Phỏng vấn tổng quát": [
            "Hãy giới thiệu bản thân trong 1 phút.",
            "Tại sao bạn muốn ứng tuyển vị trí này?",
            "Điểm mạnh và điểm yếu của bạn là gì?",
            "Kể về một lần bạn giải quyết vấn đề khó khăn.",
            "Tại sao chúng tôi nên tuyển bạn?",
            "Mức lương mong muốn của bạn là bao nhiêu?",
            "Bạn định hướng nghề nghiệp trong 3 năm tới như thế nào?"
        ],
        "Phỏng vấn ngân hàng": [
            "Hãy giới thiệu bản thân và lý do bạn chọn ngành ngân hàng.",
            "Theo bạn, nhân viên ngân hàng cần những kỹ năng nào?",
            "Bạn sẽ xử lý thế nào khi khách hàng tức giận?",
            "Nếu khách hàng từ chối sản phẩm, bạn sẽ làm gì?",
            "Bạn quản lý áp lực chỉ tiêu như thế nào?",
            "Bạn làm gì để bảo mật thông tin khách hàng?"
        ],
        "Phỏng vấn bán hàng": [
            "Bạn có kinh nghiệm bán hàng không?",
            "Bạn sẽ làm gì khi khách hàng nói sản phẩm quá đắt?",
            "Bạn làm thế nào để tăng doanh số?",
            "Nếu khách hàng phàn nàn, bạn xử lý ra sao?",
            "Bạn sắp xếp hàng hóa và kiểm soát tồn kho thế nào?"
        ],
        "Chăm sóc khách hàng": [
            "Theo bạn, dịch vụ khách hàng tốt là gì?",
            "Bạn xử lý khách hàng khó tính như thế nào?",
            "Nếu chưa biết câu trả lời, bạn sẽ làm gì?",
            "Kể một tình huống bạn lắng nghe và hỗ trợ người khác."
        ],
        "Sinh viên mới ra trường": [
            "Hãy giới thiệu bản thân.",
            "Bạn chưa có nhiều kinh nghiệm, vì sao chúng tôi nên tuyển bạn?",
            "Bạn đã học được kỹ năng gì ở trường?",
            "Bạn muốn học hỏi điều gì trong công việc đầu tiên?"
        ]
    }
    interview_type = st.selectbox("Chọn loại phỏng vấn", list(question_bank.keys()))
    difficulty = st.select_slider("Độ khó", options=["Dễ", "Trung bình", "Khó"], value="Trung bình")
    questions = question_bank[interview_type]
    if st.button("🎤 BẮT ĐẦU / LÀM LẠI", type="primary", use_container_width=True):
        st.session_state.interview_started = True
        st.session_state.interview_index = 0
        st.session_state.interview_history = []
        st.rerun()
    if st.session_state.interview_started:
        idx = min(st.session_state.interview_index, len(questions) - 1)
        st.markdown(f"### 👔 Câu hỏi {idx + 1}/{len(questions)}")
        st.markdown(f"> {questions[idx]}")
        answer_key = f"answer_{interview_type}_{idx}"
        answer = st.text_area("Nhập câu trả lời của bạn", key=answer_key, height=160,
                              placeholder="Trả lời như khi phỏng vấn trực tiếp...")
        if st.button("🔍 Nhận xét câu trả lời", use_container_width=True):
            words = len(answer.split())
            if not answer.strip():
                st.warning("Bạn hãy nhập câu trả lời trước.")
            else:
                # Điểm tham khảo dựa trên độ dài, không phải đánh giá AI thực sự.
                score = 4 if words < 15 else 6 if words < 30 else 8 if words < 60 else 9
                st.metric("Điểm tham khảo", f"{score}/10")
                if words < 15:
                    st.warning("Câu trả lời còn ngắn. Hãy giải thích lý do và thêm ví dụ.")
                elif words < 30:
                    st.info("Câu trả lời có ý chính. Hãy nêu hành động cụ thể và kết quả.")
                else:
                    st.success("Độ dài tương đối tốt. Hãy bảo đảm câu trả lời đúng trọng tâm và chân thật.")
                st.markdown("**Công thức STAR:** Tình huống → Nhiệm vụ → Hành động → Kết quả.")
                st.caption(f"Độ khó đã chọn: {difficulty}. Điểm này là tham khảo theo độ dài câu trả lời.")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("➡️ Câu tiếp theo", use_container_width=True):
                if idx < len(questions) - 1:
                    st.session_state.interview_index += 1
                    st.rerun()
                else:
                    st.success("🎉 Bạn đã hoàn thành bộ câu hỏi này!")
        with c2:
            if st.button("⏹️ Kết thúc luyện tập", use_container_width=True):
                st.session_state.interview_started = False
                st.session_state.interview_index = 0
                st.rerun()

# =========================================================
# 7. XEM, TẢI VÀ IN CV
# =========================================================
elif page == "📄 Xem hồ sơ":
    st.header("📄 HỒ SƠ XIN VIỆC CỦA BẠN")
    st.caption("Bản xem trước lấy từ dữ liệu đã lưu ở các mục bên trái.")
    s = st.session_state

    with st.container(border=True):
        cphoto, cinfo = st.columns([1, 3])
        with cphoto:
            if s.photo_bytes:
                st.image(s.photo_bytes, width=170)
            else:
                st.info("Chưa có ảnh")
        with cinfo:
            st.markdown(f"## {s.full_name or 'HỌ VÀ TÊN'}")
            st.markdown(f"### {s.job or 'VỊ TRÍ ỨNG TUYỂN'}")
            st.write(f"📱 {s.phone or 'Chưa cập nhật'}")
            st.write(f"📧 {s.email or 'Chưa cập nhật'}")
            st.write(f"📍 {s.address or 'Chưa cập nhật'}")
            st.write(f"🎂 {s.birthday or 'Chưa cập nhật'} · {s.gender}")
    sections = [
        ("🎯 MỤC TIÊU NGHỀ NGHIỆP", s.career_goal),
        ("✨ GIỚI THIỆU BẢN THÂN", s.about),
        ("🎓 HỌC VẤN", f"Trường: {s.school or 'Chưa cập nhật'}\nChuyên ngành: {s.major or 'Chưa cập nhật'}\nThời gian: {s.education_time or 'Chưa cập nhật'}\nGPA: {s.gpa:.1f}/4.0"),
        ("💼 KINH NGHIỆM LÀM VIỆC", s.experience),
        ("🛠️ KỸ NĂNG", s.skills),
        ("🌐 NGOẠI NGỮ", s.languages),
        ("📜 CHỨNG CHỈ", s.certificates),
        ("🏆 THÀNH TÍCH", s.achievements),
        ("💰 MỨC LƯƠNG MONG MUỐN", f"{s.salary:,.0f} VNĐ/tháng" if s.salary else "")
    ]
    for title, content in sections:
        with st.container(border=True):
            st.markdown(f'<div class="cv-section">{html.escape(title)}</div>', unsafe_allow_html=True)
            if content and str(content).strip():
                st.markdown(str(content))
            else:
                st.caption("Chưa cập nhật")

    st.divider()
    st.subheader("📥 LƯU HỒ SƠ / IN PDF")
    st.write("1. Tải file HTML bên dưới về thiết bị.")
    st.write("2. Mở file bằng Safari, Chrome hoặc trình duyệt trên máy tính.")
    st.write("3. Chọn nút **In / Lưu thành PDF** trong file, sau đó chọn **Save as PDF / Lưu thành PDF**.")
    cv_html = build_cv_html()
    safe_filename = "".join(ch for ch in (s.full_name or "JOBMATE_CV") if ch.isalnum() or ch in (" ", "-", "_")).strip().replace(" ", "_")
    st.download_button(
        "📄 TẢI HỒ SƠ ĐỂ IN / LƯU PDF (HTML)",
        data=cv_html.encode("utf-8"),
        file_name=f"{safe_filename or 'JOBMATE_CV'}.html",
        mime="text/html",
        type="primary",
        use_container_width=True
    )
    st.caption("File tải xuống chứa hồ sơ đã điền và ảnh chân dung. Để có PDF, mở file đã tải rồi dùng chức năng In của trình duyệt.")

# =========================================================
# FOOTER
# =========================================================
st.divider()
st.caption("💼 JOBMATE – Mini App Hồ sơ xin việc thông minh | Dự án học tập")
