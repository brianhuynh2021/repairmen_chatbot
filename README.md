# 🤖 Chatbot Tìm Thợ Sửa Chữa ở Đồng Nai

Dự án này xây dựng một chatbot bằng **FastAPI** kết hợp với **LangChain + OpenAI** để giúp người dân ở **Đồng Nai** tìm thợ sửa chữa gần khu vực của họ như thợ điện, thợ nước, sửa máy lạnh...

---

## 🎯 Mục Tiêu Dự Án

- Giúp người dùng tìm thợ sửa chữa nhanh chóng qua hội thoại tự nhiên
- Tích hợp AI hiểu tiếng Việt và trả lời linh hoạt
- Dùng dữ liệu từ file CSV đơn giản (không cần database)
- Cấu trúc mã sạch, tách lớp rõ ràng để dễ mở rộng về sau

---

## 🧠 Công Nghệ Sử Dụng

| Thành phần | Công nghệ |
|------------|-----------|
| Backend | FastAPI |
| AI / NLP | LangChain + OpenAI GPT |
| Vector Search | FAISS |
| Cấu hình | Pydantic + .env |
| Dữ liệu | CSV (danh sách thợ sửa chữa) |

---

## 📁 Cấu Trúc Dự Án

app/
├── main.py                  # Khởi chạy FastAPI
├── api/
│   └── v1/chat.py           # Định nghĩa endpoint /chat
├── schemas/
│   └── chat.py              # Pydantic model
├── services/
│   └── chatbot_service.py   # Logic tích hợp LangChain
├── db/
│   └── repairmen_loader.py  # Load dữ liệu từ CSV
├── core/
│   └── config.py            # Đọc biến môi trường
├── data/
│   └── repairmen.csv        # Danh sách thợ sửa chữa
.env                         # API key OpenAI
requirements.txt             # Thư viện cần cài

---

## ▶️ Cách Chạy Ứng Dụng

### 1. Clone & tạo môi trường ảo

```bash
git clone https://github.com/yourusername/repairbot.git
cd repairbot
python -m venv venv
source venv/bin/activate  # Windows dùng: venv\Scripts\activate

2. Cài thư viện

pip install -r requirements.txt

3. Tạo file .env

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx

4. Chạy ứng dụng

uvicorn app.main:app --reload

Mở trình duyệt: http://127.0.0.1:8000/docs
Gửi câu hỏi:

POST /api/v1/chat
{
  "message": "Tôi cần thợ điện ở Trảng Bom"
}


⸻

🛠 Dữ liệu mẫu (repairmen.csv)

name,type,phone,area
Nguyễn Văn A,Thợ điện,0909123456,Biên Hòa
Trần Thị B,Thợ nước,0912345678,Long Thành
Lê Văn C,Sửa máy lạnh,0933123123,Trảng Bom


⸻

🧱 Gợi Ý Mở Rộng
	•	Thêm chức năng đăng ký thợ sửa chữa (POST /register)
	•	Kết nối cơ sở dữ liệu (SQLite, PostgreSQL)
	•	Triển khai lên server qua Docker / Railway / Render
	•	Tích hợp chatbot vào Telegram hoặc Zalo

⸻

👨‍💻 Tác giả
	•	Họ tên: Brian Huỳnh
	•	Mục tiêu: Dự án thực tế để ứng tuyển vị trí AI Engineer hoặc Backend Developer

⸻

📌 Giấy phép

Dự án này được thực hiện vì mục đích học tập. Bạn có thể tự do chia sẻ hoặc mở rộng.

Demo