import streamlit as st
from datetime import date
import io

# =========================================================
# CẤU HÌNH APP
# =========================================================

st.set_page_config(
    page_title="JOBMATE - Hồ sơ xin việc",
    page_icon="💼",
    layout="wide"
)

# =========================================================
# CSS GIAO DIỆN
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    border: 1px solid #e5e7eb;
    margin-bottom: 20px;
}

.result {
    padding: 25px;
    border-radius: 15px;
    background-color: white;
    border: 2px solid #ddd;
    text-align: center;
}

.score {
    font-size: 42px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TIÊU ĐỀ
# =========================================================

st.markdown(
    '<div class="title">💼 JOBMATE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">HỒ SƠ XIN VIỆC THÔNG MINH</div>',
    unsafe_allow_html=True
)

st.write(
    "Tạo hồ sơ xin việc, đánh giá mức độ phù hợp "
    "và tính toán mức lương phù hợp với mục tiêu tài chính."
)

st.divider()


# =========================================================
# MENU
# =========================================================

menu = st.sidebar.radio(
    "📌 MENU",
    [
        "👤 Thông tin cá nhân",
        "🎓 Học vấn & kỹ năng",
        "💰 Tài chính cá nhân",
        "📊 Đánh giá hồ sơ",
        "📄 Xem CV"
    ]
)


# =========================================================
# LƯU DỮ LIỆU
# =========================================================

if "name" not in st.session_state:
    st.session_state.name = ""

if "phone" not in st.session_state:
    st.session_state.phone = ""

if "email" not in st.session_state:
    st.session_state.email = ""

if "address" not in st.session_state:
    st.session_state.address = ""

if "job" not in st.session_state:
    st.session_state.job = ""

if "intro" not in st.session_state:
    st.session_state.intro = ""

if "school" not in st.session_state:
    st.session_state.school = ""

if "major" not in st.session_state:
    st.session_state.major = ""

if "gpa" not in st.session_state:
    st.session_state.gpa = 0.0

if "skills" not in st.session_state:
    st.session_state.skills = ""

if "experience" not in st.session_state:
    st.session_state.experience = ""

if "salary" not in st.session_state:
    st.session_state.salary = 0

if "expense" not in st.session_state:
    st.session_state.expense = 0

if "saving" not in st.session_state:
    st.session_state.saving = 0


# =========================================================
# 1. THÔNG TIN CÁ NHÂN
# =========================================================

if menu == "👤 Thông tin cá nhân":

    st.header("👤 THÔNG TIN CÁ NHÂN")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Họ và tên",
            value=st.session_state.name,
            placeholder="Nguyễn Văn A"
        )

        phone = st.text_input(
            "Số điện thoại",
            value=st.session_state.phone,
            placeholder="09xxxxxxxx"
        )

        email = st.text_input(
            "Email",
            value=st.session_state.email,
            placeholder="example@gmail.com"
        )

    with col2:

        address = st.text_input(
            "Địa chỉ",
            value=st.session_state.address,
            placeholder="Thủ Dầu Một, Bình Dương"
        )

        job = st.selectbox(
            "Vị trí muốn ứng tuyển",
            [
                "Nhân viên ngân hàng",
                "Nhân viên kinh doanh",
                "Kế toán",
                "Nhân viên bán hàng",
                "Marketing",
                "Chăm sóc khách hàng",
                "Khác"
            ]
        )

        birthday = st.date_input(
            "Ngày sinh",
            value=date(2006, 6, 9)
        )

    intro = st.text_area(
        "✨ Giới thiệu bản thân",
        placeholder="Viết một đoạn giới thiệu ngắn về bản thân..."
    )

    uploaded_image = st.file_uploader(
        "📷 Tải ảnh cá nhân",
        type=["jpg", "jpeg", "png"]
    )

    if st.button("💾 LƯU THÔNG TIN", use_container_width=True):

        st.session_state.name = name
        st.session_state.phone = phone
        st.session_state.email = email
        st.session_state.address = address
        st.session_state.job = job
        st.session_state.intro = intro

        st.success("✅ Đã lưu thông tin!")


# =========================================================
# 2. HỌC VẤN & KỸ NĂNG
# =========================================================

elif menu == "🎓 Học vấn & kỹ năng":

    st.header("🎓 HỌC VẤN & KỸ NĂNG")

    school = st.text_input(
        "🏫 Trường",
        value=st.session_state.school,
        placeholder="Đại học ABC"
    )

    major = st.text_input(
        "📚 Chuyên ngành",
        value=st.session_state.major,
        placeholder="Tài chính - Ngân hàng"
    )

    gpa = st.number_input(
        "📊 GPA",
        min_value=0.0,
        max_value=4.0,
        value=float(st.session_state.gpa),
        step=0.1
    )

    skills = st.text_area(
        "💻 Kỹ năng",
        value=st.session_state.skills,
        placeholder="Ví dụ: Excel, giao tiếp, bán hàng, làm việc nhóm..."
    )

    experience = st.text_area(
        "💼 Kinh nghiệm làm việc",
        value=st.session_state.experience,
        placeholder="Mô tả kinh nghiệm làm việc..."
    )

    certificates = st.multiselect(
        "📜 Chứng chỉ",
        [
            "MOS",
            "IC3",
            "IELTS",
            "TOEIC",
            "Tin học văn phòng",
            "Chứng chỉ nghiệp vụ ngân hàng"
        ]
    )

    if st.button("💾 LƯU HỒ SƠ", use_container_width=True):

        st.session_state.school = school
        st.session_state.major = major
        st.session_state.gpa = gpa
        st.session_state.skills = skills
        st.session_state.experience = experience

        st.success("✅ Đã lưu học vấn và kỹ năng!")


