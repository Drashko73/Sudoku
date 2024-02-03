

"""
.
.
.
.   TERMS OF USE PAGE
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
    
    <title>Terms of use</title>
    
    <link rel="shortcut icon" href="../images/icon.png" type="image/x-icon">
    <link rel="stylesheet" href="../styles/terms.css">
    
    <script src="../scripts/script.js" defer></script>
    
</head>

<body onload="is_already_signed_in()">
    <div class=" flex-r container">
        <div class="flex-r login-wrapper">
            <div class="login-text">
            
                <div id="header_image">
                    <img src="../images/i_love_sudoku.png" alt="love_sudoku_image" draggable="false"; height=70;>
                </div>
            
                <div class="logo">
                    <span><i class="fab fa-speakap"></i></span>
                    <span>Opis projekta</span>
                    <p>
                        MindfulSudoku je sofisticirana interaktivna web aplikacija koja je koncipirana i realizovana kao deo seminarskog rada u okviru predmeta <strong>Web programiranje 1</strong> tokom skolske 2023/2024 godine. Ova aplikacija predstavlja skladno sjedinjenje tehnologija kao sto su <em>Python</em>, <em>Javascript</em>, <em>HTML</em> i <em>CSS</em>. U razvoju projekta posebna paznja posvecena je efikasnom upravljanju podacima kroz bazu podataka SQLite, kao i implementaciji tehnika komunikacije putem AJAX-a u domenu web programiranja.
                    </p>
                    <br>
                    <p>
                        <strong>
                            **Svi podaci koji se prosledjuju koriste se iskljucivo radi pracenja progresa ulogovanog korisnika u igri**
                        </strong>
                    </p>
                </div>
                
                <div id="signature">
                    <strong>Autor:</strong> <em>Radovan Draskovic 73/2021</em>
                    <div>
                        <img src="../images/linkedinLogo.png" alt="linkedin" width="25px" height="25px" title="Linkedin" draggable="false">&nbsp;&nbsp;<a href="https://www.linkedin.com/in/radovan-draskovic/" target="_blank" title="Poseti link">in/radovan-draskovic/</a> <br>
                    </div>
                    <div>
                        <img src="../images/githubLogo.png" alt="github" width="25px" height="25px" title="GitHub" draggable="false">&nbsp;&nbsp;<a href="https://github.com/Drashko73" target="_blank" title="Poseti link">github.com/Drashko73</a>
                    </div>
                </div>
                
                <div id="footer">
                    <span">Mozete zatvoriti stranicu klikom <span id="close_page_span" title="Zatvori stranicu" onclick="close_page()">ovde</span></span>
                </div>
                
            </div>
        </div>
    </div>
</body>

"""
)