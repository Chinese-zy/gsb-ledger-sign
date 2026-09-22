from __future__ import annotations
def reconcile(entries):
    total = 0
    rows = []
    last_memo = ""
    for e in sorted(entries, key=lambda x: x.get("id", 0)):
        amt = abs(int(e["amount"]))
        memo = e.get("memo")
        if memo is None or str(memo).strip() == "":
            memo = last_memo
        else:
            last_memo = str(memo)
        total += amt
        rows.append({"amount": amt, "memo": memo})
    return {"ok": total == 0, "total": total, "rows": rows}
