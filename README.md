# OTC Sales Analysis (2021)

Portfolio project phân tích doanh thu kênh OTC của Dan Khang năm 2021.  
Dùng Excel, SQL, Power BI để phân tích và trực quan hóa dữ liệu.

## Mục tiêu
- Phân tích tổng quan doanh thu OTC.
- Xác định churn rate, growth rate, hành vi khách hàng.
- Đưa ra insight và đề xuất chiến lược tăng trưởng.

## Dữ liệu
- Nguồn: Báo cáo bán hàng nội bộ 2021 (đã ẩn danh trong `data/sample/`).
- Định dạng: CSV, SQL scripts.
- Quyền riêng tư: xem `DATA_PRIVACY.md`.

## Công cụ
- Power BI (DAX)
- SQL Server
- GitHub Actions (CI)

## Kết quả chính
- Doanh thu OTC chiếm 81% tổng công ty, tăng 45% YoY.
- Churn rate 33%, growth rate 40%.
- 4 nhóm sản phẩm chiếm đa số doanh thu.

## Cách chạy lại
1. Clone repo
2. Import sample CSV vào SQL (`sql/create_schema.sql` + `sql/load_data.sql`)
3. Mở notebook `notebooks/eda_otc.ipynb` để phân tích.
4. Xem ảnh dashboard trong `powerbi/dashboard_screenshots/`.

## Liên hệ
Author: Trọng Chiến
Email: Trongchien1711@gmail.com
