#!/usr/bin/env python3
"""
Build the complete 300 poems SQLite database.
Run: python3 build_full_db.py
Output: poems.db -> copy to app/src/main/assets/poems.db
"""

import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), "poems.db")
SCRIPT_DIR = os.path.dirname(__file__)

# Load existing 50 poems from the original script
from build_poems_db import POEMS as FIRST_50

# Load extra poems from JSON files
EXTRA_FILES = [
    "extra_poems_part1.json",   # id 51-100 (from subagent)
    "extra_poems_part2.json",   # id 76-100
    "extra_poems_part3.json",   # id 101-125
    "extra_poems_part4.json",   # id 126-150
    "extra_poems_part5.json",   # id 151-175
    "extra_poems_part6.json",   # id 176-200
    "extra_poems_part7.json",   # id 201-225
    "extra_poems_part8.json",   # id 226-250
    "extra_poems_part9.json",   # id 251-275
    "extra_poems_part10.json",  # id 276-300
]

def load_extra_poems():
    all_extra = []
    seen_ids = set()
    for fname in EXTRA_FILES:
        fpath = os.path.join(SCRIPT_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for p in data:
                    if p["id"] not in seen_ids:
                        all_extra.append(p)
                        seen_ids.add(p["id"])
                print(f"Loaded {len(data)} poems from {fname} (unique: {len(seen_ids)} total)")
        else:
            print(f"Warning: {fname} not found, skipping")
    return all_extra

def build_database():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE poems (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            titlePinyin TEXT NOT NULL,
            titleEn TEXT NOT NULL,
            author TEXT NOT NULL,
            authorPinyin TEXT NOT NULL,
            authorEn TEXT NOT NULL,
            dynasty TEXT NOT NULL,
            dynastyEn TEXT NOT NULL,
            content TEXT NOT NULL,
            translation TEXT NOT NULL,
            annotation TEXT NOT NULL,
            category TEXT NOT NULL,
            difficulty INTEGER NOT NULL DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE favorites (
            poemId INTEGER PRIMARY KEY,
            note TEXT NOT NULL DEFAULT '',
            groupName TEXT NOT NULL DEFAULT 'Default',
            createdAt INTEGER NOT NULL DEFAULT 0
        )
    """)

    # Combine all poems
    all_poems = list(FIRST_50)
    existing_ids = set(p["id"] for p in all_poems)
    
    extra = load_extra_poems()
    for p in extra:
        if p["id"] not in existing_ids:
            all_poems.append(p)
            existing_ids.add(p["id"])

    # Sort by id
    all_poems.sort(key=lambda x: x["id"])

    # Insert all poems
    for poem in all_poems:
        cursor.execute("""
            INSERT INTO poems (id, title, titlePinyin, titleEn, author, authorPinyin, authorEn,
                             dynasty, dynastyEn, content, translation, annotation, category, difficulty)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            poem["id"], poem["title"], poem["titlePinyin"], poem.get("titleEn", poem["title"]),
            poem["author"], poem["authorPinyin"], poem["authorEn"],
            poem.get("dynasty", "唐"), poem.get("dynastyEn", "Tang"), poem["content"],
            poem["translation"], poem["annotation"], poem.get("category", "Nature"),
            poem.get("difficulty", 1)
        ))

    conn.commit()
    
    # Verify
    cursor.execute("SELECT COUNT(*) FROM poems")
    count = cursor.fetchone()[0]
    
    cursor.execute("SELECT author, COUNT(*) FROM poems GROUP BY author ORDER BY COUNT(*) DESC LIMIT 25")
    top_authors = cursor.fetchall()
    
    cursor.execute("SELECT difficulty, COUNT(*) FROM poems GROUP BY difficulty ORDER BY difficulty")
    diff_dist = cursor.fetchall()
    
    conn.close()
    
    print(f"\n{'='*50}")
    print(f"Database built successfully!")
    print(f"Total poems: {count}")
    print(f"Output: {DB_PATH}")
    print(f"\nDifficulty distribution:")
    for d, c in diff_dist:
        print(f"  Level {d}: {c} poems")
    print(f"\nTop 25 poets:")
    for author, cnt in top_authors:
        print(f"  {author}: {cnt} poems")
    print(f"{'='*50}")

if __name__ == "__main__":
    build_database()
