from services.rag_engine import fetch_context

def generate_adaptive_content(user_id: str, topic: str) -> str:
    context = fetch_context(topic)
    return f"""
🎯 **Personalized Learning Path for {topic}**

**Based on your learning profile (User: {user_id}) and contextual knowledge:**

{context}

**Generated using Agentic AI** with real-world alignment.
"""
