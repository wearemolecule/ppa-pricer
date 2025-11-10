# Simple Python template for Prismatic
# - trades are in params[0]
# - marks are in params[1]
# - does a small math operation via a function
# - returns updated trades in {"data": [...]}

import json

# --- Example math function ---
def demo_calculation(a, b):
    """Example calculation — replace with your own pricing logic later."""
    return a * b

# --- Safe normalize helper ---
def normalize_input(x, label):
    if x is None:
        print(f"No {label} found (None).")
        return {"data": []}
    if isinstance(x, dict) and isinstance(x.get("data"), list):
        return x
    if isinstance(x, list):
        return {"data": x}
    print(f"{label} not in expected format.")
    return {"data": []}

# --- Ensure params exist ---
try:
    _ = len(params)
except NameError:
    print("ERROR: 'params' not found in runtime.")
    result = {"data": []}
    result

# --- Access inputs ---
trades_raw = params[0] if len(params) > 0 else None
marks_raw  = params[1] if len(params) > 1 else None

# --- Normalize inputs ---
trades = normalize_input(trades_raw, "trades")
marks  = normalize_input(marks_raw, "marks")

print(f"DEBUG: trades count = {len(trades['data'])}")
print(f"DEBUG: marks count  = {len(marks['data'])}")

# --- Demo logic ---
updated_trades = []
for trade in trades["data"]:
    t = dict(trade)
    attrs = dict(t.get("attributes", {}))

    # Replace this with real math logic later
    attrs["price"] = demo_calculation(2, 3)  # Example: 2 * 3 = 6

    t["attributes"] = attrs
    updated_trades.append(t)

# --- Return updated trades ---
result = {"data": updated_trades}
result