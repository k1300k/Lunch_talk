"""애플리케이션 진입점"""
import sys
import os
from pathlib import Path

# 프로젝트 루트를 PYTHONPATH에 추가
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.environ['PYTHONPATH'] = str(PROJECT_ROOT)

import uvicorn
from src.utils.logging_config import setup_logging

# 로깅 설정
logger = setup_logging()

if __name__ == "__main__":
    logger.info("서버를 시작합니다...")
    logger.info(f"PYTHONPATH: {PROJECT_ROOT}")
    uvicorn.run(
        "src.presentation.api.main:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="info",
    )

