function validate(e) {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const pass = document.getElementById('password').value;
    const age = document.getElementById('age').value;
    const msgBox = document.getElementById('message');
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/;

    // Convert age to number

    const ageNum = Number(age);
    let message = '';
    if (email === '') {
        message = 'Enter an email.';
        msgBox.style.color = 'red';
    }
    else if (!emailPattern.test(email)) {
        message = 'Enter a valid email (e.g., user@example.com).';
        msgBox.style.color = 'red';
    }
 else if (pass === '') {
        message = 'Enter a password.';
        msgBox.style.color = 'red';
    }
    else if (pass.length < 6 ||pass.length > 15 ) {
        message = 'Password must be at least 6 characters long ans not exceed 15 characters.';
        msgBox.style.color = 'red';
    }
     else if (age === '') {
        message = 'Enter your age.';
        msgBox.style.color = 'red';
    } else {
        message = 'Login successful!';
        msgBox.style.color = 'green';
    }
    msgBox.innerText = message;
}

