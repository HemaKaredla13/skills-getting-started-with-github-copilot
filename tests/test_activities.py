"""Tests for activities API endpoints."""


def test_get_activities_returns_dict(client):
    r = client.get("/activities")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, dict)
    # Basic expected keys
    assert "Chess Club" in data


def test_signup_success_adds_participant(client):
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Ensure not already present
    resp = client.get("/activities")
    assert email not in resp.json()[activity]["participants"]

    # Sign up
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert "Signed up" in resp.json()["message"]

    # Verify added
    resp = client.get("/activities")
    assert email in resp.json()[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    activity = "Chess Club"
    email = "michael@mergington.edu"  # existing participant

    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 400


def test_signup_nonexistent_activity_returns_404(client):
    resp = client.post("/activities/NoSuchClub/signup", params={"email": "a@b.com"})
    assert resp.status_code == 404
