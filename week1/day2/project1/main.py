import sys, os
print("PYTHONPATH env var:", os.environ.get("PYTHONPATH", "NOT SET"))
print("\nsys.path:")
for i, p in enumerate(sys.path):
    print(f"  {i}: {p}")

print("\nTrying import...")
import claude_helpers
print("Result:", claude_helpers.format_prompt("  hello  "))