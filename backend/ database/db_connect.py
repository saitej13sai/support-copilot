# database/db_connect.py
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def insert_issue(customer_id, product_id, issue_text, criticality):
    response = supabase.table("issues").insert({
        "customer_id": customer_id,
        "product_id": product_id,
        "issue_text": issue_text,
        "criticality": criticality
    }).execute()
    return response
