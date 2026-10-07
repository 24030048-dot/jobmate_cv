import streamlit as st
import base64
import html

# =========================================================
# CẤU HÌNH
# =========================================================

st.set_page_config(
    page_title="JOBMATE - Hồ sơ xin việc",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f7f9fc 0%, #eef3ff 100%);
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.hero {
    background: linear-gradient(135deg, #111827, #334155);
    padding: 35px;
    border-radius: 24px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.12);
}

.hero h1 {
    font-size: 46px;
    margin-bottom: 5px;
    font-weight: 800;
}

.hero p {
    font-size: 18px;
    opacity: 0.9;
}

.section-title {
    font-size: 27px;
    font-weight: 800;
    margin-top: 15px;
    margin-bottom: 20px;
}

.cv-card {
    background: white;
    border-radius: 20px;
    padding: 35px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
}

.cv-header {
    display: flex;
    gap: 30px;
    align-items: center;
    border-bottom: 2px solid #111827;
    padding-bottom: 25px;
    margin-bottom: 25px;
}

.cv-photo {
    width: 150px;
    height: 180px;
    object-fit: cover;
    border-radius: 12px;
    border: 3px solid #111827;
}

.cv-name {
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 5px;
}

.cv-job {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 15px;
}

.cv-contact {
    line-height: 1.8;
}

.cv-section {
    margin-top: 25px;
}

.cv-section h3 {
    border-bottom: 2px solid #111827;
    padding-bottom: 8px;
    font-size: 19px;
}

.score-box {
    background: white;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.07);
}

.score-number {
    font-size: 55px;
    font-weight: 900;
}

