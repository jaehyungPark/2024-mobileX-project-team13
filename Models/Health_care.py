from typing import Literal
from pydantic import BaseModel, Field

class InputModel(BaseModel):
    Gender: Literal['남성', '여성'] = Field(
        default='남성',
        description='사용자의 성별'
    )
    Age: int = Field(
        default=20,
        ge=0,
        le=120,
        description='사용자의 나이'
    )
    Height_cm: int = Field(
        default=175,
        ge=120,
        le=220,
        description='사용자의 키 (cm)'
    )
    Weight_kg: int = Field(
        default=75,
        ge=30,
        le=200,
        description='사용자의 몸무게 (kg)'
    )
    Target: Literal[
        '전신', 
        '등', 
        '가슴', 
        '어깨', 
        '팔', 
        '하체'
    ] = Field(
        default='전신',
        description='운동 집중 부위'
    )
    Goal: Literal[
        '근성장', 
        '체력 증진', 
        '기분 전환'
    ] = Field(
        default='근성장',
        description='운동 목표'
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )

class OutputModel(BaseModel):
    output: str = Field(
        description='추천 운동 루틴',
    )