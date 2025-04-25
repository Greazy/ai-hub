const BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

export const registerUser = async (email, password) => {
  const res = await fetch(`${BASE_URL}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });

  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Registration failed");
  }

  return await res.json();
};

export const getUser = async () => {
  const res = await fetch(`${BASE_URL}/users/1`, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  }); // TODO: update url

  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Cannot get user");
  }
}