from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime
import uuid
from database import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    file_name = Column(String)
    query = Column(Text)
    result = Column(Text)
    status = Column(String, default="processing")
    created_at = Column(DateTime, default=datetime.utcnow)