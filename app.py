
    # -----------------------------------------------------
    # IN VÀ LƯU HỒ SƠ CV
    # -----------------------------------------------------

    st.divider()
    st.subheader("📥 IN VÀ LƯU HỒ SƠ XIN VIỆC")

    st.write(
        "Hồ sơ bên dưới được tạo từ thông tin cá nhân "
        "mà bạn đã nhập và lưu trong JOBMATE."
    )

    # Hàm bảo vệ và định dạng nội dung HTML
    def safe_text(value):
        return html.escape(str(value or "")).replace(
            "\n", "<br>"
        )

    # Chuyển ảnh sang Base64 để nhúng trực tiếp vào CV
    photo_html = ""

    if st.session_state.photo_bytes:
        try:
            image_base64 = base64.b64encode(
                st.session_state.photo_bytes
            ).decode("utf-8")

            image_type = (
                st.session_state.photo_type
                or "image/jpeg"
            )

            photo_html = f"""
                <img
                    class="avatar"
                    src="data:{html.escape(image_type)};base64,{image_base64}"
                    alt="Ảnh hồ sơ"
                >
            """
        except Exception:
            photo_html = ""

    # Tạo các mục trong CV
    def cv_section(title, content):
        if not content:
            content = "Chưa cập nhật"

        return f"""
            <section class="section">
                <h2>{title}</h2>
                <div class="content">{safe_text(content)}</div>
            </section>
        """

    full_name = (
        st.session_state.full_name or "HỌ VÀ TÊN"
    )

    job = (
        st.session_state.job or "VỊ TRÍ ỨNG TUYỂN"
    )

    salary_text = (
        f"{st.session_state.salary:,.0f} VNĐ/tháng"
        if st.session_state.salary > 0
        else "Chưa cập nhật"
    )

    # Tạo hồ sơ HTML hoàn chỉnh
    cv_html = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>CV - {safe_text(full_name)}</title>

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                padding: 25px;
                background: #eef2f7;
                font-family: Arial, Helvetica, sans-serif;
                color: #263244;
                line-height: 1.6;
            }}

            .toolbar {{
                max-width: 850px;
                margin: 0 auto 18px;
                display: flex;
                justify-content: center;
                gap: 12px;
                flex-wrap: wrap;
            }}

            .toolbar button {{
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                background: #1d4ed8;
                color: white;
                font-size: 15px;
                font-weight: bold;
                cursor: pointer;
            }}

            .toolbar button:hover {{
                background: #1e40af;
            }}

            .cv {{
                max-width: 850px;
                margin: auto;
                padding: 42px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 5px 25px rgba(0,0,0,0.08);
            }}

            .header {{
                display: flex;
                align-items: center;
                gap: 25px;
                padding-bottom: 25px;
                border-bottom: 3px solid #1d4ed8;
            }}

            .avatar {{
                width: 135px;
                height: 165px;
                object-fit: cover;
                border-radius: 8px;
                border: 1px solid #d1d5db;
            }}

            .name {{
                font-size: 30px;
                font-weight: 800;
                color: #17365d;
                overflow-wrap: anywhere;
            }}

            .job {{
                margin-top: 8px;
                color: #1d4ed8;
                font-size: 19px;
                font-weight: bold;
            }}

            .contact {{
                margin-top: 12px;
                font-size: 13px;
                overflow-wrap: anywhere;
            }}

            .section {{
                margin-top: 24px;
                page-break-inside: auto;
                break-inside: auto;
            }}

            .section h2 {{
                font-size: 16px;
                text-transform: uppercase;
                color: #17365d;
                border-bottom: 1px solid #cbd5e1;
                padding-bottom: 7px;
                margin-bottom: 10px;
            }}

            .content {{
                font-size: 14px;
                overflow-wrap: anywhere;
                word-break: normal;
            }}

            .salary {{
                color: #15803d;
                font-size: 17px;
                font-weight: bold;
            }}

            .footer {{
                margin-top: 30px;
                border-top: 1px solid #ddd;
                padding-top: 12px;
                color: #64748b;
                font-size: 11px;
                text-align: center;
            }}

            @page {{
                size: A4;
                margin: 15mm;
            }}

            @media print {{
                body {{
                    padding: 0;
                    background: white;
                    -webkit-print-color-adjust: exact;
                    print-color-adjust: exact;
                }}

                .toolbar {{
                    display: none !important;
                }}

                .cv {{
                    max-width: none;
                    margin: 0;
                    padding: 0;
                    box-shadow: none;
                    border-radius: 0;
                }}

                .header {{
                    break-inside: avoid;
                    page-break-inside: avoid;
                }}

                .section h2 {{
                    break-after: avoid;
                    page-break-after: avoid;
                }}

                .footer {{
                    color: #64748b;
                }}
            }}

            @media screen and (max-width: 600px) {{
                body {{
                    padding: 10px;
                }}

                .cv {{
                    padding: 20px;
                }}

                .header {{
                    align-items: flex-start;
                    gap: 14px;
                }}

                .avatar {{
                    width: 90px;
                    height: 115px;
                }}

                .name {{
                    font-size: 23px;
                }}
            }}
        </style>
    </head>

    <body>

        <div class="toolbar">
            <button onclick="window.print()">
                🖨️ IN / LƯU PDF
            </button>
        </div>

        <main class="cv">

            <div class="header">

                {photo_html}

                <div>
                    <div class="name">
                        {safe_text(full_name)}
                    </div>

                    <div class="job">
                        {safe_text(job)}
                    </div>

                    <div class="contact">
                        📱 {safe_text(st.session_state.phone or "Chưa cập nhật")}
                        <br>
                        📧 {safe_text(st.session_state.email or "Chưa cập nhật")}
                        <br>
                        📍 {safe_text(st.session_state.address or "Chưa cập nhật")}
                        <br>
                        🎂 {safe_text(st.session_state.birthday or "Chưa cập nhật")}
                        <br>
                        👤 {safe_text(st.session_state.gender)}
                    </div>
                </div>

            </div>

            {cv_section("🎯 Mục tiêu nghề nghiệp", st.session_state.career_goal)}

            {cv_section("✨ Giới thiệu bản thân", st.session_state.about)}

            {cv_section("🎓 Học vấn", (
                "Trường: " + (st.session_state.school or "Chưa cập nhật")
                + "\\nChuyên ngành: " + (st.session_state.major or "Chưa cập nhật")
                + "\\nThời gian học: " + (st.session_state.education_time or "Chưa cập nhật")
                + "\\nGPA: " + f"{st.session_state.gpa:.1f}/4.0"
            ))}

            {cv_section("💼 Kinh nghiệm làm việc", st.session_state.experience)}

            {cv_section("🛠️ Kỹ năng", st.session_state.skills)}

            {cv_section("🌐 Ngoại ngữ", st.session_state.languages)}

            {cv_section("📜 Chứng chỉ", st.session_state.certificates)}

            {cv_section("🏆 Thành tích", st.session_state.achievements)}

            <section class="section">
                <h2>💰 Mức lương mong muốn</h2>
                <div class="salary">{safe_text(salary_text)}</div>
            </section>

            <div class="footer">
                JOBMATE - HỒ SƠ XIN VIỆC
            </div>

        </main>

    </body>
    </html>
    """

    # Xem trước CV ngay trên ứng dụng
    st.markdown("### 👀 Xem trước hồ sơ")

    st.components.v1.html(
        cv_html,
        height=1100,
        scrolling=True
    )

    st.divider()

    # Tải hồ sơ thành file HTML độc lập
    safe_filename = "".join(
        c if c.isalnum() or c in ("-", "_") else "_"
        for c in full_name
    ).strip("_")

    if not safe_filename:
        safe_filename = "ung_vien"

    st.download_button(
        label="📥 TẢI HỒ SƠ VỀ MÁY",
        data=cv_html.encode("utf-8"),
        file_name=f"CV_{safe_filename}.html",
        mime="text/html",
        use_container_width=True
    )

    st.caption(
        "Sau khi tải file HTML, hãy mở file bằng trình duyệt "
        "Chrome hoặc Edge, nhấn nút IN / LƯU PDF trên hồ sơ, "
        "chọn Save as PDF (Lưu dưới dạng PDF), rồi nhấn Lưu."
    )

    st.info(
        "Mẹo: Trước khi xuất hồ sơ, hãy kiểm tra các mục "
        "Thông tin cá nhân, Học vấn, Kinh nghiệm & kỹ năng "
        "và Mức lương mong muốn để bảo đảm dữ liệu đã được lưu."
    )
