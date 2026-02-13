from airtable_client import fetch_posts_needing_summary, update_post_summary
from llm_client import generate_summary


if __name__ == "__main__":
    print("Running Insta Intel Pipeline (Mock Mode)")

    posts = fetch_posts_needing_summary(limit=5)

    if not posts:
        print("No posts need processing.")
    else:
        for post in posts:
            record_id = post["id"]
            caption = post["fields"].get("Caption", "")

            print(f"\nProcessing: {record_id}")

            summary_data = generate_summary(caption)

            # Only pass the summary string
            update_post_summary(record_id, summary_data["summary"])

    print("\nPipeline complete.")
