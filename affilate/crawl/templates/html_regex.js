document.addEventListener("DOMContentLoaded", function () {
    const loginBox = document.getElementById("loginBox");
    console.log(loginBox)
    // Delay setting opacity to 1 for the fade-in effect
    setTimeout(function () {
        loginBox.style.opacity = 1;
    }, 1000);

    const loginBox1 = document.getElementById("loginBox");
    console.log(loginBox1)

    const loginForm = document.getElementById("loginForm");
    const message = document.getElementById("message");

    loginForm.addEventListener("submit", function (e) {
        e.preventDefault();
        message.textContent = "";

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        // You can add your login logic here
        // For demonstration purposes, check for a dummy username and password
        if (username === "demo" && password === "password") {
            message.textContent = "Login successful!";
            message.style.color = "green";
        } else {
            message.textContent = "Invalid username or password.";
            message.style.color = "red";
        }
    });
});
