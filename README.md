# AI Competitor Social Media Monitoring


**Status:** v2 Complete (Core Pipeline)  
**Alert Layer:** Pending Implementation  

An AI-powered competitive intelligence pipeline that monitors competitor Instagram activity, structures raw data in Airtable, and enriches posts with LLM-generated topic summaries using a modular Python workflow.

---

## Overview

This system automates the collection and enrichment of competitor social media content.

The pipeline:

1. Scrapes competitor Instagram posts daily via Apify  
2. Stores structured post data in Airtable  
3. Identifies unprocessed posts  
4. Generates concise AI-powered topic summaries  
5. Updates Airtable records to prevent duplicate processing  

The result is a scalable, structured competitive intelligence foundation ready for alerting and reporting.

---

## Architecture

Apify (Scheduled Scraper)
↓
Airtable (Central Intelligence Database)
↓
Python Intelligence Layer
↓
OpenAI (Topic Summarization)
↓
Airtable Update (Processed State)


---

## Core Workflow (v2)

### 1. Data Collection

- Apify runs daily on a schedule
- Scrapes latest Instagram posts for defined competitors
- Extracted fields:
  - Post URL
  - Caption
  - Owner Name
  - Timestamp

Apify uses native Airtable Exporter integration to UPSERT records using URL as the primary key, preventing duplicates automatically.

---

### 2. Central Data Storage

Airtable acts as the structured intelligence database:

- Stores all raw post data
- Tracks processing state
- Filters records where `{Topic Summary}` is blank

---

### 3. Python Intelligence Layer

The Python pipeline:

- Queries Airtable for unprocessed posts
- Sends captions to an LLM client
- Generates a neutral 15–25 word topic summary
- Updates the original Airtable record
- Ensures each post is processed only once

Once the summary field is populated, Airtable formula logic automatically excludes the record from future runs.

---

## Planned Extension (v3)

After each daily run, the system will generate a structured competitive digest including:

- Number of new posts per competitor
- Key recurring themes
- Notable high-engagement posts
- Emerging patterns

The digest will be automatically emailed to stakeholders as a daily competitive intelligence briefing.

---

## What Changed vs v1

Version 2 introduced significant architectural improvements:

- Removed Make (reduced cost and complexity)
- Implemented native Apify → Airtable integration
- Introduced a dedicated Python intelligence layer
- Added modular LLM abstraction
- Designed scalable and extensible architecture

---

## Tech Stack

- Python
- OpenAI API (LLM abstraction layer)
- Apify
- Airtable
- dotenv

---

## Project Structure

src/
├── main.py # Pipeline entry point
├── airtable_client.py # Airtable integration
├── llm_client.py # LLM abstraction layer
├── models.py # Data models
├── prompts.py # Prompt templates
└── config.py # Environment configuration

---

## Setup

1. Clone repository
2. Create virtual environment
3. Install dependencies: pip install -r requirements.txt
4. Create `.env` file using `.env.example`
5. Run the pipeline: python src/main.py


---

## Design Principles

- Modular integrations
- Clear separation of orchestration and API clients
- Idempotent processing (no duplicate summaries)
- Scalable architecture ready for reporting and alerting
- Minimal external dependencies

---

## Purpose

This project demonstrates:

- Automation architecture design
- API integration workflows
- LLM-powered enrichment pipelines
- Structured intelligence system design
- Clean modular Python implementation

---




