from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# MySQL 데이터베이스 URL 설정
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://AppZam_user:Sj32993329&@localhost/AppZam"

# 데이터베이스 엔진 생성``
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_recycle=3600,  # 연결 풀 재활용 시간 설정
    echo=True  # SQL 쿼리 로깅 비활성화
)

# 세션 생성
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)