.tip {
    background: #f8fafc;
    border-left: 5px solid #334155;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 10px;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {

    "full_name": "",
    "birthday": "",
    "gender": "",
    "phone": "",
    "email": "",
    "address": "",
    "job": "",
    "salary": 0,
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

    "photo": None
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# HÀM ESCAPE HTML
# =========================================================

def safe(value):

    return html.escape(str(value or ""))


# =========================================================
# ẢNH
# =========================================================

def image_to_base64(uploaded_file):

    if uploaded_file is None:
        return None

    data = uploaded_file.getvalue()

    encoded = base64.b64encode(data).decode()

    file_type = uploaded_file.type

    return f"data:{file_type};base64,{encoded}"


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">

<h1>💼 JOBMATE</h1>

<p>
Hồ sơ xin việc thông minh – tạo CV chuyên nghiệp chỉ trong vài phút
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("💼 JOBMATE")

st.sidebar.caption("HỒ SƠ XIN VIỆC THÔNG MINH")

page = st.sidebar.radio(
    "📌 CHỌN CHỨC NĂNG",
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
    "💡 Nhập thông tin ở các mục bên trái. "
    "Sau đó vào **Xem hồ sơ** để kiểm tra CV."
)


# =========================================================
# 1. THÔNG TIN CÁ NHÂN
# =========================================================

if page == "👤 Thông tin cá nhân":

    st.markdown(
        '<div class="section-title">👤 THÔNG TIN CÁ NHÂN</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 2])

    with col1:

        st.subheader("📷 Ảnh hồ sơ")

        photo = st.file_uploader(
            "Tải ảnh chân dung",
            type=["jpg", "jpeg", "png"],
            help="Nên dùng ảnh rõ mặt, nền đơn giản."
        )

        if photo is not None:

            st.session_state.photo = photo

            st.image(
                photo,
                width=220,
                caption="Ảnh hồ sơ"
            )

        elif st.session_state.photo is not None:

            st.image(
                st.session_state.photo,
                width=220,
                caption="Ảnh hiện tại"
            )

    with col2:

        st.subheader("📝 Thông tin")

        name = st.text_input(
            "Họ và tên *",
            value=st.session_state.full_name,
            placeholder="Ví dụ: Nguyễn Văn A"
        )

        birthday = st.text_input(
            "Ngày sinh",
            value=st.session_state.birthday,
            placeholder="DD/MM/YYYY"
        )

        gender = st.selectbox(
            "Giới tính",
            [
                "Chưa chọn",
                "Nam",
                "Nữ",
                "Khác"
            ],
            index=(
                ["Chưa chọn", "Nam", "Nữ", "Khác"]
                .index(st.session_state.gender)
                if st.session_state.gender in
                ["Chưa chọn", "Nam", "Nữ", "Khác"]
                else 0
            )
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
        "🎯 Vị trí ứng tuyển *",
        value=st.session_state.job,
        placeholder="Ví dụ: Nhân viên ngân hàng"
    )

    career_goal = st.text_area(
        "🎯 Mục tiêu nghề nghiệp",
        value=st.session_state.career_goal,
        height=120,
        placeholder=(
            "Ví dụ: Mong muốn phát triển trong lĩnh vực "
            "Tài chính - Ngân hàng..."
        )
    )

    about = st.text_area(
        "✨ Giới thiệu bản thân",
        value=st.session_state.about,
        height=150,
        placeholder=(
            "Hãy giới thiệu ngắn gọn về bản thân, "
            "điểm mạnh và định hướng nghề nghiệp..."
        )
    )

    if st.button(
        "💾 LƯU THÔNG TIN",
        type="primary",
        use_container_width=True
    ):

        st.session_state.full_name = name
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

    st.markdown(
        '<div class="section-title">🎓 HỌC VẤN</div>',
        unsafe_allow_html=True
    )

    school = st.text_input(
        "🏫 Tên trường",
        value=st.session_state.school,
        placeholder="Ví dụ: Đại học ABC"
    )

    major = st.text_input(
        "📚 Chuyên ngành",
        value=st.session_state.major,
        placeholder="Ví dụ: Tài chính - Ngân hàng"
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
        step=0.1,
        format="%.1f"
    )

    st.info(
        "💡 Nếu trường bạn sử dụng thang điểm 10, "
        "bạn có thể ghi GPA vào phần mô tả thay vì ô này."
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

    st.markdown(
        '<div class="section-title">💼 KINH NGHIỆM & KỸ NĂNG</div>',
        unsafe_allow_html=True
    )

    experience = st.text_area(
        "💼 Kinh nghiệm làm việc",
        value=st.session_state.experience,
        height=220,
        placeholder=(
            "Ví dụ:\n"
            "• Công ty ABC – Nhân viên bán hàng\n"
            "• 06/2025 - 08/2026\n"
            "• Tư vấn khách hàng\n"
            "• Quản lý hàng hóa\n"
            "• Đạt KPI..."
        )
    )

    skills = st.text_area(
        "🛠️ Kỹ năng",
        value=st.session_state.skills,
        height=150,
        placeholder=(
            "Ví dụ:\n"
            "• Giao tiếp\n"
            "• Làm việc nhóm\n"
            "• Excel\n"
            "• Bán hàng\n"
            "• Chăm sóc khách hàng"
        )
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
        placeholder="Ví dụ: MOS Excel, TOEIC, HSK..."
    )

    achievements = st.text_area(
        "🏆 Thành tích",
        value=st.session_state.achievements,
        height=120,
        placeholder="Ví dụ: Nhân viên xuất sắc, đạt giải cuộc thi..."
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

    st.markdown(
        '<div class="section-title">💰 MỨC LƯƠNG MONG MUỐN</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Nhập mức lương bạn mong muốn bằng bàn phím. "
        "Không còn phần tiết kiệm."
    )

    salary = st.number_input(
        "💵 Mức lương mong muốn (VNĐ/tháng)",
        min_value=0,
        value=int(st.session_state.salary),
        step=100000,
        format="%d"
    )

    st.caption(
        "Ví dụ: nhập 8000000 nếu mong muốn mức lương 8 triệu đồng/tháng."
    )

    if salary > 0:

        st.metric(
            "Mức lương mong muốn",
            f"{salary:,.0f} VNĐ/tháng"
        )

    if st.button(
        "💾 LƯU MỨC LƯƠNG",
        type="primary",
        use_container_width=True
    ):

        st.session_state.salary = salary

        st.success("✅ Đã lưu mức lương mong muốn!")


# =========================================================
# 5. ĐÁNH GIÁ HỒ SƠ
# =========================================================

elif page == "📊 Đánh giá hồ sơ":

    st.markdown(
        '<div class="section-title">📊 ĐÁNH GIÁ HỒ SƠ</div>',
        unsafe_allow_html=True
    )

    score = 0
    details = []

    # Thông tin cá nhân: 20
    personal = 0

    if st.session_state.full_name:
        personal += 5

    if st.session_state.phone:
        personal += 5

    if st.session_state.email:
        personal += 5

    if st.session_state.photo:
        personal += 5

    score += personal

    details.append(
        ("👤 Thông tin cá nhân", personal, 20)
    )

    # Học vấn: 20
    education = 0

    if st.session_state.school:
        education += 7

    if st.session_state.major:
        education += 7

    if st.session_state.gpa > 0:
        education += 6

    score += education

    details.append(
        ("🎓 Học vấn", education, 20)
    )

    # Kinh nghiệm: 20
    experience_score = 0

    if st.session_state.experience:
        experience_score += 20

    score += experience_score

    details.append(
        ("💼 Kinh nghiệm", experience_score, 20)
    )

    # Kỹ năng: 20
    skill_score = 0

    if st.session_state.skills:
        skill_score += 12

    if st.session_state.languages:
        skill_score += 8

    score += skill_score

    details.append(
        ("🛠️ Kỹ năng & ngoại ngữ", skill_score, 20)
    )

    # Bổ sung: 20
    extra = 0

    if st.session_state.certificates:
        extra += 10

    if st.session_state.achievements:
        extra += 10

    score += extra

    details.append(
        ("🏆 Chứng chỉ & thành tích", extra, 20)
    )

    col1, col2 = st.columns([1, 2])

    with col1:

        st.markdown(
            f"""
            <div class="score-box">
                <div>ĐIỂM HỒ SƠ</div>
                <div class="score-number">{score}/100</div>
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
                "👍 HỒ SƠ KHÁ TỐT – Có thể bổ sung thêm để nổi bật."
            )

        elif score >= 50:

            st.warning(
                "⚠️ HỒ SƠ CẦN BỔ SUNG – Một số phần còn thiếu."
            )

        else:

            st.error(
                "❗ HỒ SƠ CHƯA ĐỦ THÔNG TIN."
            )

    st.divider()

    st.subheader("📋 Chi tiết điểm")

    for title, got, maximum in details:

        st.write(
            f"**{title}: {got}/{maximum} điểm**"
        )

        st.progress(got / maximum)

    st.subheader("💡 Gợi ý cải thiện")

    suggestions = []

    if not st.session_state.photo:
        suggestions.append(
            "📷 Tải ảnh chân dung chuyên nghiệp."
        )

    if not st.session_state.experience:
        suggestions.append(
            "💼 Bổ sung kinh nghiệm làm việc hoặc hoạt động thực tế."
        )

    if not st.session_state.skills:
        suggestions.append(
            "🛠️ Bổ sung các kỹ năng nổi bật."
        )

    if not st.session_state.languages:
        suggestions.append(
            "🌐 Bổ sung trình độ ngoại ngữ nếu có."
        )

    if not st.session_state.certificates:
        suggestions.append(
            "📜 Bổ sung chứng chỉ liên quan đến vị trí ứng tuyển."
        )

    if not suggestions:

        st.success(
            "🎉 Hồ sơ của bạn đã có đầy đủ các phần quan trọng!"
        )

    else:

        for suggestion in suggestions:

            st.markdown(
                f'<div class="tip">{suggestion}</div>',
                unsafe_allow_html=True
            )


# =========================================================
# 6. XEM HỒ SƠ
# =========================================================

elif page == "📄 Xem hồ sơ":

    st.markdown(
        '<div class="section-title">📄 HỒ SƠ XIN VIỆC</div>',
        unsafe_allow_html=True
    )

    photo_base64 = image_to_base64(
        st.session_state.photo
    )

    if photo_base64:

        photo_html = f"""
        <img
            src="{photo_base64}"
            class="cv-photo"
        >
        """

    else:

        photo_html = """
        <div class="cv-photo"
             style="
             display:flex;
             align-items:center;
             justify-content:center;
             background:#f1f5f9;
             color:#64748b;
             text-align:center;">
            CHƯA CÓ<br>ẢNH
        </div>
        """

    cv_html = f"""
    <div class="cv-card">

        <div class="cv-header">

            {photo_html}

            <div>

                <div class="cv-name">
                    {safe(st.session_state.full_name) or "HỌ VÀ TÊN"}
                </div>

                <div class="cv-job">
                    {safe(st.session_state.job) or "VỊ TRÍ ỨNG TUYỂN"}
                </div>

                <div class="cv-contact">

                    📱 {safe(st.session_state.phone) or "Số điện thoại"}<br>

                    📧 {safe(st.session_state.email) or "Email"}<br>

                    📍 {safe(st.session_state.address) or "Địa chỉ"}<br>

                    🎂 {safe(st.session_state.birthday) or "Ngày sinh"}

                </div>

            </div>

        </div>


        <div class="cv-section">

            <h3>🎯 MỤC TIÊU NGHỀ NGHIỆP</h3>

            <p>
                {safe(st.session_state.career_goal)
                or "Chưa cập nhật."}
            </p>

        </div>


        <div class="cv-section">

            <h3>✨ GIỚI THIỆU BẢN THÂN</h3>

            <p>
                {safe(st.session_state.about)
                or "Chưa cập nhật."}
            </p>

        </div>


        <div class="cv-section">

            <h3>🎓 HỌC VẤN</h3>

            <p>
                <b>{safe(st.session_state.school)
                or "Chưa cập nhật"}</b>
            </p>

            <p>
                Chuyên ngành:
                {safe(st.session_state.major)
                or "Chưa cập nhật"}
            </p>

            <p>
                Thời gian:
                {safe(st.session_state.education_time)
                or "Chưa cập nhật"}
            </p>

            <p>
                GPA:
                {st.session_state.gpa:.1f}/4.0
            </p>

        </div>


        <div class="cv-section">

            <h3>💼 KINH NGHIỆM LÀM VIỆC</h3>

            <p>
                {safe(st.session_state.experience)
                or "Chưa cập nhật."}
            </p>

        </div>


        <div class="cv-section">

            <h3>🛠️ KỸ NĂNG</h3>

            <p>
                {safe(st.session_state.skills)
                or "Chưa cập nhật."}
            </p>

        </div>


        <div class="cv-section">

            <h3>🌐 NGOẠI NGỮ</h3>

            <p>
                {safe(st.session_state.languages)
                or "Chưa cập nhật."}
            </p>

        </div>


        <div class="cv-section">

            <h3>📜 CHỨNG CHỈ</h3>

            <p>
                {safe(st.session_state.certificates)
                or "Chưa cập nhật."}
            </p>

        </div>


        <div class="cv-section">

            <h3>🏆 THÀNH TÍCH</h3>

            <p>
                {safe(st.session_state.achievements)
                or "Chưa cập nhật."}
            </p>

        </div>


        <div class="cv-section">

            <h3>💰 MỨC LƯƠNG MONG MUỐN</h3>

            <p>
                <b>
                    {st.session_state.salary:,.0f}
                    VNĐ/tháng
                </b>
            </p>

        </div>

    </div>
    """

    st.markdown(
        cv_html,
        unsafe_allow_html=True
    )

    st.divider()

    st.subheader("📥 TẢI HỒ SƠ")

    st.info(
        "Bạn có thể dùng chức năng in của trình duyệt "
        "để lưu hồ sơ thành PDF."
    )

    # Tạo phiên bản HTML tải xuống
    download_html = f"""
<!DOCTYPE html>
<html lang="vi">

<head>

<meta charset="UTF-8">

<title>
{safe(st.session_state.full_name) or "Ho so xin viec"}
</title>

<style>

body {{
    font-family: Arial, sans-serif;
    background: #f3f4f6;
    margin: 0;
    padding: 30px;
}}

.cv {{
    max-width: 850px;
    margin: auto;
    background: white;
    padding: 40px;
}}

.header {{
    display:flex;
    gap:25px;
    align-items:center;
    border-bottom:2px solid #111;
    padding-bottom:20px;
}}

.photo {{
    width:140px;
    height:170px;
    object-fit:cover;
}}

h1 {{
    margin:0;
}}

h2 {{
    border-bottom:2px solid #222;
    padding-bottom:5px;
    margin-top:25px;
}}

p {{
    line-height:1.7;
    white-space:pre-line;
}}

</style>

</head>

<body>

<div class="cv">

<div class="header">

{
    f'<img src="{photo_base64}" class="photo">'
    if photo_base64
    else ''
}

<div>

<h1>
{safe(st.session_state.full_name) or "HỌ VÀ TÊN"}
</h1>

<h3>
{safe(st.session_state.job) or "VỊ TRÍ ỨNG TUYỂN"}
</h3>

<p>
📱 {safe(st.session_state.phone)}<br>
📧 {safe(st.session_state.email)}<br>
📍 {safe(st.session_state.address)}<br>
🎂 {safe(st.session_state.birthday)}
</p>

</div>

</div>


<h2>🎯 MỤC TIÊU NGHỀ NGHIỆP</h2>

<p>
{safe(st.session_state.career_goal)}
</p>


<h2>✨ GIỚI THIỆU BẢN THÂN</h2>

<p>
{safe(st.session_state.about)}
</p>


<h2>🎓 HỌC VẤN</h2>

<p>
<b>{safe(st.session_state.school)}</b>

Chuyên ngành:
{safe(st.session_state.major)}

Thời gian:
{safe(st.session_state.education_time)}

GPA:
{st.session_state.gpa:.1f}/4.0
</p>


<h2>💼 KINH NGHIỆM</h2>

<p>
{safe(st.session_state.experience)}
</p>


<h2>🛠️ KỸ NĂNG</h2>

<p>
{safe(st.session_state.skills)}
</p>


<h2>🌐 NGOẠI NGỮ</h2>

<p>
{safe(st.session_state.languages)}
</p>


<h2>📜 CHỨNG CHỈ</h2>

<p>
{safe(st.session_state.certificates)}
</p>


<h2>🏆 THÀNH TÍCH</h2>

<p>
{safe(st.session_state.achievements)}
</p>


<h2>💰 MỨC LƯƠNG MONG MUỐN</h2>

<p>
<b>{st.session_state.salary:,.0f} VNĐ/tháng</b>
</p>

</div>

</body>

</html>
"""

    st.download_button(
        label="📥 TẢI HỒ SƠ XIN VIỆC",
        data=download_html,
        file_name="ho_so_xin_viec.html",
        mime="text/html",
        use_container_width=True
    )

    st.caption(
        "Sau khi tải file HTML, mở file bằng trình duyệt "
        "→ chọn In/Print → Save as PDF để có CV PDF."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
    💼 JOBMATE – Hồ sơ xin việc thông minh<br>
    Mini App phục vụ học tập môn Tài chính / Ngân hàng
    </div>
    """,
    unsafe_allow_html=True
)
