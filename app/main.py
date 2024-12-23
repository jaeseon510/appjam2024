from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

Base = declarative_base()

class Chat(Base):
    __tablename__ = "chat"

    cc_id = Column(Integer, primary_key=True, autoincrement=True)
    chat_context = Column(String(5000), nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.now)
    type = Column(Integer, nullable=False)

DATABASE_URL = f'mysql+pymysql://AppZam_user:Sj32993329&@localhost:3306/AppZam'

# 데이터베이스 엔진 생성
engine = create_engine(
    DATABASE_URL,
    pool_recycle=3600,
    echo=True
)

# 세션 생성
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
key=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Flask 애플리케이션 생성
app = Flask(__name__)
CORS(app)

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# 의존성 주입: 데이터베이스 세션
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.route("/", methods=["POST"])
def chat_with_ai():
    
    db = SessionLocal()
    # 요청 데이터 받기
    data = request.get_json()
    user_message = data.get("request", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    else :
        print("채팅 요청 : " + user_message)
    user_chat = Chat(
            chat_context=user_message,
            type=1,
            timestamp=datetime.now()
        )
    db.add(user_chat)
    db.commit()
    db.refresh(user_chat)
    
    # AI 응답 생성
    response = model.generate_content(f'편의점에서 {user_message}과 어떤 것을 곁들여 먹으면 좋을까? 쓸모없는 말을 제외하고 간결하게 답변해줘. 편의점 가격으로 예상 총액만 알려줘.')
    ai_reply = response.text
    print(ai_reply)

    try:
        ai_chat = Chat(
            chat_context=ai_reply,
            type=0,
            timestamp=datetime.now()
        )
        db.add(ai_chat)
        db.commit()
        db.refresh(ai_chat)

        return jsonify({
            "ai_response": ai_reply
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)