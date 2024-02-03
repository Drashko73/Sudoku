

"""
.
.
.
.   SIGN IN PAGE
.
.
.
"""

print("Content-type:text/html\n\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Radovan Draskovic">
    
    <title>Sign In</title>
    
    <link rel="stylesheet" href="../styles/style_signin_signup.css">
    <link rel="shortcut icon" href="../images/icon.png" type="image/x-icon">
    
    <script src="../scripts/toggle_password.js" defer></script>
    <script src="../scripts/script.js" defer></script>
    
</head>

<body onload="is_already_signed_in()">
    <div class=" flex-r container">
        <div class="flex-r login-wrapper">
            <div class="login-text">
                <div class="logo">
                    <span><i class="fab fa-speakap"></i></span>
                    <span>MindfulSudoku</span>
                    <p>Unlock the Sudoku adventure! Sign in for limitless puzzles and strategic fun. Let the gaming joy commence!</p>
                </div>
                <h1>Sign In</h1>

                <div class="flex-c">
                    
                    <div class="input-box">
                        <span class="label">E-mail</span>
                        <div class=" flex-r input">
                            <input type="text" placeholder="name@abc.com" spellcheck="false" id="input_email" autocomplete="off">
                            <i class="fas fa-at"></i>
                        </div>
                    </div>
                    
                    <div class="input-box">
                        <span class="label">Password</span>
                        <div class="flex-r input">
                            <input id="passwordInput" type="password" placeholder="8+ (a, A, 1, #)" spellcheck="false">
                            <span id="show-hide-pass" class="toggle-password" onclick="togglePasswordVisibility()">Show</span>
                            <i class="fas fa-lock"></i>
                        </div>
                    </div>
                    
                    <p id='error_msg_display'></p>

                    <input class="btn" type="submit" value="Sing In" onclick="login_user()">
                    <span class="extra-line">
                        <span>Don't have an account?</span>
                        <a href="./signup.py">Sign Up</a>
                    </span>
                </div>

            </div>
        </div>
    </div>
</body>

"""
)