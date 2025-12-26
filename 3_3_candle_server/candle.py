import csv
import logging
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# 全局变量存储预处理的数据
# key: (code, year, month, day, hour), value: [prices...] (按时间顺序)
candle_data = {}


class FlagRequest(BaseModel):
    flag: str


@app.on_event("startup")
def load_candle_data():
    """启动时读取CSV文件并按小时组织数据"""
    global candle_data
    csv_path = str(Path(__file__).parent / "order_books.csv")
    logger.info(f"Loading CSV file from: {csv_path}")
    
    row_count = 0
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_count += 1
            # 解析时间字段: "2021-12-22 09:00:00 +0900 JST"
            time_str = row["time"]
            # 提取日期时间部分（去掉时区信息）
            dt_str = time_str.split(" +")[0]
            dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
            
            code = row["code"]
            price = int(row["price"])
            
            # 创建key: (code, year, month, day, hour)
            key = (code, dt.year, dt.month, dt.day, dt.hour)
            
            # 将价格添加到对应小时的列表中
            if key not in candle_data:
                candle_data[key] = []
            candle_data[key].append(price)
    
    logger.info(f"Loaded {row_count} rows from CSV")
    logger.info(f"Total unique keys (code, year, month, day, hour): {len(candle_data)}")
    
    # 打印前几个示例keys
    if candle_data:
        sample_keys = list(candle_data.keys())[:5]
        logger.info(f"Sample keys: {sample_keys}")
        for key in sample_keys:
            logger.info(f"  Key {key}: {len(candle_data[key])} prices")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/candle")
def candle(code: str, year: int, month: int, day: int, hour: int):
    """获取指定股票代码在指定小时内的K线数据"""
    key = (code, year, month, day, hour)
    logger.info(f"Querying candle data for: code={code}, year={year}, month={month}, day={day}, hour={hour}")
    logger.info(f"Query key: {key}")
    logger.info(f"Key exists in candle_data: {key in candle_data}")
    logger.info(f"Total keys in candle_data: {len(candle_data)}")
    
    if key not in candle_data or len(candle_data[key]) == 0:
        raise HTTPException(status_code=404, detail="No data found for the specified parameters")
    
    prices = candle_data[key]
    
    # 计算K线数据
    open_price = prices[0]  # 开盘价：第一条记录
    close_price = prices[-1]  # 收盘价：最后一条记录
    high_price = max(prices)  # 最高价
    low_price = min(prices)  # 最低价
    
    return {
        "open": open_price,
        "close": close_price,
        "high": high_price,
        "low": low_price
    }


@app.put("/flag")
def flag(request: FlagRequest):
    logger.info(f"Flag request received: {request.flag}")
    return {"flag": request.flag}