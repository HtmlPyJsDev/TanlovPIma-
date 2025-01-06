// Имитация базы данных
let users = [];

function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

function validatePassword(password) {
  return (
    password.length >= 8 &&
    /[A-Z]/.test(password) &&
    /[a-z]/.test(password) &&
    /[0-9]/.test(password)
  );
}

function register() {
  const username = document.getElementById("reg-username").value;
  const email = document.getElementById("reg-email").value;
  const password = document.getElementById("reg-password").value;
  const confirmPassword = document.getElementById("reg-confirm-password").value;
  const errorElement = document.getElementById("reg-error");

  if (!username || !email || !password || !confirmPassword) {
    errorElement.textContent = "Barcha maydonlarni to'ldiring";
    return;
  }

  if (!validateEmail(email)) {
    errorElement.textContent = "Noto'g'ri email formati";
    return;
  }

  if (users.some((user) => user.email === email)) {
    errorElement.textContent = "Bu email allaqachon ro'yxatdan o'tgan";
    return;
  }

  if (!validatePassword(password)) {
    errorElement.textContent =
      "Parol kamida 8 ta belgidan iborat bo'lishi, katta va kichik harflar hamda raqamlarni o'z ichiga olishi kerak";
    return;
  }

  if (password !== confirmPassword) {
    errorElement.textContent = "Parollar mos kelmayapti";
    return;
  }

  users.push({ username, email, password });
  document.getElementById("reg-success").textContent =
    "Muvaffaqiyatli ro'yxatdan o'tdingiz!";
  setTimeout(() => {
    showLoginForm();
  }, 2000);
}

function login() {
  const email = document.getElementById("login-email").value;
  const password = document.getElementById("login-password").value;
  const errorElement = document.getElementById("login-error");

  if (!email || !password) {
    errorElement.textContent = "Barcha maydonlarni to'ldiring";
    return;
  }

  const user = users.find((u) => u.email === email && u.password === password);
  if (user) {
    document.getElementById("login-success").textContent =
      "Muvaffaqiyatli kirdingiz!";
    setTimeout(() => {
      window.location.href = "index.html";
    }, 2000);
  } else {
    errorElement.textContent = "Noto'g'ri email yoki parol";
  }
}

function showRegisterForm() {
  document.getElementById("login-form").style.display = "none";
  document.getElementById("register-form").style.display = "block";
}

function showLoginForm() {
  document.getElementById("register-form").style.display = "none";
  document.getElementById("login-form").style.display = "block";
}
