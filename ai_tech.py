import json
import os
import requests

DB_FILE = "data.json"
HF=  ""
MODEL = "openai/gpt-oss-120b"
API_URL = "https://router.huggingface.co/v1/chat/completions"


def load_data():
    if not os.path.exists(DB_FILE):
        raise FileNotFoundError(f"{DB_FILE} not found - run client.py first to collect data.")
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def ask_model(prompt):
    if not HF:
        raise RuntimeError("HF environment variable is not set.")

    headers = {
        "Authorization": f"Bearer {HF}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "אתה יועץ פדגוגי מומחה. אתה מקבל הודעות שכתבו מורים על "
                    "תלמידים/כיתה, ועליך להציע שיטת הוראה מתאימה - "
                    "בצורה תמציתית, מעשית ומנומקת."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.4,
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    result = response.json()
    return result["choices"][0]["message"]["content"]


def build_prompt(region, grade, messages):
    joined_messages = "\n".join(f"- {m}" for m in messages)
    return (
        f"להלן הודעות שנאספו ממורים באזור '{region}', כיתה '{grade}':\n\n"
        f"{joined_messages}\n\n"
        "בהתבסס על ההודעות האלו, מהי שיטת הלימוד הכי מתאימה לכיתה הזו? "
        "תן המלצה קצרה וברורה, כולל נימוק."
    )


def main():
    db = load_data()

    for region, grades in db.items():
        for grade, messages in grades.items():
            if not messages:
                continue

            print(f"\n=== אזור: {region} | כיתה: {grade} ===")
            prompt = build_prompt(region, grade, messages)
            try:
                recommendation = ask_model(prompt)
                print(recommendation)
            except Exception as e:
                print(f"שגיאה בעת פנייה למודל: {e}")


if __name__ == "__main__":
    main()