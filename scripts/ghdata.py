"""GitHub GraphQL helpers shared by the analytics and calendar generators."""
import datetime as dt
import json
import urllib.request

API = "https://api.github.com/graphql"
TZ = dt.timezone(dt.timedelta(hours=8), "Asia/Manila")  # Philippines has no daylight saving

YEARS_QUERY = """query($login:String!){user(login:$login){createdAt
  contributionsCollection{contributionYears}}}"""
RANGE_QUERY = """query($login:String!,$from:DateTime!,$to:DateTime!){
  user(login:$login){contributionsCollection(from:$from,to:$to){
    contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}"""


def today():
    return dt.datetime.now(TZ).date()


def gql(query, variables, token):
    req = urllib.request.Request(
        API, data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json",
                 "User-Agent": "angelfrancel-profile"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if data.get("errors") or not data.get("data", {}).get("user"):
        raise RuntimeError("GitHub did not return contribution data: " + str(data.get("errors", "user missing")))
    return data["data"]["user"]


def account_info(login, token):
    """(years with activity, account creation date)."""
    u = gql(YEARS_QUERY, {"login": login}, token)
    return u["contributionsCollection"]["contributionYears"], dt.date.fromisoformat(u["createdAt"][:10])


def fetch_range(login, token, start, end):
    """({date: count}, total) for start..end (at most one year)."""
    u = gql(RANGE_QUERY, {"login": login, "from": f"{start}T00:00:00Z", "to": f"{end}T23:59:59Z"}, token)
    cal = u["contributionsCollection"]["contributionCalendar"]
    days = {}
    for week in cal["weeks"]:
        for d in week["contributionDays"]:
            days[dt.date.fromisoformat(d["date"])] = d["contributionCount"]
    return days, cal["totalContributions"]


def fetch_all(login, token):
    """Every day's count across all years -> ({date: count}, total)."""
    years, _ = account_info(login, token)
    days, total = {}, 0
    for y in years:
        d, t = fetch_range(login, token, dt.date(y, 1, 1), dt.date(y, 12, 31))
        days.update(d)
        total += t
    return days, total