# =========================================================
# 3. TÀI CHÍNH CÁ NHÂN
# =========================================================

elif menu == "💰 Tài chính cá nhân":

    st.header("💰 TÍNH TOÁN TÀI CHÍNH CÁ NHÂN")

    st.write(
        "Nhập mức chi tiêu và số tiền muốn tiết kiệm mỗi tháng. "
        "Ứng dụng sẽ đề xuất mức lương tối thiểu."
    )

    salary = st.number_input(
        "💵 Mức lương mong muốn (VNĐ/tháng)",
        min_value=0,
        value=int(st.session_state.salary),
        step=500000
    )

    expense = st.number_input(
        "🛒 Chi phí sinh hoạt (VNĐ/tháng)",
        min_value=0,
        value=int(st.session_state.expense),
        step=500000
    )

    saving = st.number_input(
        "🏦 Mục tiêu tiết kiệm (VNĐ/tháng)",
        min_value=0,
        value=int(st.session_state.saving),
        step=500000
    )

    if st.button("🧮 TÍNH TOÁN", use_container_width=True):

        st.session_state.salary = salary
        st.session_state.expense = expense
        st.session_state.saving = saving

        minimum_salary = expense + saving

        st.subheader("📊 KẾT QUẢ")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Chi phí",
                f"{expense:,.0f} VNĐ"
            )

        with col2:
            st.metric(
                "Tiết kiệm",
                f"{saving:,.0f} VNĐ"
            )

        with col3:
            st.metric(
                "Lương tối thiểu",
                f"{minimum_salary:,.0f} VNĐ"
            )

        if salary >= minimum_salary:

            st.success(
                "🎉 Mức lương mong muốn phù hợp với mục tiêu tài chính!"
            )

        else:

            st.warning(
                "⚠️ Mức lương mong muốn chưa đủ để đáp ứng "
                "chi phí và mục tiêu tiết kiệm."
            )


# =========================================================
# 4. ĐÁNH GIÁ HỒ SƠ
# =========================================================

elif menu == "📊 Đánh giá hồ sơ":

    st.header("📊 ĐÁNH GIÁ HỒ SƠ")

    score = 0

    # GPA
    if st.session_state.gpa >= 3.5:
        score += 20
    elif st.session_state.gpa >= 3.0:
        score += 15
    elif st.session_state.gpa >= 2.5:
        score += 10
    else:
        score += 5

    # Kỹ năng
    if st.session_state.skills:
        score += 20

    # Kinh nghiệm
    if st.session_state.experience:
        score += 20

    # Học vấn
    if st.session_state.school and st.session_state.major:
        score += 20

    # Thông tin cá nhân
    if (
        st.session_state.name
        and st.session_state.phone
        and st.session_state.email
    ):
        score += 20

    st.markdown(
        f"""
        <div class="result">
            <div>ĐIỂM HỒ SƠ CỦA BẠN</div>
            <div class="score">{score}/100</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if score >= 80:

        st.success(
            "🌟 Hồ sơ rất tốt! Bạn đã sẵn sàng ứng tuyển."
        )

    elif score >= 60:

        st.warning(
            "👍 Hồ sơ khá tốt nhưng vẫn nên bổ sung thêm thông tin."
        )

    else:

        st.error(
            "⚠️ Hồ sơ còn thiếu nhiều thông tin."
        )

    st.subheader("💡 Gợi ý cải thiện")

    if not st.session_state.name:
        st.write("❌ Bổ sung họ tên.")

    if not st.session_state.email:
        st.write("❌ Bổ sung email.")

    if not st.session_state.skills:
        st.write("❌ Bổ sung kỹ năng.")

    if not st.session_state.experience:
        st.write("❌ Bổ sung kinh nghiệm.")

    if st.session_state.gpa < 3.0:
        st.write("💡 Có thể bổ sung chứng chỉ hoặc kinh nghiệm thực tế.")


# =========================================================
# 5. XEM CV
# =========================================================

elif menu == "📄 Xem CV":

    st.header("📄 HỒ SƠ XIN VIỆC")

    st.markdown(
        f"""
        # {st.session_state.name or "HỌ VÀ TÊN"}

        **Vị trí ứng tuyển:** {st.session_state.job}

        📱 **Điện thoại:** {st.session_state.phone}

        📧 **Email:** {st.session_state.email}

        📍 **Địa chỉ:** {st.session_state.address}

        ---

        ## 🎯 GIỚI THIỆU

        {st.session_state.intro or "Chưa nhập thông tin."}

        ## 🎓 HỌC VẤN

        **Trường:** {st.session_state.school}

        **Chuyên ngành:** {st.session_state.major}

        **GPA:** {st.session_state.gpa}/4.0

        ## 💻 KỸ NĂNG

        {st.session_state.skills or "Chưa nhập thông tin."}

        ## 💼 KINH NGHIỆM

        {st.session_state.experience or "Chưa nhập thông tin."}

        ## 💰 TÀI CHÍNH CÁ NHÂN

        **Lương mong muốn:** {st.session_state.salary:,.0f} VNĐ/tháng

        **Chi phí sinh hoạt:** {st.session_state.expense:,.0f} VNĐ/tháng

        **Mục tiêu tiết kiệm:** {st.session_state.saving:,.0f} VNĐ/tháng

        **Lương tối thiểu đề xuất:**
        {st.session_state.expense + st.session_state.saving:,.0f} VNĐ/tháng
        """
    )

    st.success(
        "✅ Hồ sơ đã được tổng hợp. "
        "Bạn có thể chụp màn hình hoặc dùng nội dung này để đưa vào CV."
    )
