# api/issue_api.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database.db_connect import insert_issue
from logic.criticality import get_criticality
from llm.template_generator import generate_template

router = APIRouter()

class Issue(BaseModel):
    customer_id: int
    product_id: int
    issue_text: str

@router.post("/new_issue/")
def new_issue(issue: Issue):
    try:
        criticality = get_criticality(issue.issue_text)
        template = generate_template(issue.issue_text, criticality)
        response = insert_issue(
            customer_id=issue.customer_id,
            product_id=issue.product_id,
            issue_text=issue.issue_text,
            criticality=criticality
        )
        return {
            "message": "Issue saved successfully",
            "criticality": criticality,
            "suggested_reply": template,
            "supabase_response": response.data  # response is from Supabase
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
