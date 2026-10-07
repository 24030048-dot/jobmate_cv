import streamlit as st
import html

# =========================================================
# CẤU HÌNH APP
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

.stApp {
    background: linear-gradient(135deg, #f5f7fb, #edf2ff);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.hero {
    background: linear-gradient(135deg, #111827, #374151);
    padding: 35px;
    border-radius: 24px;
    color: white;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 45px;
    font-weight: 800;
    margin-bottom: 5px;
}

.hero-subtitle {
    font-size: 18px;
}

.cv-box {
    background: white;
    padding: 35px;
    border-radius: 20px;
    border: 1px solid #dfe3ea;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
}

.cv-name {
    font-size: 34px;
    font-weight: 800;
}

.cv-job {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 12px;
}

.cv-section {
    font-size: 20px;
    font-weight: 800;
    border-bottom: 2px solid #222;
    padding-bottom: 7px;
    margin-top: 25px;
    margin-bottom: 12px;
}

.score-box {
    background: white;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid #ddd;
}

.score-number {
    font-size: 55px;
    font-weight: 800;
}

.small-note {
    color: #64748b;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

default_values = {
    "full_name": "",
    "birthday": "",
    "gender": "Chưa chọn",
    "phone": "",
    "email": "",
    "address": "",
    "job": "",
    "career_goal": "",
    "about": "",
    "school": "",
    "major": "",
    "education_time": "",
    "gpa": 0.0,
    "experience": "",
    "skills": "",
    "languages": "",
    "certificates": "",
    "achievements": "",
    "salary": 0,
    "photo_bytes": None,
    "photo_type": None
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">

<div class="hero-title">💼 JOBMATE</div>

<div class="hero-subtitle">
HỒ SƠ XIN VIỆC THÔNG MINH
</div>

<p>
Tạo hồ sơ xin việc chuyên nghiệp, đánh giá hồ sơ
và xác định mức lương mong muốn.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("💼 JOBMATE")
st.sidebar.caption("HỒ SƠ XIN VIỆC THÔNG MINH")

page = st.sidebar.radio(
    "📌 CHỨC NĂNG",
    [
        "👤 Thông tin cá nhân",
        "🎓 Học vấn",
        "💼 Kinh nghiệm & kỹ năng",
        "💰 Mức lương mong muốn",
        "📊 Đánh giá hồ sơ",
        "📄 Xem hồ sơ"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "Nhập thông tin ở từng mục. "
    "Sau đó chọn **📄 Xem hồ sơ** để xem CV."
)


# =========================================================
# 1. THÔNG TIN CÁ NHÂN
# =========================================================

if page == "👤 Thông tin cá nhân":

    st.header("👤 THÔNG TIN CÁ NHÂN")

    col_photo, col_info = st.columns([1, 2])

    with col_photo:

        st.subheader("📷 Ảnh hồ sơ")

        uploaded_photo = st.file_uploader(
            "Tải ảnh chân dung",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_photo is not None:

            st.session_state.photo_bytes = uploaded_photo.getvalue()
            st.session_state.photo_type = uploaded_photo.type

            st.image(
                st.session_state.photo_bytes,
                width=220
            )

        elif st.session_state.photo_bytes is not None:

            st.image(
                st.session_state.photo_bytes,
                width=220
            )

        st.caption(
            "Nên sử dụng ảnh rõ mặt, nghiêm túc và nền đơn giản."
        )

    with col_info:

        st.subheader("📝 Thông tin cá nhân")

        full_name = st.text_input(
            "Họ và tên *",
            value=st.session_state.full_name,
            placeholder="Nguyễn Văn A"
        )

        birthday = st.text_input(
            "Ngày sinh",
            value=st.session_state.birthday,
            placeholder="09/06/2006"
        )

        gender_options = [
            "Chưa chọn",
            "Nam",
            "Nữ",
            "Khác"
        ]

        current_gender = st.session_state.gender

        if current_gender not in gender_options:
            current_gender = "Chưa chọn"

        gender = st.selectbox(
            "Giới tính",
            gender_options,
            index=gender_options.index(current_gender)
        )

        phone = st.text_input(
            "Số điện thoại *",
            value=st.session_state.phone,
            placeholder="09xxxxxxxx"
        )

        email = st.text_input(
            "Email *",
            value=st.session_state.email,
            placeholder="example@gmail.com"
        )

        address = st.text_input(
            "Địa chỉ",
            value=st.session_state.address,
            placeholder="Thủ Dầu Một, Bình Dương"
        )

    st.divider()

    job = st.text_input(
        "🎯 Vị trí muốn ứng tuyển *",
        value=st.session_state.job,
        placeholder="Ví dụ: Nhân viên ngân hàng"
    )

    career_goal = st.text_area(
        "🎯 Mục tiêu nghề nghiệp",
        value=st.session_state.career_goal,
        height=120,
        placeholder="Viết mục tiêu nghề nghiệp của bạn..."
    )

    about = st.text_area(
        "✨ Giới thiệu bản thân",
        value=st.session_state.about,
        height=150,
        placeholder="Giới thiệu ngắn gọn về bản thân..."
    )

    if st.button(
        "💾 LƯU THÔNG TIN",
        type="primary",
        use_container_width=True
    ):

        st.session_state.full_name = full_name
        st.session_state.birthday = birthday
        st.session_state.gender = gender
        st.session_state.phone = phone
        st.session_state.email = email
        st.session_state.address = address
        st.session_state.job = job
        st.session_state.career_goal = career_goal
        st.session_state.about = about

        st.success("✅ Đã lưu thông tin cá nhân!")


# =========================================================
# 2. HỌC VẤN
# =========================================================

elif page == "🎓 Học vấn":

    st.header("🎓 HỌC VẤN")

    school = st.text_input(
        "🏫 Tên trường",
        value=st.session_state.school,
        placeholder="Đại học ABC"
    )

    major = st.text_input(
        "📚 Chuyên ngành",
        value=st.session_state.major,
        placeholder="Tài chính - Ngân hàng"
    )

    education_time = st.text_input(
        "📅 Thời gian học",
        value=st.session_state.education_time,
        placeholder="2024 - 2028"
    )

    gpa = st.number_input(
        "📊 GPA",
        min_value=0.0,
        max_value=4.0,
        value=float(st.session_state.gpa),
        step=0.1
    )

    if st.button(
        "💾 LƯU HỌC VẤN",
        type="primary",
        use_container_width=True
    ):

        st.session_state.school = school
        st.session_state.major = major
        st.session_state.education_time = education_time
        st.session_state.gpa = gpa

        st.success("✅ Đã lưu thông tin học vấn!")


# =========================================================
# 3. KINH NGHIỆM & KỸ NĂNG
# =========================================================

elif page == "💼 Kinh nghiệm & kỹ năng":

    st.header("💼 KINH NGHIỆM & KỸ NĂNG")

    experience = st.text_area(
        "💼 Kinh nghiệm làm việc",
        value=st.session_state.experience,
        height=220,
        placeholder="""Ví dụ:

Công ty ABC
Vị trí: Nhân viên bán hàng
Thời gian: 06/2025 - 08/2026

- Tư vấn khách hàng
- Quản lý hàng hóa
- Đạt KPI doanh số"""
    )

    skills = st.text_area(
        "🛠️ Kỹ năng",
        value=st.session_state.skills,
        height=150,
        placeholder="""Ví dụ:

- Giao tiếp
- Làm việc nhóm
- Excel
- Bán hàng
- Chăm sóc khách hàng"""
    )

    languages = st.text_area(
        "🌐 Ngoại ngữ",
        value=st.session_state.languages,
        height=100,
        placeholder="Ví dụ: Tiếng Anh TOEIC 650, Tiếng Trung HSK 3..."
    )

    certificates = st.text_area(
        "📜 Chứng chỉ",
        value=st.session_state.certificates,
        height=100,
        placeholder="Ví dụ: MOS, TOEIC, HSK..."
    )

    achievements = st.text_area(
        "🏆 Thành tích",
        value=st.session_state.achievements,
        height=100,
        placeholder="Ví dụ: Nhân viên xuất sắc, giải cuộc thi..."
    )

    if st.button(
        "💾 LƯU THÔNG TIN",
        type="primary",
        use_container_width=True
    ):

        st.session_state.experience = experience
        st.session_state.skills = skills
        st.session_state.languages = languages
        st.session_state.certificates = certificates
        st.session_state.achievements = achievements

        st.success("✅ Đã lưu kinh nghiệm và kỹ năng!")


# =========================================================
# 4. MỨC LƯƠNG
# =========================================================

elif page == "💰 Mức lương mong muốn":

    st.header("💰 MỨC LƯƠNG MONG MUỐN")

    st.write(
        "Nhập trực tiếp mức lương bằng bàn phím."
    )

    salary = st.number_input(
        "💵 Mức lương mong muốn (VNĐ/tháng)",
        min_value=0,
        value=int(st.session_state.salary),
        step=100000,
        format="%d"
    )

    if salary > 0:

        st.success(
            f"💰 Mức lương mong muốn: "
            f"{salary:,.0f} VNĐ/tháng"
        )

    if st.button(
        "💾 LƯU MỨC LƯƠNG",
        type="primary",
        use_container_width=True
    ):

        st.session_state.salary = salary

        st.success("✅ Đã lưu mức lương!")


# =========================================================
# 5. ĐÁNH GIÁ HỒ SƠ
# =========================================================

elif page == "📊 Đánh giá hồ sơ":

    st.header("📊 ĐÁNH GIÁ HỒ SƠ")

    score = 0

    # Thông tin cá nhân: 20
    personal_score = 0

    if st.session_state.full_name:
        personal_score += 5

    if st.session_state.phone:
        personal_score += 5

    if st.session_state.email:
        personal_score += 5

    if st.session_state.photo_bytes:
        personal_score += 5

    score += personal_score

    # Học vấn: 20
    education_score = 0

    if st.session_state.school:
        education_score += 7

    if st.session_state.major:
        education_score += 7

    if st.session_state.gpa > 0:
        education_score += 6

    score += education_score

    # Kinh nghiệm: 20
    experience_score = 20 if st.session_state.experience else 0

    score += experience_score

    # Kỹ năng: 20
    skill_score = 0

    if st.session_state.skills:
        skill_score += 12

    if st.session_state.languages:
        skill_score += 8

    score += skill_score

    # Chứng chỉ + thành tích: 20
    extra_score = 0

    if st.session_state.certificates:
        extra_score += 10

    if st.session_state.achievements:
        extra_score += 10

    score += extra_score

    col1, col2 = st.columns([1, 2])

    with col1:

        st.markdown(
            f"""
            <div class="score-box">

            <div>ĐIỂM HỒ SƠ</div>

            <div class="score-number">
            {score}/100
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        if score >= 85:

            st.success(
                "🌟 HỒ SƠ RẤT TỐT – Sẵn sàng ứng tuyển!"
            )

        elif score >= 70:

            st.info(
                "👍 HỒ SƠ KHÁ TỐT – Có thể bổ sung thêm."
            )

        elif score >= 50:

            st.warning(
                "⚠️ HỒ SƠ CẦN BỔ SUNG."
            )

        else:

            st.error(
                "❗ HỒ SƠ CÒN THIẾU NHIỀU THÔNG TIN."
            )

    st.divider()

    st.subheader("📋 Chi tiết điểm")

    score_items = [
        ("👤 Thông tin cá nhân", personal_score, 20),
        ("🎓 Học vấn", education_score, 20),
        ("💼 Kinh nghiệm", experience_score, 20),
        ("🛠️ Kỹ năng & ngoại ngữ", skill_score, 20),
        ("🏆 Chứng chỉ & thành tích", extra_score, 20)
    ]

    for title, got, maximum in score_items:

        st.write(
            f"**{title}: {got}/{maximum} điểm**"
        )

        st.progress(
            got / maximum
        )

    st.subheader("💡 Gợi ý")

    if not st.session_state.photo_bytes:
        st.write("📷 Tải ảnh hồ sơ.")

    if not st.session_state.experience:
        st.write("💼 Bổ sung kinh nghiệm.")

    if not st.session_state.skills:
        st.write("🛠️ Bổ sung kỹ năng.")

    if not st.session_state.languages:
        st.write("🌐 Bổ sung ngoại ngữ.")

    if not st.session_state.certificates:
        st.write("📜 Bổ sung chứng chỉ.")

    if (
        st.session_state.photo_bytes
        and st.session_state.experience
        and st.session_state.skills
        and st.session_state.languages
        and st.session_state.certificates
    ):

        st.success(
            "🎉 Hồ sơ đã đầy đủ các nội dung quan trọng!"
        )

# =========================================================
# AI PHỎNG VẤN THÔNG MINH
# =========================================================

elif page == "🤖 AI Phỏng vấn":

    st.header("🤖 AI INTERVIEW COACH")

    st.markdown("""
    ### 🎤 Trợ lý phỏng vấn thông minh

    AI sẽ đóng vai **nhà tuyển dụng** và giúp bạn luyện tập
    trước khi tham gia phỏng vấn thật.

    AI có thể:
    - 🎯 Đặt câu hỏi phỏng vấn
    - 💬 Phân tích câu trả lời
    - ⭐ Chấm điểm câu trả lời
    - 💡 Gợi ý cách trả lời tốt hơn
    - 📝 Đưa ra câu trả lời mẫu
    - 🎤 Mô phỏng một buổi phỏng vấn
    """)

    st.divider()

    # -----------------------------------------------------
    # THÔNG TIN ỨNG VIÊN
    # -----------------------------------------------------

    st.subheader("👤 Thông tin ứng viên")

    col1, col2 = st.columns(2)

    with col1:

        ai_name = st.text_input(
            "Họ và tên",
            value=st.session_state.full_name,
            placeholder="Nguyễn Văn A"
        )

        ai_job = st.text_input(
            "Vị trí ứng tuyển",
            value=st.session_state.job,
            placeholder="Nhân viên ngân hàng"
        )

    with col2:

        ai_experience = st.text_area(
            "Kinh nghiệm",
            value=st.session_state.experience,
            height=120,
            placeholder="Nhập kinh nghiệm làm việc..."
        )

        ai_skills = st.text_area(
            "Kỹ năng",
            value=st.session_state.skills,
            height=120,
            placeholder="Giao tiếp, Excel, bán hàng..."
        )

    st.divider()

    # -----------------------------------------------------
    # CHỌN LOẠI PHỎNG VẤN
    # -----------------------------------------------------

    st.subheader("🎯 Chọn loại phỏng vấn")

    interview_type = st.selectbox(
        "Bạn muốn luyện tập nội dung nào?",
        [
            "Phỏng vấn tổng quát",
            "Phỏng vấn xin việc ngân hàng",
            "Phỏng vấn nhân viên bán hàng",
            "Phỏng vấn chăm sóc khách hàng",
            "Phỏng vấn thực tập sinh",
            "Phỏng vấn sinh viên mới ra trường",
            "Phỏng vấn về kỹ năng giao tiếp",
            "Phỏng vấn về điểm mạnh - điểm yếu",
            "Phỏng vấn về mức lương"
        ]
    )

    difficulty = st.select_slider(
        "🔥 Độ khó",
        options=[
            "Dễ",
            "Trung bình",
            "Khó"
        ],
        value="Trung bình"
    )

    st.divider()

    # -----------------------------------------------------
    # NGÂN HÀNG CÂU HỎI
    # -----------------------------------------------------

    interview_questions = {

        "Phỏng vấn tổng quát": [
            "Hãy giới thiệu bản thân của bạn.",
            "Tại sao bạn muốn ứng tuyển vào vị trí này?",
            "Điểm mạnh của bạn là gì?",
            "Điểm yếu của bạn là gì?",
            "Bạn có kinh nghiệm gì liên quan đến công việc?",
            "Tại sao chúng tôi nên tuyển bạn?",
            "Bạn mong muốn mức lương bao nhiêu?",
            "Bạn định hướng nghề nghiệp trong 3 năm tới như thế nào?"
        ],

        "Phỏng vấn xin việc ngân hàng": [
            "Hãy giới thiệu bản thân.",
            "Tại sao bạn muốn làm việc trong ngành ngân hàng?",
            "Bạn hiểu gì về vị trí mà bạn đang ứng tuyển?",
            "Theo bạn, nhân viên ngân hàng cần những kỹ năng gì?",
            "Nếu khách hàng tức giận, bạn sẽ xử lý như thế nào?",
            "Nếu khách hàng từ chối sản phẩm, bạn sẽ làm gì?",
            "Bạn có chịu được áp lực doanh số không?",
            "Mục tiêu nghề nghiệp của bạn trong 3 năm tới là gì?"
        ],

        "Phỏng vấn nhân viên bán hàng": [
            "Hãy giới thiệu bản thân.",
            "Bạn có kinh nghiệm bán hàng không?",
            "Bạn sẽ làm gì khi khách hàng không hài lòng?",
            "Nếu khách hàng nói sản phẩm quá đắt, bạn xử lý thế nào?",
            "Bạn làm gì để tăng doanh số?",
            "Bạn có chịu được áp lực KPI không?",
            "Bạn sẽ tư vấn sản phẩm cho khách hàng như thế nào?"
        ],

        "Phỏng vấn chăm sóc khách hàng": [
            "Hãy giới thiệu bản thân.",
            "Theo bạn chăm sóc khách hàng tốt là gì?",
            "Bạn sẽ làm gì khi khách hàng nổi giận?",
            "Nếu không biết câu trả lời của khách hàng, bạn xử lý thế nào?",
            "Bạn có chịu được áp lực công việc không?",
            "Điểm mạnh nào giúp bạn phù hợp với vị trí này?"
        ],

        "Phỏng vấn thực tập sinh": [
            "Hãy giới thiệu bản thân.",
            "Tại sao bạn muốn thực tập tại công ty chúng tôi?",
            "Bạn đã học được những gì ở trường?",
            "Bạn có kinh nghiệm làm việc nhóm không?",
            "Điểm mạnh của bạn là gì?",
            "Bạn mong muốn học hỏi điều gì trong kỳ thực tập?"
        ],

        "Phỏng vấn sinh viên mới ra trường": [
            "Hãy giới thiệu bản thân.",
            "Bạn chưa có nhiều kinh nghiệm, tại sao chúng tôi nên tuyển bạn?",
            "Bạn đã chuẩn bị gì cho công việc này?",
            "Bạn có kỹ năng nào nổi bật?",
            "Bạn mong muốn học hỏi điều gì?",
            "Mức lương bạn mong muốn là bao nhiêu?"
        ],

        "Phỏng vấn về kỹ năng giao tiếp": [
            "Bạn đánh giá khả năng giao tiếp của mình như thế nào?",
            "Bạn sẽ làm gì khi xảy ra mâu thuẫn với đồng nghiệp?",
            "Bạn xử lý thế nào khi phải nói chuyện với một khách hàng khó tính?",
            "Bạn làm gì để thuyết phục người khác?",
            "Bạn có thích làm việc nhóm không?"
        ],

        "Phỏng vấn về điểm mạnh - điểm yếu": [
            "Điểm mạnh lớn nhất của bạn là gì?",
            "Điểm yếu lớn nhất của bạn là gì?",
            "Bạn đang làm gì để cải thiện điểm yếu đó?",
            "Bạn nghĩ đồng nghiệp sẽ nhận xét bạn như thế nào?",
            "Điều gì khiến bạn tự tin nhất?"
        ],

        "Phỏng vấn về mức lương": [
            "Mức lương mong muốn của bạn là bao nhiêu?",
            "Nếu công ty đưa ra mức lương thấp hơn kỳ vọng, bạn sẽ làm gì?",
            "Bạn quan tâm đến lương hay cơ hội phát triển hơn?",
            "Bạn kỳ vọng gì về chế độ đãi ngộ?",
            "Bạn có sẵn sàng làm việc theo KPI không?"
        ]
    }

    questions = interview_questions[interview_type]

    # -----------------------------------------------------
    # SESSION STATE CHO PHỎNG VẤN
    # -----------------------------------------------------

    if "interview_index" not in st.session_state:
        st.session_state.interview_index = 0

    if "interview_answer" not in st.session_state:
        st.session_state.interview_answer = ""

    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False

    # -----------------------------------------------------
    # BẮT ĐẦU
    # -----------------------------------------------------

    if not st.session_state.interview_started:

        st.info(
            "💡 Hãy nhấn bắt đầu. AI sẽ đóng vai nhà tuyển dụng "
            "và lần lượt đưa ra các câu hỏi."
        )

        if st.button(
            "🎤 BẮT ĐẦU PHỎNG VẤN",
            type="primary",
            use_container_width=True
        ):

            st.session_state.interview_started = True
            st.session_state.interview_index = 0
            st.session_state.interview_answer = ""

            st.rerun()

    # -----------------------------------------------------
    # ĐANG PHỎNG VẤN
    # -----------------------------------------------------

    else:

        current_index = st.session_state.interview_index

        if current_index < len(questions):

            question = questions[current_index]

            st.markdown(
                f"""
                ### 👔 NHÀ TUYỂN DỤNG

                **Câu hỏi {current_index + 1}/{len(questions)}**

                > {question}
                """
            )

            answer = st.text_area(
                "💬 Câu trả lời của bạn",
                value=st.session_state.interview_answer,
                height=180,
                placeholder="Hãy nhập câu trả lời như khi bạn đang phỏng vấn thật..."
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "🔍 PHÂN TÍCH CÂU TRẢ LỜI",
                    use_container_width=True
                ):

                    if not answer.strip():

                        st.warning(
                            "⚠️ Hãy nhập câu trả lời trước."
                        )

                    else:

                        st.session_state.interview_answer = answer

                        # Chấm điểm cơ bản
                        word_count = len(answer.split())

                        if word_count >= 80:
                            point = 9
                        elif word_count >= 50:
                            point = 8
                        elif word_count >= 30:
                            point = 7
                        elif word_count >= 15:
                            point = 6
                        else:
                            point = 4

                        st.success(
                            f"⭐ Điểm tham khảo: {point}/10"
                        )

                        st.markdown("### 💡 Nhận xét")

                        if word_count < 15:

                            st.warning(
                                "Câu trả lời hơi ngắn. "
                                "Bạn nên đưa thêm ví dụ thực tế."
                            )

                        elif word_count < 30:

                            st.info(
                                "Câu trả lời khá ổn nhưng "
                                "nên giải thích rõ hơn."
                            )

                        else:

                            st.success(
                                "Câu trả lời có độ dài tốt. "
                                "Hãy cố gắng nói tự nhiên và đưa ví dụ cụ thể."
                            )

                        st.markdown("### 🧠 Công thức trả lời gợi ý")

                        st.write(
                            "**STAR:** Situation → Task → Action → Result"
                        )

                        st.write(
                            "Hãy đưa ra hoàn cảnh, nhiệm vụ, "
                            "cách bạn xử lý và kết quả đạt được."
                        )

            with col2:

                if st.button(
                    "➡️ CÂU HỎI TIẾP THEO",
                    use_container_width=True
                ):

                    st.session_state.interview_index += 1
                    st.session_state.interview_answer = ""

                    st.rerun()

        else:

            st.success(
                "🎉 Bạn đã hoàn thành buổi phỏng vấn!"
            )

            st.balloons()

            st.markdown("""
            ### 🏆 Chúc mừng!

            Bạn đã hoàn thành phần luyện tập.

            Hãy nhớ:

            - Trả lời ngắn gọn, rõ ràng.
            - Không học thuộc câu trả lời một cách máy móc.
            - Đưa ra ví dụ thực tế.
            - Giữ thái độ tự tin.
            - Nhìn vào nhà tuyển dụng khi phỏng vấn trực tiếp.
            """)

            if st.button(
                "🔄 PHỎNG VẤN LẠI",
                use_container_width=True
            ):

                st.session_state.interview_started = False
                st.session_state.interview_index = 0
                st.session_state.interview_answer = ""

                st.rerun()


# =========================================================
# KẾT THÚC AI PHỎNG VẤN
# =========================================================
# =========================================================
# 6. XEM HỒ SƠ
# =========================================================

elif page == "📄 Xem hồ sơ":

    st.header("📄 HỒ SƠ XIN VIỆC")

    st.caption(
        "Đây là bản xem trước hồ sơ của bạn."
    )

    # -----------------------------------------------------
    # PHẦN ĐẦU CV
    # -----------------------------------------------------

    with st.container(border=True):

        col_photo, col_name = st.columns([1, 3])

        with col_photo:

            if st.session_state.photo_bytes:

                st.image(
                    st.session_state.photo_bytes,
                    width=180
                )

            else:

                st.info(
                    "📷 Chưa có ảnh"
                )

        with col_name:

            st.markdown(
                f"""
                <div class="cv-name">
                {html.escape(
                    st.session_state.full_name
                    or "HỌ VÀ TÊN"
                )}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="cv-job">
                {html.escape(
                    st.session_state.job
                    or "VỊ TRÍ ỨNG TUYỂN"
                )}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                f"📱 {st.session_state.phone or 'Chưa cập nhật'}"
            )

            st.write(
                f"📧 {st.session_state.email or 'Chưa cập nhật'}"
            )

            st.write(
                f"📍 {st.session_state.address or 'Chưa cập nhật'}"
            )

            st.write(
                f"🎂 {st.session_state.birthday or 'Chưa cập nhật'}"
            )

            st.write(
                f"👤 {st.session_state.gender}"
            )

    # -----------------------------------------------------
    # MỤC TIÊU
    # -----------------------------------------------------

    with st.container(border=True):

        st.markdown(
            '<div class="cv-section">🎯 MỤC TIÊU NGHỀ NGHIỆP</div>',
            unsafe_allow_html=True
        )

        if st.session_state.career_goal:

            st.write(
                st.session_state.career_goal
            )

        else:

            st.info(
                "Chưa nhập mục tiêu nghề nghiệp."
            )

    # -----------------------------------------------------
    # GIỚI THIỆU
    # -----------------------------------------------------

    with st.container(border=True):

        st.markdown(
            '<div class="cv-section">✨ GIỚI THIỆU BẢN THÂN</div>',
            unsafe_allow_html=True
        )

        if st.session_state.about:

            st.write(
                st.session_state.about
            )

        else:

            st.info(
                "Chưa nhập giới thiệu bản thân."
            )

    # -----------------------------------------------------
    # HỌC VẤN
    # -----------------------------------------------------

    with st.container(border=True):

        st.markdown(
            '<div class="cv-section">🎓 HỌC VẤN</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"### {st.session_state.school or 'Chưa cập nhật'}"
        )

        st.write(
            f"**Chuyên ngành:** "
            f"{st.session_state.major or 'Chưa cập nhật'}"
        )

        st.write(
            f"**Thời gian:** "
            f"{st.session_state.education_time or 'Chưa cập nhật'}"
        )

        st.write(
            f"**GPA:** "
            f"{st.session_state.gpa:.1f}/4.0"
        )

    # -----------------------------------------------------
    # KINH NGHIỆM
    # -----------------------------------------------------

    with st.container(border=True):

        st.markdown(
            '<div class="cv-section">💼 KINH NGHIỆM LÀM VIỆC</div>',
            unsafe_allow_html=True
        )

        if st.session_state.experience:

            st.write(
                st.session_state.experience
            )

        else:

            st.info(
                "Chưa nhập kinh nghiệm."
            )

    # -----------------------------------------------------
    # KỸ NĂNG
    # -----------------------------------------------------

    with st.container(border=True):

        st.markdown(
            '<div class="cv-section">🛠️ KỸ NĂNG</div>',
            unsafe_allow_html=True
        )

        if st.session_state.skills:

            st.write(
                st.session_state.skills
            )

        else:

            st.info(
                "Chưa nhập kỹ năng."
            )

    # -----------------------------------------------------
    # NGOẠI NGỮ
    # -----------------------------------------------------

    with st.container(border=True):

        st.markdown(
            '<div class="cv-section">🌐 NGOẠI NGỮ</div>',
            unsafe_allow_html=True
        )

        if st.session_state.languages:

            st.write(
                st.session_state.languages
            )

        else:

            st.info(
                "Chưa nhập ngoại ngữ."
            )

    # -----------------------------------------------------
    # CHỨNG CHỈ
    # -----------------------------------------------------

    with st.container(border=True):

        st.markdown(
            '<div class="cv-section">📜 CHỨNG CHỈ</div>',
            unsafe_allow_html=True
        )

        if st.session_state.certificates:

            st.write(
                st.session_state.certificates
            )

        else:

            st.info(
                "Chưa nhập chứng chỉ."
            )

    # -----------------------------------------------------
    # THÀNH TÍCH
    # -----------------------------------------------------

    with st.container(border=True):

        st.markdown(
            '<div class="cv-section">🏆 THÀNH TÍCH</div>',
            unsafe_allow_html=True
        )

        if st.session_state.achievements:

            st.write(
                st.session_state.achievements
            )

        else:

            st.info(
                "Chưa nhập thành tích."
            )

    # -----------------------------------------------------
    # LƯƠNG
    # -----------------------------------------------------

    with st.container(border=True):

        st.markdown(
            '<div class="cv-section">💰 MỨC LƯƠNG MONG MUỐN</div>',
            unsafe_allow_html=True
        )

        if st.session_state.salary > 0:

            st.success(
                f"{st.session_state.salary:,.0f} VNĐ/tháng"
            )

        else:

            st.info(
                "Chưa nhập mức lương mong muốn."
            )

    # -----------------------------------------------------
    # TẢI NỘI DUNG
    # -----------------------------------------------------

    st.divider()

    st.subheader("📥 LƯU HỒ SƠ")

    st.info(
        "Bạn có thể sử dụng chức năng In/Print của trình duyệt "
        "để lưu bản hồ sơ này thành PDF."
    )

    if st.button(
        "🖨️ IN / LƯU HỒ SƠ PDF",
        use_container_width=True
    ):

        st.components.v1.html(
            """
            <script>
            window.print();
            </script>
            """,
            height=0
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "💼 JOBMATE – Mini App Hồ sơ xin việc thông minh | "
    "Dự án học tập môn Tài chính / Ngân hàng"
)
